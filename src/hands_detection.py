# -*- coding: utf-8 -*-
"""

"""

import mediapipe as mp

class HandsDetector():
    def __init__(self, max_num_hands = 2, min_detection_confidence = 0.5, min_tracking_confidence = 0.5) -> None:
        self._mphands = mp.solutions.hands
        self._hands = self._mphands.Hands(max_num_hands=max_num_hands,
                                          min_detection_confidence=min_detection_confidence,
                                          min_tracking_confidence=min_tracking_confidence)
        self._mpdrawing = mp.solutions.drawing_utils
        self._hands_results = None

    def get_hands_results(self, image) -> object:
        self.__detect_hands__(image)
        return self._hands_results

    def get_mphands_drawing(self) -> object:
        return self._mpdrawing

    def get_mphands(self) -> object:
        return self._mphands

    def __detect_hands__(self, image) -> None:
        self._hands_results = self._hands.process(image)
