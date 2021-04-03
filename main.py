import os
import time

import serial
from serial.threaded import ReaderThread

from client.protocol import RobotInventorProtocol
from client.utils import setup_logging


if __name__ == "__main__":
    setup_logging()

    port = os.environ["PORT"]
    ser = serial.serial_for_url(port, baudrate=115200, timeout=1)

    with ReaderThread(ser, RobotInventorProtocol) as protocol:
        time.sleep(10)
