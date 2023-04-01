__all__ = ['init_logging']

import logging
from pathlib import Path
from typing import Optional

import coloredlogs


VERBOSE = 5
MAX_MODNAME_LEN = 20
LOG_FMT = (
    '%(asctime)s %(process)d %(levelname)s %(name)s:%(lineno)s %(message)s'
)


def init_logging(level_name: str = 'debug', fmt: Optional[str] = None):
    logging.addLevelName(logging.FATAL, 'F')
    logging.addLevelName(logging.ERROR, 'E')
    logging.addLevelName(logging.WARNING, 'W')
    logging.addLevelName(logging.INFO, 'I')
    logging.addLevelName(logging.DEBUG, 'D')
    logging.addLevelName(VERBOSE, 'V')

    coloredlogs.DEFAULT_LEVEL_STYLES = {
        'C': {'bold': True, 'color': 'red'},
        'D': {'faint': True},
        'E': {'color': 'red'},
        'I': {},
        'N': {'color': 'magenta'},
        'P': {'color': 'green', 'faint': True},
        'S': {'bold': True, 'color': 'green'},
        'V': {'color': 'blue'},
        'W': {'color': 'yellow'},
    }

    fmt = fmt or LOG_FMT
    log_level = (
        VERBOSE
        if level_name == 'verbose'
        else getattr(logging, level_name.upper())
    )

    coloredlogs.install(level=level_name, fmt=fmt)

    logging.getLogger('matplotlib.font_manager').disabled = True
    logging.getLogger('matplotlib').setLevel(logging.ERROR)
    logging.getLogger('h5py').setLevel(logging.ERROR)
    logging.basicConfig(format=fmt, level=log_level)
    logger = logging.getLogger()

    return logger
