import os
from fpdf import FPDF
import argparse


def convert_scripts_to_pdf(do_file_path, pdf, encoding="utf-8"):
    # Read the contents of the .do file
    with open(do_file_path, 'r', encoding=encoding) as do_file:
        do_content = do_file.read()

    # Add a new page with the .do file title
    pdf.add_page()
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 10, os.path.basename(do_file_path), ln=True)

    # Add the .do file content to the PDF
    pdf.set_font('Courier', '', 8)
    pdf.multi_cell(0, 4, do_content.replace('\n\n', '\n').strip())
    pdf.ln()


def process_folder(folder_path, output_pdf_path, extension='do'):
    # Initialize the PDF document
    pdf = FPDF()

    # Walk through the folder recursively
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file is a Stata .do file
            if file.endswith(f'.{extension}'):
                do_file_path = os.path.join(root, file)

                # Convert the .do file to PDF
                convert_scripts_to_pdf(do_file_path, pdf, encoding="latin1")

                print(f"Processed {do_file_path}")

    # Save the PDF file
    pdf.output(output_pdf_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert scripts to PDF')
    parser.add_argument('folder_path', type=str, help='Path to the folder containing scripts')
    parser.add_argument('output_pdf_path', type=str, help='Path to the output PDF file')
    parser.add_argument('--ext', type=str, default='py', help='File extension to search for (default is "py")')
    args = parser.parse_args()

    # Call the function to process the folder
    process_folder(args.folder_path, args.output_pdf_path, extension=args.ext)
