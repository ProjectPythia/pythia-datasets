import os
import pathlib

import pooch

here = pathlib.Path(os.path.dirname(__file__))
data_dir = here.parent / 'data'

pooch.make_registry(data_dir, here / 'temp_registry.txt')
