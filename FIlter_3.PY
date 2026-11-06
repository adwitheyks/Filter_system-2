import cv2
import random
import time


selection = 1

cap = cv2.VideoCapture(0)
while True:
    ret,frames = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 0, 255)
    
    
    
    

    if selection == 1:

        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        inv = 255 - gray 
        blur = cv2.GaussianBlur(inv, (25, 25), 0)
        div = cv2.divide(gray, 255 - blur, scale=256)
        sketch = cv2.cvtColor(div, cv2.COLOR_GRAY2BGR)
        sketch[:,:,0] = div
        sketch[:,:,1] = div
        sketch[:,:,2] = div
        
        base_filter = sketch

    elif selection == 2:
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        edges = cv2.Canny(blur, 50,150)
        
        black = edges * 0
        cycle = int(time.time() * 3) % 3
        if cycle == 0:
            neon_line = cv2.merge((black,edges,black))
        if cycle == 1:
            neon_line = cv2.merge((edges,black,edges))
        else:
            neon_line = cv2.merge((black,black,edges))
        
        neon_filter = frames
        neon_filter = cv2.add(neon_filter, neon_line)
        base_filter = neon_filter

    
    elif selection == 3:
        colorful = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(colorful, (5, 5), 0)
        small = cv2.resize(colorful, (64,48))
        pixelated = cv2.resize(small, (640,480), interpolation=cv2.INTER_NEAREST)
        canny = cv2.Canny(pixelated, 0 ,255)
        base_filter = canny
        


    elif selection == 4:
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9 ,9)
        color = cv2.bilateralFilter(frames, 9 ,300, 300)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        base_filter = cartoon

    elif selection == 5:
        small = cv2.resize(frames, (64,48))
        pixelated = cv2.resize(small, (640,480), interpolation=cv2.INTER_NEAREST)
        base_filter = pixelated
    
    cv2.imshow("Filter", base_filter)

    cv2.putText(base_filter, f"MODE: {selection}: 1:Sketch 2:Disco 3:Pixelated edges 4: cartoon 5: pixelated q: quit ",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

    key = cv2.waitKey(20) & 0xFF
    if key == ord("q"):
        break

    if key == ord("1"):
        selection = 1
    elif key == ord("2"):
        selection = 2
    elif key == ord("3"):
        selection = 3
    elif key == ord("4"):
        selection = 4
    elif key == ord("5"):
        selection = 5

cap.release()
cv2.destroyAllWindows()
    




