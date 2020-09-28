# translate-po

Simple quick script for automatically translating .po files using Google. In attempt to give translators a quick baseline to correct and work off from. Which speeds up and simplifies the internationalization process.

## Usage

```python
from translate_po.main import run

run(fro="en" to="et" src="./untranslated" dest="./translated")
```

### Changelog
1.0.11
- Fixed distributable not including parts of code
- Build script improvements
- Fixed dependencies not automatically installing
- Added .po file recognition
- Changed default constants for simpler use

1.0.4 

- Swapped out my own implementation of .po file parser for polib one. 
- Fixed metadata writing into new files.