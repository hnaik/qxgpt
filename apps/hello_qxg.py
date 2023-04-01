import logging
import os
from argparse import ArgumentParser

import openapi

from qxg.log import init_logging
from qxg.secrets import SECRET_KEY

LOG = logging.getLogger('hello_qxg')
os.environ['OPENAI_API_KEY'] = SECRET_KEY
openapi.api_key = SECRET_KEY


def main(args):
    LOG.info('Starting ...')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '--log-level',
        default='info',
        choices=['debug', 'info', 'warning', 'error', 'fatal'],
    )
    args = parser.parse_args()
    init_logging(level_name=args.log_level)
    main(args)
