import logging

from serial.threaded import LineReader

logger = logging.getLogger()


class RobotInventorProtocol(LineReader):

    TERMINATOR = b"\r"

    def connection_made(self, transport):
        super().connection_made(transport)
        logger.info("port opened")

    def handle_line(self, line):
        logger.info(f"line received: {line}")

    def connection_lost(self, exc):
        if exc:
            logger.exception("serial error", exc)
        logger.info("port closed")
