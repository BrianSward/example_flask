# Flask User Post API

This is a simple Flask application that defines an API endpoint for receiving user posts. The /user-post endpoint accepts a JSON payload containing a username and text field, restructures the data, and returns it as a JSON response.

## Requirements

To run this Flask application, you'll need:

- Python 3.x (for example)  
        `python3.11 -m venv .venv`
- Then just use  
        `pip install -r requirements.txt`

## Usage

1. Clone this repository to your local machine.
2. Open a terminal or command prompt and navigate to the repository directory.
3. To start the Flask server:  
    `flask run`
4. Send a POST request to the /user-post endpoint with a JSON payload containing a username and text field. For example:  
    `curl -X POST -H "Content-Type: application/json" -d '{"username": "testUsername", "text": "testText"}' http://localhost:5000/user-post`
5. The Flask server will return a JSON response containing the restructured data.

## Testing

This repository includes a simple backend test for the /user-post endpoint, implemented using the pytest testing framework. To run the test, follow these steps:

- Ensure that the Flask server is running (python app.py).
- Open a terminal or command prompt and navigate to the repository directory.
- Run the test_app.py file:  
    `python -m pytest test_app.py`
- The test should pass if the /user-post endpoint returns the expected JSON response.

## License

This Flask User Post API is released under the MIT License. See LICENSE for details.

### Acknowledgments

- This Flask application is based on the Flask tutorial found at https://flask.palletsprojects.com/en/2.0.x/quickstart/.
- My teachers at Codefellows.
