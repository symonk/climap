from rich.panel import Panel
from rich.tree import Tree

from ._client import Client


class MailboxView:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.items = [name.decode() for name in self.client.retrieve_mailboxes()[1]]  # type: ignore [union-attr]
        self.tree = Tree(label="Mailboxes")
        for item in self.items:
            self.tree.add(item)

    def __rich__(self) -> Panel:
        return Panel(renderable=self.tree)
