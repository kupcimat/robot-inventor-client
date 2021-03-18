import logging
import os
import time

import serial
from serial.threaded import LineReader, ReaderThread

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


port = os.getenv("PORT")
ser = serial.serial_for_url(port, baudrate=115200, timeout=1)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(message)s",
)
with ReaderThread(ser, RobotInventorProtocol) as protocol:
    # protocol.write_line(message)
    time.sleep(10)
