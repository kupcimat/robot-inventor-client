import serial
from serial.threaded import ReaderThread

from client.protocol import RobotInventorProtocol


class RobotInventorClient:
    def __init__(self, port: str):
        self.port = port

    def start(self):
        serial_instance = serial.serial_for_url(self.port, baudrate=115200, timeout=1)
        self.reader = ReaderThread(serial_instance, RobotInventorProtocol)
        self.reader.start()
        _, self.protocol = self.reader.connect()

    def close(self):
        self.reader.close()

    def __enter__(self) -> RobotInventorProtocol:
        self.start()
        return self.protocol

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
