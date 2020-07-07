import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image

#Open image for reading the text
imagereader = Image.open("test.png")

#coversion of text in image to string
#lang specifies the language present in the text
text_from_image = pytesseract.image_to_string(imagereader, lang = 'eng')

#print the text extracted from the image
print(text_from_image)

#Open the file for reading operation
file_text=open("text_file.txt","w")

#Only append if its a character
for i in text_from_image:
    if(i.isalpha() or i==" " or i=="\n"):
        file_text.write(i)

#close the file
file_text.close()

