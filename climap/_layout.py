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
    header = Layout(name="header", renderable=HeaderView(config), size=2)
    meta_data = Layout(name="metadata")
    footer = Layout(name="footer", renderable=FooterView(client=client), size=2)
    base.split(header, meta_data, footer)
    base["metadata"].split_row(
        Layout(name="meta"),
        Layout(name="emails"),
    )
    base["metadata"]["meta"].split_column(Layout(name="Connection"), Layout(name="Mailboxes"))
    base["metadata"]["meta"]["Connection"].split_row(Layout(name="connection_info"), Layout(name="tasks"))
    return base
