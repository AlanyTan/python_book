"""Demo running a package as main module

Usage:
    $ python -m m6_3_package.m6_4_3
"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)


logger.debug(f"initialized package {__package__}")

