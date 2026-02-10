import json
import os,re,csv
import pdfplumber

# Extract pdf chunks page wise
def extract_pdf_chunks(pdf_path, chunk_size=500):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"The file {pdf_path} does not exist.")
    
    chunks = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                # Split the text into chunks of the specified size
                for i in range(0, len(text), chunk_size):
                    chunk = text[i:i + chunk_size]
                    chunks.append(chunk)
    return chunks

# save the extracted chunks from extract_pdf_chunks to a text file based on the page number in a single file
def save_chunks_to_file(chunks, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, chunk in enumerate(chunks):
            f.write(f"Page {i+1}:\n")
            f.write(chunk + "\n\n")
