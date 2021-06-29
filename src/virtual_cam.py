# -*- coding: utf-8 -*-
"""

"""

import pyvirtualcam

class VirtualCam():
    def __init__(self, width = 1280, height = 720, fps = 30) -> None:
        self._Cam = pyvirtualcam.Camera(width=width, height=height, fps=fps)
        print(f'Using virtual camera: {self._Cam.device}')

    def send(self, image) -> None:
        self._Cam.send(image)
