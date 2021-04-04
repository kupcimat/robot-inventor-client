import json
import logging
from dataclasses import dataclass
from typing import Any, Dict

from serial.threaded import LineReader

logger = logging.getLogger()


@dataclass
class Message:
    id: str
    method: str
    params: Any

    def to_dict(self) -> Dict[str, Any]:
        return {"i": self.id, "m": self.method, "p": self.params}


class RobotInventorProtocol(LineReader):

    TERMINATOR = b"\r"

    def connection_made(self, transport):
        super().connection_made(transport)
        logger.info("port opened")

    def handle_line(self, line):
        self._handle_message(line)

    def connection_lost(self, exc):
        if exc:
            logger.error("serial error", exc_info=exc)
        logger.info("port closed")

    def send_meessage(self, message: Message):
        message_json = json.dumps(message.to_dict())
        self.write_line(message_json)
        logger.debug(f"message sent: {message_json}")

    def _handle_message(self, line: str):
        try:
            message_data = json.loads(line)
        except json.JSONDecodeError:
            logger.warning(f"json decode error: {line}")
        else:
            logger.debug(f"message received: {line}")
