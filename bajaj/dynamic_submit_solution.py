
import requests

def main():
    registration_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    registration_payload = {
        "name": "John Doe",
        "regNo": "REG12347",
        "email": "john@example.com"
    }

    response = requests.post(registration_url, json=registration_payload)

    if response.status_code != 200:
        print("Failed to generate webhook.")
        print("Response:", response.text)
        return

    data = response.json()
    webhook_url = data.get("webhook")
    access_token = data.get("accessToken")

    if not webhook_url or not access_token:
        print("Webhook URL or Access Token missing in response.")
        return

    try:
        with open("query.sql", "r") as f:
            final_query = f.read().strip()
    except FileNotFoundError:
        print("query.sql file not found. Please place your SQL query in a file named 'query.sql'.")
        return

    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }

    submission_payload = {
        "finalQuery": final_query
    }

    submission_response = requests.post(webhook_url, json=submission_payload, headers=headers)

    if submission_response.status_code == 200:
        print(" Solution submitted successfully.")
    else:
        print(" Submission failed.")
        print("Status Code:", submission_response.status_code)
        print("Response:", submission_response.text)

if __name__ == "__main__":
    main()
