import requests

GITHUB_TOKEN = "your_token_here"
REPO = "your_username/your_repo"

def create_issue(title, body):
    url = f"https://api.github.com/repos/{REPO}/issues"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "title": title,
        "body": body
    }
    response = requests.post(url, json=payload, headers=headers)
    print("Issue created:", response.status_code, response.json())

if __name__ == "__main__":
    create_issue("🚨 Security Alert", "Suspicious login from 198.51.100.0 detected in AWS logs.")
