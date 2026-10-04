"""
CodeCraftHub - A Simple Learning Platform API
This Flask application manages a personal course learning tracker.
All data is stored in a JSON file (courses.json).
"""

from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

# ============================================
# FLASK APP INITIALIZATION
# ============================================

app = Flask(__name__)

# Configuration
DATA_FILE = 'courses.json'
VALID_STATUSES = ['Not Started', 'In Progress', 'Completed']

# ============================================
# HELPER FUNCTIONS
# ============================================

def read_courses():
    """
    Read all courses from the JSON file.
    Returns an empty list if file doesn't exist or is empty.
    """
    # Check if file exists
    if not os.path.exists(DATA_FILE):
        # Create empty file with empty array
        write_courses([])
        return []
    
    try:
        with open(DATA_FILE, 'r') as file:
            content = file.read().strip()
            # Handle empty file
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error reading file: {e}")
        return []


def write_courses(courses):
    """
    Write courses list to the JSON file.
    Creates the file if it doesn't exist.
    """
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(courses, file, indent=4)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False


def get_next_id(courses):
    """
    Generate the next available ID for a new course.
    Starts from 1 if no courses exist.
    """
    if not courses:
        return 1
    # Find the maximum ID and add 1
    return max(course['id'] for course in courses) + 1


def find_course_index(courses, course_id):
    """
    Find the index of a course in the list by its ID.
    Returns the index if found, None otherwise.
    """
    for index, course in enumerate(courses):
        if course['id'] == course_id:
            return index
    return None


def validate_course_data(data, is_update=False):
    """
    Validate course data from request.
    Returns (is_valid, error_message)
    """
    if not data:
        return False, "No data provided in request body"
    
    # For POST requests, all fields are required
    if not is_update:
        required_fields = ['name', 'description', 'target_date', 'status']
        for field in required_fields:
            if field not in data or not data[field]:
                return False, f"Missing required field: {field}"
    
    # Validate status if provided
    if 'status' in data:
        if data['status'] not in VALID_STATUSES:
            return False, f"Invalid status. Must be one of: {', '.join(VALID_STATUSES)}"
    
    # Validate date format if provided
    if 'target_date' in data:
        try:
            datetime.strptime(data['target_date'], '%Y-%m-%d')
        except ValueError:
            return False, "Invalid date format. Use YYYY-MM-DD (e.g., 2024-12-31)"
    
    return True, None


def get_current_timestamp():
    """
    Get current timestamp in ISO format.
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# ============================================
# API ENDPOINTS
# ============================================

@app.route('/')
def home():
    """
    Home endpoint - displays API documentation
    """
    return jsonify({
        "message": "Welcome to CodeCraftHub Learning Platform API!",
        "version": "1.0",
        "endpoints": {
            "GET /": "API documentation",
            "GET /api/courses": "Get all courses",
            "GET /api/courses/stats": "Get course statistics",
            "GET /api/courses/<id>": "Get a specific course by ID",
            "POST /api/courses": "Create a new course",
            "PUT /api/courses/<id>": "Update a course by ID",
            "DELETE /api/courses/<id>": "Delete a course by ID"
        }
    })


@app.route('/api/courses', methods=['GET'])
def get_all_courses():
    """
    Get all courses.
    Query parameters:
    - status: Filter by status (Not Started, In Progress, Completed)
    """
    courses = read_courses()
    
    # Filter by status if provided
    status_filter = request.args.get('status')
    if status_filter:
        courses = [c for c in courses if c['status'] == status_filter]
    
    return jsonify({
        "count": len(courses),
        "courses": courses
    })


@app.route('/api/courses/stats', methods=['GET'])
def get_course_stats():
    """
    Get statistics about courses.
    Returns total count and breakdown by status.
    """
    courses = read_courses()
    
    # Count courses by status
    stats = {
        "total": len(courses),
        "by_status": {
            "Not Started": 0,
            "In Progress": 0,
            "Completed": 0
        }
    }
    
    # Count each status
    for course in courses:
        status = course['status']
        if status in stats['by_status']:
            stats['by_status'][status] += 1
    
    return jsonify(stats)


@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Get a specific course by ID.
    """
    courses = read_courses()
    index = find_course_index(courses, course_id)
    
    if index is None:
        return jsonify({"error": "Course not found"}), 404
    
    return jsonify(courses[index])


@app.route('/api/courses', methods=['POST'])
def create_course():
    """
    Create a new course.
    Required fields: name, description, target_date, status
    """
    data = request.get_json()
    
    # Validate data
    is_valid, error_message = validate_course_data(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400
    
    # Read existing courses
    courses = read_courses()
    
    # Create new course
    new_course = {
        "id": get_next_id(courses),
        "name": data['name'],
        "description": data['description'],
        "target_date": data['target_date'],
        "status": data['status'],
        "created_at": get_current_timestamp(),
        "updated_at": get_current_timestamp()
    }
    
    # Add to list and save
    courses.append(new_course)
    write_courses(courses)
    
    return jsonify({
        "message": "Course created successfully",
        "course": new_course
    }), 201


@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """
    Update a course by ID.
    All fields are optional.
    """
    data = request.get_json()
    
    # Validate data
    is_valid, error_message = validate_course_data(data, is_update=True)
    if not is_valid:
        return jsonify({"error": error_message}), 400
    
    # Read existing courses
    courses = read_courses()
    index = find_course_index(courses, course_id)
    
    if index is None:
        return jsonify({"error": "Course not found"}), 404
    
    # Update course fields
    if 'name' in data:
        courses[index]['name'] = data['name']
    if 'description' in data:
        courses[index]['description'] = data['description']
    if 'target_date' in data:
        courses[index]['target_date'] = data['target_date']
    if 'status' in data:
        courses[index]['status'] = data['status']
    
    # Update timestamp
    courses[index]['updated_at'] = get_current_timestamp()
    
    # Save changes
    write_courses(courses)
    
    return jsonify({
        "message": "Course updated successfully",
        "course": courses[index]
    })


@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    """
    Delete a course by ID.
    """
    courses = read_courses()
    index = find_course_index(courses, course_id)
    
    if index is None:
        return jsonify({"error": "Course not found"}), 404
    
    # Remove course
    deleted_course = courses.pop(index)
    write_courses(courses)
    
    return jsonify({
        "message": "Course deleted successfully",
        "deleted_course": deleted_course
    })


# ============================================
# ERROR HANDLERS
# ============================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


# ============================================
# MAIN ENTRY POINT
# ============================================

if __name__ == '__main__':
    # Ensure data file exists
    if not os.path.exists(DATA_FILE):
        write_courses([])
        print(f"Created {DATA_FILE}")
    
    # Get absolute path for display
    data_file_path = os.path.abspath(DATA_FILE)
    
    print("- CodeCraftHub API is starting...")
    print(f"- Data will be stored in: '{data_file_path}'")
    print("- API will be available at: http://localhost:5000")
    app.run(debug=True, host='127.0.0.1', port=5000)
