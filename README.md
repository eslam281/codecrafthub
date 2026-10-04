# CodeCraftHub 📚

A simple learning platform API built with Flask that helps you track your personal course learning journey. This project is perfect for beginners who want to learn about REST APIs, JSON data storage, and Python web development.

## 🌟 Project Overview

CodeCraftHub is a RESTful API that allows you to:
- Create and manage your learning courses
- Track the status of each course (Not Started, In Progress, Completed)
- Set target dates for completing courses
- Update course information as you progress
- Delete courses you no longer need

All data is stored in a simple JSON file, making it easy to understand how data persistence works without needing a complex database.

## ✨ Features

- **Full CRUD Operations**: Create, Read, Update, and Delete courses
- **JSON Data Storage**: Simple file-based storage (no database required)
- **Input Validation**: Ensures data is correct before saving
- **Status Tracking**: Track course progress with three statuses
- **Date Validation**: Ensures dates are in the correct format
- **Error Handling**: Clear error messages for common issues
- **API Documentation**: Built-in endpoint documentation
- **Filtering**: Filter courses by status

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your computer:

- **Python 3.7 or higher** - Download from [python.org](https://www.python.org/downloads/)
- **pip** (Python package installer) - Usually installed with Python
- **A code editor** - Visual Studio Code, PyCharm, or any text editor
- **A terminal or command prompt** - PowerShell, Command Prompt, or Git Bash

### Check if Python is installed
Open your terminal and run:
```bash
python --version
```
or
```bash
python3 --version
```

You should see a version number like `Python 3.13.6`.

### Check if pip is installed
```bash
pip --version
```

## 🚀 Installation Instructions

### Step 1: Download or Clone the Project

If you have the project files:
```bash
cd U:\StudioProjects\aitask
```

### Step 2: Install Dependencies

The project requires Flask, a Python web framework. Install it using pip:

```bash
pip install -r requirements.txt
```

If you don't have a requirements.txt file, you can install Flask directly:
```bash
pip install Flask
```

**Note:** If you see a message about "user installation", that's normal. It means Flask will be installed for your user account only.

### Step 3: Verify Installation

Check that Flask is installed:
```bash
pip show Flask
```

You should see information about Flask including the version.

## 🏃 How to Run the Application

### Starting the Server

1. Open your terminal
2. Navigate to the project directory:
   ```bash
   cd U:\StudioProjects\codecrafthub
   ```
3. Run the application:
   ```bash
   python app.py
   ```

You should see output like this:
```
Created courses.json
Starting CodeCraftHub API...
Access the API at http://localhost:5000
 * Serving Flask app 'CodeCraftHub'
 * Debug mode: on
 * Running on http://localhost:5000
```

### Stopping the Server

To stop the server, press `Ctrl + C` in your terminal.

## 📡 API Endpoints Documentation

The API runs on `http://localhost:5000`

### Base URL
```
http://localhost:5000
```

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | View API documentation |
| GET | `/api/courses` | Get all courses |
| GET | `/api/courses/stats` | Get course statistics |
| GET | `/api/courses?status=X` | Filter courses by status |
| GET | `/api/courses/<id>` | Get a specific course |
| POST | `/api/courses` | Create a new course |
| PUT | `/api/courses/<id>` | Update a course |
| DELETE | `/api/courses/<id>` | Delete a course |

---

### 1. GET / - API Documentation

**Description:** Returns information about the API and available endpoints.

**Example Request:**
```powershell
curl http://localhost:5000 -UseBasicParsing
```

**Response (200 OK):**
```json
{
  "message": "Welcome to CodeCraftHub Learning Platform API!",
  "version": "1.0",
  "endpoints": {
    "GET /": "API documentation",
    "GET /courses": "Get all courses",
    "GET /courses/<id>": "Get a specific course by ID",
    "POST /courses": "Create a new course",
    "PUT /courses/<id>": "Update a course by ID",
    "DELETE /courses/<id>": "Delete a course by ID"
  }
}
```

---

### 2. GET /api/courses - Get All Courses

**Description:** Returns a list of all courses in your learning tracker.

**Example Request:**
```powershell
curl http://localhost:5000/api/courses -UseBasicParsing
```

**Response (200 OK):**
```json
{
  "count": 2,
  "courses": [
    {
      "id": 1,
      "name": "Python Fundamentals",
      "description": "Learn Python programming from scratch",
      "target_date": "2024-12-31",
      "status": "In Progress",
      "created_at": "2024-10-04 18:10:00",
      "updated_at": "2024-10-04 18:10:00"
    },
    {
      "id": 2,
      "name": "Advanced JavaScript",
      "description": "Master JS concepts",
      "target_date": "2025-01-15",
      "status": "Not Started",
      "created_at": "2024-10-04 18:11:00",
      "updated_at": "2024-10-04 18:11:00"
    }
  ]
}
```

---

### 3. GET /api/courses/stats - Get Course Statistics

**Description:** Returns statistics about all courses including total count and breakdown by status.

**Example Request:**
```powershell
curl http://localhost:5000/api/courses/stats -UseBasicParsing
```

**Response (200 OK):**
```json
{
  "total": 5,
  "by_status": {
    "Not Started": 2,
    "In Progress": 1,
    "Completed": 2
  }
}
```

**Fields:**
- `total`: Total number of courses
- `by_status`: Object containing count for each status
  - `Not Started`: Number of courses not started
  - `In Progress`: Number of courses in progress
  - `Completed`: Number of completed courses

---

### 4. GET /api/courses?status=X - Filter by Status

**Description:** Returns courses filtered by their status.

**Valid Status Values:**
- `Not Started`
- `In Progress`
- `Completed`

**Example Request (In Progress):**
```powershell
curl "http://localhost:5000/api/courses?status=In%20Progress" -UseBasicParsing
```

**Note:** In URLs, spaces must be replaced with `%20`

**Response (200 OK):**
```json
{
  "count": 1,
  "courses": [
    {
      "id": 1,
      "name": "Python Fundamentals",
      "description": "Learn Python programming from scratch",
      "target_date": "2024-12-31",
      "status": "In Progress",
      "created_at": "2024-10-04 18:10:00",
      "updated_at": "2024-10-04 18:10:00"
    }
  ]
}
```

---

### 5. GET /api/courses/<id> - Get Specific Course

**Description:** Returns a single course by its ID.

**Example Request:**
```powershell
curl http://localhost:5000/api/courses/1 -UseBasicParsing
```

**Response (200 OK):**
```json
{
  "id": 1,
  "name": "Python Fundamentals",
  "description": "Learn Python programming from scratch",
  "target_date": "2024-12-31",
  "status": "In Progress",
  "created_at": "2024-10-04 18:10:00",
  "updated_at": "2024-10-04 18:10:00"
}
```

**Error Response (404 Not Found):**
```json
{
  "error": "Course not found"
}
```

---

### 6. POST /api/courses - Create New Course

**Description:** Creates a new course in your learning tracker.

**Required Fields:**
- `name` - Course name (string)
- `description` - Course description (string)
- `target_date` - Target completion date (string, format: YYYY-MM-DD)
- `status` - Course status (string: "Not Started", "In Progress", or "Completed")

**Example Request (PowerShell):**
```powershell
$body = @{
    name = "Python Fundamentals"
    description = "Learn Python programming from scratch"
    target_date = "2024-12-31"
    status = "In Progress"
} | ConvertTo-Json

Invoke-RestMethod -Method POST -Uri "http://localhost:5000/api/courses" -Headers @{"Content-Type"="application/json"} -Body $body
```

**Response (201 Created):**
```json
{
  "message": "Course created successfully",
  "course": {
    "id": 1,
    "name": "Python Fundamentals",
    "description": "Learn Python programming from scratch",
    "target_date": "2024-12-31",
    "status": "In Progress",
    "created_at": "2024-10-04 18:10:00",
    "updated_at": "2024-10-04 18:10:00"
  }
}
```

**Error Response (400 Bad Request) - Missing Field:**
```json
{
  "error": "Missing required field: name"
}
```

**Error Response (400 Bad Request) - Invalid Status:**
```json
{
  "error": "Invalid status. Must be one of: Not Started, In Progress, Completed"
}
```

**Error Response (400 Bad Request) - Invalid Date:**
```json
{
  "error": "Invalid date format. Use YYYY-MM-DD (e.g., 2024-12-31)"
}
```

---

### 7. PUT /api/courses/<id> - Update Course

**Description:** Updates an existing course. All fields are optional.

**Example Request (Update Status):**
```powershell
$body = @{
    status = "Completed"
} | ConvertTo-Json

Invoke-RestMethod -Method PUT -Uri "http://localhost:5000/api/courses/1" -Headers @{"Content-Type"="application/json"} -Body $body
```

**Example Request (Update Multiple Fields):**
```powershell
$body = @{
    name = "Python Fundamentals - Updated"
    description = "Updated description"
    status = "Completed"
    target_date = "2025-01-15"
} | ConvertTo-Json

Invoke-RestMethod -Method PUT -Uri "http://localhost:5000/api/courses/1" -Headers @{"Content-Type"="application/json"} -Body $body
```

**Response (200 OK):**
```json
{
  "message": "Course updated successfully",
  "course": {
    "id": 1,
    "name": "Python Fundamentals - Updated",
    "description": "Updated description",
    "target_date": "2025-01-15",
    "status": "Completed",
    "created_at": "2024-10-04 18:10:00",
    "updated_at": "2024-10-04 18:15:00"
  }
}
```

**Error Response (404 Not Found):**
```json
{
  "error": "Course not found"
}
```

---

### 8. DELETE /api/courses/<id> - Delete Course

**Description:** Deletes a course by its ID.

**Example Request:**
```powershell
Invoke-RestMethod -Method DELETE -Uri "http://localhost:5000/api/courses/1" -Headers @{"Content-Type"="application/json"}
```

**Response (200 OK):**
```json
{
  "message": "Course deleted successfully",
  "deleted_course": {
    "id": 1,
    "name": "Python Fundamentals",
    "description": "Learn Python programming from scratch",
    "target_date": "2024-12-31",
    "status": "In Progress",
    "created_at": "2024-10-04 18:10:00",
    "updated_at": "2024-10-04 18:10:00"
  }
}
```

**Error Response (404 Not Found):**
```json
{
  "error": "Course not found"
}
```

---

## 🧪 Testing Instructions

### Automated Testing

We provide automated test scripts to help you test all API endpoints quickly.

#### Windows (PowerShell)
```powershell
.\test_api.bat
```

#### Windows (Git Bash/WSL)
```bash
bash test_api.sh
```

These scripts will:
- Create test courses
- Retrieve all courses
- Filter courses by status
- Get specific courses
- Update courses
- Delete courses
- Test error scenarios

### Manual Testing

You can also test the API manually using curl or any API client like Postman.

#### Example Workflow

1. **Start the server:**
   ```bash
   python CodeCraftHub.py
   ```

2. **Create a course** (in a new terminal):
   ```powershell
   $body = @{name="Python"; description="Learn Python"; target_date="2024-12-31"; status="In Progress"} | ConvertTo-Json
   Invoke-RestMethod -Method POST -Uri "http://localhost:5000/api/courses" -Headers @{"Content-Type"="application/json"} -Body $body
   ```

3. **Get all courses:**
   ```powershell
   curl http://localhost:5000/courses -UseBasicParsing
   ```

4. **Update the course:**
   ```powershell
   $body = @{status="Completed"} | ConvertTo-Json
   Invoke-RestMethod -Method PUT -Uri "http://localhost:5000/api/courses/1" -Headers @{"Content-Type"="application/json"} -Body $body
   ```

5. **Delete the course:**
   ```powershell
   Invoke-RestMethod -Method DELETE -Uri "http://localhost:5000/api/courses/1" -Headers @{"Content-Type"="application/json"}
   ```

### Using Postman (Recommended for Beginners)

1. Download and install [Postman](https://www.postman.com/downloads/)
2. Create a new request
3. Set the method (GET, POST, PUT, DELETE)
4. Enter the URL: `http://localhost:5000/courses`
5. For POST/PUT requests, go to the "Body" tab, select "raw", and choose "JSON"
6. Paste your JSON data
7. Click "Send"

## 📁 Project Structure

```
codecrafthub/
│
├── app.py               # Main Flask application file
├── courses.json          # Data storage file (auto-created)
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── TEST_GUIDE.md        # Detailed test documentation
├── QUICK_REFERENCE.md   # Quick reference for API commands
├── test_api.bat         # Windows batch test script
└── test_api.sh          # Bash test script
```

### File Explanations

- **app.py**: The main application file containing all the API logic
  - Flask app initialization
  - Helper functions for reading/writing data
  - API endpoint definitions
  - Error handling

- **courses.json**: Stores all course data in JSON format
  - Automatically created when you first run the app
  - Contains an array of course objects
  - Modified by the API when you create, update, or delete courses

- **requirements.txt**: Lists Python package dependencies
  - Currently only requires Flask
  - Used by pip to install dependencies

- **test_api.bat**: Automated test script for Windows
  - Tests all endpoints
  - Tests error scenarios
  - Easy to run with one command

- **test_api.sh**: Automated test script for Linux/Mac/Git Bash
  - Same functionality as the batch file
  - Uses bash syntax

## 🔧 Troubleshooting Common Issues

### Issue 1: "ModuleNotFoundError: No module named 'flask'"

**Problem:** Flask is not installed.

**Solution:**
```bash
pip install Flask
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

---

### Issue 2: Port already in use

**Problem:** Another application is using port 5000.

**Solution:** Change the port in CodeCraftHub.py:

Find this line at the bottom of the file:
```python
app.run(debug=True, host='127.0.0.1', port=5000)
```

Change it to a different port:
```python
app.run(debug=True, host='127.0.0.1', port=5001)
```

Then update all your test URLs to use the new port (e.g., `http://127.0.0.1:5001`).

---

### Issue 3: "Permission denied" when writing to courses.json

**Problem:** The application doesn't have permission to write to the file.

**Solution:**
- Make sure you're running the terminal with appropriate permissions
- On Windows, try running PowerShell as Administrator
- Check that the file isn't open in another program

---

### Issue 4: PowerShell security warning with curl

**Problem:** PowerShell shows a security warning when using curl.

**Solution:** Add `-UseBasicParsing` to your curl command:
```powershell
curl http://localhost:5000/courses -UseBasicParsing
```

---

### Issue 5: "Address already in use" error

**Problem:** The server is already running from a previous session.

**Solution:**
- Find the terminal where the server is running
- Press `Ctrl + C` to stop it
- Or, restart your computer to clear all running processes

---

### Issue 6: Invalid date format error

**Problem:** Date format is incorrect.

**Solution:** Always use the format `YYYY-MM-DD`:
- ✅ Correct: `2024-12-31`
- ❌ Wrong: `12/31/2024`
- ❌ Wrong: `31-12-2024`
- ❌ Wrong: `December 31, 2024`

---

### Issue 7: Test script shows "The filename, directory name, or volume label syntax is incorrect"

**Problem:** Special characters in JSON data (like &) are causing issues in batch files.

**Solution:** This has been fixed in the updated test scripts. Make sure you're using the latest version of the test files.

---

## 📚 Learning Resources

### REST API Concepts

- **What is a REST API?** A way for different applications to communicate over HTTP using standard methods (GET, POST, PUT, DELETE)
- **HTTP Methods:**
  - GET: Retrieve data
  - POST: Create new data
  - PUT: Update existing data
  - DELETE: Remove data

### JSON Format

- **What is JSON?** JavaScript Object Notation - a lightweight data format
- **Structure:** Uses key-value pairs, similar to Python dictionaries
- **Example:**
  ```json
  {
    "name": "Python",
    "status": "In Progress"
  }
  ```

### Flask Framework

- **What is Flask?** A lightweight Python web framework
- **Why use it?** Simple, easy to learn, perfect for beginners
- **Alternatives:** Django (more complex), FastAPI (modern)

## 🎯 Next Steps for Learning

1. **Experiment with the API:** Try creating, updating, and deleting courses
2. **Read the Code:** Open CodeCraftHub.py and understand how it works
3. **Add New Features:** Try adding a new endpoint or field
4. **Build a Frontend:** Create a simple HTML/JavaScript page to interact with the API
5. **Add Authentication:** Learn how to secure your API with user authentication
6. **Use a Database:** Replace JSON storage with SQLite or PostgreSQL

## 🤝 Contributing

This is a learning project. Feel free to:
- Fork the project
- Make changes
- Learn from the code
- Share your improvements

## 📝 License

This project is open source and available for educational purposes.

## 🆘 Need Help?

If you encounter issues not covered in this guide:
1. Check the error message carefully
2. Review the troubleshooting section above
3. Make sure the server is running
4. Verify your JSON format is correct
5. Check that you're using the correct HTTP method

---

**Happy Learning! 🎓**

Built with ❤️ using Flask and Python
