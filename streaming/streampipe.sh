python3 cv2_toffmpg.py | ffmpeg -f rawvideo -pixel_format rgb24 -video_size 640x480 -framerate 30 -i - http://localhost:8090/feed1.ffm
