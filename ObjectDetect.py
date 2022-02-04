import cv2
import numpy as np


classes = []
with open('coco.names','rt') as f:
    classes = f.read().rstrip('\n').split('\n')

net = cv2.dnn_DetectionModel('frozen_inference_graph.pb', 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)


def objects(image,objectlist = []):
    classIds,confs,bbox = net.detect(image,confThreshold = 0.65)
    if len(objectlist) == 0:
        objectlist = classes
    if len(classIds) !=0:
        for classID, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            classname = classes[classID - 1]
            objectlist.append([box, classname])
            if classname in objectlist:
                cv2.rectangle(image, box, color=(160, 32, 240), thickness=1)
                cv2.putText(image, classname.upper(), (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,
                            (160, 32, 240), 2)
                result = True
                count = 0
                while (result):
                    print("image saved"+str(count+1))
                    file = r"C:\Users\aiman\Downloads\Manb_life\FYP project\evidence\image"+str(count+1)+".jpg"
                    cv2.imwrite(file,image)
                    count = count +1
                    if count == 3:
                        result = False



    return image,objectlist

if __name__ == "__main__":
    cap = cv2.VideoCapture('video.mp4')
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        success, image = cap.read()
        result,objectlist = objects(image,objectlist=['cat']) #to add specific object list to detect
        print(objectlist)
        cv2.imshow("output", image)
        cv2.waitKey(2)
