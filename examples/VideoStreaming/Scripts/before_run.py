# noinspection PyUnusedLocal
import time
import os
from AndroidRunner.Device import Device

def main(device, *args, **kwargs):

    video_youtube(device, "360p", "https://www.youtube.com/watch?v=1YaTfmeRu98end=0")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=MffmJdVVJy4")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=oEEEnwr5azI")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=KY3vUWPwWr4")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=hlqJxgsR2ic")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=_7Tq7QJd7zc")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=oZ4nuod4jyc")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=fBSgTCyaE6o")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=Gth1_XbcxYQ")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=AKqny63UCM0")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=Uqd_15i0YbQ")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=hXKnFj51OQI")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=v_Mff0JqjEM")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=WyIvl5dPxDE")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=hTMvoVVdBP8")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=_UZNNGYgcjQ")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=KlpE7B6hCTY")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=-Nx0ucWFCto")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=TXIYTO_MvKA")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=by6w1KLAyWM")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=e5dxEQ5q9Q8")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=vdsw1f3rs2M")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=-VsLqn9i95Q")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=HPCmLXqGqUM")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=oZlYPyJuMM8")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=gqCUZiXNcQo")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=hY0WfJifcM4")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=9OfeNDukXm8")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=0_-pAvA5YII")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=ddgKA7-v_MM")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=ACQyYbUFmEU")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=mh9bZCKG-CM")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=xc61U1aFkik")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=E60lnvda7Kw")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=vabwGiTWRVo")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=GWenb9Noq_A")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=aGWbuyoIBF0")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=OSKRQWFAXcQ")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=QqknSms8VVI")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=udTdL-NTPRc")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=JySMUhT6Jso")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=OaXRdvsCRsI")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=WJwx-XJWVU0")
    video_youtube(device, "360p", "https://www.youtube.com/watch?v=HgFqvplXml4")

def tap(device: Device, x: int, y: int, sleep = 0) -> None:
    device.shell('input tap %s %s' % (x, y))
    # We need to wait for the display to update after the last click.
    # The time to update is vary.
    time.sleep(sleep)

def video_youtube(device, quality, url):
    os.system("echo Hello from the other side!")
    os.system("adb shell am start -a android.intent.action.VIEW '"+url+"'")

    default_wait_time = 4

    tap(device, 348, 226, default_wait_time * 2)

    # click ____
    tap(device, 348, 226)

    # click ____ this takes longer to load, wait more time
    tap(device, 712, 96, default_wait_time * 2)
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
