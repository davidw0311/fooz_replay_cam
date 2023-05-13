from picamera2 import Picamera2, Preview

from libcamera import controls, ColorSpace
#picamimport imutils

from pprint import *

import time

import cv2

picam2 = Picamera2()
preview_config = picam2.create_preview_configuration() #not needed for actual use, helpful for debugging
capture_config = picam2.create_still_configuration()
#fps can be specified by altering the raw stream (~14 fps is picam2.sensor_modes[2])
picam2.align_configuration(capture_config) #speeds code up when a suboptimal resolution is used
picam2.configure(preview_config) #results in a couple less warnings
picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition":15.0})
#picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
#For mannual, LensPosition can range from 0 to 32, with 1 as the default
#Manually triggered autofocusing is also an option
#Note that "LensPosition" is specified in image metadata
#pprint(picam2.sensor_modes)

picam2.start_preview(Preview.QTGL)
picam2.start()


time.sleep(10)
#picam2.capture_file("test.jpg")
raw_img = picam2.capture_array("main")
#raw_img = picam2.switch_mode_and_capture_array(capture_config,"main")
#capturing the request and saving MAY result in fewer dropped frames by parallelizing (see section 6.4 of manual)
#wait and signal_function args can also be used to stop blocking or call a function in response to a completed capture
metadata = picam2.capture_metadata()
print(metadata)


#cv2.imwrite('rot_image_march18.png', cropped_img)
#capturing video with the Null encoder looks like it could work as well - would allow asynchronus processing

#num_captured = 0
#while num_captured < 10:
#	timestamp = str(int(time.time()))
#	picam2.capture_file(timestamp +".jpg")
#	print("frame captured")
#	time.sleep(1.0)
#	num_captured=num_captured+1
