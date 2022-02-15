from PIL import Image, ImageEnhance

def grayscale_transform(coloured_image_blob: str) -> str:
    coloured_img = Image.from_blob(coloured_image_blob)
#     filter = ImageEnhance.Color(coloured_img)
#     grayscaled_img = filter.enhance(0)
#     grayscaled_img.save('../../assets/res.png', 'PNG')
    return 'ttt'