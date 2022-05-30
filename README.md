# Streaming2OpenCV
## Introduction
Turn streaming data (e.g. Bilibili, Youtube) to OpenCV Frames, also can use in PyTorch.  
Using C/S structure, using a server program to fetch streaming, and client program use Video Capture in OpenCV to get the frames. Client and Sever can be deployed in different machine.  
The program is based on streamlink, and it will be a part of a larger project————Plan "WaterFlow".  
## Design
A tool class is placed in server.py, you can change the url or modify the class to support different source.   
The client is a demo, when you want to develop program using this library, it will be better to write processing codes in the client.   

