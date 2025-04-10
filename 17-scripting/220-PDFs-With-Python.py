# 220 : PDFs With Python

# TODO: [PyPDF2] ---------------------------------------------------------------
# > pip3 install PyPDF2 == 1.26
#   AND NOT
# > pip3 install PyPDF2

# TODO: [3x PDF] ---------------------------------------------------------------
# - dummy.pdf       13 kB	1 page		Dummy PDF file
# - twopage.pdf      3 kB	2 pages		A Simple PDF File, Simple PDF File 2
# - wtr.pdf         46 kB	1 page		DRAFT (watermark)

import PyPDF2

with open("./PDF/dummy.pdf", "rb") as file:
    # 'rb' is read binary, for pdf we append 'b' to it.
    # so it converts the file to binary and PyPDF2 works with binary files.
    # reader = PyPDF2.PdfFileReader(file)
    reader = PyPDF2.PdfReader(file)

    print(file)  # <_io.BufferedReader name='./PDF/dummy.pdf'>
    print(reader)  # <PyPDF2._reader.PdfReader object at 0x000001DF6ED886E0>
    # print(reader.numPages)  # 1
    # print(reader.getPage(0))
    print(reader.pages)  # <PyPDF2._page._VirtualList object at 0x000001DF71028E00>
    print(reader.pages[0])
    # {
    #     "/Type": "/Page",
    #     "/Parent": IndirectObject(4, 0, 2059149018848),
    #     "/Resources": IndirectObject(11, 0, 2059149018848),
    #     "/MediaBox": [0, 0, 595, 842],
    #     "/Group": {"/S": "/Transparency", "/CS": "/DeviceRGB", "/I": True},
    #     "/Contents": IndirectObject(2, 0, 2059149018848),
    # }

    # page = reader.getPage(0)
    # page.rotateClockwise(-90)
    # writer = PyPDF2.PdfFileWriter()
    # writer.addPage(page)
    page = reader.pages[0]
    page.rotate(-90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)

    with open("./PDF/rotated.pdf", "wb") as new_file:
        writer.write(new_file)

# TODO: What you will see with version 1.26 ------------------------------------

# template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# output = PyPDF2.PdfFileWriter()
#
# for i in range(template.getNumPages()):
#     page = template.getPage(i)
#     page.mergePage(watermark.getPage(0))
#     output.addPage(page)
#
#     with open('watermarked_output.pdf', 'wb') as file:
#         output.write(file)

# TODO: What you need to do with latest version: -------------------------------

# import PyPDF2
#
# template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
# watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
# output = PyPDF2.PdfWriter()
#
# for i in range(len(template.pages)):
#     page = template.pages[i]
#     page.merge_page(watermark.pages[0])
#     output.add_page(page)
#
# with open('watermaked_output.pdf', 'wb') as outputFile:
#     output.write(outputFile)
