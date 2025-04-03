import base64
import logging
from pathlib import Path

def encode_image_to_base64(image_path: str) -> str:
    """
    Encodes an image file to a base64 string.
    
    :param image_path: The path to the image file.
    :return: Base64-encoded string of the image.
    """
    try:
        file_path = Path(image_path)
        if not file_path.exists():
            logging.error(f"Image file not found: {image_path}")
            return ""
        with file_path.open("rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode("utf-8")
            return encoded
    except Exception as e:
        logging.error(f"Error encoding image: {e}")
        return ""
