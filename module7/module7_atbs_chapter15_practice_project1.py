# PDF Paranoia

import os, PyPDF2
from pathlib import Path

def encrypt_pdfs(folder, password):

    folder = os.path.abspath(folder)
    file_counter = 0

    # Walk the entire folder tree and encrypt the files.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Encrypting files in {foldername}...")

        # Encrypt files.
        for filename in filenames:
            if filename.lower().endswith("_encrypted.pdf"):
                continue
            if filename.lower().endswith(".pdf"):
                print(f"Encrypting file: {filename}")
                filename_wo_ext = Path(filename).stem
                pdfFile = open(filename, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                pdfWriter.encrypt(password)
                resultPdf = open(f"{filename_wo_ext}_encrypted.pdf", 'wb')
                pdfWriter.write(resultPdf)
                resultPdf.close()
                # Check if encrypted
                pdfReader = PyPDF2.PdfFileReader(open(f"{filename_wo_ext}_encrypted.pdf", 'rb'))
                if pdfReader.isEncrypted:
                    print("File encrypted successfully, deleting original.")
                else:
                    print("File encryption failed, retaining original.")
                file_counter += 1
    print(f"Done, encrypted {file_counter} files.")

encrypt_pdfs(os.getcwd(), "qwerty")

def decrypt_pdfs(folder, password):

    folder = os.path.abspath(folder)
    file_counter = 0

    # Walk the entire folder tree and decrypt the files.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Decrypting files in {foldername}...")

        # Decrypt files.
        for filename in filenames:
            if filename.lower().endswith("_decrypted.pdf"):
                continue
            if filename.lower().endswith(".pdf"):
                # Check if encrypted
                pdfFile = open(filename, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                if pdfReader.isEncrypted:
                    print(f"Decrypting file: {filename}")
                    try:
                        pdfReader.decrypt(password)
                    except:
                        print("Decryption failed, moving to next PDF-file.")
                        continue
                else:
                    continue          
                filename_wo_ext = Path(filename).stem
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                resultPdf = open(f"{filename_wo_ext}_decrypted.pdf", 'wb')
                pdfWriter.write(resultPdf)
                resultPdf.close()
                file_counter += 1
    print(f"Done, decrypted {file_counter} files.")

decrypt_pdfs(os.getcwd(), "qwerty")