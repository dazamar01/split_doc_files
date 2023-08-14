# pip3 install pypdf2
import os
from PyPDF2 import PdfReader, PdfWriter

path = "/some/folder/location/notificacion.pdf"
fname = "noti_"

pdf = PdfReader(path)
for page in range(len(pdf.pages)):
    pdf_writer = PdfWriter()
    pdf_writer.add_page(pdf.pages[page])

    output_filename = '{}_page_{}.pdf'.format(fname, page+1)

    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)

    print('Created: {}'.format(output_filename))
