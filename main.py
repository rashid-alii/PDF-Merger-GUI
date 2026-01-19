

import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter
import os

class PDFMergerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger GUI")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        self.pdf_list = []
        
        # Title Label
        title = tk.Label(root, text="PDF Merger Tool", font=("Arial", 18, "bold"))
        title.pack(pady=10)
        
        # Frame for buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        # Add PDF Button
        add_btn = tk.Button(button_frame, text="➕ Add PDF", command=self.add_pdf, bg="#4CAF50", fg="white", padx=10, pady=5)
        add_btn.grid(row=0, column=0, padx=5)
        
        # Remove PDF Button
        remove_btn = tk.Button(button_frame, text="❌ Remove PDF", command=self.remove_pdf, bg="#f44336", fg="white", padx=10, pady=5)
        remove_btn.grid(row=0, column=1, padx=5)
        
        # Clear All Button
        clear_btn = tk.Button(button_frame, text="🗑️ Clear All", command=self.clear_all, bg="#FF9800", fg="white", padx=10, pady=5)
        clear_btn.grid(row=0, column=2, padx=5)
        
        # Label for listbox
        list_label = tk.Label(root, text="Selected PDFs:", font=("Arial", 12, "bold"))
        list_label.pack(anchor="w", padx=20, pady=(10, 5))
        
        # Listbox to display selected PDFs
        self.listbox = tk.Listbox(root, height=10, width=70)
        self.listbox.pack(padx=20, pady=5)
        
        # Scrollbar for listbox
        scrollbar = tk.Scrollbar(root, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y", padx=5)
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # Output filename frame
        output_frame = tk.Frame(root)
        output_frame.pack(pady=10)
        
        output_label = tk.Label(output_frame, text="Output Filename:", font=("Arial", 10))
        output_label.pack(side="left", padx=5)
        
        self.output_entry = tk.Entry(output_frame, width=30)
        self.output_entry.pack(side="left", padx=5)
        self.output_entry.insert(0, "merged_document.pdf")
        
        # Merge Button
        merge_btn = tk.Button(root, text="🔗 Merge PDFs", command=self.merge_pdfs, bg="#2196F3", fg="white", padx=20, pady=10, font=("Arial", 12, "bold"))
        merge_btn.pack(pady=20)
    
    def add_pdf(self):
        """Add PDF files to the list"""
        files = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        for file in files:
            if file not in self.pdf_list:
                self.pdf_list.append(file)
                self.listbox.insert(tk.END, os.path.basename(file))
    
    def remove_pdf(self):
        """Remove selected PDF from the list"""
        try:
            index = self.listbox.curselection()[0]
            self.pdf_list.pop(index)
            self.listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a PDF to remove!")
    
    def clear_all(self):
        """Clear all PDFs"""
        self.pdf_list.clear()
        self.listbox.delete(0, tk.END)
        messagebox.showinfo("Info", "All PDFs cleared!")
    
    def merge_pdfs(self):
        """Merge selected PDFs"""
        if not self.pdf_list:
            messagebox.showerror("Error", "Please add PDF files first!")
            return
        
        output_filename = self.output_entry.get()
        
        if not output_filename.endswith(".pdf"):
            output_filename += ".pdf"
        
        try:
            merger = PdfWriter()
            
            for pdf in self.pdf_list:
                merger.append(pdf)
            
            merger.write(output_filename)
            messagebox.showinfo("Success", f"PDFs merged successfully!\nSaved as: {output_filename}")
            
            # Clear the list after successful merge
            self.pdf_list.clear()
            self.listbox.delete(0, tk.END)
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, "merged_document.pdf")
            
        except FileNotFoundError:
            messagebox.showerror("Error", "One or more PDF files not found!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerGUI(root)
    root.mainloop().__annotations__


