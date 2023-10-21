from flask import Flask, render_template, Response
import cv2
import random

app = Flask(__name__)
camera = cv2.VideoCapture(0)
video = cv2.VideoCapture(0)


left = 5
top = 5
right = 5
bottom = 5

text = "Happiness!"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 0, 0)  # Green color in BGR
font_thickness = 2
position = (100, 50)  # Coordinates (x, y) where the text will be displayed


def generate_frames():
    i = 0

    while True:
        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # text = f"Random Text: {random.randint(1, 100)}"
            cv2.putText(
                frame, text, position, font, font_scale, font_color, font_thickness
            )
            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()

        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


while True:
    # 4.Create a frame object
    check, frame = video.read()
    # Converting to grayscale
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 5.show the frame!
    if key == ord("q"):
        break
    elif key == ord("w"):
        break


@app.route("/")
def index():
    return render_template("client/generate.js")


# whatever the route it is
@app.route("/video")
def video():
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(debug=True)
