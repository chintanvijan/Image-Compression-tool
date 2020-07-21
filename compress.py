import os
from PIL import Image

try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

def generate(self, image, format='jpg'):
    im = self.generate_image(image)
    out = BytesIO()
    im.save(out, format=format, quality=75)
    out.seek(0)
    return out


def compress():
    for image in os.listdir("examples"):
        path = image
        foo = Image.open(path)
        print(foo.size, end=" ")

        out_path = r"examples" + os.sep + "image_" + image.replace("-","_")
        foo.save(out_path, optimize=True, quality=20)
        foo = Image.open(out_path)
        print(foo.size)


if __name__ == '__main__':
    compress()