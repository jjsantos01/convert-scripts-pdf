# Convert a list of do-files into a single PDF file

This is a simple script to convert a list of do-files into a single PDF file with it's contents. The `convert_do_to_pdf.py` script creates simple PDF without code highlighting and requires only the `FPDF` package. For this script, Python 3.8 or lower are required, as FPDF is not currently mantained.

The `convert_do_to_pdf_highlight.py` script creates a PDF with code highlighting and requires the `pygments`, `PyPDF2` and `pdfkit` package, and also to install the [pdfkit binares](https://wkhtmltopdf.org/downloads.html) in your computer. Only tested on Python 3.8, but higher versions could work.

## Usage
Without highlighting:

```bash
python convert_do_to_pdf.py <input_folder> <output_file>
```

With highlighting:
```bash
python convert_do_to_pdf_highlight.py <input_folder> <output_file>
```
