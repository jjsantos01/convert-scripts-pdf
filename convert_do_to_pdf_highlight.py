import os
import sys
from pathlib import Path
import pdfkit
import PyPDF2
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def convert_do_to_pdf(do_file_path, output_pdf_path):
    # Read the contents of the .do file
    with open(do_file_path, 'r', encoding="latin1") as do_file:
        do_content = do_file.read()

    # Highlight the .do file content using Pygments
    lexer = get_lexer_by_name('stata')
    formatter = HtmlFormatter(style='default')
    highlighted_code = highlight(do_content, lexer, formatter)

    # Generate the HTML content
    html_content = f"""
    <html>
    <head>
        <style>
            {formatter.get_style_defs('.highlight')}
        </style>
    </head>
    <body>
        <p><h1>{Path(do_file_path).stem}</h1></p>
        <pre class="highlight">{highlighted_code}</pre>
    </body>
    </html>
    """

    # Convert HTML to PDF using pdfkit
    pdfkit.from_string(html_content, output_pdf_path)

def merge_pdfs(input_pdf_paths, output_pdf_path):
    merger = PyPDF2.PdfMerger()

    # Merge all input PDFs into a single PDF
    for pdf_path in input_pdf_paths:
        merger.append(pdf_path)

    # Save the merged PDF to the output path
    merger.write(output_pdf_path)
    merger.close()

    for file in input_pdf_paths:
        file_path = Path(file)    
        os.remove(file_path)

def process_folder(folder_path, output_pdf_path):
    # Walk through the folder recursively
    pdf_files_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file is a Stata .do file
            if file.endswith('.do'):
                do_file_path = os.path.join(root, file)
                pdf_file_path = f"./{folder_path}/{file.strip('.do')}.pdf"
                
                # Convert the .do file to PDF
                print("##############", pdf_file_path)
                convert_do_to_pdf(do_file_path, pdf_file_path)
                pdf_files_paths.append(pdf_file_path)
                print(f"Converted {do_file_path} to {pdf_file_path}")
    
    # Merge all the PDF files into a single PDF using pdfkit
    merge_pdfs(pdf_files_paths, output_pdf_path)

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
