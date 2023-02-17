import time
import typing

from rich import print
from rich.console import Console
from rich.live import Live
from rich.prompt import IntPrompt
from rich.prompt import Prompt
from rich.spinner import Spinner

from .__version__ import __version__
from ._client import Client
from ._layout import layout

console = Console()


def main() -> int:
    """Main entry point into cli map."""
    host, port = initialise()
    spinner = Spinner(name="aesthetic", text="Connecting to the imap server...")
    with Live(spinner) as live:
        with Client(host=host, port=port):
            live.update(layout)
            while True:
                time.sleep(10)
                break
    return 0


def initialise() -> typing.Tuple[str, int]:
    """Prompt for configuration."""
    print(f"[{__version__} Successfully loaded.]")
    host = Prompt().ask(":rocket: What is the host of the imap server", default="localhost")
    port = IntPrompt().ask(":rocket: What is the port of the imap server", default=993)
    return host, port


if __name__ == "__main__":
    raise SystemExit(main())
