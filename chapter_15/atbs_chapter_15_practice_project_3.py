# Brute-Force PDF Password Breaker

import PyPDF2


def brute_force_pdf(pdf, dictionary):
    # Open PDF and read .txt-file.
    pdfFile = open(pdf, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    with open(dictionary, "r") as file:
        lines = file.readlines()
    # Loop passwords.
    for line in lines:
        word = line.strip()
        for cand in (word.lower(), word.upper()):
            if pdfReader.decrypt(cand):
                print(f"Correct password is: {line}")
                return
    print("Correct password was not found from given dictionary.")


brute_force_pdf("bruteforcetest.pdf", "dictionary.txt")
