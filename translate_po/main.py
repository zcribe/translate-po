import argparse
import os

import polib
from googletrans import Translator

from .utilities.constants import UNTRANSLATED_PATH, TRANSLATED_PATH, LANGUAGE_SOURCE, LANGUAGE_DESTINATION, RECURSIVE
from .utilities.io import read_lines, save_lines
from .utilities.match import recognize_po_file


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
    found_files = False

    parser = argparse.ArgumentParser(description='Automatically translate PO files using Google translate.')
    parser.add_argument('--fro', type=str, help='Source language you want to translate from to (Default: en)',
                        default=kwargs.get('fro', LANGUAGE_SOURCE))
    parser.add_argument('--to', type=str, help='Destination language you want to translate to (Default: et)',
                        default=kwargs.get('to', LANGUAGE_DESTINATION))
    parser.add_argument('--src', type=str, help='Source directory or the files you want to translate',
                        default=kwargs.get('src', UNTRANSLATED_PATH))
    parser.add_argument('--dest', type=str, help='Destination directory you want to translated files to end up in',
                        default=kwargs.get('dest', TRANSLATED_PATH))
    parser.add_argument('--recursive', action='store_true', help='If provided, treat src and dest as directory hierarchies',
                        default=kwargs.get('recursive', RECURSIVE))
    arguments = parser.parse_args()

    if arguments.recursive == True:
        for root, _, files in os.walk(arguments.src):
            for file in files:
                if recognize_po_file(file):
                    found_files = True
                    relative_path = os.path.relpath(root, arguments.src)
                    if relative_path == '.': relative_path = ''
                    solve(os.path.join(arguments.dest, relative_path, file), os.path.join(root, file), arguments)
    else:
        for file in os.listdir(arguments.src):
            if recognize_po_file(file):
                found_files = True
                solve(os.path.join(arguments.dest, file), os.path.join(arguments.src, file), arguments)

    if not found_files:
        raise Exception(f"Couldn't find any .po files at: '{arguments.src}'")


if __name__ == '__main__':
    run()
