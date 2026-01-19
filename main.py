from pypdf import PdfWriter

merger = PdfWriter()

pdfs = ["Rashid_Ali.pdf", "Abdul.pdf", "Medical.pdf"]

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_document.pdf")