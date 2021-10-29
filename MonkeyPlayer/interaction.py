import time
from AndroidRunner.Device import Device

default_wait_time = 4

def tap(device: Device, x: int, y: int, sleep = 0) -> None:
    device.shell('input tap %s %s' % (x, y))
    # We need to wait for the display to update after the last click.
    # The time to update is vary.
    time.sleep(sleep)


def main(device: Device, *args, **kwargs) -> None:
    # Do task 1
    # click ____
    tap(device, 348, 226, default_wait_time * 2)

    # click ____
    tap(device, 348, 226)

    # click ____ this takes longer to load, wait more time
    tap(device, 712, 96, default_wait_time * 2)
    tap(device, 155, 810, default_wait_time)
    tap(device, 186, 1069, default_wait_time)
    tap(device, 146, 850, default_wait_time)
    # # Do task 2
    # # click ____
    # tap(device, 1300, 400)
    #
    # # click ____
    # tap(device, 1089, 2528)
    #
    # # click ____
    # tap(device, 1228, 517)
