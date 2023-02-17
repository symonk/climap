from __future__ import annotations

import types
import typing
from imaplib import IMAP4
from imaplib import IMAP4_SSL

CLIENT_FACTORY = {993: IMAP4_SSL, 143: IMAP4}


class Client:
    """An encapsulation of an IMAP Client.  This client is underpinned by
    either a IMAP4 client if port 143 is provided otherwise it utilises an
    IMAP4_SSL Client.

    :param host: The imap server host.
    :param port: The imap server port.
    """

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self._delegate = CLIENT_FACTORY.get(self.port, IMAP4)(host=self.host, port=port)

    def __enter__(self) -> Client:
        return self

    def __exit__(
        self,
        exc_type: typing.Optional[typing.Type[BaseException]] = None,
        exc_val: typing.Optional[BaseException] = None,
        exc_tb: typing.Optional[types.TracebackType] = None,
    ) -> None:
        """Allow the client to be used as a context manager itself."""
        self._delegate.__exit__(exc_type, exc_val, exc_tb)
