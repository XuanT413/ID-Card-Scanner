import cv2
import time as time
class WebCamCap:

    cam = cv2.VideoCapture(0)

    def __init__(self):
        self.name = None
        
    def Capture(self):
        cv2.namedWindow("test")
##        img_counter = 0

        while True:
            ret, frame = self.cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                self.name = "Capture {}.png".format(time.ctime().replace(':', '_'))
                cv2.imwrite(self.name, frame)
##                print("{} written!".format(self.name))
##                img_counter += 1
                break

##        self.cam.release()

        cv2.destroyAllWindows()
        
    def get_name(self):
        return self.name
    
    def res_1080p(self):
        self.cam.set(3, 1920)
        self.cam.set(4, 1080)

    def res_720p(self):
        self.cam.set(3, 1280)
        self.cam.set(4, 720)

    def res_480p(self):
        self.cam.set(3, 640)
        self.cam.set(4, 480)

