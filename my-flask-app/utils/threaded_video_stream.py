from threading import Thread
from imutils.video import WebcamVideoStream
from imutils.video import FPS
from cv2 import VideoCapture

class WebcamVideoStream:
    def __init__(self, src=2):
        self.stream = VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True