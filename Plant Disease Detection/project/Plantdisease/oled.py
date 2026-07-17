import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

WIDTH = 128
HEIGHT = 64

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

def display_text(text):
    image = Image.new("1", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    draw.text((0, 20), text, font=font, fill=255)

    oled.fill(0)
    oled.image(image)
    oled.show()