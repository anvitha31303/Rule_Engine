import requests
import json

url = "http://127.0.0.1:5000/evaluate_rule"
headers = {"Content-Type": "application/json"}
payload = {
    "ast": {
        "type": "operator",
        "value": "AND",
        "left": {
            "type": "operator",
            "value": "Gt",
            "left": {
                "type": "operand",
                "value": "age"
            },
            "right": {
                "type": "operand",
                "value": 30
            }
        },
        "right": {
            "type": "operator",
            "value": "Eq",
            "left": {
                "type": "operand",
                "value": "department"
            },
            "right": {
                "type": "operand",
                "value": "Sales"
            }
        }
    },
    "data": {
        "age": 35,
        "department": "Sales"
    }
}

# Send POST request to the Flask server
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Print the response
print(response.json())
