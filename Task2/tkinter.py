from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("200x200")

def encrypt_image():
    file1 = filedialog.askopenfile(mode='rb', filetypes=[('jpg file', '*.jpg')])
    if file1 is not None:
        file_name = file1.name
        key = entry1.get(1.0, END)
        image = file1.read()
        file1.close()
        image = bytearray(image)
        for index, value in enumerate(image):
            image[index] = value ^ int(key)
        with open(file_name, 'wb') as fi1:
            fi1.write(image)
        entry1.delete(1.0, END)  # Clear the entry after encryption

def decrypt_image():
    file1 = filedialog.askopenfile(mode='rb', filetypes=[('jpg file', '*.jpg')])
    if file1 is not None:
        file_name = file1.name
        key = entry2.get(1.0, END)
        image = file1.read()
        file1.close()
        image = bytearray(image)
        for index, value in enumerate(image):
            image[index] = value ^ int(key)
        with open(file_name, 'wb') as fi1:
            fi1.write(image)
        entry2.delete(1.0, END)  # Clear the entry after decryption

b1 = Button(root, text="Encrypt", command=encrypt_image)
b1.place(x=70, y=10)

b2 = Button(root, text="Decrypt", command=decrypt_image)
b2.place(x=70, y=50)

entry1 = Text(root, height=1, width=10)
entry1.place(x=50, y=90)

entry2 = Text(root, height=1, width=10)
entry2.place(x=50, y=130)

root.mainloop()
