"""" The main logic of the live terminal output.

Exit codes are as follows:
    1 - Unable to establish a connection to the imap server.
    2 - An issue with authenticating occurred, likely invalid credentials.
"""

import imaplib
import time

from rich.live import Live

from ._client import Client
from ._commandline import handle_argv
from ._config import Configuration
from ._console import console
from ._initialiser import SessionView
from ._layout import generate_base_layout


def main() -> int:
    """Main entry point into cli map."""
    config: Configuration = handle_argv()
    init = SessionView(config=config)
    with Live(renderable=init, console=console, refresh_per_second=20) as live:
        time.sleep(1)  # mock for now.
        try:
            with Client(config=config) as client:  # noqa
                layout = generate_base_layout(config=config, client=client)
                while True:
                    live.update(layout)
                    time.sleep(10)  # mock for now.
                    break
        except ConnectionError:
            return 1
        except imaplib.IMAP4.error:
            return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
