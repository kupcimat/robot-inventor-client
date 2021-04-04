import logging
import os
import time

from client.client import RobotInventorClient
from client.utils import setup_logging


if __name__ == "__main__":
    setup_logging(level=logging.DEBUG)

    port = os.environ["PORT"]

    with RobotInventorClient(port) as protocol:
        time.sleep(10)
