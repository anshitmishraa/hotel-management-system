# Hotel Management System

## Overview

The Hotel Management System is a comprehensive software solution designed to streamline the check-in, check-out, and room management processes for a hotel. Built using Python's Tkinter library for the graphical user interface and MySQL for the database management, this system provides a user-friendly interface for both staff and guests to manage room bookings, check-ins, and check-outs efficiently.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Contributors](#contributors)

## Features

- **Check-In Process:** Allows guests to input their details and select a room type (AC/Non-AC). Automatically assigns an available room and provides a payment interface.
- **Check-Out Process:** Facilitates the check-out process, including room number selection, feedback submission, and room status update.
- **Room Details:** Displays current room status (Occupied/Not Occupied) and type (AC/Non-AC).
- **Staff Details:** Shows staff information including their contact details and addresses.
- **Database Management:** Utilizes MySQL to handle data persistence and management for rooms, bookings, and staff details.

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/anshitmishraa/hotel-management-system.git
   cd hotel-management-system
   ```

2. **Install Required Libraries:**
   Ensure you have Python installed. Then, install the required Python libraries using pip:
   ```sh
   pip install mysql-connector-python pymysql
   ```

3. **Database Setup:**
   Ensure you have a MySQL server running and create a database named `hotelManagementSystem`. Import the provided SQL scripts to set up the required tables.

4. **Configure Database Connection:**
   Update the database connection details in the Python scripts if necessary.

## Usage

1. **Run the Main Application:**
   ```sh
   python main_application.py
   ```

2. **Navigate Through the Application:**
   - **Check-In:** Click the "Check In" button to start the check-in process.
   - **Check-Out:** Click the "Check Out" button to start the check-out process.
   - **Room Details:** View room status and details.
   - **Staff Details:** View staff information.

3. **Perform Operations:**
   - For **Check-In**, enter the guest details and room preferences, and proceed with room booking and payment.
   - For **Check-Out**, select the room number, provide feedback, and proceed with check-out.

## File Descriptions

- **`main_application.py`:** The main entry point of the application with options to navigate to check-in, check-out, and staff details.
- **`check_in.py`:** Handles the guest check-in process, including room selection and payment.
- **`check_out.py`:** Manages the check-out process and feedback collection.
- **`room_details.py`:** Displays current room status and availability.
- **`staff_details.py`:** Shows staff information.
- **`constant_variable.py`:** Contains constant values such as room charges and dimensions used throughout the application.

## Contributors

- **Chinmaya Panigrahi** - Registration No.: 11901718
- **Akash Shiladitya** - Registration No.: 11901807
- **Anshit Mishra** - Registration No.: 11901808
