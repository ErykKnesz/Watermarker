import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFont, ImageDraw

FONT = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf",
                          size=30)

window = tk.Tk()
window.title("Watermarker")
window.config(padx=20, pady=20)

image = Image.Image()
image_label = tk.Label()

watermark_image = Image.Image()
watermark_label = tk.Label()
watermark_label.grid(column=2, row=3)

inputtxt = tk.Text(window,
                   height=5,
                   width=20)
inputtxt.grid(column=1, row=3)


def display_image(img, kind="main image"):
    global image_label
    global watermark_label
    img = ImageTk.PhotoImage(img)
    if kind == "main image":
        image_label.destroy()
        image_label = tk.Label(window, image=img)
        image_label.image = img
        image_label.grid(columnspan=3, row=2)
    else:
        watermark_label.destroy()
        watermark_label = tk.Label(window, image=img)
        watermark_label.image = img
        watermark_label.grid(column=2, row=3)


def add_watermark(watermark):
    global image
    if isinstance(watermark, str):

        draw = ImageDraw.Draw(image)
        draw.text((0, 0), watermark,
                  (255, 255, 255), font=FONT)
    else:
        image.paste(watermark, (50, 50))
    display_image(image)


def upload_file(kind='main image'):
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    global image
    global watermark_image
    if kind == 'main image':
        image = Image.open(filename)
        display_image(image, 'main image')
    else:
        watermark_image = Image.open(filename)
        watermark_image.thumbnail((100, 100))
        display_image(watermark_image, 'watermark')


def save_image():
    fp = filedialog.asksaveasfilename()
    image.save(fp)


upload_button = tk.Button(text="upload", command=upload_file)
upload_button.grid(column=1, row=1, padx=20, pady=20)
save_button = tk.Button(text="Save", command=save_image)
save_button.grid(column=2, row=1, padx=20, pady=20)
text_watermark_button = tk.Button(text="Add as Watermark", command=lambda: add_watermark(inputtxt.get(1.0, "end-1c")))
text_watermark_button.grid(column=1, row=4, padx=20, pady=20)
img_watermark_button = tk.Button(text="Add as Watermark", command=lambda: add_watermark(watermark_image))
img_watermark_button.grid(column=2, row=4, padx=20, pady=20)
upload_watermark_button = tk.Button(text="Upload Watermark", command=lambda: upload_file("watermark"))
upload_watermark_button.grid(column=2, row=5, padx=5, pady=5)

window.mainloop()