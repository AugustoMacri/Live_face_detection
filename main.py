import threading
import logging

import cv2
from deepface import DeepFace  # Neural network behind the face recognition


# First we need to capture the video
# 0 cus we want to use the first camera
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

# now we will config the frame of the video
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# we did not want to  test in every frame, so now we will put a counter to do this once in a while
counter = 0

face_match = False

reference_img = cv2.imread("reference.jpg")


def check_face(frame):
    global face_match

    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True
        else:
            face_match = False

    except:
        face_match = False


while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:  # each 30 frames
            try:
                threading.Thread(target=check_face,
                                 args=(frame.copy(),)).start()
            except ValueError as e:
                logging.error(f"Thread error: {e}")

        counter += 1

        if face_match:
            cv2.putText(frame, "MATCH!", (20, 450),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("video", frame)  # This will show the results

    key = cv2.waitKey(1)
    if key == ord("q"):
        break


cv2.destroyAllWindows()
