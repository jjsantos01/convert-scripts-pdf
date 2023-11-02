# Convert a set of Scripts into a Single PDF File

This script facilitates the conversion of various script files into a consolidated PDF document. Two versions of the script are available: one that creates a PDF without code highlighting (`convert_scripts_to_pdf.py`) and another that incorporates syntax highlighting using `pygments`, `PyPDF2`, and `pdfkit` (`convert_scripts_to_pdf_highlight.py`). The latter version also requires the installation of [pdfkit binaries](https://wkhtmltopdf.org/downloads.html) on your system.

Please note that `convert_scripts_to_pdf.py` is designed for Python 3.8 or lower, as the `FPDF` package is not currently actively maintained. The highlighting version (`convert_scripts_to_pdf_highlight.py`) has been tested on Python 3.8, but it might be compatible with higher versions as well.

## Motivation
When I worked in government, I often had to present evidence of my work, which was usually done in the form of Python, Stata, and R scripts. As auditors often don't know how to read code, I had to convert my scripts into PDF files. This was a tedious process, as I had to copy and paste the code into a txt file, then convert it into a PDF file. This script automates this process.

This project was built using ChatGPT and Copilot.

## Usage

### Without Highlighting:

```bash
python convert_scripts_to_pdf.py <input_folder> <output_file> --ext <extension> --lang <language>
```
### With Highlighting:
```bash
python convert_scripts_to_pdf_highlight.py <input_folder> <output_file> --ext <extension> --lang <language>
```

### Parameters

- `<input_folder>`: The path to the folder containing the script files.
- `<output_file>`: The desired path for the output PDF file.
- `--ext <extension>`: Optional. Specifies the file extension to search for (default is "py").
- `--lang <language>`: Optional. Specifies the language to use for syntax highlighting (default is "python").

The options for --ext and --lang are the same as those available in `pygments`. For a list of supported languages, see [here](https://pygments.org/languages/).

## Examples

### Without Highlighting:

For R scripts:
```bash
python convert_scripts_to_pdf.py examples examples/example_r.pdf --ext r
```

--> Produced PDF file: [examples/example_r.pdf](examples/example_r.pdf)

For Stata do files:
```bash
python convert_scripts_to_pdf.py examples examples/example_do.pdf --ext do
```

--> Produced PDF file: [examples/example_do.pdf](examples/example_do.pdf)

For Python scripts:
```bash
python convert_scripts_to_pdf.py . examples/example_py.pdf --ext py
```

--> Produced PDF file: [examples/example_py.pdf](examples/example_py.pdf)

### With Highlighting:
For R scripts:
```bash
python convert_scripts_to_pdf_highlight.py examples examples/example_highlight_r.pdf --ext r --lang r
```

--> Produced PDF file: [examples/example_highlight_r.pdf](examples/example_highlight_r.pdf)

For Stata do files:

```bash
python convert_scripts_to_pdf_highlight.py examples examples/example_highlight_do.pdf --ext do --lang stata
```

--> Produced PDF file: [examples/example_highlight_do.pdf](examples/example_highlight_do.pdf)

For Python scripts:
```bash
python convert_scripts_to_pdf_highlight.py . examples/example_highlight_py.pdf --ext py --lang python
```
--> Produced PDF file: [examples/example_highlight_py.pdf](examples/example_highlight_py.pdf)

Remember to replace example with your actual folder name and adapt the file extensions and languages as needed.

## Running with Docker

To run the script in a Docker container, follow these steps:
1. Clone the repository
2. Build the Docker image: `docker build -t script-to-pdf .`
3. Run the Docker image:
*  Without Highlighting:
    ```bash
    docker run --rm -v $(pwd)/examples:/app/examples script-to-pdf python convert_scripts_to_pdf.py examples examples/example_r.pdf --ext r
    ```
* With Highlighting:
  ```bash
  docker run --rm -v $(pwd)/examples:/app/examples script-to-pdf python convert_scripts_to_pdf_highlight.py examples examples/example_highlight_r.pdf --ext r --lang r
  ```
