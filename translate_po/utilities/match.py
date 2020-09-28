import re


def recognize_po_file(filename: str) -> bool:
    """ Recognize .po file """
    if filename.endswith(".po"):
        return True
    return False


def recognize_source(line: str) -> bool:
    """ Recognizes .po file source string. """
    if line.startswith("msgid"):
        return True
    return False


def recognize_plurals(line: str) -> bool:
    """ Recognizes .po file plural source string. """
    if line.startswith("msgid_plural"):
        return True
    return False


def recognize_destination(line: str) -> bool:
    """ Recognizes .po file target string.  """
    if line.startswith("msgstr"):
        return True
    return False


def match_quotes(line: str) -> str:
    """ Matches quotes within quotes. """
    result = re.findall(r'"([^"]*)"', line)
    if len(result) > 0:
        return result[0]
    return ""
