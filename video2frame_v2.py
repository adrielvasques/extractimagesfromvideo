#Script to all extract frames from a video and save each frame in a jpg file 
#Autor:Adriel Santos
#Date: 13/05/2021 (One day until my birthday)
#Use as you want
#Dependecies: opencv, python 3.x.x and os 
#Based on Breno algorithms
import cv2
import os 


def createDir(outputDir): #this fuction verify if exist a directory in the current path, 
                 # if does not it will create a directory with the custom name            
    try:
        os.mkdir(outputDir)
        print(outputDir + " created")
    except FileExistsError:
        print("Directory already exists")
def extractFrames(video, outputDir): #this fuction will extract every frame from video and save as jpg file
    success,image = video.read()
    cont = 0
    while success and cont<=frameNumbers:
        cv2.imwrite(os.path.join(outputDir, "Sample%d.jpg" % cont), image)     # save frame as JPEG file      
        success,image = video.read()
        cont += 1
        print("Process in: ", int((cont/frameNumbers)*100), "%", end='\r' )

outputDir = "outImages" #Define folder to save output images
video = cv2.VideoCapture('insert-here-your-video') # video path
success,image = video.read() # readvideo
fps = video.get(cv2.CAP_PROP_FPS) # frames per second of inserted video
frameNumbers = video.get(cv2.CAP_PROP_FRAME_COUNT) # total numbers of frame of inserted video
videoDuration = frameNumbers/fps #Duration of inserted video in seconds
print("Frame Rate: " + str(fps) + " fps")
print("Total Frames Numbers: ", str(frameNumbers)
print("Video Duration: ", str(videoDuration) + " seconds")
createDir(outputDir)
extractFrames(video, outputDir)
print("\nComplete!")
