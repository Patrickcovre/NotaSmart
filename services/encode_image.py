import base64

def encode_img():
    image = get_image()
    with open(image, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def get_image():
    image_path = "/Users/patrickcovrerodrigues/Desktop/extrac_info/notasmart/temp/image.png"
    return image_path

var = encode_img()
print(var)