# CodeCraftHub API Test Guide

Complete test cases for the CodeCraftHub Learning Platform API.  
Server should be running at: http://localhost:5000

## Running the Server

To start the server:
```bash
cd U:\StudioProjects\codecrafthub
python app.py
```

You should see output similar to:
```
- CodeCraftHub API is starting...
- Data will be stored in: '/path/to/courses.json'
- API will be available at: http://localhost:5000
```

## Table of Contents
1. [Setup & Helper Commands](#setup--helper-commands)
2. [GET / - API Documentation](#get---api-documentation)
3. [POST /courses - Create Course](#post-courses---create-course)
4. [GET /courses - Get All Courses](#get-courses---get-all-courses)
5. [GET /courses/<id> - Get Specific Course](#get-coursesid---get-specific-course)
6. [PUT /courses/<id> - Update Course](#put-coursesid---update-course)
7. [DELETE /courses/<id> - Delete Course](#delete-coursesid---delete-course)
8. [Error Scenarios](#error-scenarios)

---

## Setup & Helper Commands

### PowerShell users: Use this wrapper to avoid security warnings
```powershell
function Invoke-ApiRequest {
    param(
        [string]$Method = "GET",
        [string]$Url,
        [string]$Body = $null
    )
    
    $headers = @{
        "Content-Type" = "application/json"
    }
    
    if ($Body) {
        Invoke-RestMethod -Method $Method -Uri $Url -Headers $headers -Body $Body
    } else {
        Invoke-RestMethod -Method $Method -Uri $Url -Headers $headers
    }
}
```

### Clear all data (reset courses.json)
```powershell
Remove-Item courses.json -ErrorAction SilentlyContinue
```

---

## GET / - API Documentation

### Test Command
```powershell
curl http://localhost:5000 -UseBasicParsing
```

### Expected Response (Success - 200 OK)
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

## POST /courses - Create Course

### Test 1: Create a valid course (All required fields)

#### Command
```powershell
$body = @{
    name = "Python Fundamentals"
    description = "Learn Python programming from scratch"
    target_date = "2024-12-31"
    status = "In Progress"
} | ConvertTo-Json

Invoke-RestMethod -Method POST -Uri "http://localhost:5000/courses" -Headers @{"Content-Type"="application/json"} -Body $body
```

#### Expected Response (Success - 201 Created)
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

### Test 2: Create course with "Not Started" status

#### Command
```powershell
$body = @{
    name = "Advanced JavaScript"
    description = "Master advanced JS concepts"
    target_date = "2025-01-15"
    status = "Not Started"
} | ConvertTo-Json

Invoke-RestMethod -Method POST -Uri "http://localhost:5000/courses" -Headers @{"Content-Type"="application/json"} -Body $body
```

#### Expected Response (Success - 201 Created)
```json
{
  "message": "Course created successfully",
  "course": {
    "id": 2,
    "name": "Advanced JavaScript",
    "description": "Master advanced JS concepts",
    "target_date": "2025-01-15",
    "status": "Not Started",
    "created_at": "2024-10-04 18:11:00",
    "updated_at": "2024-10-04 18:11:00"
  }
}
```

### Test 3: Create course with "Completed" status

#### Command
```powershell
$body = @{
    name = "HTML and CSS Basics"
    description = "Build beautiful web pages"
    target_date = "2024-09-30"
    status = "Completed"
} | ConvertTo-Json

Invoke-RestMethod -Method POST -Uri "http://localhost:5000/courses" -Headers @{"Content-Type"="application/json"} -Body $body
```

#### Expected Response (Success - 201 Created)
```json
{
  "message": "Course created successfully",
  "course": {
    "id": 3,
    "name": "HTML and CSS Basics",
    "description": "Build beautiful web pages",
    "target_date": "2024-09-30",
    "status": "Completed",
    "created_at": "2024-10-04 18:12:00",
    "updated_at": "2024-10-04 18:12:00"
  }
}
```

---

## GET /courses - Get All Courses

### Test 1: Get all courses (no filter)

#### Command
```powershell
curl http://localhost:5000/courses -UseBasicParsing
```

#### Expected Response (Success - 200 OK)
```json
{
  "count": 3,
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
      "description": "Master advanced JS concepts",
      "target_date": "2025-01-15",
      "status": "Not Started",
      "created_at": "2024-10-04 18:11:00",
      "updated_at": "2024-10-04 18:11:00"
    },
    {
      "id": 3,
      "name": "HTML and CSS Basics",
      "description": "Build beautiful web pages",
      "target_date": "2024-09-30",
      "status": "Completed",
      "created_at": "2024-10-04 18:12:00",
      "updated_at": "2024-10-04 18:12:00"
    }
  ]
}
```

### Test 2: Filter courses by status "In Progress"

#### Command
```powershell
curl "http://localhost:5000/courses?status=In%20Progress" -UseBasicParsing
```

#### Expected Response (Success - 200 OK)
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

### Test 3: Filter courses by status "Completed"

#### Command
```powershell
curl "http://localhost:5000/courses?status=Completed" -UseBasicParsing
```

#### Expected Response (Success - 200 OK)
```json
{
  "count": 1,
  "courses": [
    {
      "id": 3,
      "name": "HTML and CSS Basics",
      "description": "Build beautiful web pages",
      "target_date": "2024-09-30",
      "status": "Completed",
      "created_at": "2024-10-04 18:12:00",
      "updated_at": "2024-10-04 18:12:00"
    }
  ]
}
```

### Test 4: Filter courses by status "Not Started"

#### Command
```powershell
curl "http://localhost:5000/courses?status=Not Started" -UseBasicParsing
```

#### Expected Response (Success - 200 OK)
```json
{
  "count": 1,
  "courses": [
    {
      "id": 2,
      "name": "Advanced JavaScript",
      "description": "Master advanced JS concepts",
      "target_date": "2025-01-15",
      "status": "Not Started",
      "created_at": "2024-10-04 18:11:00",
      "updated_at": "2024-10-04 18:11:00"
    }
  ]
}
```

---

## GET /courses/<id> - Get Specific Course

### Test 1: Get existing course (ID: 1)

#### Command
```powershell
curl http://localhost:5000/courses/1 -UseBasicParsing
```

#### Expected Response (Success - 200 OK)
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

### Test 2: Get existing course (ID: 2)

#### Command
```powershell
curl http://localhost:5000/courses/2 -UseBasicParsing
```

#### Expected Response (Success - 200 OK)
```json
{
  "id": 2,
  "name": "Advanced JavaScript",
  "description": "Master advanced JS concepts",
  "target_date": "2025-01-15",
  "status": "Not Started",
  "created_at": "2024-10-04 18:11:00",
  "updated_at": "2024-10-04 18:11:00"
}
```

---

## PUT /courses/<id> - Update Course

### Test 1: Update course name and description

#### Command
```powershell
$body = @{
    name = "Python Fundamentals - Updated"
    description = "Updated: Learn Python programming from scratch with advanced topics"
} | ConvertTo-Json

Invoke-RestMethod -Method PUT -Uri "http://localhost:5000/courses/1" -Headers @{"Content-Type"="application/json"} -Body $body
```

#### Expected Response (Success - 200 OK)
```json
{
  "message": "Course updated successfully",
  "course": {
    "id": 1,
    "name": "Python Fundamentals - Updated",
    "description": "Updated: Learn Python programming from scratch with advanced topics",
    "target_date": "2024-12-31",
    "status": "In Progress",
    "created_at": "2024-10-04 18:10:00",
    "updated_at": "2024-10-04 18:15:00"
  }
}
```

### Test 2: Update course status to "Completed"

#### Command
```powershell
$body = @{
    status = "Completed"
} | ConvertTo-Json

Invoke-RestMethod -Method PUT -Uri "http://localhost:5000/courses/1" -Headers @{"Content-Type"="application/json"} -Body $body
```

#### Expected Response (Success - 200 OK)
```json
{
  "message": "Course updated successfully",
  "course": {
    "id": 1,
    "name": "Python Fundamentals - Updated",
    "description": "Updated: Learn Python programming from scratch with advanced topics",
    "target_date": "2024-12-31",
    "status": "Completed",
    "created_at": "2024-10-04 18:10:00",
    "updated_at": "2024-10-04 18:16:00"
  }
}
```

### Test 3: Update target date

#### Command
```powershell
$body = @{
    target_date = "2025-02-28"
} | ConvertTo-Json

Invoke-RestMethod -Method PUT -Uri "http://localhost:5000/courses/2" -Headers @{"Content-Type"="application/json"} -Body $body
```

#### Expected Response (Success - 200 OK)
```json
{
  "message": "Course updated successfully",
  "course": {
    "id": 2,
    "name": "Advanced JavaScript",
    "description": "Master advanced JS concepts",
    "target_date": "2025-02-28",
    "status": "Not Started",
    "created_at": "2024-10-04 18:11:00",
    "updated_at": "2024-10-04 18:17:00"
  }
}
```

### Test 4: Update multiple fields at once

#### Command
```powershell
$body = @{
    name = "Advanced JavaScript and ES6"
    description = "Master modern JavaScript including ES6+ features"
    status = "In Progress"
    target_date = "2025-03-15"
} | ConvertTo-Json

Invoke-RestMethod -Method PUT -Uri "http://localhost:5000/courses/2" -Headers @{"Content-Type"="application/json"} -Body $body
```

#### Expected Response (Success - 200 OK)
```json
{
  "message": "Course updated successfully",
  "course": {
    "id": 2,
    "name": "Advanced JavaScript & ES6",
    "description": "Master modern JavaScript including ES6+ features",
    "target_date": "2025-03-15",
    "status": "In Progress",
    "created_at": "2024-10-04 18:11:00",
    "updated_at": "2024-10-04 18:18:00"
  }
}
```

---

## DELETE /courses/<id> - Delete Course

### Test 1: Delete existing course (ID: 3)

#### Command
```powershell
Invoke-RestMethod -Method DELETE -Uri "http://localhost:5000/courses/3" -Headers @{"Content-Type"="application/json"}
```

#### Expected Response (Success - 200 OK)
```json
{
  "message": "Course deleted successfully",
  "deleted_course": {
    "id": 3,
    "name": "HTML & CSS Basics",
    "description": "Build beautiful web pages",
    "target_date": "2024-09-30",
    "status": "Completed",
    "created_at": "2024-10-04 18:12:00",
    "updated_at": "2024-10-04 18:12:00"
  }
}
```

### Test 2: Verify deletion by getting all courses

#### Command
```powershell
curl http://localhost:5000/courses -UseBasicParsing
```

#### Expected Response (Success - 200 OK - should show only 2 courses)
```json
{
  "count": 2,
  "courses": [
    {
      "id": 1,
      "name": "Python Fundamentals - Updated",
      "description": "Updated: Learn Python programming from scratch with advanced topics",
      "target_date": "2024-12-31",
      "status": "Completed",
      "created_at": "2024-10-04 18:10:00",
      "updated_at": "2024-10-04 18:16:00"
    },
    {
      "id": 2,
      "name": "Advanced JavaScript & ES6",
      "description": "Master modern JavaScript including ES6+ features",
      "target_date": "2025-03-15",
      "status": "In Progress",
      "created_at": "2024-10-04 18:11:00",
      "updated_at": "2024-10-04 18:18:00"
    }
  ]
}
```

---

## Error Scenarios

### Error 1: POST - Missing required field (name)

#### Command
```powershell
$body = @{
    description = "Learn Python programming"
    target_date = "2024-12-31"
    status = "In Progress"
} | ConvertTo-Json

Invoke-RestMethod -Method POST -Uri "http://localhost:5000/courses" -Headers @{"Content-Type"="application/json"} -Body $body
```

#### Expected Response (Error - 400 Bad Request)
```json
{
  "error": "Missing required field: name"
}
```

### Error 2: POST - Missing all required fields

#### Command
```powershell
$body = @{} | ConvertTo-Json

Invoke-RestMethod -Method POST -Uri "http://localhost:5000/courses" -Headers @{"Content-Type"="application/json"} -Body $body
```

#### Expected Response (Error - 400 Bad Request)
```json
{
  "error": "Missing required field: name"
}
```

### Error 3: POST - Invalid status value

#### Command
```powershell
$body = @{
    name = "Data Science"
    description = "Learn data science with Python"
    target_date = "2024-12-31"
    status = "Active"
} | ConvertTo-Json

Invoke-RestMethod -Method POST -Uri "http://localhost:5000/courses" -Headers @{"Content-Type"="application/json"} -Body $body
```

#### Expected Response (Error - 400 Bad Request)
```json
{
  "error": "Invalid status. Must be one of: Not Started, In Progress, Completed"
}
```

### Error 4: POST - Invalid date format

#### Command
```powershell
$body = @{
    name = "Machine Learning"
    description = "Learn ML algorithms"
    target_date = "12/31/2024"
    status = "Not Started"
} | ConvertTo-Json

Invoke-RestMethod -Method POST -Uri "http://localhost:5000/courses" -Headers @{"Content-Type"="application/json"} -Body $body
```

#### Expected Response (Error - 400 Bad Request)
```json
{
  "error": "Invalid date format. Use YYYY-MM-DD (e.g., 2024-12-31)"
}
```

### Error 5: POST - Empty field value

#### Command
```powershell
$body = @{
    name = ""
    description = "Learn Python"
    target_date = "2024-12-31"
    status = "In Progress"
} | ConvertTo-Json

Invoke-RestMethod -Method POST -Uri "http://localhost:5000/courses" -Headers @{"Content-Type"="application/json"} -Body $body
```

#### Expected Response (Error - 400 Bad Request)
```json
{
  "error": "Missing required field: name"
}
```

### Error 6: PUT - Invalid status on update

#### Command
```powershell
$body = @{
    status = "Active"
} | ConvertTo-Json

Invoke-RestMethod -Method PUT -Uri "http://localhost:5000/courses/1" -Headers @{"Content-Type"="application/json"} -Body $body
```

#### Expected Response (Error - 400 Bad Request)
```json
{
  "error": "Invalid status. Must be one of: Not Started, In Progress, Completed"
}
```

### Error 7: PUT - Invalid date format on update

#### Command
```powershell
$body = @{
    target_date = "31-12-2024"
} | ConvertTo-Json

Invoke-RestMethod -Method PUT -Uri "http://localhost:5000/courses/1" -Headers @{"Content-Type"="application/json"} -Body $body
```

#### Expected Response (Error - 400 Bad Request)
```json
{
  "error": "Invalid date format. Use YYYY-MM-DD (e.g., 2024-12-31)"
}
```

### Error 8: GET - Course not found (non-existent ID)

#### Command
```powershell
curl http://localhost:5000/courses/999 -UseBasicParsing
```

#### Expected Response (Error - 404 Not Found)
```json
{
  "error": "Course not found"
}
```

### Error 9: PUT - Update non-existent course

#### Command
```powershell
$body = @{
    name = "New Name"
} | ConvertTo-Json

Invoke-RestMethod -Method PUT -Uri "http://localhost:5000/courses/999" -Headers @{"Content-Type"="application/json"} -Body $body
```

#### Expected Response (Error - 404 Not Found)
```json
{
  "error": "Course not found"
}
```

### Error 10: DELETE - Delete non-existent course

#### Command
```powershell
Invoke-RestMethod -Method DELETE -Uri "http://localhost:5000/courses/999" -Headers @{"Content-Type"="application/json"}
```

#### Expected Response (Error - 404 Not Found)
```json
{
  "error": "Course not found"
}
```

### Error 11: Invalid endpoint (404)

#### Command
```powershell
curl http://localhost:5000/invalid -UseBasicParsing
```

#### Expected Response (Error - 404 Not Found)
```json
{
  "error": "Endpoint not found"
}
```

---

## Quick Test Script (PowerShell)

Copy and paste this entire script to run all tests:

```powershell
# Define helper function
function Test-Api {
    param([string]$Method, [string]$Uri, [hashtable]$Body)
    
    $headers = @{"Content-Type" = "application/json"}
    $bodyJson = if ($Body) { $Body | ConvertTo-Json } else { $null }
    
    try {
        $response = Invoke-RestMethod -Method $Method -Uri $Uri -Headers $headers -Body $bodyJson
        Write-Host "✓ SUCCESS: $Method $Uri" -ForegroundColor Green
        return $response
    } catch {
        Write-Host "✗ ERROR: $Method $Uri" -ForegroundColor Red
        Write-Host "  $($_.Exception.Message)" -ForegroundColor Red
        return $null
    }
}

Write-Host "`n=== CodeCraftHub API Test Suite ===`n" -ForegroundColor Cyan

# Test 1: Create courses
Write-Host "Creating test courses..." -ForegroundColor Yellow
Test-Api -Method POST -Uri "http://localhost:5000/courses" -Body @{
    name = "Python Fundamentals"
    description = "Learn Python programming"
    target_date = "2024-12-31"
    status = "In Progress"
}

Test-Api -Method POST -Uri "http://localhost:5000/courses" -Body @{
    name = "Advanced JavaScript"
    description = "Master JS concepts"
    target_date = "2025-01-15"
    status = "Not Started"
}

Test-Api -Method POST -Uri "http://localhost:5000/courses" -Body @{
    name = "HTML and CSS"
    description = "Build web pages"
    target_date = "2024-09-30"
    status = "Completed"
}

# Test 2: Get all courses
Write-Host "`nGetting all courses..." -ForegroundColor Yellow
Test-Api -Method GET -Uri "http://localhost:5000/courses"

# Test 3: Get specific course
Write-Host "`nGetting course ID 1..." -ForegroundColor Yellow
Test-Api -Method GET -Uri "http://localhost:5000/courses/1"

# Test 4: Update course
Write-Host "`nUpdating course ID 1..." -ForegroundColor Yellow
Test-Api -Method PUT -Uri "http://localhost:5000/courses/1" -Body @{
    status = "Completed"
}

# Test 5: Delete course
Write-Host "`nDeleting course ID 3..." -ForegroundColor Yellow
Test-Api -Method DELETE -Uri "http://localhost:5000/courses/3"

# Test 6: Error - Missing field
Write-Host "`nTesting error: Missing required field..." -ForegroundColor Yellow
Test-Api -Method POST -Uri "http://localhost:5000/courses" -Body @{
    description = "Test"
    target_date = "2024-12-31"
    status = "In Progress"
}

# Test 7: Error - Invalid status
Write-Host "`nTesting error: Invalid status..." -ForegroundColor Yellow
Test-Api -Method POST -Uri "http://localhost:5000/courses" -Body @{
    name = "Test"
    description = "Test"
    target_date = "2024-12-31"
    status = "Invalid"
}

# Test 8: Error - Course not found
Write-Host "`nTesting error: Course not found..." -ForegroundColor Yellow
Test-Api -Method GET -Uri "http://localhost:5000/courses/999"

Write-Host "`n=== Test Suite Complete ===`n" -ForegroundColor Cyan
```

---

## Notes

- All timestamps in responses are dynamic and will vary
- IDs are auto-incremented starting from 1
- The `updated_at` field changes on every PUT operation
- Use `-UseBasicParsing` with curl in PowerShell to avoid security warnings
- For Git Bash or Linux/macOS, use standard curl without `-UseBasicParsing`
