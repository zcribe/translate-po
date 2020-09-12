import io

import polib


def read_lines(file: str) -> list:
    """ Read lines into memory. """
    # all_lines = []
    # with io.open(file, 'r', encoding='utf8') as infile:
    #     for line in infile:
    #         all_lines.append(line)
    # return all_lines
    return polib.pofile(file)


def save_lines(file: str, lines: list):
    """ Save lines from memory into a file.
     :parameter file:
     :parameter lines:
     """
    with io.open(file, 'w', encoding='utf8') as infile:
        infile.write("""
msgid ""
msgstr ""
""")
        for keys, values in lines.metadata.items():
            infile.write(f'"{keys}:{values}"\n')
        infile.write('\n')
        for line in lines:
            infile.write(line.__unicode__())
    # polib.save(file)
