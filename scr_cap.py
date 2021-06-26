import cv2 as cv
import time
import numpy as np
import os
import mss
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    with mss.mss() as sct:
        #define color
        color = "grayscale"
        #color = "rgb"

        args = get_screen()
        screen = {"top": int(args[1]), "left": int(args[0]), "width": int(args[2]), "height": int(args[3])}

        #while input not 'q'
        while(True):

            start_time  = time.time()
            screen_np = np.array(sct.grab(screen))

            if(color == "rgb"):
                cv.imshow("OpenCV RGB",screen_np)
            elif(color == "grayscale"):
                cv.imshow("OpenCV Grayscale",cv.cvtColor(screen_np,cv.COLOR_BGR2GRAY))

            print("FPS : {}".format(1/(time.time()-start_time)))

            if(cv.waitKey(1) == ord('q')):
                cv.destroyAllWindows()
                break
    

def get_screen():
    
    _screen = re.split(", {",str(mss.mss().monitors))
    print("Monitors : ",int(len(_screen)/2))

    for i in range(0,len(_screen)) :
        _screen[i] = _screen[i].replace("[","")
        _screen[i] = _screen[i].replace("]","")
        _screen[i] = _screen[i].replace("'","\"")
        if(i > 0):
           _screen[i] = "{" + _screen[i]
    
    for i in range(0, int(len(_screen)/2)) :
        _tmp_dimensions = re.findall('\d+',_screen[i])
        _tmp_width = _tmp_dimensions[2]
        _tmp_height = _tmp_dimensions[3]
        print("Screen ",i," : ",_tmp_width,"x",_tmp_height)
        i=i+1

    _answer = input("Select monitor : ")
    _answer_screen = str(_screen[int(_answer)])
    _ret_array = re.findall('\d+',_answer_screen)
    return _ret_array

    
if __name__ == "__main__":
    main()


