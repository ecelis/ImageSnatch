# ImageSnatch

Extract images from PDF files with Python

## Development Setup

```
python3 -m venv env
. env/bin/activate
pip3 install -r requirements.txt
```

## Run

```
python3
from image_snatch.converters import toPNG
toPNG("/path/to.pdf")
```

