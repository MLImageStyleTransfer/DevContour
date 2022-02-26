import base64
from io import BytesIO
from PIL import Image, ImageEnhance

def grayscale_transform(coloured_image_code: str) -> str:
    # image creating
    code_only = coloured_image_code[23:]
    img_data = base64.b64decode(code_only)
    coloured_img = Image.open(BytesIO(img_data))

    # grayscale transformation
    filtered = ImageEnhance.Color(coloured_img)
    grayscaled_img = filtered.enhance(0)

    # return base64 format
    buffered = BytesIO()
    grayscaled_img.save(buffered, format='JPEG')
    return base64.b64encode(buffered.getvalue())
