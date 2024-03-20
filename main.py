import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def organize_files():
    source_folder = source_entry.get()
    destination_folder = destination_entry.get()
    file_type_to_folder = {
        #Documents
        '.pdf': 'Documents',
        '.docx': 'Documents',
        '.doc': 'Documents',
        #Images
        '.webp': 'Images',
        '.jpg': 'Images',
        '.png': 'Images',
        '.gif': 'Images',
        '.svg': 'Images',
        '.bmp': 'Images',
        #Videos
        '.mp4': 'Videos',
        '.avi': 'Videos',
        '.mkv': 'Videos',
        '.mov': 'Videos',
        '.wmv': 'Videos',
        '.flv': 'Videos',
        #Audio
        '.mp3': 'Audio',
        #Program Files
        '.c': 'Code',
        '.cpp': 'Code',
        '.cxx': 'Code',
        '.cc': 'Code',
        '.css': 'Code',
        '.html': 'Code',
        '.js': 'Code',
        '.json': 'Code',
        '.java': 'Code',
        '.py': 'Code',
        '.php': 'Code',
        '.rb': 'Code',
        #Other
        '.zip': 'Other',
        '.exe': 'Other',
        '.txt': 'Other'
    }

    # Create the folders if they don't exist
    for folder in file_type_to_folder.values():
        folder_path = os.path.join(destination_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to respective folders
    for filename in os.listdir(source_folder):
        name, extension = os.path.splitext(filename)
        if extension in file_type_to_folder:
            shutil.move(os.path.join(source_folder, filename),
                        os.path.join(destination_folder, file_type_to_folder[extension], filename))
    messagebox.showinfo("Success", "Files have been organized!")

def browse_source_folder():
    dirname = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, dirname)

def browse_destination_folder():
    dirname = filedialog.askdirectory()
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, dirname)

app = tk.Tk()
app.title("File Organizer")

# Source Folder
tk.Label(app, text="Source Folder:").grid(row=0, column=0, sticky=tk.W, pady=2)
source_entry = tk.Entry(app, width=50)
source_entry.grid(row=0, column=1, pady=2)
tk.Button(app, text="Browse...", command=browse_source_folder).grid(row=0, column=2, pady=2, padx=5)

# Destination Folder
tk.Label(app, text="Destination Folder:").grid(row=1, column=0, sticky=tk.W, pady=2)
destination_entry = tk.Entry(app, width=50)
destination_entry.grid(row=1, column=1, pady=2)
tk.Button(app, text="Browse...", command=browse_destination_folder).grid(row=1, column=2, pady=2, padx=5)

# Organize Button
organize_button = tk.Button(app, text="Organize Files", command=organize_files)
organize_button.grid(row=2, column=1, pady=10)

app.mainloop()