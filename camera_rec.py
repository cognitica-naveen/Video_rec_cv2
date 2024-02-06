import cv2
import numpy as np
import time
 
# Create a VideoCapture object
cap = cv2.VideoCapture(2)
 
# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
 
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
 
# text 
# Write some Text

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (0,100)
fontScale              = 1
fontColor              = (255,255,255)
thickness              = 1
lineType               = 2




# used to record the time when we processed last frame 
prev_frame_time = 0
  
# used to record the time at which we processed current frame 
new_frame_time = 0


i=0
while(True):
  ret, frame = cap.read()
 
  if ret == True: 
     
    # Write the frame into the file 'output.avi'
    out.write(frame)
    
    new_frame_time = time.time()
    # i +=1

    fps = 1/(new_frame_time-prev_frame_time) 
    prev_frame_time = new_frame_time 
    # frame rotation
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    
    cv2.putText(frame,f'FPS : {fps:.2f}', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    thickness,
    lineType)

    
    # Display the resulting frame    
    cv2.imshow('frame',frame)
    
    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else:
    break 
 
# When everything done, release the video capture and video write objects
cap.release()
out.release()
 
# Closes all the frames
cv2.destroyAllWindows()