import qrcode
import argparse
from typing import Optional

def generate_qr_code(data: str, filename: str = "qr_code.png", box_size: int = 10, border: int = 4, fill_color: str = "black", back_color: str = "white"):
    """
    Generates a QR code for the given data and saves it as an image file.

    :param data: The data to encode in the QR code.
    :param filename: The name of the file to save the QR code image.
    :param box_size: How many pixels each “box” of the QR code is.
    :param border: How many boxes thick the border should be.
    :param fill_color: Color of the QR code.
    :param back_color: Background color of the QR code.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a QR code from provided data.")
    parser.add_argument("data", type=str, help="The data/text to encode in the QR code.")
    parser.add_argument("--filename", type=str, default="qr_code.png", help="Filename to save the QR code image. Default is 'qr_code.png'.")
    parser.add_argument("--box_size", type=int, default=10, help="Size of each box in the QR code in pixels. Default is 10.")
    parser.add_argument("--border", type=int, default=4, help="Thickness of the border around the QR code in boxes. Default is 4.")
    parser.add_argument("--fill_color", type=str, default="black", help="Color of the QR code. Default is 'black'.")
    parser.add_argument("--back_color", type=str, default="white", help="Background color of the QR code. Default is 'white'.")

    args = parser.parse_args()

    generate_qr_code(
        data=args.data,
        filename=args.filename,
        box_size=args.box_size,
        border=args.border,
        fill_color=args.fill_color,
        back_color=args.back_color
    )

    