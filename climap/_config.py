from dataclasses import dataclass
from typing import TypedDict


class ClientArgs(TypedDict):
    """Encapsulation of a plain IMAP authentication scheme."""

    host: str
    port: int


@dataclass(frozen=True)
class Configuration:
    """An encapsulation of the runtime configuration."""

    user: str
    password: str
    host: str = "localhost"
    port: int = 993
    ssl: bool = True

    @property
    def client_args(self) -> ClientArgs:
        return {
            "host": self.host,
            "port": self.port,
        }
