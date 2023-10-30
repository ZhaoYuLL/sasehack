from deepface import DeepFace
import cv2

faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

backends = ["opencv", "ssd", "dlib", "retinaface", "mediapipe"]

video = cv2.VideoCapture(0)

a = 1

while True:
    check, frame = video.read()
    cv2.imshow("Capturing", frame)

    # Press 'q' to capture and save the frame
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.imwrite(
            "/Users/zhao/Desktop/person projacks/sasehack/server/photo.jpg", frame
        )
        break

video.release()
cv2.destroyAllWindows()

img = cv2.imread("/Users/zhao/Desktop/person projacks/sasehack/server/photo.jpg")
result = DeepFace.analyze(img, actions=["emotion"])
print(result)

# Print the emotion analysis results
print("Emotion:", result["dominant_emotion"])
