import cv2

import numpy as np

if __name__ == "__main__":

    invideopath = "metadata/sample_video.mp4"

    videoreader = cv2.VideoCapture(invideopath)

    placeholder = []

    scale = 3
    w = int(videoreader.get(cv2.CAP_PROP_FRAME_WIDTH) / scale)
    h = int(videoreader.get(cv2.CAP_PROP_FRAME_HEIGHT) / scale)

    ret = True

    while ret is True:

        ret, frame = videoreader.read()

        if ret is False:
            break

        outframe = cv2.resize(frame, (w, h))

        placeholder.append(outframe)

    videoreader.release()
    cv2.destroyAllWindows()

    # stack array of np.array into one
    npvideo = np.stack(placeholder, axis=0)

    videodtype = npvideo.dtype  # "uint8" : str
    videoshape = npvideo.shape  # (138, 480, 853, 3) : tuple

    # numpy nparray -> bytes: when save frame to bytes to save in db
    videoinbytes = npvideo.tobytes()

    # bytes -> numpy nparray: after extract from database and become stream of numpy array to show
    videoinnumpyarray = np.frombuffer(videoinbytes, dtype=videodtype)

    # stream videoinnumpyarray
    outvideo = np.reshape(videoinnumpyarray, videoshape)

    for i in range(0, outvideo.shape[0]):

        outframe = outvideo[i, :, :, :]

        cv2.imshow("win", outframe)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
