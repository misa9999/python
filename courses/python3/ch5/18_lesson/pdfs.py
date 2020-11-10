import PyPDF2
import os


path_pdf = "pdf"

with open("pdf/new_file.pdf", "rb") as pdf_file:
    reader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = reader.getNumPages()

    for num_page in range(num_pages):
        writer = PyPDF2.PdfFileWriter()
        atual_page = reader.getPage(num_page)
        writer.addPage(atual_page)

        with open(f"new_pdf/{num_page}.pdf", "wb") as new_pdf:
            writer.write(new_pdf)

# JOIN PDFs
# new_pdf = PyPDF2.PdfFileMerger()

# for root, dirs, files in os.walk(path_pdf):
#     for file in files:
#         complete_path = os.path.join(root, file)

#         pdf_file = open(complete_path, "rb")
#         new_pdf.append(pdf_file)

# with open(f"{path_pdf}/new_file.pdf", "wb") as my_new_pdf:
#     new_pdf.write(my_new_pdf)
