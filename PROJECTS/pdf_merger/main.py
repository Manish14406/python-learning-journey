from PyPDF2 import PdfWriter
merger = PdfWriter()

pdfs = []
n = int(input("Enter how many pdf's\n"))

for i in range(0,n):
   o = input(f"Pdfname {i+1} : ")
   pdfs.append(o)

for pdf in pdfs:
   merger.append(pdf)
   
merger.write("merged-pdf.pdf")
merger.close()