import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

st.title("يارب يشتغل")
st.write("Hello, world")


#flag = False 
class VideoProcessor:
    def __init__(self) -> None:
        self.threshold1 = 100
        self.threshold2 = 200
        # Load pre-trained face detection cascade classifier
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.smile_cascade = cv2.CascadeClassifier( cv2.data.haarcascades + 'haarcascade_smile.xml')
        


    def recv(self, frame):
        #global flag
        img = frame.to_ndarray(format="bgr24")

        # Detect faces
        faces = self.face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            flag= True            
            # Region of interest for smile detection within the face
            roi_gray = img[y:y+h, x:x+w]
            smiles = self.smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_gray, (x+sx, y+sy), (x+sx+sw, y+sy+sh), (0, 255, 0), 2)
            
        return av.VideoFrame.from_ndarray(img, format="bgr24")

        

ctx = webrtc_streamer(
    key="example",
    video_processor_factory=VideoProcessor,
    rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)


    




