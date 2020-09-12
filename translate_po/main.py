import argparse
import os

import polib
from googletrans import Translator
from utilities.constants import UNTRANSLATED_PATH, TRANSLATED_PATH, LANGUAGE_SOURCE, LANGUAGE_DESTINATION
from utilities.io import read_lines, save_lines


def translate(source: str, arguments) -> str:
    """ Translates a single string into target language. """
    translator = Translator()
    return translator.translate(source, dest=arguments.to, src=arguments.fro).text


def create_close_string(line: str) -> str:
    """ Creates single .po file translation target sting. """
    return r"msgstr " + '"' + line + '"' + "\n"


def solve(new_file: str, old_file: str, arguments):
    """ Translates single file. """
    lines = read_lines(old_file)
    for line in lines:
        line.msgstr = polib.unescape(translate(polib.escape(line.msgid), arguments))
        print(f"Translated {lines.percent_translated()}% of the lines.")
    save_lines(new_file, lines)


def run(**kwargs):
    """ Core process that translates all files in a directory.
     :parameter fro:
     :parameter to:
     :parameter src:
     :parameter dest:
     """
    parser = argparse.ArgumentParser(description='Automatically translate PO files using Google translate.')
    parser.add_argument('--fro', type=str, help='Source language you want to translate from to (Default: en)',
                        default=kwargs.get('fro', LANGUAGE_SOURCE))
    parser.add_argument('--to', type=str, help='Destination language you want to translate to (Default: et)',
                        default=kwargs.get('to', LANGUAGE_DESTINATION))
    parser.add_argument('--src', type=str, help='Source directory or the files you want to translate',
                        default=kwargs.get('src', UNTRANSLATED_PATH))
    parser.add_argument('--dest', type=str, help='Destination directory you want to translated files to end up in',
                        default=kwargs.get('dest', TRANSLATED_PATH))
    arguments = parser.parse_args()

    for file in os.listdir(arguments.src):
        solve(os.path.join(arguments.dest, file), os.path.join(arguments.src, file), arguments)


if __name__ == '__main__':
    run()
