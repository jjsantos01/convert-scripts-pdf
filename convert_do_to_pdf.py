import os
from fpdf import FPDF
import sys

def convert_do_to_pdf(do_file_path, pdf):
    # Read the contents of the .do file
    with open(do_file_path, 'r', encoding="latin1") as do_file:
        do_content = do_file.read()

    # Add a new page with the .do file title
    pdf.add_page()
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 10, os.path.basename(do_file_path), ln=True)

    # Add the .do file content to the PDF
    pdf.set_font('Courier', '', 8)
    pdf.multi_cell(0, 4, do_content.replace('\n\n', '\n').strip())
    pdf.ln()


def process_folder(folder_path, output_pdf_path):
    # Initialize the PDF document
    pdf = FPDF()
    
    # Walk through the folder recursively
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file is a Stata .do file
            if file.endswith('.do'):
                do_file_path = os.path.join(root, file)
                
                # Convert the .do file to PDF
                convert_do_to_pdf(do_file_path, pdf)
                
                print(f"Processed {do_file_path}")
    
    # Save the PDF file
    pdf.output(output_pdf_path)


if __name__ == '__main__':
    # Check if the required arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python script_name.py folder_path output_pdf_path")
        sys.exit(1)

    # Get the folder path and output PDF path from command-line arguments
    folder_path = sys.argv[1]
    output_pdf_path = sys.argv[2]

    # Call the function to process the folder
    process_folder(folder_path, output_pdf_path)