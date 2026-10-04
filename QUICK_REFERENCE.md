# CodeCraftHub API - Quick Reference

## Running the Server
```bash
cd U:\StudioProjects\codecrafthub
python app.py
```

## Base URL
```
http://localhost:5000
```

## Endpoints Summary

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API documentation |
| GET | `/api/courses` | Get all courses |
| GET | `/api/courses/stats` | Get course statistics |
| GET | `/api/courses?status=X` | Filter by status |
| GET | `/api/courses/<id>` | Get specific course |
| POST | `/api/courses` | Create new course |
| PUT | `/api/courses/<id>` | Update course |
| DELETE | `/api/courses/<id>` | Delete course |

## Valid Status Values
- `Not Started`
- `In Progress`
- `Completed`

## Date Format
`YYYY-MM-DD` (e.g., 2024-12-31)

## Quick Copy-Paste Commands (PowerShell)

### Create Course
```powershell
$body = @{name="Course Name"; description="Description"; target_date="2024-12-31"; status="In Progress"} | ConvertTo-Json
Invoke-RestMethod -Method POST -Uri "http://localhost:5000/api/courses" -Headers @{"Content-Type"="application/json"} -Body $body
```

### Get All Courses
```powershell
curl http://localhost:5000/api/courses -UseBasicParsing
```

### Get Course Statistics
```powershell
curl http://localhost:5000/api/courses/stats -UseBasicParsing
```

### Get One Course
```powershell
curl http://localhost:5000/api/courses/1 -UseBasicParsing
```

### Update Course
```powershell
$body = @{status="Completed"} | ConvertTo-Json
Invoke-RestMethod -Method PUT -Uri "http://localhost:5000/api/courses/1" -Headers @{"Content-Type"="application/json"} -Body $body
```

### Delete Course
```powershell
Invoke-RestMethod -Method DELETE -Uri "http://localhost:5000/api/courses/1" -Headers @{"Content-Type"="application/json"}
```

## Run All Tests

### Windows (PowerShell)
```powershell
.\test_api.bat
```

### Windows (Git Bash/WSL)
```bash
bash test_api.sh
```

### Or use the PowerShell script from TEST_GUIDE.md
