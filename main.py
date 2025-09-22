from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

def unlock_pdf(input_pdf_path, password):
    input_pdf_path = Path(input_pdf_path)
    if not input_pdf_path.exists():
        print("PDF not found:", input_pdf_path)
        return

    output_pdf_path = input_pdf_path.with_name(input_pdf_path.stem + "_unlocked.pdf")
    try:
        reader = PdfReader(str(input_pdf_path))
        if reader.is_encrypted:
            reader.decrypt(password)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        with open(output_pdf_path, "wb") as f_out:
            writer.write(f_out)
        print(f"Unlocked PDF saved to: {output_pdf_path}")
    except Exception as e:
        print(f"Failed to unlock PDF: {e}")

if __name__ == "__main__":
    pdf_path = r"C:\Users\samii\Downloads\Documents\ইঞ্জিনিয়ারিং কনসেপ্ট বুক রসায়ন ১ম পত্র ২০২৫-২৬.pdf"
    pdf_password = "Educationblog24.com"
    unlock_pdf(pdf_path, pdf_password)
