import requests
import os
from urllib.parse import urlparse
import sys

def fetch_image(url, save_dir="images"):
    """
    Fetches an image from the web and saves it locally.
    Implements Ubuntu principles:
      - Community: Connect to the web community via requests
      - Respect: Handle errors gracefully
      - Sharing: Organize images into a directory
      - Practicality: Simple reusable function
    """

    try:
        # Send HTTP request
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not fetch image: {e}")
        return None

    # Ensure the save directory exists
    os.makedirs(save_dir, exist_ok=True)

    # Extract filename from URL
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    # If no filename found, generate one
    if not filename:
        filename = "downloaded_image.jpg"

    # Full path
    filepath = os.path.join(save_dir, filename)

    try:
        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"[SUCCESS] Image saved at: {filepath}")
        return filepath
    except Exception as e:
        print(f"[ERROR] Could not save image: {e}")
        return None


# ---------------- RUN SCRIPT ----------------
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fetch_image.py <image_url>")
    else:
        url = sys.argv[1]
        fetch_image(url)
