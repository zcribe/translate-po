import os

from googletrans import Translator

from .constants import UNTRANSLATED_PATH, TRANSLATED_PATH, LANGUAGE_SOURCE, LANGUAGE_DESTINATION
from .io import read_lines, save_lines
from .match import recognize_source, recognize_destination, recognize_plurals, match_quotes


def translate(source: str) -> str:
    """ Translates a single string into target language. """
    translator = Translator()
    cleaned = match_quotes(source)
    if cleaned:
        return translator.translate(cleaned, dest=LANGUAGE_DESTINATION, src=LANGUAGE_SOURCE).text
    return ""


def create_close_string(line: str) -> str:
    """ Creates single .po file translation target sting. """
    return r"msgstr " + '"' + line + '"' + "\n"


def categorise_lines(strings: list) -> list:
    """ Categorises lines in a list based on .po file standard. """
    line_type_collection = []
    open_sequence = False
    for line in strings:
        line_type = 0
        if recognize_source(line):
            line_type = 1
            open_sequence = True
        elif recognize_plurals(line):
            line_type = 2
        elif recognize_destination(line):
            line_type = 3
            open_sequence = False
        elif open_sequence:
            line_type = 4
        line_type_collection.append(line_type)
    return line_type_collection


def solve(new_file: str, old_file: str):
    """ Translates single file. """
    lines = read_lines(old_file)
    lines_processed = 0
    lines_total = len(lines)
    categories = categorise_lines(lines)
    cache_out = []
    cache_translation = []

    for line, category in zip(lines, categories):
        if category == 1:
            translation = create_close_string(translate(line))
            cache_translation.append(translation)
            cache_out.append(line)
        elif category == 2:
            cache_out.append(line)
        elif category == 3:
            cache_out.extend(cache_translation)
            cache_translation = []
        elif category == 4:
            cache_translation.append('"' + translate(line) + '"' + "\n")
            cache_out.append(line)
        else:
            cache_out.append(line)

        lines_processed += 1
        print(f"Lines processed: {lines_processed}/{lines_total}")

    save_lines(new_file, cache_out)


def run(directory: str):
    """ Core process that translates all files in a directory. """
    for file in os.listdir(directory):
        solve(os.path.join(TRANSLATED_PATH, file), os.path.join(UNTRANSLATED_PATH, file))


if __name__ == '__main__':
    run(UNTRANSLATED_PATH)
