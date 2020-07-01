import datetime
import math
import cv2
import numpy as np
import imutils

#variaveis globais
width = 0
height = 0
ContadorEntradas = 0
ContadorSaidas = 0
AreaContornoLimiteMin = 2000  #this value is empirical. Adjust it according to your need. 
ThresholdBinarizacao = 70  #this value is empirical. Adjust it according to your need.
OffsetLinhasRef = 150  #this value is empirical. Adjust it according to your need. reference line offset

#Check if the detected body is entering the monitored area
def TestaInterseccaoEntrada(y, CoordenadaYLinhaEntrada, CoordenadaYLinhaSaida):
    DiferencaAbsoluta = abs(y - CoordenadaYLinhaEntrada)

    if ((DiferencaAbsoluta <= 2) and (y < CoordenadaYLinhaSaida)):
        return 1
    else:
        return 0

#Check if the detected body is leaving the monitored area
def TestaInterseccaoSaida(y, CoordenadaYLinhaEntrada, CoordenadaYLinhaSaida):
    DiferencaAbsoluta = abs(y - CoordenadaYLinhaSaida)    

    if ((DiferencaAbsoluta <= 2) and (y > CoordenadaYLinhaEntrada)):
        return 1
    else:
        return 0

camera = cv2.VideoCapture(0)

#force the camera to have 640x480 resolution
camera.set(3,640)
camera.set(4,480)

PrimeiroFrame = None

# do some frame readings before considering the analysis
# motive: some cameras may take longer to "get used to the brightness" 
# when they turn on, capturing consecutive frames with a lot of brightness variation. 
# In order not to bring this effect to image processing, successive captures are made 
# outside the image processing, giving the camera time to "get used" to the brightness of the environment

for i in range(0,20):
    (grabbed, Frame) = camera.read()

while True:
    #le first frame and determines image resolution
    (grabbed, Frame) = camera.read()
    height = np.size(Frame,0)
    width = np.size(Frame,1)

    #if it was not possible to get a frame, nothing else should be done
    if not grabbed:
        break

    #converts frame to grayscale and applies blur effect (to highlight outlines)
    FrameGray = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
    FrameGray = cv2.GaussianBlur(FrameGray, (21, 21), 0)

    # as the comparison is made between two subsequent images, 
    # if the first frame is null (that is, the first "passed" in the loop), this is initialized
    if PrimeiroFrame is None:
        PrimeiroFrame = FrameGray
        continue

    #every absolute difference between starting frame and current frame (background subtraction)
    #also, make the frame binary with subtracted background 
    FrameDelta = cv2.absdiff(PrimeiroFrame, FrameGray)
    FrameThresh = cv2.threshold(FrameDelta, ThresholdBinarizacao, 255, cv2.THRESH_BINARY)[1]
    
    # makes the binarized frame expand, in order to eliminate "holes" / white areas within detected outlines. 
    # In this way, detected objects will be considered a "mass" of black color 
    # Moreover, find the contours after expansion.
    FrameThresh = cv2.dilate(FrameThresh, None, iterations=2)
    cnts = cv2.findContours(FrameThresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # _, cnts, _ = cv2.findContours(FrameThresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    QtdeContornos = 0

    #draw reference lines
    CoordenadaYLinhaEntrada = (height / 2) - OffsetLinhasRef
    CoordenadaYLinhaSaida = (height / 2) + OffsetLinhasRef
    #print(CoordenadaYLinhaEntrada) #90
    #print(CoordenadaYLinhaSaida) #390
    #print(width) #640
    #cv2.line(Frame, (0, 90), (640, 90), (255, 0, 0), 2)
    cv2.line(Frame, (0, int(CoordenadaYLinhaEntrada)), (int(width), int(CoordenadaYLinhaEntrada)), (255, 0, 0), 2)
    #cv2.line(Frame, (0, 390), (640, 390), (0, 0, 255), 2)
    cv2.line(Frame, (0, int(CoordenadaYLinhaSaida)), (int(width), int(CoordenadaYLinhaSaida)), (0, 0, 255), 2)


    #Sweep all found contours
    for c in cnts:
        #contours of very small area are ignored.
        if cv2.contourArea(c) < AreaContornoLimiteMin:
            continue

        #For debugging purposes, account for number of contours found
        QtdeContornos = QtdeContornos+1    

        # get contour coordinates (actually, a rectangle that can cover the entire contour) and
        #emphasizes the outline with a rectangle.
        (x, y, w, h) = cv2.boundingRect(c) #x e y: coordinates of the upper left vertex
                                           #w e h: width and height of the rectangle, respectively

        cv2.rectangle(Frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        #determines the center point of the contour and draws a circle to indicate
        CoordenadaXCentroContorno = (x+x+w)/2
        CoordenadaYCentroContorno = (y+y+h)/2
        PontoCentralContorno = (int(CoordenadaXCentroContorno),int(CoordenadaYCentroContorno))
        print(PontoCentralContorno)
        cv2.circle(Frame, PontoCentralContorno, 1, (0, 0, 0), 5)

        #testa intersection of the centers of the contours with the reference lines
        #dthis way, it counts which contours crossed which lines (in a certain direction)
        if (TestaInterseccaoEntrada(CoordenadaYCentroContorno,CoordenadaYLinhaEntrada,CoordenadaYLinhaSaida)):
            ContadorEntradas += 1

        if (TestaInterseccaoSaida(CoordenadaYCentroContorno,CoordenadaYLinhaEntrada,CoordenadaYLinhaSaida)):
            ContadorSaidas += 1

        #If necessary, uncomment the lines below to show the frames used in image processing
        #cv2.imshow("Frame binarizado", FrameThresh)
        #cv2.waitKey(1);
        #cv2.imshow("Frame com subtracao de background", FrameDelta)
        #cv2.waitKey(1);


    foo = 'Contours Found: ' + str(QtdeContornos)
    print(foo)

    #Write in the image the number of people who entered or left the guarded area
    cv2.putText(Frame, "Entry: {}".format(str(ContadorEntradas)), (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (250, 0, 1), 2)
    cv2.putText(Frame, "Exit: {}".format(str(ContadorSaidas)), (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Original", Frame)
    cv2.waitKey(1);


# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
