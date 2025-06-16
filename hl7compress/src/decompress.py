def decompress_hl7(compressed, template):
    """
    Decompress HL7 messages based on templates
    :param compressed: Compressed HL7 message string
    :param template: HL7 template string
    :return: Original HL7 message string
    """
    comp_lines = compressed.splitlines()
    tpl_lines = template.splitlines()
    decompressed_lines = []

    # Ensure that the number of template lines is not less than the number of compressed lines
    tpl_lines = tpl_lines + [''] * (len(comp_lines) - len(tpl_lines))

    for comp_line, tpl_line in zip(comp_lines, tpl_lines):
        if not tpl_line.strip():  # No corresponding template lines, reserved directly
            decompressed_lines.append(comp_line)
            continue

        comp_fields = comp_line.split('|')
        tpl_fields = tpl_line.split('|')

        # segment must match
        if comp_fields[0] != tpl_fields[0]:
            decompressed_lines.append(comp_line)
            continue

        decompressed_fields = [comp_fields[0]]  # keep segment
        tpl_idx, comp_idx = 1, 1

        # rebuild
        while tpl_idx < len(tpl_fields) or comp_idx < len(comp_fields):
            if tpl_idx < len(tpl_fields):
                if comp_idx < len(comp_fields) and comp_fields[comp_idx] != '':
                    # use compressed value
                    decompressed_fields.append(comp_fields[comp_idx])
                    comp_idx += 1
                    tpl_idx += 1
                else:
                    # use template value
                    decompressed_fields.append(tpl_fields[tpl_idx])
                    if comp_idx < len(comp_fields):
                        comp_idx += 1  # skip empty field
                    tpl_idx += 1
            else:
                # Handle redundant compression fields
                decompressed_fields.append(comp_fields[comp_idx])
                comp_idx += 1

        decompressed_lines.append('|'.join(decompressed_fields))

    return '\r'.join(decompressed_lines)