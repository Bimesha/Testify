import pytesseract
from PIL import Image

def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Example usage with specific image path
image_path = r'C:\Users\Bimesha\PycharmProjects\pythonProject7\A1.png'  # Ensure this is the correct path to your image
extracted_text = extract_text(image_path)
print(extracted_text)
