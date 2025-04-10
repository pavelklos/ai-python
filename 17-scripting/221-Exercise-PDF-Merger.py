# 221 : Exercise: PDF Merger

import sys

import PyPDF2

# this will stores all the arguments passes except the first one, and store them in a list
# TODO: inputs from command line
# TODO: - grab all arguments passed from command line except the first one [1:]
# TODO: - first argument is script name [0]
# inputs = sys.argv[1:]  # TODO: we get list[str] = sys.argv[1:]

# TODO: hard coded inputs
inputs = ["./PDF/dummy.pdf", "./PDF/twopage.pdf", "./PDF/wtr.pdf", "./PDF/rotated.pdf"]


def pdf_merger(pdf_list):
    # merger = PyPDF2.PdfFileMerger()
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write("./PDF/merged.pdf")


pdf_merger(inputs)
