# Color-Tracking-in-Video

This program runs in the command line:
python track.py -v [VIDEO_DIRECTORY] -c [COLOR]

For starters, various ranges for the colors, red, blue, yellow and green have been defined.
Feel free to add your color ranges, remember the color arrays are in BGR format.

After picking our color in the command line:
It grabs each frame from the video and passes it through a Gaussian Blur 
Also feel free to experiment with the kernel size ie. the tuple passed to the cv2.GaussianBlur function.
Kernel size (3,3) worked well for me 

It then passes a copy of our blurred result to the cv2.findContours function which returns contour points.
These contour points are then sorted according to area, and the smallest is selected and passed to the cv2.minAreaRect function 

Using this rect, we draw rectangles around highly prominent thresholds in our video.
We show the video in the "Tracking" window
And also show a Binary window, in the "Binary" window where only the threshold color is highlighted and all other areas blackened




