# Cat/Human Classifier
"Face detection is a computer technology that determines the locations and sizes of human faces in arbitrary (digital) images. 
It detects facial features and ignores anything else, such as buildings, trees and bodies. Face detection can be regarded as a more general case of face localization. In face localization, the task is to find the locations and sizes of a known number of faces (usually one)." - wiki - Face detection

This computer vision project detects and classifies human and cat faces in videos. Detection is achieved using OpenCV's 
Haar feature-based cascade classifiers. I found implementing a combination of the available algorithms improved accuracy in imperfect conditions, such as poor lighting and shots of distant faces.
