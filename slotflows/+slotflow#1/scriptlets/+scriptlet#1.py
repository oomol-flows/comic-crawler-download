from oocana import Context
import os
import requests
from urllib.parse import unquote, urlparse

#region generated meta
import typing
class Inputs(typing.TypedDict):
    item: typing.Any
    save_dir: str | None
class Outputs(typing.TypedDict):
    item: typing.Any
#endregion

def main(params: Inputs, context: Context) -> Outputs:
    url = params.get("item")
    save_dir = params.get("save_dir")
    if save_dir is None:
        save_dir = context.session_dir
    image_path = download_image(url, save_dir)

    return {"item": image_path}

def download_image(url, save_dir='images'):
    """
    Downloads an image and saves it with the filename from the URL.
    
    Args:
        url (str): The URL of the image.
        save_dir (str): The directory to save the image, defaults to 'images' folder in the current directory.
    """
    # Create the save directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)
    
    try:
        # Send HTTP GET request
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check if the request was successful
        
        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = unquote(os.path.basename(parsed_url.path))
        
        # Use a default filename if no filename is present in the URL
        if not filename:
            filename = "downloaded_image.jpg"
        
        # Construct the save path
        save_path = os.path.join(save_dir, filename)
        
        # Save the image
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"Image saved to: {save_path}")
        return save_path
    
    except Exception as e:
        print(f"Download failed: {e}")
        return None