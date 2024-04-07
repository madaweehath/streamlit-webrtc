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

    def recv(self, frame):
        st.write("def recv")
        img = frame.to_ndarray(format="bgr24")

        # Detect faces
        faces = self.face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Region of interest for smile detection within the face
            roi_gray = img[y:y+h, x:x+w]
            smiles = self.smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
#                if len(smiles) > 0:
#                    self.smile_detected = True
#                    break  # Exit the loop if a smile is detected
#            break
        
                # Check if a smile is detected
        if self.smile_detected:
        if len(smiles) > 0:
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

