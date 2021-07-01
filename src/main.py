# -*- coding: utf-8 -*-
"""

"""

from os import error
import cv2
import argparse
import csv

import hands_detection as hd
import virtual_cam as vcam
import config as _

def build_parser() -> object:
    parser = argparse.ArgumentParser()

    parser.add_argument('--max_num_hands', action='store', dest='max_num_hands',
                        default=2, type=int,
                        help='Maximum Number of Hands on Detection and Tracking, Default = 2')
    parser.add_argument('--min_detection_threshold', action='store', dest='min_detection_threshold',
                        default=0.7, type=float,
                        help='Minimum Threshold Score for Hand Detection, Default = 0.7')
    parser.add_argument('--min_tracking_threshold', action='store', dest='min_tracking_threshold',
                        default=0.7, type=float,
                        help='Minimum Threshold Score for Hand Tracking, Default = 0.7')
    parser.add_argument('-v', '--verbose', action='store_true', dest='verbose',
                        help="Verbose the Debug Information, Default = False")
    parser.add_argument('-d', '--debug', action='store_true', dest='debug',
                        help='Enable Debug Window, Default = True')
    parser.add_argument('--window_width', action='store', dest='window_width',
                        default=1280, type=int,
                        help='Debug Window Width, Default = 1280')
    parser.add_argument('--window_height', action='store', dest='window_height',
                        default=720, type=int,
                        help='Debug Window height, Default = 720')
    parser.add_argument('--window_fps', action='store', dest='window_fps',
                        default=30, type=int,
                        help='Debug Window FPS, Default = 30')

    return parser

def log_gesture_keypoints(mode, hand_results) -> None:
    is_empty = isinstance(hand_results.multi_hand_landmarks, type(None))

    if (is_empty):
        return None

    if (_.mode == _.Mode.LOG_SIGN_GESTURE):
        with open(_.SIGN_GESTURE_FILE_PATH, 'a', newline="") as file:
            writer = csv.writer(file)
            # TODO: think of data format to logout (class, data)

    elif (_.mode == _.Mode.LOG_MOTION_GESTURE):
        with open(_.MOTION_GESTURE_FILE_PATH, 'a', newline="") as file:
            writer = csv.writer(file)
            # TODO: think of data format to logout (class, data)
    return


def handle_key_events(key, is_quiet) -> None:

    if (key == _.LOG_CODE_SIGN_GESTURE):
        _.mode = _.Mode.LOG_SIGN_GESTURE
    elif (key == _.LOG_CODE_MOTION_GESTURE):
        _.mode = _.Mode.LOG_MOTION_GESTURE
    elif (key == _.DEBUG_CODE and is_quiet):
        _.mode = _.Mode.QUIET
    elif (key == _.DEBUG_CODE and not is_quiet):
        _.mode = _.Mode.DEBUG
    elif (key == _.QUIET_CODE):
        _.mode = _.Mode.QUIET

    return None

def main():

    # Create Parser to parse the arguments
    parser = build_parser()
    args = parser.parse_args()

    if (not args.debug):
        _.mode = _.Mode.QUIET

    # capture the video frame with native camera
    cap = cv2.VideoCapture(0)

    # initial the hands detector
    hands_detector = hd.HandsDetector(
        max_num_hands=args.max_num_hands,
        min_detection_confidence=args.min_detection_threshold,
        min_tracking_confidence=args.min_tracking_threshold)
    hands_drawing = hands_detector.get_mphands_drawing()
    hands_skeletons = hands_detector.get_mphands()

    # initial virtual camera
    virtual_cam = vcam.VirtualCam(width=args.window_width,
                                  height=args.window_height,
                                  fps=args.window_fps)

    # capture the current video stream
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        key = cv2.waitKey(5) & 0xFF

        if (key == _.QUIT_CODE):
            cv2.destroyAllWindows()
            break
        else:
            handle_key_events(key, not args.debug)

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False

        hands_results = hands_detector.get_hands_results(image)

        if (_.mode == _.Mode.LOG_MOTION_GESTURE or _.mode == _.Mode.LOG_SIGN_GESTURE):
            log_gesture_keypoints(_.mode, hands_results)

        # Draw the hand annotations on the image.
        image.flags.writeable = True

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        print(hands_results.multi_hand_landmarks)

        if hands_results.multi_hand_landmarks:
          for hand_landmarks in hands_results.multi_hand_landmarks:
              hands_drawing.draw_landmarks(
                image, # input image
                hand_landmarks, # landmark positions
                hands_skeletons.HAND_CONNECTIONS, # lankmark connections
                # landmark 's drawing settings: color, line thickness, and circle radius.
                hands_drawing.DrawingSpec(color=_.WHITE_COLOR, thickness=_.LINE_THICKNESS, circle_radius=_.CIRCLE_RADIUS),
                  # connection 's drawing settings: color and line thickness.
                hands_drawing.DrawingSpec(color=_.SILVER_COLOR, thickness=_.LINE_THICKNESS))

        if (_.mode != _.Mode.QUIET):
            cv2.imshow('Hands', image)
        else:
            cv2.destroyAllWindows()


    cap.release()

if __name__ == "__main__":

    main()

