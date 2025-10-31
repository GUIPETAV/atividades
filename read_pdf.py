#!/usr/bin/env python3
"""
Script to read and extract text from PDF file 1644843613529.pdf
"""

import sys

try:
    import PyPDF2
except ImportError:
    print("PyPDF2 is not installed. Please install it using: pip install -r requirements.txt")
    sys.exit(1)


def read_pdf(pdf_path):
    """
    Read and extract text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text from the PDF
    """
    try:
        with open(pdf_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Get the number of pages
            num_pages = len(pdf_reader.pages)
            print(f"PDF has {num_pages} page(s)\n")
            
            # Extract text from all pages
            text_parts = []
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                text_parts.append(f"\n--- Page {page_num + 1} ---\n")
                text_parts.append(text)
                text_parts.append("\n")
            
            full_text = ''.join(text_parts)
            return full_text
            
    except FileNotFoundError:
        print(f"Error: File '{pdf_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Path to the PDF file
    pdf_file = "1644843613529.pdf"
    
    print(f"Reading PDF: {pdf_file}")
    print("=" * 50)
    
    # Read and display the PDF content
    content = read_pdf(pdf_file)
    print(content)
