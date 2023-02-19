from rich.panel import Panel
from rich.text import Text

from .__version__ import __version__
from ._config import Configuration


class HeaderView:
    """A renderable for the Application header."""

    def __init__(self, config: Configuration) -> None:
        self.config = config
        self.version = __version__

    def __rich__(self) -> Text:
        return Panel(
            renderable=Text(
                text=f"Authenticated as {self.config.user} on {self.config.host}:{self.config.port}",
                justify="center",
            ),
            title="climap",
        )
