import cv2
import numpy as np
import io
import imageio
import base64

def getFacesFromImage(b64_string):
    # List of detected faces
    detected_faces = []

    # Read the input image
    img = imageio.imread(io.BytesIO(base64.b64decode(b64_string)))

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load the cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces and crop the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        faces = img[y:y + h, x:x + w]

        retval, buffer = cv2.imencode('.jpg', faces)
        jpg_as_text = base64.b64encode(buffer)

        b64_face_string = jpg_as_text.decode('utf-8')
        detected_faces.append(b64_face_string)

    return detected_faces
