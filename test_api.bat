@echo off
REM CodeCraftHub API Test Script for Windows
REM Usage: test_api.bat
REM Make sure you're in the codecrafthub directory before running

set BASE_URL=http://localhost:5000

echo === CodeCraftHub API Test Suite ===
echo.

echo --- Creating Test Courses ---
curl -s -X POST %BASE_URL%/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Python Fundamentals\",\"description\":\"Learn Python programming\",\"target_date\":\"2024-12-31\",\"status\":\"In Progress\"}"
echo.
curl -s -X POST %BASE_URL%/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Advanced JavaScript\",\"description\":\"Master JS concepts\",\"target_date\":\"2025-01-15\",\"status\":\"Not Started\"}"
echo.
curl -s -X POST %BASE_URL%/api/courses -H "Content-Type: application/json" -d "{\"name\":\"HTML and CSS\",\"description\":\"Build web pages\",\"target_date\":\"2024-09-30\",\"status\":\"Completed\"}"
echo.

echo --- Get All Courses ---
curl -s %BASE_URL%/api/courses
echo.

echo --- Get Course Statistics ---
curl -s %BASE_URL%/api/courses/stats
echo.

echo --- Filter by Status ---
curl -s "%BASE_URL%/api/courses?status=In%20Progress"
echo.
curl -s "%BASE_URL%/api/courses?status=Completed"
echo.

echo --- Get Specific Course ---
curl -s %BASE_URL%/api/courses/1
echo.

echo --- Update Course ---
curl -s -X PUT %BASE_URL%/api/courses/1 -H "Content-Type: application/json" -d "{\"status\":\"Completed\"}"
echo.
curl -s -X PUT %BASE_URL%/api/courses/2 -H "Content-Type: application/json" -d "{\"name\":\"Advanced JavaScript and ES6\",\"description\":\"Master modern JS\"}"
echo.

echo --- Delete Course ---
curl -s -X DELETE %BASE_URL%/api/courses/3
echo.

echo --- Error Scenarios ---
curl -s -X POST %BASE_URL%/api/courses -H "Content-Type: application/json" -d "{\"description\":\"Test\",\"target_date\":\"2024-12-31\",\"status\":\"In%20Progress\"}"
echo.
curl -s -X POST %BASE_URL%/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Test\",\"description\":\"Test\",\"target_date\":\"2024-12-31\",\"status\":\"Invalid\"}"
echo.
curl -s %BASE_URL%/api/courses/999
echo.
curl -s -X PUT %BASE_URL%/api/courses/999 -H "Content-Type: application/json" -d "{\"name\":\"Test\"}"
echo.
curl -s -X DELETE %BASE_URL%/api/courses/999
echo.

echo === Test Suite Complete ===
pause
