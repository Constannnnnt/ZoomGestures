# -*- coding: utf-8 -*-
"""

"""

from enum import IntEnum, unique

@unique
class Mode(IntEnum):
    DEBUG = 0,
    LOG_SIGN_GESTURE = 1,
    LOG_MOTION_GESTURE = 2,
    QUIET = 3

mode = Mode.DEBUG

# visualization variables
RGB_CHANNELS = 3
RED_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 128, 0)
BLUE_COLOR = (255, 0, 0)
WHITE_COLOR = (255, 255, 255)
SILVER_COLOR = (192, 192, 192)
LINE_THICKNESS = 2
CIRCLE_RADIUS = 5

# keycode variables
QUIT_CODE = ord('q')
LOG_CODE_SIGN_GESTURE = ord('n')
LOG_CODE_MOTION_GESTURE = ord('m')
DEBUG_CODE = ord('d')
QUIET_CODE = ord('e')

# file path
SIGN_GESTURE_FILE_PATH = '../data/sign_gesture.csv'
MOTION_GESTURE_FILE_PATH = '../data/motion_gesture.csv'




