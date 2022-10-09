import cv2
import os
import time
import numpy as np

"""
Functionalities includes
- Concat n video frame to n windows
- Save to mp4
"""

videopath = r"C:\Users\codenamewei\Documents\deepfake\Wav2Lip\results"
path1 = r"C:\Users\codenamewei\Documents\deepfake\video_wav\chiawei_short.mp4"
path2 = os.path.join(videopath, "chiawei_wav2lip.mp4")


cap = cv2.VideoCapture(path1, 0)
cap1 = cv2.VideoCapture(path2, 0)

w = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

w_half = int(w/2)
h_half = int(h/2)

fps = cap1.get(cv2.CAP_PROP_FPS)

title = "Wav2Lip"

out_w = 1280
out_h = 360


out = cv2.VideoWriter("result.mp4", cv2.VideoWriter_fourcc(
    *'MP4V'), fps, (out_w, out_h))


if __name__ == "__main__":

    time.sleep(3)

    while(cap.isOpened()):

        ret, frame = cap.read()
        ret1, frame1 = cap1.read()

        if ret == True:

            resized_frame = cv2.resize(frame, (w_half, h_half))
            resized_frame1 = cv2.resize(frame1, (w_half, h_half))

            concatframe = np.concatenate(
                (resized_frame, resized_frame1), axis=1)

            # print(concatframe.shape) #concatframe.shape must match VideoWriter shape

            cv2.imshow(title, concatframe)
            out.write(concatframe)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break

    cap.release()
    out.release()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
