# 222 : Exercise: Watermarker

import PyPDF2

# template = PyPDF2.PdfFileReader(open('./Watermark/super.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('./Watermark/wtr.pdf', 'rb'))
# template = PyPDF2.PdfFileReader(open("./PDF/merged.pdf", "rb"))
# watermark = PyPDF2.PdfFileReader(open("./PDF/wtr.pdf", "rb"))
# output = PyPDF2.PdfFileWriter()
template = PyPDF2.PdfReader(open("./PDF/merged.pdf", "rb"))
watermark = PyPDF2.PdfReader(open("./PDF/wtr.pdf", "rb"))
output = PyPDF2.PdfWriter()

# print(f"{template.getNumPages()} pdf(s)")  # 5 pdf(s)
# for i in range(template.getNumPages()):
#     page = template.getPage(i)
#     page.mergePage(watermark.getPage(0))
#     output.addPage(page)
print(f"{len(template.pages)} pdf(s)")  # 5 pdf(s)
for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

# with open('./Watermark/watermarked_output.pdf', 'wb') as file:
with open("./PDF/watermarked_output.pdf", "wb") as file:
    output.write(file)

# TODO: watermarker ------------------------------------------------------------
# - https://github.com/aneagoie/watermarker

# import PyPDF2
#
# # template = PyPDF2.PdfFileReader(open('superduper.pdf', 'rb'))
# # watermark = PyPDF2.PdfFileReader(open('water.pdf', 'rb'))
# # output = PyPDF2.PdfFileWriter()
# # This is the new way to do this:
# template = PyPDF2.PdfReader(open('superduper.pdf', 'rb'))
# watermark = PyPDF2.PdfReader(open('water.pdf', 'rb'))
# output = PyPDF2.PdfWriter()
#
# # for i in range(template.getNumPages()):
# # New way to do this:
# for i in range(len(template.pages)):
#     page = template.pages[i]
#     page.merge_page(watermark.pages[0])
#     output.add_page(page)
#
# with open('watermaked_output.pdf', 'wb') as outputFile:
#     output.write(outputFile)
