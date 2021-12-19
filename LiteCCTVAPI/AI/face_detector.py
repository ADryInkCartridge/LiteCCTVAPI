import cv2
import numpy as np
import io
import imageio
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import base64
import os

def getFacesFromImage(b64_string):
    # List of detected faces
    detected_faces = []
    
    # Model file path
    model_file_path = os.path.dirname(__file__) + '/EmotionDetectionModel.h5'

    classifier = load_model(model_file_path)
    class_labels=['Angry','Happy','Neutral','Sad','Surprise']

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
        faces = img[y:y + h, x:x + w]
        roi_gray=gray[y:y+h,x:x+w]
        roi_gray=cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)

        emotion = 'none'

        if np.sum([roi_gray])!=0:
            roi=roi_gray.astype('float')/255.0
            roi=img_to_array(roi)
            roi=np.expand_dims(roi,axis=0)
            preds=classifier.predict(roi)[0]
            label=class_labels[preds.argmax()]
            # print(label)
            # cv2.imwrite('a.jpg', img)
            # label_position=(x+40,y+50)
            # print(label_position)
            # cv2.putText(img,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,0.65,(100,240,0),1)
            # cv2.imwrite('b.jpg', img)
            emotion = label

        retval, buffer = cv2.imencode('.jpg', faces)
        jpg_as_text = base64.b64encode(buffer)

        b64_face_string = jpg_as_text.decode('utf-8')
        detected_faces.append([b64_face_string, emotion])
    return detected_faces
