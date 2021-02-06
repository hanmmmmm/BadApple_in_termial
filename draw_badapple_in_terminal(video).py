import os
import cv2
import time
import numpy as np
np.set_printoptions(threshold=np.inf)
from colorama import *

cap = cv2.VideoCapture('badapple.mp4')

size = (80, 30)

init()

def move (y, x):
    return ("\033[%d;%dH" % (y, x))

count = 0

t_print_last = time.time() * 1000000

while(cap.isOpened()):

    ret, frame = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = frame[:,:,0] # one channel can reprenst the color intensity 

    resize_gray = cv2.resize(gray, size ) 
    ret,thresh1 = cv2.threshold(resize_gray,10,255,cv2.THRESH_BINARY)
    c = (thresh1 < 3).astype(int)
    thresh1_str = np.array2string(c, max_line_width=np.inf)

    thresh1_str = thresh1_str.replace(" ", "") # remove white spaces
    thresh1_str = thresh1_str.replace("[", "") # remove [
    thresh1_str = thresh1_str.replace("]", "") # remove ]
    thresh1_str = thresh1_str.replace("0", '&')# "\u2588" is solid block
    thresh1_str = thresh1_str.replace("1", " ")

    if count %200 == 0: # clear terminal once awhile 
        os.system('cls')
    
    #os.system('cls')
    #print ("\n" * 30)

    print("\033[12A");

    #pos = move(0, 0)
    #print( Fore.RED + pos + thresh1_str)
    #print(chr(27) + "[2J")
    
    #print( thresh1_str) # print the content to terminal 
    
    t_print = time.time() * 1000000
    t_interval = t_print - t_print_last
    t_print_last = t_print
    fps = 1000000.0/t_interval
    info_str = 'frame # ' + str(count) + '   FPS: ' + str(fps)[:4] + '   '
    info_str_len = len(info_str)
    content_string_posi = size[0]*(size[1])-51
    thresh1_str_list = list(thresh1_str)
    thresh1_str_list[content_string_posi: content_string_posi+info_str_len+1] = info_str
    thresh1_str = "".join(thresh1_str_list)
    print( thresh1_str) # print the content to terminal 
    count += 1

    cv2.imshow('video',gray)

    #print(t_process_img - t_loop_start ,t_to_str - t_process_img, t_str_modify-t_to_str, t_clear_term-t_str_modify,t_print-t_clear_term   )

    if cv2.waitKey(28) & 0xFF == ord('q'):
        break

    
cap.release()
cv2.destroyAllWindows()

#os.system('cls')




