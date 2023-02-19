from rich.layout import Layout

from ._client import Client
from ._config import Configuration
from ._footer import FooterView
from ._header import HeaderView


def generate_base_layout(config: Configuration, client: Client) -> Layout:
    """Generates the full screen layout for climap.

    :param config: The Configuration object.
    """

    base = Layout()
    header = Layout(name="header", renderable=HeaderView(config), size=3)
    meta_data = Layout(name="metadata", size=2)
    footer = Layout(name="footer", renderable=FooterView(client=client), size=3)
    base.split(header, meta_data, footer)
    base["metadata"].split_row(Layout(name="mailboxes"), Layout("name=emails"))
    return base
