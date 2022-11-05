import cv2

if __name__ == "__main__":

    cap = cv2.VideoCapture(0)

    #Get the width, height, and fps
    out_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    out_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fps = cap.get(cv2.CAP_PROP_FPS)

    out = cv2.VideoWriter("result.mp4", cv2.VideoWriter_fourcc(
        *'MP4V'), fps, (out_w, out_h))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret is False:
            break

        frame = cv2.flip(frame, 1)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
