from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_document = "G:\Kaushik Kochhar\Personal\India Trip\Tum2 - DS-160 & Interview appointment\Tum2 supporting\L1Afull.PDF"
pdf_document=r"G:\kaushik kochhar\Scratch\Latest I-129A.pdf"

pdf = PdfFileReader(pdf_document)

for page in range(pdf.getNumPages()):
    pdf_writer = PdfFileWriter()
    current_page = pdf.getPage(page)
    pdf_writer.addPage(current_page)

    outputFilename = "example-page-{}.pdf".format(page + 1)
    with open(outputFilename, "wb") as out:
        pdf_writer.write(out)

        print("created", outputFilename)


pdf_document1 = r"G:\Kaushik Kochhar\Personal\India Trip\Tum2 - DS-160 & Interview appointment\Tum2 supporting\20200128-statements-2564-.pdf"
pdf1 = PdfFileReader(pdf_document1)
pdf_document2 = r"G:\Kaushik Kochhar\Personal\India Trip\Tum2 - DS-160 & Interview appointment\Tum2 supporting\20191226-statements-2564-.pdf"
pdf2 = PdfFileReader(pdf_document2)
pdf_document3 = r"G:\Kaushik Kochhar\Personal\India Trip\Tum2 - DS-160 & Interview appointment\Tum2 supporting\20191127-statements-2564-.pdf"
pdf3 = PdfFileReader(pdf_document3)

pdf_writer = PdfFileWriter()
pdf_writer.addPage(pdf1.getPage(0))
pdf_writer.addPage(pdf1.getPage(1))
pdf_writer.addPage(pdf2.getPage(0))
pdf_writer.addPage(pdf2.getPage(1))
pdf_writer.addPage(pdf3.getPage(0))
pdf_writer.addPage(pdf3.getPage(1))
outputFilename =r"G:\Kaushik Kochhar\Personal\India Trip\Tum2 - DS-160 & Interview appointment\Tum2 supporting\Chase-statements-2564-.pdf"
with open(outputFilename, "wb") as out:
        pdf_writer.write(out)

print("created", outputFilename)


==
import glob
from os import path
#pdfs=glob.glob(r"G:\Kaushik Kochhar\Personal\Kaul N\Salary slips\*"+".pdf")
pdfs=glob.glob(r"G:\kaushik kochhar\Scratch\aa\*"+".pdf")
len(pdfs)
pdf_writer = PdfFileWriter()
for i,pdf in enumerate(pdfs):
    work_pdf=PdfFileReader(pdf)
    print(f'{i}. Appending {path.basename(pdf)}; no. of pages:{work_pdf.numPages}')
    pdf_writer.appendPagesFromReader(work_pdf)

#outputFilename =r"G:\Kaushik Kochhar\Personal\Kaul N\Salary slips\Consolidated.pdf"
outputFilename =r"G:\kaushik kochhar\Scratch\aa\PowerBI dashboards - Hemanth.pdf"
with open(outputFilename, "wb") as out:
        pdf_writer.write(out)

print("created", outputFilename)

from glob import glob
import os

files=glob(r"G:\Kaushik Kochhar\Scratch\aa\*.pdf")

for f in files:
        pdf = PdfFileReader(f)
        pdf_writer = PdfFileWriter()
        for page in range(pdf.getNumPages()):
                current_page = pdf.getPage(page)
                pdf_writer.addPage(current_page)
        o_f=f.split("\\")[-1].split(".")[0] + "aa" + ".pdf"
        outputFilename=os.path.join(r"G:\Kaushik Kochhar\Scratch\aa",o_f)
        with open(outputFilename, "wb") as out:
                pdf_writer.write(out)

#======+==+=+======+=====

folder=r"G:\kaushik kochhar\Scratch\zy"
files=os.listdir(folder)

janfeb=[f for f in files if ('-01' in f) or ('-02' in f)]
mar=[f for f in files if '-03' in f]
apr=[f for f in files if '-04' in f]

pdf_writer = PdfFileWriter()
for i,f in enumerate(apr):
    pdf=os.path.join(folder,f)
    work_pdf=PdfFileReader(pdf)
    print(f'{i}. Appending {f}; no. of pages:{work_pdf.numPages}')
    pdf_writer.appendPagesFromReader(work_pdf)


outputFilename =r"G:\kaushik kochhar\Scratch\zy\apr.pdf"
with open(outputFilename, "wb") as out:
        pdf_writer.write(out)
 
