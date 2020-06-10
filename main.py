from os import path
from pathlib import Path

from network import get_files
from odictlib import write_odict

Path('dictionaries').mkdir(parents=True, exist_ok=True)
get_files(
    lambda key, contents: write_odict(
        contents,
        path.join('dictionaries', '%s.odict' % key)
    )
)
