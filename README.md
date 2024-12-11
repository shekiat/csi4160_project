# Automated Employee Clock-In System - README  

## Project Overview  
The **Automated Employee Clock-In System** is a facial recognition-based system developed to streamline employee clock-ins and clock-outs. Using a **Raspberry Pi 4 Model B**, an **Arducam 5MP Camera**, and software like **OpenCV**, the system identifies employees, records their attendance, and automates timesheets. This project utilizes **Google Cloud Platform (GCP)** for data storage and backup, ensuring scalability and reliability.

---

## Features  
- **Facial Recognition**  
  - Uses OpenCV for image processing and face encoding.  
  - Employees in the system are identified through a trained model.  
  - Real-time feedback using Sense HAT LEDs:  
    - Green for successful recognition.  
    - No LED for unrecognized individuals (future: red LED for errors).  

- **Automated Timesheets**  
  - Captures the time of clock-in and clock-out.  
  - Data is stored in a `.csv` file and synchronized with a **GCP VM** database.  
  - A dynamic webpage displays attendance records and confidence levels.  

- **Cloud Integration**  
  - Backups via **Google Cloud Storage (GCS)** ensure data security.  
  - Incremental backups scheduled using GCP Transfer Jobs.
  - *** ADD CLOUD SQL DETAILS

- **Web Interface**  
  - Displays timesheets and shift schedules.  
  - Live data updates through automated scripts.  

---

## System Requirements  

### Hardware  
- **Raspberry Pi 4 Model B**  
- **Arducam 5MP Camera**  
- **Sense HAT**  

### Software  
- **Raspberry Pi OS (Buster)**  
- **OpenCV**  
- **Google Cloud Platform**  
  - Virtual Machine (VM)  
  - MySQL Database  
  - Google Cloud Storage
  - Google Cloud SQL  

### Dependencies  
- OpenCV library and packages  
- PHP and NGINX for the web server  
- Secure Copy Protocol (SCP)  
- Google Cloud SDK  

---

## Setup  

### Raspberry Pi Configuration  
1. Install Raspberry Pi OS (Buster).  
2. Set up the Arducam 5MP Camera.  
3. Install OpenCV and clone the facial recognition repository.  
4. Capture and store at least 20 headshots for each employee from various angles.  
5. Train the system using the headshots dataset.  

### Google Cloud Platform  
1. Create a VM instance with a static external IP.  
2. Install NGINX and set up the MySQL database with columns:  
   - `name (VARCHAR(50))`  
   - `time (DATETIME)`  
   - `confidence (DOUBLE)`  
   - `action (VARCHAR(50))`  
3. Configure GCS for backups:  
   - Create a bucket and agent pool.  
   - Set up transfer jobs to run every 12 hours.
4. *** ADD CLOUD SQL SETUP DETAILS  

### Automation Scripts  
- **send_data.sh**: Sends `data.csv` from Raspberry Pi to the VM.  
- **update_website.sh**: Updates the MySQL database with changes in `data.csv`.  
- **Cron Jobs**: Schedule scripts "send_data.sh" and "update_website.sh," for regular execution.  

---

## Usage  

### Facial Recognition  
1. Start the system.  
2. Employees stand in front of the camera for recognition.  
3. LED feedback indicates the recognition result.  
4. Data is logged and updated dynamically.  

### Web Interface  
1. Access the website hosted on the VM.  
2. View attendance records, confidence levels, and shift schedules.  

---

## Project Structure

Bash_Scripts_Milestone2\
|--move_data.sh\
|--send_data.sh\
|--update_mysql_backup.sh\
|--update_website.sh\
GoogleCloudRunFunction\
|--data_transfer.py\
|--requirements.txt\
dataset\
|--Peyton\
|--Sam\
|--Z\
|--Danny\
|--Ryan\
|--Keanu\
photo\
php_files_milestone2\
|--index.php\
|--timesheet.php\
phpfiles_milestone4\
|--about.php\
|--timesheet.php\
LICENSE\
README.md\
encodings.pickle\
facial_req.py\
facial_req_email.py\
haarcascade_frontalface_default.xml\
headshots.py\
headshots_picam.py\
send_test_email.py\
train_model.py\

### Raspberry Pi Files
send_data.sh, dataset directory, photo directory, encodings.pickle, facial_req.py, facialt_req_email.py, haarcascade_frontalface_default.xml, headshots.py, headshots_picam.py, send_test_email,py, train_model.py

### VM Instance Files
move_data.sh, update_mysql_backup.sh, update_website.sh, php_files_milestone2 directory, phpfiles_milestone4 directory

### Google Cloud Run Function Files
GoogleCloudRunFunction directory

---

## Contributions  

- **Shekia Tillerson**  
   

- **Halee Tisler**  
   

- **Peyton Vecchi**  
   

---

## Future Enhancements  
1. Improve recognition accuracy by expanding the employee dataset.  
2. Add feedback for unrecognized users (e.g., red LED and error message).  
3. Fully integrate clock-in/clock-out data into the database and website.  
4. Scale the system for larger datasets and user bases.  

---

## References  
1. Jha, A., "Class Room Attendance System Using Facial Recognition," *International Journal of Mathematics*.  
2. ”About.” OpenCV, 4 Nov. 2020, https://opencv.org/about/ CM, Basil.
3. “Face Recognition in Python: A Comprehensive Guide.” Medium, 17 May 2023. https://basilchackomathew.medium.com/face-recognition-in-python-a-comprehensive-guide-960a48436d0f
4. Mafukidze, Harry. “How to Write Data to a File on the Raspberry Pi - Circuit Basics %.” Circuit Basics, 25 Nov. 2021. https://www.circuitbasics.com/writing-data-to-files-on-the-raspberry-pi/
5. “How to Install and Use the Raspberry Pi Camera Module” The Pi Hut, 25 Nov. 2014. thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera?srsltid=AfmBOoqCBA4R620VOgZJdkr8oKzb4nIB7IVDoBMjzysiJlP3Qv74f7kE  

---  

**Developed by:**  
Shekia Tillerson, Halee Tisler, Peyton Vecchi  
*Oakland University*  

