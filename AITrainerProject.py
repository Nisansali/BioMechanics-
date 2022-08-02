import cv2
import numpy as np
import time
import PoseModule as pm
import csv
import pandas as pd
import DFCP as dfcp

count = 0
dir = 0
pTime = 0
sTime = 0
eTime = 0

# Colors
GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#cap = cv2.VideoCapture("F:\\Personal AI trainer\\c6.mp4")
detector = pm.poseDetector()
cap = cv2.VideoCapture(0)

Focal_length_found = dfcp.Focal_length_found
Known_width = dfcp.Known_width


# faceFound = []
# ts = [0, 0, False]

while True:
    #img = cv2.imread("F:\\Personal AI trainer\\img15.jpg")
    success, img = cap.read()
    img = cv2.resize(img, (1200, 720))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    face_width_in_frame = dfcp.face_data(img)
    #print(img)
    #print(lmList)

    if len(lmList) !=0:
        #angle = detector.findAngle(img, 11, 13, 15)
        #angle_2 = detector.findAngle2(0, 11)
        #dist = detector.findDist(img, 16, 15)
        cam_distance = dfcp.Distance_finder(Focal_length_found, Known_width, face_width_in_frame)
        dist2 = detector.distance(img, 16, 15)
        stride_length = (dist2*2)/ 37.795
        #print(stride_length, "cm")
        #print(cam_distance)
        #per = np.interp(angle, (80, 145), (100, 0)) #to get the percentage values for the angle 0 - 100%
        #bar = np.interp(angle, (80, 145), (100, 400)) #Max first, Min second
        #print(angle, per)

        # color = (252, 29, 29)
        # if per == 100:
        #     color = (0, 255, 255)
        #     if dir == 0:
        #         count += 1
        #         dir = 1
        #
        # if per == 0:
        #     if dir == 1:
        #         dir = 0

        # if cv2.waitKey(1) & 0xFF == ord('r'):
        #     count = 0

        # print(count, "%.2f" % per, int(angle), dist, round(angle_2, 2))

        # #Save data to CSV file
        # with open('values1.csv', 'a', encoding='UTF8', newline='') as f:
        #     # row1 = ('count', 'per', 'angle')
        #     row = (count, "%.2f" % per, int(angle), dist)
        #     writer = csv.writer(f)
        #     writer.writerow(row)
        #     f.close()
        #
        # #Rename the headers of CSV file and save to same CSV file
        # file = pd.read_csv("values1.csv")
        # headerList = ['COUNT', 'PER%', 'ANGLE', 'DIST']
        # file.to_csv("values1.csv", header=headerList, index=False)

        # #Draw bar
        # cv2.rectangle(img, (1130, 100), (1100, 400), color, 2)
        # cv2.rectangle(img, (1130, int(bar)), (1100, 400), color, cv2.FILLED)
        # cv2.putText(img, f'{int(per)}%', (1080, 70), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
        #
        # draw line as background of text
        cv2.line(img, (50, 65), (300, 65), RED, 90)
        cv2.line(img, (50, 65), (300, 65), BLACK, 80)

        # #Draw curl counts
        #cv2.rectangle(img, (95, 720), (200, 700), WHITE, cv2.FILLED)
        # cv2.putText(img, str("Curl count:"), (30, 675), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 0, 0), 2)
        # #cv2.putText(img, str(int(count)), (380, 675), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 0, 255), 2)
        cv2.putText(img, str(f"Cam Distance: {float(round(cam_distance+15, 1))} cm"), (35, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, GREEN, 2)
        cv2.putText(img, str(f"Stride Length: {int(stride_length)} cm"), (35, 90), cv2.FONT_HERSHEY_COMPLEX, 0.7, WHITE, 2)
        print("modify")
        print("modify2")

        # cTime = time.time()
        # fps = 1 / (cTime - pTime)  # fps calculation formula
        # pTime = cTime
        #
        # cv2.putText(img, str(int(fps)), (40, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0),
        #             2)  # calculated fps is displayed on screen with given position

        # try:
        #     if angle <= 70:
        #         if ts[2] == False:
        #             ts[0] = time.time()
        #             ts[2] = True
        # except:
        #     if angle <= 60:
        #         if ts[2] == True:
        #             ts[1] = time.time()
        #             ts[2] = False
        #             faceFound.append([ts[0], ts[1]])
        #     pass
        #
        # for list in faceFound:
        #     print (list[1] - list[0])

        #while True:
        # if angle <= 70:
        #     sTime = time.time()
        #     print(round(time.time()-sTime, 2), 'secs')
        #     time.sleep(100)
        #
        #     if angle <= 60:
        #         eTime = time.time()
        #         print("The time elapsed is", round(eTime-sTime, 2), 'secs')
        #         break

    cv2.imshow("frame", img)
    #cv2.imwrite('savedimage_15.jpeg', img)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
