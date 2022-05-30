import cv2
import random
import numpy as np
fps=60
if __name__=="__main__":
    vc=cv2.VideoCapture("http://127.0.0.1:16384")
    pname=f"play{random.randint(0,65536)}"
    while True:
        ret,frame=vc.read()
        if not ret:
            break
        frame=cv2.resize(frame,(640,480))
        #framek=cv2.bilateralFilter(frame,10,10,10)
        framek=cv2.GaussianBlur(frame,(3,3),100)
        kframe=np.hstack([frame,framek])
        if cv2.waitKey(1000//fps)&0xFF==ord('q'):
            break
        cv2.imshow(pname,kframe)
    vc.release()