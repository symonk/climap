from rich.panel import Panel
from rich.spinner import Spinner

from ._config import Configuration


class SessionView:
    def __init__(self, config: Configuration) -> None:
        self.config = config

    def __rich__(self) -> Panel:
        return Panel(
            title="Initialising Session",
            renderable=Spinner(name="aesthetic", text="hello world"),
        )
