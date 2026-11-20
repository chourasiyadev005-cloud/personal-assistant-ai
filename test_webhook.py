
import requests

# Your n8n Webhook URL
WEBHOOK_URL = "https://dev0149.app.n8n.cloud/webhook-test/personal-assistant"

# Data we want to send to n8n
payload = {
    "message": "Tell me the conversion of INR TO USD"
}

try:
    # Send POST request to n8n
    response = requests.post(
        WEBHOOK_URL,
        json=payload,
        timeout=30
    )

    # Check if request was successful
    response.raise_for_status()

    # Print response from n8n
    print("Response from n8n:")
    print(response.json()[0]["output"])


except requests.exceptions.RequestException as e:
    print("Error:", e)
