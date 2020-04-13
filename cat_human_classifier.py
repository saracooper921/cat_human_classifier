import cv2

# Load cascades
human_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eyes_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
cat_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")

# Open video file
cap = cv2.VideoCapture("captain_marvel_goose.mp4")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

x = width // 2
y = height // 2

w = width // 4
h = height // 4

if cap.isOpened() == False:
    print("Error! Check your filepath.")

# Read video file
while cap.isOpened():
    # Read video frame by frame
    ret, frame = cap.read()
    # Initialize detection
    humans = human_cascade.detectMultiScale(frame, 1.1, 2)
    # Higher scaling factor for cat because detector was classifying fluffy
    # human hair as cat
    cats = cat_cascade.detectMultiScale(frame, 1.3, 3)
    # Human faces are tracked with a fuschia square
    for (x, y, w, h) in humans:
        roi_color = frame[y:y+h, x:x+w]
        eyes = eyes_cascade.detectMultiScale(roi_color, 1.1, 3)
        # Detector picks up inanimate objects in low lighting so face
        # must have eyes too
        if eyes is not ():
            human_box = cv2.rectangle(frame, (x, y), (x+w, y+h),
            color=(255,0,255), thickness=5)
            cv2.putText(human_box, 'Human', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
            0.9, (255,0,255), 2)
    # Cat faces are tracked with a lime green square
    for (x, y, w, h) in cats:
        cat_box = cv2.rectangle(frame, (x, y), (x+w, y+h), color=(0,255,0),
        thickness=5)
        cv2.putText(cat_box, 'Cat', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0,255,0), 2)
    cv2.imshow('Video', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.release()
cv2.destroyAllWindows()
