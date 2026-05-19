import face_recognition
import cv2
import numpy as np
import os
import csv
from datetime import datetime

# Load known faces dynamically from the "faces" folder
known_face_encodings = []
known_face_names = []

faces_dir = "faces"
for filename in os.listdir(faces_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        path = os.path.join(faces_dir, filename)
        image = face_recognition.load_image_file(path)
        encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(encoding)
        # Use filename (without extension) as the name
        known_face_names.append(os.path.splitext(filename)[0])

# Prepare attendance list
students = known_face_names.copy()

# Create CSV file for today
csv_filename = f"attendance_{datetime.now().strftime('%Y-%m-%d')}.csv"
f = open(csv_filename, "w+", newline="")
lnwriter = csv.writer(f)
lnwriter.writerow(["Name", "Date", "Time"])

# Start webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        # Compare with known faces (stricter tolerance)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index] and face_distances[best_match_index] < 0.5:
            name = known_face_names[best_match_index]
        else:
            name = "Unknown"

        # Mark attendance only once
        if name in students and name != "Unknown":
            students.remove(name)
            now = datetime.now()
            lnwriter.writerow([name, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")])
            print(f"{name} marked present at {now.strftime('%H:%M:%S')}")

        # Show name on screen
        cv2.putText(frame, f"{name} Present", (10, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3, 2)

    cv2.imshow("Attendance System", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video_capture.release()
cv2.destroyAllWindows()
f.close()
print(f"Attendance saved to {csv_filename}")
