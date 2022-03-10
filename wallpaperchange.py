import struct
import ctypes
import requests
import os
import time


SPI_SETDESKWALLPAPER = 20



def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64


def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA


def change_wallpaper(WALLPAPER_PATH):
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)

    # When the SPI_SETDESKWALLPAPER flag is used,
    # SystemParametersInfo returns TRUE
    # unless there is an error (like when the specified file doesn't exist).
    if not r:
        print(ctypes.WinError())


while True:
    url = "https://micswallpaperapi.herokuapp.com/wallpaper"
    response = requests.get(url)
    file = open("sample_image.png", "wb")
    file.write(response.content)
    file.close()
    os.path.abspath("sample_image.png")
    change_wallpaper(os.path.abspath("sample_image.png"))
    os.remove("sample_image.png")
    time.sleep(30)




