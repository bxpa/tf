import time

from tf import tf


@tf(precision=1, time_format="ms")
def test_func_short():
    time.sleep(0.5)


@tf(precision=2, time_format="sec")
def test_func_medium():
    time.sleep(2)


@tf(precision=1, time_format="min")
def test_func_long():
    time.sleep(10)


@tf(time_format='sec')
def test_func_default():
    time.sleep(1.25)


if __name__ == "__main__":
    test_func_short()
    test_func_medium()
    test_func_long()
    test_func_default()