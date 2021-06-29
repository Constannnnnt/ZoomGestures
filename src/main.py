# -*- coding: utf-8 -*-
"""

"""

import cv2

import hands_detection as hd
import virtual_cam

if __name__ == "__main__":
    # capture the video frame with native camera
    cap = cv2.VideoCapture(0)

    # initial the hands detector
    hands_detector = hd.HandsDetector(
        max_num_hands=2, min_detection_confidence=0.6, min_tracking_confidence=0.6)
    hands_drawing = hands_detector.get_mphands_drawing()
    hands_skeletons = hands_detector.get_mphands()

    # initial virtual camera
    virtual_cam = virtual_cam.VirtualCam(width=1280, height=720, fps=30)

    # capture the curretn
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False

        hands_results = hands_detector.get_hands_results(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if hands_results.multi_hand_landmarks:
          for hand_landmarks in hands_results.multi_hand_landmarks:
              hands_drawing.draw_landmarks(
                  image, hand_landmarks, hands_skeletons.HAND_CONNECTIONS)

        cv2.imshow('Hands', image)

        # press q to exit the program
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cap.release()

