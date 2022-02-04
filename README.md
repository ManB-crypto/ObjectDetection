# ObjectDetection
A more advance version of the https://github.com/ManB-crypto/SimpleObjectDetect

### Requirements
* coco.names " is a data set that help the program identify the objects"
* frozen_inference_graph.pb " is a  file that contains the graph definition as well as the weights of the model"
* ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt "Allows you to save multiple versions of a graph that share the same assets and variables "

### Features
* Uses OpenCV and TenserFlow.
* Able to identfy 90 objects with high accuracy.
* SSD with MobileNet provides the best accuracy tradeoff within the fastest detectors.
* Able to customize what object that the user want to detect.
* Able to convert the video stream to an image.
* Able to save the image of the object capture and store them.

### Customizable
* confThreshold = 0.65 "The object confidence level."
* cv2.FONT_HERSHEY_PLAIN "the font type can be change to others type to be more suitable"
* color=(160, 32, 240) "the box and fond color"
* objectlist=['cat'] "The object that want to be detected."
* if count == 3: " The number of image store at a given time"

### Example
* #Filter the object that is detected which is the cat
![Screenshot 2022-02-04 204029](https://user-images.githubusercontent.com/80488842/152530864-b855125d-788d-4faa-ae8a-23c017f832f3.png)

* #the object that is detected are store in a folder
![Screenshot 2022-02-04 204140](https://user-images.githubusercontent.com/80488842/152530932-764261f1-441d-4f2d-8510-15976dfeee37.png)
