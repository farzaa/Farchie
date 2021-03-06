import cv2
import sys
from face_detective import mark_faces
from object_detective import mark_plates


class Detective():
    ui = None

    def __init__(self, ui):
        self.ui = ui
        pass

    def track_faces(self):
        video_capture = cv2.VideoCapture(0)
        #video_capture_front = cv2.VideoCapture(1)

        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()
            #ret_front, frame_front = video_capture_front.read()
            frame = cv2.resize(frame, None,fx=0.4, fy=0.4, interpolation = cv2.INTER_CUBIC)
            
            #frame_front = cv2.resize(frame_front,5k None,fx=0.3, fy=0.3, interpolation = cv2.INTER_CUBIC)
            txt, sleep, focused = mark_faces(frame)
            #mark_plates(frame_front)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            #cv2.imshow('Video_Front', frame_front)

            # Send true or false params over to UI.
            self.ui.change_colors(txt, sleep, focused)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        # When everything is done, release the capture
        video_capture.release()
        #video_capture_front.release()
        cv2.destroyAllWindows()


