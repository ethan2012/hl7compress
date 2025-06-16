def is_dynamic_field(field):
    """Check if the field is a dynamic field (including brackets)"""
    return '{' in field and '}' in field


def compress_hl7(message, template):
    """
    Compress HL7 messages based on templates
    :param message: Original HL7 message string
    :param template: HL7 template string
    :return: Compressed HL7 message string
    """
    msg_lines = message.splitlines()
    tpl_lines = template.splitlines()
    compressed_lines = []

    # Ensure that the number of template lines is not less than the number of message lines
    tpl_lines = tpl_lines + [''] * (len(msg_lines) - len(tpl_lines))

    for msg_line, tpl_line in zip(msg_lines, tpl_lines):
        if not tpl_line.strip():  # No corresponding template lines, reserved directly
            compressed_lines.append(msg_line)
            continue

        msg_fields = msg_line.split('|')
        tpl_fields = tpl_line.split('|')

        # segment must match
        if msg_fields[0] != tpl_fields[0]:
            compressed_lines.append(msg_line)
            continue

        compressed_fields = [msg_fields[0]]  # keep segment

        # handle every segment
        for j in range(1, min(len(msg_fields), len(tpl_fields))):
            if is_dynamic_field(tpl_fields[j]):
                compressed_fields.append(msg_fields[j])
            else:
                compressed_fields.append('' if msg_fields[j] == tpl_fields[j] else msg_fields[j])

        # handle segments those have more messages than temple does
        for j in range(len(tpl_fields), len(msg_fields)):
            compressed_fields.append(msg_fields[j])

        compressed_lines.append('|'.join(compressed_fields))

    return '\r'.join(compressed_lines)
