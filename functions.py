from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def writer_func(raqam, guvohnoma_num, fam, ism, ismi_sharifi, xona_num, date, image_file_name):
    img = Image.open(f"pic.jpg")

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("arial.ttf", 43)
    if len(raqam) == 1:
        draw.text((35, 173), f"{raqam}", (4,24,107), font=ImageFont.truetype("arial.ttf", 40))
    elif len(raqam) == 2:
        draw.text((30, 180), f"{raqam}", (4,24,107), font=ImageFont.truetype("arial.ttf", 30))
    draw.text((320, 348), f"{guvohnoma_num}", (34, 21, 94), font=font)
    draw.text((250, 415), f"{fam.title()}", (34, 21, 94), font=font)
    draw.text((250, 477), f"{ism.title()}", (34, 21, 94), font=font)
    draw.text((315, 537), f"{ismi_sharifi.capitalize()}", (34, 21, 94), font=font)
    draw.text((400, 600), f"{xona_num}", (34, 21, 94), font=font)

    for_date = ImageFont.truetype("arial.ttf", 25)
    draw.text((522, 948), f"{date}", (34, 21, 94), font=for_date)

    img.save(f'{image_file_name}_written.jpg')


def resize_image(image_url):
    img = Image.open(f'{image_url}')
    img = img.resize((265, 350), Image.ANTIALIAS)
    img.save(f'{image_url}')


def fully_saved_image(downloaded_image_url):
    img1 = Image.open(rf"{downloaded_image_url}_written.jpg")

    resize_image(f'{downloaded_image_url}.jpg')
    img2 = Image.open(rf"{downloaded_image_url}.jpg")

    img1.paste(img2, (30, 635))
    img1.save(f'{downloaded_image_url}_fully_saved_image.jpg')
