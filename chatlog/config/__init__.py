import os

from config import default


class Config(object):

    def __getattribute__(self, attr):
        if os.getenv(attr) is not None:      # Priority-1: enviornment variables
            return os.getenv(attr)
        if hasattr(default, attr):              # Priority-2: default.py
            return getattr(default, attr)
        raise KeyError(f"Configuration key missing: {attr}")
