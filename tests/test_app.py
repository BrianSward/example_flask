import requests
from datetime import datetime
import json

def test_user_post_route():
    # Define test data
    test_username = 'testUsername'
    test_text = 'testText'
    
    # Define expected response data
    expected_data = {
        'data': {
            'username': test_username,
            'text': test_text,
            'created': datetime.now().strftime("%a, %d %b %Y %H:%M:%S"),
        },
        'success': True
    }
    
    # Send POST request with test data
    url = 'http://localhost:5000/user-post'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'username': test_username, 'text': test_text})
    response = requests.post(url, headers=headers, data=data)
    
    # Check response status code
    assert response.status_code == 200
    
    # Check response data
    response_data = response.json()
    assert response_data['success'] == True
    assert response_data['data']['username'] == expected_data['data']['username']
    assert response_data['data']['text'] == expected_data['data']['text']
    assert response_data['data']['created'][:19] == expected_data['data']['created'][:19]


   # will remove these after confirming test results 
    print("response data: ", response_data)  
    print("expected data: ", expected_data)


# will remove after confirming test results
test_user_post_route()
