from rich.layout import Layout

from ._config import Configuration
from ._header import Header


def generate_base_layout(config: Configuration) -> Layout:
    """Generates the full screen layout for climap.

    :param config: The Configuration object.
    """

    base = Layout()
    header = Layout(name="header", renderable=Header(config), size=3)
    base.split(
        header,
    )
    return base
