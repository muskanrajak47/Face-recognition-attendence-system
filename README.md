
## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/muskanrajak47/Face-recognition-attendence-system.git
   cd Face-recognition-attendence-system
2.Create a virtual environment
python -m venv .venv
source .venv/Scripts/activate 
  # On Windows
3.Install dependencies
pip install -r requirements.txt


🚀 Usage
Run the script:
python attendence_system.py
Press Q to stop the camera.

Attendance is automatically saved in a CSV file named:
attendance_<date>.csv


✨ Features
Real-time face detection and recognition via webcam

Logs attendance with timestamps

Configurable faces/ folder for user images

CSV export for attendance records

Lightweight and easy to integrate with other systems

🛠️ Tech Stack
Python 3.13+

OpenCV

face_recognition

NumPy

📂 Project Structure
Face-recognition-attendence-system/
│
├── attendence_system.py        # Main script
├── attendance_<date>.csv       # Auto-generated attendance logs
├── faces/                      # Folder for user images (ignored in repo)
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation


📈 Project Impact
This system demonstrates practical application of AI + Computer Vision.
It can be deployed in:

Schools and universities for automated student attendance

Offices for employee check-in systems

Events for participant tracking
