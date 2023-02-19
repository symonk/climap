import argparse
import os
from getpass import getpass

from ._config import Configuration


def handle_argv() -> Configuration:
    """Parse sys argv and generate a usable configuration object."""
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "--host",
        action="store",
        dest="host",
        default="localhost",
        help="The host address of the IMAP server.",
        type=str,
    )
    parser.add_argument(
        "--port",
        action="store",
        dest="port",
        default=993,
        type=int,
        help="The port of the IMAP server.",
    )
    parser.add_argument(
        "--ssl",
        action="store_false",
        dest="ssl",
        default=True,
        help="Whether or not to use an IMAP4_SSL client.",
    )
    parser.add_argument(
        "--user",
        action="store",
        dest="user",
        required=True,
        help="The user to use for plain imap auth.",
    )
    parser.add_argument(
        "--pass",
        action="store",
        dest="password",
        default=None,
        help="The (optional) password.  if not provided will lookup CLIMAP_PASS in the env before secure prompt.",
    )

    namespace = parser.parse_args()
    if namespace.password is None:
        namespace.password = os.environ.get("CLIMAP_PASSWORD") or getpass(prompt="Please enter your IMAP password")

    return Configuration(**vars(namespace))
