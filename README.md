# LiteCCTV API

LiteCCTV API is Web API to help <a href="https://github.com/ADryInkCartridge/LiteCCTV">LiteCCTV</a> Android Application features. 
This Web API will receive an image from LiteCCTV Android Application and will do analysis to get Face Images from the image.
After that, this Web API will predict emotion of the Face Images.

## Installation (Ubuntu 20.04)

1. Update dependencies by using `apt get update`.
2. Install virtual environment by `pip3 install virtualenv` 
3. Clone this repository by typing command `git clone [git url]`.
4. Set working directory to it.
5. Create new virtual environment called env `virtualenv env`.
6. Activate the virtual environment `. env/bin/activate`.
7. Install python pip by using `apt install python3-pip`.
8. Install django rest framework, OpenCV, Tensorflow 2 by using `pip install djangorestframework opencv-python tensorflow`.
9. Run `py manage.py runserver [server ip]`

## Library Used
1. <a href="https://pypi.org/project/opencv-python/">OpenCV</a> for Face Recognition
2. <a href="https://www.tensorflow.org/">Tensorflow 2</a> for Emotional Prediction
3. <a href="https://www.djangoproject.com/">Django</a> for Web Framework
4. <a href="https://www.django-rest-framework.org/">Django Rest Framework</a> for Web API

## Emotional Prediction Model
Model that this application use to predict emotion from face image is taken from <a href="https://github.com/karansjc1/emotion-detection">Karan Sethi's Work</a>

## References
1. <a href="https://www.django-rest-framework.org/">Django Rest Framework Official Website</a>
2. <a href="https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81">Face Detection using OpenCV Python</a>
3. <a href="https://www.tensorflow.org/install">Tensorflow 2 Installation Manual</a>
4. <a href="https://www.python.org/downloads/release/python-380/">Python 3.8</a>
5. <a href="https://www.django-rest-framework.org/api-guide/serializers/">Django Serializers Documentation</a>
