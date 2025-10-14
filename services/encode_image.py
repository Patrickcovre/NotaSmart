import base64

def get_image():
    image_path = "/Users/patrickcovrerodrigues/Desktop/extrac_info/notasmart/temp/image.png"
    return image_path


def encode_img():
    image = get_image()
    with open(image, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode("utf-8")
        return f"data:image/png;base64,{base64_string}"

var = encode_img()
print(var)