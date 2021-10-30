# noinspection PyUnusedLocal
import time
import os
from AndroidRunner.Device import Device

def main(device, *args, **kwargs):

    with open('/media/external/android-runner/examples/VideoStreaming/state.txt') as f:
        first_line = f.readline()
    print(first_line)

    video_youtube(device, "480p", first_line)


    with open('/media/external/android-runner/examples/VideoStreaming/state.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('/media/external/android-runner/examples/VideoStreaming/state.txt', 'w') as fout:
        fout.writelines(data[1:])

    
def tap(device: Device, x: int, y: int, sleep = 0) -> None:
    device.shell('input tap %s %s' % (x, y))
    # We need to wait for the display to update after the last click.
    # The time to update is vary.
    time.sleep(sleep)

def video_youtube(device, quality, url):
    os.system("echo Hello from the other side!")
    os.system("adb shell am start -a android.intent.action.VIEW '"+url+"'")

    default_wait_time = 4

    tap(device, 627, 354, default_wait_time + 3)

    tap(device, 627, 354, default_wait_time + 30)

    tap(device, 627, 354, default_wait_time)

    tap(device, 348, 226, default_wait_time + 5)

    # click ____
    tap(device, 348, 226)

    # click ____ this takes longer to load, wait more time
    tap(device, 712, 96, default_wait_time)
    tap(device, 155, 810, default_wait_time)
    tap(device, 186, 1069, default_wait_time)

    if quality == "360p":
        #320p
        tap(device, 162, 922, default_wait_time)

    if quality == "480p":
        # 480p
        tap(device, 146, 850, default_wait_time)

    if quality == "720p":
        #720p
        tap(device, 164, 765, default_wait_time)

    if quality == "1080p":
        ##1080p
        tap(device, 173, 680, default_wait_time)
