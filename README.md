# Zotero Remarkable Sync

This is a little utility that I made to keep a collection/folder in sync with Zotero and Remarkable.
My zotero setup uses external storage (I store all attachments on OneDrive)

## Setup
 - install rmapi
 - Download the [sync.py](https://raw.githubusercontent.com/oscarmorrison/zoteroRemarkableO/master/sync.py)
 - create a `.env` file

### Dependancies

- python3
- [rmapi](https://github.com/juruen/rmapi)
- pyzotero
- pydash
- dotenv
(the above 3 python libraries can be installed using pip3)

### Env file

- Create a zotero api key
- get zotero library_id (from zotero web)
- create a folder on remarkable and a collection in zotero
- get base path for zotero pdf (papers)

## Installation

- Add (e.g. a symlink) to your `.local/bin/`
- Copy your `.env` into `.config/zoteroRemarkable/`
- Then you can run the name of what you symlinked from the command line

## Usage

_(ensure you have a .env file, with zotero api key, and rmapi setup)_  
Then to sync, just run:  
  `python3 sync.py`
