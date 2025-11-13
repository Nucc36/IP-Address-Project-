import requests
import json
import sys
from typing import Optional, Dict
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
@app.route('/')

def index():
    """Home page with links to JSON and HTML views."""
    return (
        "<html>"
        "<head><title>IP Address Information Service</title></head>"
        "<body>"
        "<h1>IP Address Information Service</h1>"
        "<ul>"
        "<li><a href=\"/ip\">View JSON</a></li>"
        "<li><a href=\"/ip/html\">View HTML</a></li>"
        "</ul>"
        "</body>"
        "</html>"
    )

BASE_URL = "https://ipapi.co/json/"

def get_ip_info() -> Optional[Dict[str, object]]:
    try:
        # Request with timeout to avoid freezing
        response = requests.get(BASE_URL, timeout=5)

        # Check for rate limiting
        if response.status_code == 429:
            print("Error: Rate limit reached. Please wait before trying again.")
            return None

        # Raise error for other 4xx/5xx codes
        response.raise_for_status()

        # Parse the JSON data
        data = response.json()

        # ipapi.co returns an "error" field if there is a problem with the request
        if isinstance(data, dict) and data.get("error"):
            print(f"API Error: {data.get('reason', 'Unknown error')}")
            return None
        return data

    except requests.Timeout:
        print("Error: Request timed out. Please check your internet connection.")
        return None
    except requests.RequestException as e:
        print(f"Error fetching IP information: {e}")
        return None
    except json.JSONDecodeError:
        print("Error: Received invalid JSON response")
        return None

@app.route('/ip')
def ip_json():
    """Return IP information as JSON."""
    data = get_ip_info()
    print("[DEBUG] /ip called; get_ip_info returned {}".format("data" if data else "None"))
    if not data:
        return jsonify({"error": "Failed to retrieve IP information"}), 503

    result = {
        "ip": data.get("ip"),
        "city": data.get("city"),
        "region": data.get("region"),
        "country": data.get("country"),
        "isp": data.get("org"),
        "asn": data.get("asn"),
    }
    return jsonify(result)

@app.route('/ip/')
def ip_json_slash():
    """Support trailing-slash URL by forwarding to the canonical `/ip` handler."""
    return ip_json()

@app.route('/ip/html')
def ip_html():
    """Return a small HTML page with the IP information."""
    data = get_ip_info()
    if not data:
        return ("<h1>Failed to retrieve IP information</h1>"), 503

    html = (
        f"<html><head><title>IP Info: {data.get('ip','Unknown')}</title></head><body>"
        f"<h1>IP Address Information</h1>"
        f"<p><strong>IP Address:</strong> {data.get('ip','Unknown')}</p>"
        f"<p><strong>City:</strong> {data.get('city','Unknown')}</p>"
        f"<p><strong>Region:</strong> {data.get('region','Unknown')}</p>"
        f"<p><strong>Country:</strong> {data.get('country','Unknown')}</p>"
        f"<p><strong>ISP:</strong> {data.get('org','Unknown')}</p>"
        f"<p><strong>ASN:</strong> {data.get('asn','Unknown')}</p>"
        "</body></html>"
    )
    return html

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
