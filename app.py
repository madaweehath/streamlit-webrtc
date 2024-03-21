import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

# Load pre-trained face and smile cascade classifiers (adjust paths if needed)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

st.title("My first Streamlit app")
st.write("Hello, world")


class VideoProcessor:
    def __init__(self) -> None:
        self.threshold1 = 100
        self.threshold2 = 200

    def recv(frame: av.VideoFrame) -> av.VideoFrame:
        img = frame.to_ndarray(format="bgr24")
        # Convert frame to grayscale for faster processing
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        if len(faces) > 0:
            st.title("hi2")

        # Loop through detected faces
        for (x, y, w, h) in faces:
            # Extract the region of interest (ROI) for the face
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            # Detect smiles within the face ROI
            smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

            # Display "Happy Birthday" on smile detection
            if len(smiles) > 0:
                st.title("hi")
                # Put a text label "Happy Birthday!" on top
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, "Happy Birthday!", (x + int(w/2), y - 10), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

        # Display the resulting frame
        cv2.imshow('Smile Capture App', img)
        #+++++++++++++++++++++++++++++++++++++++++++
        # img = frame.to_ndarray(format="bgr24")

        # img = cv2.cvtColor(cv2.Canny(img, self.threshold1, self.threshold2), cv2.COLOR_GRAY2BGR)

        return av.VideoFrame.from_ndarray(img, format="bgr24")

# def recv(frame: av.VideoFrame) -> av.VideoFrame:
#         img = frame.to_ndarray(format="bgr24")
#         # Convert frame to grayscale for faster processing
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#         # Detect faces in the grayscale frame
#         faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#         if len(faces) > 0:
#             st.title("hi2")

#         # Loop through detected faces
#         for (x, y, w, h) in faces:
#             # Extract the region of interest (ROI) for the face
#             roi_gray = gray[y:y+h, x:x+w]
#             roi_color = img[y:y+h, x:x+w]

#             # Detect smiles within the face ROI
#             smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

#             # Display "Happy Birthday" on smile detection
#             if len(smiles) > 0:
#                 st.title("hi")
#                 # Put a text label "Happy Birthday!" on top
#                 font = cv2.FONT_HERSHEY_SIMPLEX
#                 cv2.putText(img, "Happy Birthday!", (x + int(w/2), y - 10), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

#         # Display the resulting frame
#         cv2.imshow('Smile Capture App', img)
#         #+++++++++++++++++++++++++++++++++++++++++++
#         # img = frame.to_ndarray(format="bgr24")

#         # img = cv2.cvtColor(cv2.Canny(img, self.threshold1, self.threshold2), cv2.COLOR_GRAY2BGR)

#         return av.VideoFrame.from_ndarray(img, format="bgr24")
ctx = webrtc_streamer(
    key="example",
    video_processor_factory=VideoProcessor,
    rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)
# ctx = webrtc_streamer(
#     key="example",
#     rtc_configuration={
#         "iceServers":  [{"urls": ["stun:stun.l.google.com:19302"]}],
#         "iceTransportPolicy": "relay",
#     },
#     video_frame_callback=recv,
#     media_stream_constraints={"video": True, "audio": False},
#     async_processing=True,
# )
# if ctx.video_processor:
#     ctx.video_processor.threshold1 = st.slider("Threshold1", min_value=0, max_value=1000, step=1, value=100)
#     ctx.video_processor.threshold2 = st.slider("Threshold2", min_value=0, max_value=1000, step=1, value=200)
##############________________________________________________________________________________________________________________
