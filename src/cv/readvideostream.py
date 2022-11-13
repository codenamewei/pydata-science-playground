import cv2

if __name__ == "__main__":

    invideopath = "metadata/sample_video.mp4"

    videoreader = cv2.VideoCapture(invideopath)

    scale = 3
    w = int(videoreader.get(cv2.CAP_PROP_FRAME_WIDTH) / scale)
    h = int(videoreader.get(cv2.CAP_PROP_FRAME_HEIGHT) / scale)

    ret = True

    while ret is True:

        ret, frame = videoreader.read()

        if ret is False:
            break

        outframe = cv2.resize(frame, (w, h))

        cv2.imshow("win", outframe)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    videoreader.release()
    cv2.destroyAllWindows()
