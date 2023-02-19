from rich.panel import Panel
from rich.text import Text

from ._client import Client


class FooterView:
    def __init__(self, client: Client) -> None:
        self.client = client

    def __rich__(self) -> Panel:
        return Panel(title="Footer", renderable=Text(text="placeholder", justify="center"))
