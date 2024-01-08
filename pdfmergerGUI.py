import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")

        self.file_list = []
        self.listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.EXTENDED)
        self.listbox.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

        add_button = tk.Button(root, text="Add PDF", command=self.add_pdf)
        add_button.grid(row=1, column=0, padx=10, pady=5, sticky='ew')

        merge_button = tk.Button(root, text="Merge PDFs", command=self.merge_pdfs)
        merge_button.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

        move_up_button = tk.Button(root, text="Move Up", command=self.move_up)
        move_up_button.grid(row=2, column=0, padx=10, pady=5, sticky='ew')

        move_down_button = tk.Button(root, text="Move Down", command=self.move_down)
        move_down_button.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

        root.grid_rowconfigure(1, weight=1)
        root.grid_rowconfigure(2, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def add_pdf(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        for file_path in files:
            if file_path and file_path not in self.file_list:
                self.file_list.append(file_path)
                self.listbox.insert(tk.END, file_path)

    def move_up(self):
        selected_indices = self.listbox.curselection()
        for i in selected_indices:
            if i > 0:
                self.listbox.insert(i-1, self.listbox.get(i))
                self.listbox.delete(i+1)
                self.listbox.select_set(i-1)

                # Reorder file_list
                self.file_list.insert(i-1, self.file_list.pop(i))

    def move_down(self):
        selected_indices = self.listbox.curselection()
        for i in reversed(selected_indices):
            if i < self.listbox.size() - 1:
                self.listbox.insert(i+2, self.listbox.get(i))
                self.listbox.delete(i)
                self.listbox.select_set(i+1)

                # Reorder file_list
                self.file_list.insert(i+1, self.file_list.pop(i))

    def merge_pdfs(self):
        if not self.file_list:
            return

        output_file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if not output_file_path:
            return

        pdf_merger = PyPDF2.PdfMerger()
        for pdf_file in self.file_list:
            pdf_merger.append(pdf_file)

        with open(output_file_path, 'wb') as output_pdf:
            pdf_merger.write(output_pdf)

        self.file_list.clear()
        self.listbox.delete(0, tk.END)
        messagebox.showinfo("Success", "PDFs merged successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
