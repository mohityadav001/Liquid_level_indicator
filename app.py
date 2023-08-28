import cv2
import subprocess

cam = cv2.VideoCapture(0)
cv2.namedWindow("Python Webcam creenshot App")

img_counter = 0

while True:
    ret, frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow("test", frame)

    k = cv2.waitKey(1)

    if k % 256 == 27:
        print("Escape hit, closing the app")
        break

    elif k % 256 == 32:
        img_name = "outimg_{}.png".format(
            img_counter)  # will save captured image
        cv2.imwrite(img_name, frame)
        print("screenshot taken")
        img_counter += 1


cam.release()
# cam.destroyAllWindows()

# run client.py file from this code
subprocess.run(["python", "client.py"])
#
