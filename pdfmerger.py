import PyPDF2

def merge_pdfs(paths, output_path):
    pdf_merger = PyPDF2.PdfMerger()
    for path in paths:
        pdf_merger.append(path)
    with open(output_path, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)

def get_file_paths():
    print("Drag and drop PDF files here. Press Enter after the last file.")
    file_paths = []
    while True:
        path = input(f"File path {len(file_paths) + 1} (press Enter to finish): ").strip()
        # Remove surrounding quotes if present
        path = path.strip("'\"")
        if path == "":
            break
        file_paths.append(path)
        print("\nCurrent list of files:")
        for i, file_path in enumerate(file_paths, start=1):
            print(f"{i} - {file_path}")
    return file_paths

if __name__ == "__main__":
    paths = get_file_paths()
    if len(paths) == 0:
        print("No files provided.")
    else:
        output_file_name = input("Enter the name for the merged file: ").strip()
        if output_file_name == "":
            print("No output file name provided.")
        else:
            merge_pdfs(paths, output_file_name)
            print(f"Merged PDFs into {output_file_name}")
