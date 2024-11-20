#! /usr/bin/python

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import numpy as np
import cv2
import csv
import os
from datetime import datetime, timedelta
from sense_hat import SenseHat

def check_last_entry(file_path, name):
    if not os.path.exists(file_path):
        return None
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reversed(list(reader)):
            if row['Name'] == name:
                return datetime.strptime(row['Time'], "%Y-%m-%d %I:%M:%S %p")
    return None

# create sense_hat object, initialize colors
sense = SenseHat()
sense.clear()
G = [0,255,0]
pixels = [G] * 64

# initialize variable for the "punch card" timestamp of when the face is first recognized
time_punch = None

#Initialize 'currentname' to trigger only when a new person is identified.
currentname = "Unknown"
#Determine faces from encodings.pickle file model created from train_model.py
encodingsP = "encodings.pickle"

# load the known faces and embeddings along with OpenCV's Haar
# cascade for face detection
print("[INFO] loading encodings + face detector...")
data = pickle.loads(open(encodingsP, "rb").read())

# initialize the video stream and allow the camera sensor to warm up
# Set the ser to the followng
# src = 0 : for the build in single web cam, could be your laptop webcam
# src = 2 : I had to set it to 2 inorder to use the USB webcam attached to my laptop
vs = VideoStream(src=0,framerate=10).start()
#vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# start the FPS counter
fps = FPS().start()

csv_file_path="/home/pi/Desktop/data.csv"

# open up a file to send the punch times to
with open(csv_file_path, mode='w', newline='') as file:
    headers = ["Name", "Time", "Confidence", "Action"]
    writer = csv.writer(file)
    if os.stat(csv_file_path).st_size == 0:
        writer.writerow(headers)
    # loop over frames from the video file stream
    while True:
        # grab the frame from the threaded video stream and resize it
        # to 500px (to speedup processing)
        frame = vs.read()
        frame = imutils.resize(frame, width=500)
        # Detect the fce boxes
        boxes = face_recognition.face_locations(frame)
        # compute the facial embeddings for each face bounding box
        encodings = face_recognition.face_encodings(frame, boxes)
        names = []
   
        # loop over the facial embeddings
        for encoding in encodings:
            # attempt to match each face in the input image to our known
            # encodings
            matches = face_recognition.compare_faces(data["encodings"],
                encoding)
            name = "Unknown" #if face is not recognized, then print Unknown
   
            # check to see if we have found a match
            if True in matches:
                # find the indexes of all matched faces then initialize a
                # dictionary to count the total number of times each face
                # was matched
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}
   
                # loop over the matched indexes and maintain a count for
                # each recognized face face
                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1
   
                # determine the recognized face with the largest number
                # of votes (note: in the event of an unlikely tie Python
                # will select first entry in the dictionary)
                name = max(counts, key=counts.get)
               
                #CHANGING THE CODE HERE TO TRY TO GET THE CONFIDENCE LEVEL!!!!!!!
                #Calculate the confidence level (distance)
                distances = face_recognition.face_distance(data["encodings"], encoding)
                confidence = np.min(distances[matchedIdxs])  #Get the minimum distance from matched faces
                confidence_percentage = (1 - confidence) * 100  # Convert to percentage

                #Print the confidence level
                print(f"Confidence for {name}: {confidence_percentage:.2f}%")
                #END CHANGE FOR ATTEMPT AT CONFIDENCE LEVEL!!!!!!!!!!!!!!!!!!!!!!!
   
                #If someone in your dataset is identified, print their name on the screen
                if currentname != name:
                    currentname = name
                    print(currentname)
   
            # update the list of names
            names.append(name)
   
        # loop over the recognized faces
        for ((top, right, bottom, left), name) in zip(boxes, names):
            # draw the predicted face name on the image - color is in BGR
            cv2.rectangle(frame, (left, top), (right, bottom),
                (0, 255, 225), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                .8, (0, 255, 255), 2)
            # sensehat leds light up green when a face is recognized
            sense.set_pixels(pixels)
            # if it's the first time the face is detected, display the timestamp to "clock in" or "clock out"
            if currentname != name:
                currentname = name
   
            if time_punch is None:
                last_entry_time = check_last_entry(csv_file_path, name)
                current_time = datetime.now()
                if last_entry_time:
                    action = "Clock Out"
                else:
                    action="Clock In"
                time_punch = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
                print(f"{currentname} has logged {action} at {time_punch}")
                csv_name = name
                csv_time = time_punch
                csv_confidence = round(confidence_percentage, 2)
                row = [csv_name, csv_time, csv_confidence, action]
                writer.writerow(row)
                file.flush()
               
            y_action = bottom + 30
            cv2.putText(frame, action, (left, y_action), cv2.FONT_HERSHEY_SIMPLEX, .8, (0, 255, 255), 2)
                   
               # timesheet.write(f"{currentname} : {time_punch}\n")
               # timesheet.flush()
   
        # If no faces were detected, clear the sensehat
        if not boxes:
            sense.clear()
            time_punch = None
   
        # display the image to our screen
        cv2.imshow("Facial Recognition is Running", frame)
        key = cv2.waitKey(1) & 0xFF
   
        # quit when 'q' key is pressed
        if key == ord("q"):
            break
   
        # update the FPS counter
        fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()