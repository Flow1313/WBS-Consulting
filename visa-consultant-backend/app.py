from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# 1. Enable CORS for all routes (allows frontend on a different port to connect)
CORS(app) 

# Dummy data for services (to replace your static HTML list)
SERVICES_DATA = [
    {"id": 1, "title": "Visa Consultation", "description": "We guide you through the visa application process with personalized expert advice and attention to detail.", "image": "shadeconsult1.jpg"},
    {"id": 2, "title": "Document Preparation", "description": "We ensure all your documents are accurately prepared and meet visa requirements, reducing the chances of rejection.", "image": "shade2.jpg"},
    {"id": 3, "title": "Interview Coaching", "description": "Get professional coaching to confidently prepare for your visa interview with mock sessions and tailored feedback.", "image": "shade3.jpg"},
    # ... add the other 3 services here for a complete list ...
]

@app.route('/', methods=['GET'])
def home():
    """Simple health check route."""
    return jsonify({"message": "Visa Consultant Backend is running!"})

# 2. API Endpoint to retrieve services
@app.route('/api/services', methods=['GET'])
def get_services():
    """Returns the list of all services as JSON."""
    return jsonify(SERVICES_DATA)

if __name__ == '__main__':
    # 3. Run the server on the specified port
    app.run(debug=True, port=5000)