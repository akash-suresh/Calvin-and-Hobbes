from fpdf import FPDF
import os
from os import listdir
from os.path import isfile, join 
from PIL import Image

list_of_images=[]
import os.path

for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".gif")]:
        list_of_images.append(os.path.join(dirpath, filename))

for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".png")]:
        print filename
        book_cover = (os.path.join(dirpath, filename))

def split(image):
    fname = (image.split('/')[4]).split('.')[0]
    year = fname[:4]
    month = fname[4:6] 
    day = fname[6:]
    date = day+'-'+month+'-'+year
    return date, day, int(month), year

def createPDF(list_of_images):
    calendar = ['0','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    pdf = FPDF(orientation='L')
    pdf.add_page()
    pdf.image(book_cover, x = None, y = None, w = 250, h = 0, type = 'png', link = '')
    pdf.add_page()
    date, day, old_month, year = split(list_of_images[0])
    pdf.set_font("Courier", size=22)
    pdf.cell(200,15, txt=calendar[old_month]+', '+year, ln=1, align="C")
    pdf.set_font("courier", size=8)
    for image in list_of_images:
        date, day, month, year = split(image)
        if month!=old_month:
            print date
            pdf.add_page()
            pdf.set_font("Courier", size=22)
            pdf.cell(200,15, txt=calendar[month]+', '+year, ln=1, align="C")
            pdf.set_font("courier",size=8)
        pdf.cell(200,5, txt=date, ln=1, align="L")
        pdf.image(image, x = None, y = None, w = 250, h = 0, type = 'gif', link = '')
        old_month= month
        break;
    pdf.output("Calvin and Hobbes.pdf", "F")
print list_of_images[0]

createPDF(list_of_images)