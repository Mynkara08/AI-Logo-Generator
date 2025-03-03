from PIL import Image, ImageDraw, ImageFont

def generate_image(text, filename):
    img = Image.new('RGB', (400, 200), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    # Load a font with fallback
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font = ImageFont.load_default()

    # Get text size properly
    bbox = d.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (img.width - text_width) / 2
    text_y = (img.height - text_height) / 2

    d.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

    img.save(filename)
