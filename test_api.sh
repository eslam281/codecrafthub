#!/bin/bash

# CodeCraftHub API Test Script
# Usage: ./test_api.sh
# Make sure you're in the codecrafthub directory before running

BASE_URL="http://localhost:5000"

echo "=== CodeCraftHub API Test Suite ==="
echo ""

# Helper function to print test results
test_api() {
    local method=$1
    local endpoint=$2
    local data=$3
    
    echo "Testing: $method $endpoint"
    
    if [ -z "$data" ]; then
        response=$(curl -s -X "$method" "$BASE_URL$endpoint" -H "Content-Type: application/json")
    else
        response=$(curl -s -X "$method" "$BASE_URL$endpoint" -H "Content-Type: application/json" -d "$data")
    fi
    
    echo "Response: $response"
    echo ""
}

# Test 1: Create courses
echo "--- Creating Test Courses ---"
test_api "POST" "/api/courses" '{"name":"Python Fundamentals","description":"Learn Python programming","target_date":"2024-12-31","status":"In Progress"}'
test_api "POST" "/api/courses" '{"name":"Advanced JavaScript","description":"Master JS concepts","target_date":"2025-01-15","status":"Not Started"}'
test_api "POST" "/api/courses" '{"name":"HTML and CSS","description":"Build web pages","target_date":"2024-09-30","status":"Completed"}'

# Test 2: Get all courses
echo "--- Get All Courses ---"
test_api "GET" "/api/courses"

# Test 3: Filter by status
echo "--- Filter by Status ---"
test_api "GET" "/api/courses?status=In%20Progress"
test_api "GET" "/api/courses?status=Completed"

# Test 4: Get specific course
echo "--- Get Specific Course ---"
test_api "GET" "/api/courses/1"

# Test 5: Update course
echo "--- Update Course ---"
test_api "PUT" "/api/courses/1" '{"status":"Completed"}'
test_api "PUT" "/api/courses/2" '{"name":"Advanced JavaScript and ES6","description":"Master modern JS"}'

# Test 6: Delete course
echo "--- Delete Course ---"
test_api "DELETE" "/api/courses/3"

# Test 7: Error scenarios
echo "--- Error Scenarios ---"
test_api "POST" "/api/courses" '{"description":"Test","target_date":"2024-12-31","status":"In%20Progress"}'
test_api "POST" "/api/courses" '{"name":"Test","description":"Test","target_date":"2024-12-31","status":"Invalid"}'
test_api "GET" "/api/courses/999"
test_api "PUT" "/api/courses/999" '{"name":"Test"}'
test_api "DELETE" "/api/courses/999"

echo "=== Test Suite Complete ==="
