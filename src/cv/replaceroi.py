import cv2
import numpy as np

# https://stackoverflow.com/questions/40895785/using-opencv-to-overlay-transparent-image-onto-another-image

if __name__ == "__main__":
    

    background = cv2.imread('metadata/background.jpg')
    overlay = cv2.imread("metadata/heart_eyes.png")
    
    overlay = cv2.resize(overlay, (150,150))
    # overlay = for_transparent_removal(overlay)
    h, w = overlay.shape[:2]
    
    startpos = (200, 500)
    
    #https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html
    #Return an array of zeros with the same shape and type as a given array.
    shapes = np.zeros_like(background, np.uint8)
    
    shapes[startpos[0]:(startpos[0]+h), startpos[1]:(startpos[1]+w)] = overlay
    
    alpha : float = 1.0
    
    mask = shapes.astype(bool)

    # option first
    background[mask] = cv2.addWeighted(shapes, alpha, shapes, 1 - alpha, 0)[mask]
    cv2.imwrite('combined.png', background)
    
    print("complete")