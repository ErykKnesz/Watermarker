import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFont, ImageDraw

window = tk.Tk()
window.title("Watermarker")
window.config(padx=20, pady=20)
image = Image.Image()
image_label = tk.Label()

font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf",
                          size=30)


def display_image(img):
    global image_label
    image_label.destroy()
    img = img if isinstance(img, ImageTk.PhotoImage) else ImageTk.PhotoImage(img)
    image_label = tk.Label(window, image=img)
    image_label.image = img
    image_label.grid(columnspan=3, row=2)


def add_watermark(watermark):
    if isinstance(watermark, str):
        global image
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), watermark,
                  (255, 255, 255), font=font)
        display_image(image)


def upload_file(kind='main image'):
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    global image
    global watermark_image
    if kind == 'main image':
        image = Image.open(filename)
        display_image(image)
    else:
        watermark_image = ImageTk.PhotoImage(Image.open(filename))


def save_image():
    fp = filedialog.asksaveasfilename()
    image.save(fp)


inputtxt = tk.Text(window,
                   height=5,
                   width=20)
inputtxt.grid(column=1, row=3)
watermark = inputtxt.get(1.0, "end-1c")


upload_button = tk.Button(text="upload", command=upload_file)
upload_button.grid(column=1, row=1, padx=20, pady=20)
save_button = tk.Button(text="Save", command=save_image)
save_button.grid(column=2, row=1, padx=20, pady=20)
text_watermark_button = tk.Button(text="Add as Watermark", command=lambda: add_watermark(inputtxt.get(1.0, "end-1c")))
text_watermark_button.grid(column=1, row=4, padx=20, pady=20)
img_watermark_button = tk.Button(text="Add as Watermark", command=lambda: add_watermark)
img_watermark_button.grid(column=2, row=4, padx=20, pady=20)


inputtxt.get(1.0, "end-1c")
window.mainloop()