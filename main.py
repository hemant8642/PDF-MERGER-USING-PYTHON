from PyPDF2 import PdfWriter

merger = PdfWriter()
pdfs=[]
n= int(input("How many pdfs do you want to merge?\n"))
for i in range (0,n):
    name=input(f"Enter the name of{i+1} first pdf:")
    pdfs.append(name)
    
for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()