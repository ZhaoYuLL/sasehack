from flask import Flask, render_template, Response, jsonify
import cv2
import random
from deepface import DeepFace


app = Flask(__name__)
camera = cv2.VideoCapture(0)

left = 5
top = 5
right = 5
bottom = 5

text = "Happiness!"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 255, 0)  # Green color in BGR
font_thickness = 2
position = (50, 100)  # Coordinates (x, y) where the text will be displayed

faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "sasehack/server/haarcascade_frontalface_default.xml"
)


def generate_frames():
    i = 0

    while True:
        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            text = f"Random Text: {random.randint(1, 100)}"
            cv2.putText(
                frame, text, position, font, font_scale, font_color, font_thickness
            )

            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()

            # showPic = cv2.imwrite("photo.jpg", frame)

        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video")
def video():
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/analyze_emotion", methods=["POST"])
def analyze_emotion():
    success, frame = camera.read()
    cv2.imwrite("photo.jpg", frame)

    img = cv2.imread("photo.jpg")
    print(random.randint(1, 100))
    predictions = DeepFace.analyze(img, enforce_detection=False)
    mE = predictions[0]["dominant_emotion"]
    # Return the emotion analysis result as JSON
    return jsonify({"emotion": mE})


if __name__ == "__main__":
    app.run(debug=True)
