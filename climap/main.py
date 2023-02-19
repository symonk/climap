"""" The main logic of the live terminal output.

Exit codes are as follows:
    1 - Unable to establish a connection to the imap server.
    2 - An issue with authenticating occurred, likely invalid credentials.
"""

import imaplib
import time

from rich import print
from rich.live import Live
from rich.prompt import IntPrompt
from rich.prompt import Prompt

from .__version__ import __version__
from ._client import Client
from ._config import Configuration
from ._console import console
from ._initialiser import SessionView
from ._layout import generate_base_layout


def main() -> int:
    """Main entry point into cli map."""
    config: Configuration = initialise()
    layout = generate_base_layout(config=config)
    init = SessionView(config=config)
    with Live(renderable=init, console=console, refresh_per_second=20) as live:
        time.sleep(1)  # mock for now.
        try:
            with Client(config=config) as client:  # noqa
                while True:
                    live.update(layout)
                    time.sleep(10)  # mock for now.
                    break
        except ConnectionError:
            return 1
        except imaplib.IMAP4.error:
            return 2
    return 0


def initialise() -> Configuration:
    """Prompt for configuration."""
    print(f"[{__version__} Successfully loaded.]")
    host = Prompt().ask(":rocket: What is the host of the imap server", default="localhost")
    port = IntPrompt().ask(":rocket: What is the port of the imap server", default=993)
    ssl = IntPrompt().ask(":rocket: Use an ssl client", default=True)
    user = Prompt().ask(":couple: What is the imap username")
    password = Prompt().ask(":unlock: Enter the password", password=True)
    return Configuration(host=host, port=port, ssl=ssl, user=user, password=password)


if __name__ == "__main__":
    raise SystemExit(main())
