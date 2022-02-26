from base64 import b64encode
from io import BytesIO
from PIL import Image, ImageEnhance

def grayscale_transform(coloured_image_code: str) -> str:
    # image creating
    coloured_image_path = '/mnt/d/Computer_science/HSE/2_course/coursework/repo/DevContour/DemoApp/assets/demo.png'
    coloured_img = Image.open(coloured_image_path)

    # grayscale transformation
    filtered = ImageEnhance.Color(coloured_img)
    grayscaled_img = filtered.enhance(0)

    # return base64 format
    buffered = BytesIO()
    grayscaled_img.save(buffered, format='PNG')
    return b64encode(buffered.getvalue())
