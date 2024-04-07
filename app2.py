import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

st.title("My first Streamlit app")
st.write("Hello, world")
st.write("hihihihihi")




class VideoProcessor:
    def __init__(self) -> None:
        self.threshold1 = 100
        self.threshold2 = 200
        # Load pre-trained face detection cascade classifier
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.smile_cascade = cv2.CascadeClassifier( cv2.data.haarcascades + 'haarcascade_smile.xml')
        self.smile_detected = False
        #self.faces = ()
        #self.smiles = ()
    
    def detect_smile(self, img):
        st.write("def detect_smile")
        # Detect smiles within the image
        smiles = self.smile_cascade.detectMultiScale(img, scaleFactor=1.8, minNeighbors=20)
        return len(smiles) > 0

    def recv(self, frame):
        st.write("def recv")
        img = frame.to_ndarray(format="bgr24")

        # Detect faces
        faces = self.face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Detect smiles within the region of interest
            # Region of interest for smile detection within the face
            roi_gray = img[y:y+h, x:x+w]

            # Detect smiles within the region of interest
            if self.detect_smile(roi_gray):
                self.smile_detected = True
                break  # Exit the loop if a smile is detected
                
            #if len(smiles) > 0:
                #webrtc_streamer.stop()
                #break
                #self.smile_detected = True
                #break  # Exit the loop if a smile is detected
        
                # Check if a smile is detected
        if self.smile_detected:
            # Display an image
            st.image('Screenshot (137).png', caption='Sunrise by the mountains')    
            st.subheader('msg after detect smile')
            # Close the camera
            #webrtc_streamer.stop()


        return av.VideoFrame.from_ndarray(img, format="bgr24")

ctx = webrtc_streamer(
    key="example",
    video_processor_factory=VideoProcessor,
    rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)

