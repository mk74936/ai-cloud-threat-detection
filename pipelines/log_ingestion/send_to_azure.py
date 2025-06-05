import json
import requests

# Azure Log Analytics Workspace Info (replace with your actual values)
WORKSPACE_ID = "YOUR_WORKSPACE_ID"
SHARED_KEY = "YOUR_SHARED_KEY"
LOG_TYPE = "CustomAzureLogs"

def build_signature(date, content_length, method, content_type, resource):
    import hashlib, hmac, base64
    x_headers = 'x-ms-date:' + date
    string_to_hash = f"{method}\n{str(content_length)}\n{content_type}\n{x_headers}\n{resource}"
    bytes_to_hash = bytes(string_to_hash, encoding="utf-8")
    decoded_key = base64.b64decode(SHARED_KEY)
    encoded_hash = base64.b64encode(hmac.new(decoded_key, bytes_to_hash, digestmod=hashlib.sha256).digest()).decode()
    return f"SharedKey {WORKSPACE_ID}:{encoded_hash}"

def post_data(file_path):
    with open(file_path, "r") as f:
        body = f.read()
    uri = f"https://{WORKSPACE_ID}.ods.opinsights.azure.com/api/logs?api-version=2016-04-01"
    content_type = "application/json"
    rfc1123date = requests.utils.formatdate(timeval=None, localtime=False, usegmt=True)
    resource = "/api/logs"
    method = "POST"
    content_length = len(body)
    signature = build_signature(rfc1123date, content_length, method, content_type, resource)
    headers = {
        "Content-Type": content_type,
        "Authorization": signature,
        "Log-Type": LOG_TYPE,
        "x-ms-date": rfc1123date
    }
    response = requests.post(uri, data=body, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(response.text)

if __name__ == "__main__":
    post_data("../../logs/azure_sample.json")