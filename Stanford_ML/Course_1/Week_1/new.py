def parse_chapter_title(line):
    return line.startswith("# ")


def parse_section_title(line):
    return line.startswith("## ")


def tableOfContents(text):
    table_of_contents = []
    chapter_number = 1
    section_number = 1

    for line in text:
        if parse_chapter_title(line):
            table_of_contents.append(f"{chapter_number}. {line[2:].strip()}")
            chapter_number += 1
            section_number = 1
        elif parse_section_title(line):
            table_of_contents.append(f"{chapter_number - 1}.{section_number}. {line[3:].strip()}")
            section_number += 1

    return table_of_contents