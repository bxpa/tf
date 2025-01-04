import time

from tf import tf


@tf
def sample():
    time.sleep(1)


if __name__ == "__main__":
    sample()
