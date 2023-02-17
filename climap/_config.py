from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    """An encapsulation of the runtime configuration."""

    host: str
    port: int = 993
