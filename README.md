# Template generator

All commands executed from this folder.

# Usage
## Windows
```
generate.bat
```

## Linux
```shell
./generate.sh
```

# Manual setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
* Paste pixelart images in the following format `generator/pixelart/{hpos}x{vpos}.png`
* Run `python generator/generator.py`
* Commit
* Success