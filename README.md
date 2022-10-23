# translate-po

Simple quick script for automatically translating .po files using Google. It speeds up internationalization by giving translators machine translated base version to correct.

## Usage

Installation
```cmd
pip install translate-po
```

Script usage
```python
from translate_po.main import run

run(fro="en", to="et", src="./untranslated", dest="./translated", recursive=True)
```

Command-line usage
```bash
translate-po --fro="en" --to="et" --src="./untranslated" --dest="./translated" --recursive
```

### Changelog
1.0.13
- Fixed typo in the readme

1.0.11
- Fixed distributable not including parts of code
- Build script improvements
- Fixed dependencies not automatically installing
- Added .po file recognition
- Changed default constants for simpler use

1.0.4 
- Swapped out my own implementation of .po file parser for polib one. 
- Fixed metadata writing into new files.