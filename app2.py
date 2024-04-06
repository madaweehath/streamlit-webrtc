import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

st.title("My first Streamlit app")
st.write("Hello, world")



class VideoProcessor:
    def __init__(self) -> None:
        self.threshold1 = 100
        self.threshold2 = 200
        # Load pre-trained face detection cascade classifier
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.smile_cascade = cv2.CascadeClassifier( cv2.data.haarcascades + 'haarcascade_smile.xml')
        self.faces = ()
        self.smiles = ()

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # Detect faces
        faces = self.face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        smiles = smile_cascade.detectMultiScale(img, 1.8, 20)

        # Draw rectangles around detected faces
        for (x, y, w, h) in smiles:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        return av.VideoFrame.from_ndarray(img, format="bgr24")

#        if len(faces) > 0 :
    st.image('Screenshot (137).png', caption='Sunrise by the mountains')
 #       else:
  #           st.title("No Faces Detected")


ctx = webrtc_streamer(
    key="example",
    video_processor_factory=VideoProcessor,
    rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)
