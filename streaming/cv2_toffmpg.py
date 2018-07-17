#!/usr/bin/env python
import freenect
#import cv2
#import frame_convert2
import sys

#cv2.namedWindow('Depth')
#cv2.namedWindow('Video')
print('Press ESC in window to stop')


def get_depth():
    #return frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])
    return freenect.sync_get_depth()[0]

def get_video():
    #return frame_convert2.video_cv(freenect.sync_get_video()[0])
    return freenect.sync_get_video()[0]

while 1:
    depthframe = get_depth()
    videoframe = get_video()
    #cv2.imshow('Depth', depthframe)
    #cv2.imshow('Video', videoframe)
    
    #sys.stdout.write( depthframe.tostring() )
    sys.stdout.buffer.write( videoframe.tostring() )

    #if cv2.waitKey(10) == 27:
    #    break
