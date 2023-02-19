from rich.panel import Panel
from rich.text import Text

from ._config import Configuration
from ._version import VERSION


class _HeaderStyle:
    """Styling for the header object."""


class Header:
    """A renderable for the Application header."""

    def __init__(self, config: Configuration) -> None:
        self.config = config

    def __rich__(self) -> Text:
        return Panel(
            renderable=Text(
                text=f"Authenticated as {self.config.user} on {self.config.host}:{self.config.port}",
                style="red on white",
                justify="center",
            ),
            title=VERSION,
            style="green on black",
        )
