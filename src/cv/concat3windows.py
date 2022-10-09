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
path0 = r"C:\Users\codenamewei\Documents\deepfake\video_wav\chiawei_short.mp4"
path1 = os.path.join(videopath, "chiawei_wav2lip.mp4")
path2 = os.path.join(videopath, "chiawei_wav2lipgan.mp4")

cap0 = cv2.VideoCapture(path0, 0)
cap1 = cv2.VideoCapture(path1, 0)
cap2 = cv2.VideoCapture(path2, 0)

w = int(cap0.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap0.get(cv2.CAP_PROP_FRAME_HEIGHT))

w_half = int(w/3)
h_half = int(h/3)

fps = cap0.get(cv2.CAP_PROP_FPS)

title = "Wav2Lip"

out_w = 1278
out_h = 240

out = cv2.VideoWriter("result.mp4", cv2.VideoWriter_fourcc(
    *'MP4V'), fps, (out_w, out_h))


if __name__ == "__main__":

    time.sleep(3)

    while(cap1.isOpened()):

        ret0, frame0 = cap0.read()
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if ret1 == True:

            resized_frame0 = cv2.resize(frame0, (w_half, h_half))
            resized_frame1 = cv2.resize(frame1, (w_half, h_half))
            resized_frame2 = cv2.resize(frame2, (w_half, h_half))

            concatframe = np.concatenate(
                (resized_frame0, resized_frame1, resized_frame2), axis=1)

            #print(concatframe.shape)

            cv2.imshow(title, concatframe)
            out.write(concatframe)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break

    cap0.release()
    cap1.release()
    cap2.release()
    out.release()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
