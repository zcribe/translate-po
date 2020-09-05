import io


def read_lines(file: str) -> list:
    """ Read lines into memory. """
    all_lines = []
    with io.open(file, 'r', encoding='utf8') as infile:
        for line in infile:
            all_lines.append(line)
    return all_lines


def save_lines(file: str, lines: list):
    """ Save lines from memory into a file. """
    with io.open(file, 'w', encoding='utf8') as infile:
        for line in lines:
            infile.write(line)
