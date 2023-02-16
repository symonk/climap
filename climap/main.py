import time

from rich.console import Console
from rich.live import Live
from rich.prompt import Prompt
from rich.prompt import IntPrompt
from ._layout import layout

console = Console()


def main() -> int:
    host = Prompt().ask(":rocket: [bold green]Host: [/bold green]", default="localhost")
    port = IntPrompt().ask(":rocket: [bold green]Port: [/bold green]", default=993)
    with Live(layout):
        while True:
            time.sleep(1)
    return 0
