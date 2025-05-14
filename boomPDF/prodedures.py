from pdf_procedures import PDFOperations


file = r'path'
pdf_operations = PDFOperations()
pdf_operations.select_pdf_files([file])

# ----------------------------------------------------------------------
# EXTRACT 
# ----------------------------------------------------------------------

# Extract a single page
# extracted_writer_single = pdf_operations.extract_pdf_pages('2-2024.pdf', 4, "extracted.pdf")

# Extract a range pages and save
#extracted_writer_single = pdf_operations.extract_pdf_pages('Maths.pdf', "1-5", "extracted.pdf")

# Extract non-contigeous
#extracted_writer_single = pdf_operations.extract_pdf_pages('Maths.pdf', [1, 3, 5], "extracted.pdf")

# ----------------------------------------------------------------------
# Split Document 
# ----------------------------------------------------------------------
""" start_page = 1
end_page = 2
for x in range(start_page, end_page):
    pdf_operations.extract_pdf_pages('test.pdf', x, f"extracted-{x}.pdf")

 """
# ----------------------------------------------------------------------
# MERGE
# ----------------------------------------------------------------------
# Merge the selected PDF files into a single file
# pdf_operations.merge_pdf_files('Merged.pdf')


# ----------------------------------------------------------------------
# DELETE
# ----------------------------------------------------------------------

# Delete a single page from the original file (1-based)
# pdf_operations.delete_pdf_pages('Scan - Scan Admin #001.pdf', [1, 4])

# Delete a single page from the original file (1-based)
# pdf_operations.delete_pdf_pages('xyz.pdf', 2)

# Delete a range of pages from the original file (1-based)
# pdf_operations.delete_pdf_pages('file1.pdf', "1-5")

# Delete non-contiguous pages from the original file (1-based)
# pdf_operations.delete_pdf_pages('file1.pdf', [1, 3, 5])

# ----------------------------------------------------------------------
# INSERT
# ----------------------------------------------------------------------

# Insert a page from file2.pdf into merged_output.pdf
# pdf_operations.insert_into_pdf('Scan - Scan Admin #001.pdf', 'extracted.pdf', 1, 2)  # Insert page 1 from file2.pdf at position 2 in merged_output.pdf

# ----------------------------------------------------------------------
# ROTATE
# ----------------------------------------------------------------------

# Rotate page 1 in merged_output.pdf by 90 degrees
pdf_operations.rotate_pdf_pages(file, 1, 270)

# Rotate pages 2-3 in merged_output.pdf by 180 degrees
# pdf_operations.rotate_pdf_pages('xyz.pdf', "3-11", 90)

# Rotate non-contiguous pages in merged_output.pdf
# pdf_operations.rotate_pdf_pages('merged_output.pdf', [1, 3], 270)

# ----------------------------------------------------------------------
# Convert PDF document to Word
# ----------------------------------------------------------------------
# Convert the entire PDF to Word
# pdf_operations.convert_pdf_to_word('ISC_Notes.pdf', 'file1.docx')

# Convert specific pages (1-based indexing)
# pdf_operations.convert_pdf_to_word('file1.pdf', 'file1_partial.docx', page_specifications="1-3")

# Convert non-contiguous pages
# pdf_operations.convert_pdf_to_word('file1.pdf', 'file1_selected.docx', page_specifications=[1, 3, 5])

