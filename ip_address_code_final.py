import requests
import json
import sys
from typing import Optional, Dict

BASE_URL = "https://ipapi.co/json/"


def get_ip_info() -> Optional[Dict[str, object]]:
    """Fetch information about the current public IP address.

    Returns:
        A dictionary of IP information on success, or ``None`` if there was
        a network problem, an API error, or the request was rate limited.
    """
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


def main() -> None:
    """CLI entry point for the IP Address Project."""
    # Fetch IP information
    ip_info = get_ip_info()

    if not ip_info:
        print("Failed to retrieve IP information")
        sys.exit(1)

    # Print information with consistent formatting
    print("\n=== IP Address Information ===")
    print(f"IP Address : {ip_info.get('ip', 'Unknown')}")
    print(f"City      : {ip_info.get('city', 'Unknown')}")
    print(f"Region    : {ip_info.get('region', 'Unknown')}")
    print(f"Country   : {ip_info.get('country', 'Unknown')}")
    print(f"ISP       : {ip_info.get('org', 'Unknown')}")
    print(f"ASN       : {ip_info.get('asn', 'Unknown')}")
    print("===========================\n")


if __name__ == "__main__":
    main()

    main()
