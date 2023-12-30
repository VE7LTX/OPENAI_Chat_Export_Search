import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import zipfile
import json
from pathlib import Path

def create_db_and_tables():
    """
    Create SQLite database and tables for storing conversation data.
    """
    conn = sqlite3.connect('chat_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id TEXT PRIMARY KEY,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_data_to_db(data):
    """
    Insert conversation data into the SQLite database.

    Parameters:
    data (list): List of conversation data to be inserted.
    """
    conn = sqlite3.connect('chat_data.db')
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT OR REPLACE INTO conversations (id, content)
        VALUES (?, ?)
    ''', data)
    conn.commit()
    conn.close()

def browse_file():
    """
    Open a file dialog to browse and select a ZIP file.
    Trigger extraction and data loading upon file selection.
    """
    filename = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])
    if filename:
        extract_and_load_data(filename)

def extract_and_load_data(zip_file_path):
    """
    Extract the selected ZIP file and load its contents.

    Parameters:
    zip_file_path (str): The path of the selected ZIP file.
    """
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            extract_to = Path(zip_file_path).stem + "_extracted"
            zip_ref.extractall(extract_to)
            load_data_from_extracted(extract_to)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def load_data_from_extracted(directory):
    """
    Load data from extracted JSON files in the given directory.

    Parameters:
    directory (str): The directory containing the extracted JSON files.
    """
    conversations = []
    for file in Path(directory).glob('*.json'):
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                # Assuming each item in the list has 'id' and 'content'
                conversations.extend([(item['id'], json.dumps(item['content'])) for item in data])
    insert_data_to_db(conversations)

def search_conversations(search_term):
    """
    Search for a given term within conversations in the SQLite database.

    Parameters:
    search_term (str): The term to search for within the conversation data.

    Returns:
    list: A list of conversation IDs and content that contain the search term.
    """
    conn = sqlite3.connect('chat_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, content FROM conversations
        WHERE content LIKE ?
    ''', ('%' + search_term.lower() + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

def update_table(results):
    """
    Update the results table with the given search results.

    Parameters:
    results (list): A list of conversations that matched the search term.
    """
    for i in tree.get_children():
        tree.delete(i)
    for conversation_id, content in results:
        tree.insert('', 'end', values=(conversation_id, content[:100]))  # Displaying first 100 characters

def on_search():
    """
    Callback function for the search button.
    Retrieves the search term and updates the table with search results.
    """
    search_term = search_entry.get()
    results = search_conversations(search_term)
    update_table(results)

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Chat Search")

# Create database and tables
create_db_and_tables()

# Browse file button
browse_button = tk.Button(root, text="Browse ZIP File", command=browse_file)
browse_button.pack()

# Search entry and button
search_entry = tk.Entry(root)
search_entry.pack(side=tk.LEFT)
search_button = tk.Button(root, text="Search", command=on_search)
search_button.pack(side=tk.LEFT)

# Table to display search results
columns = ('id', 'content')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('id', text='ID')
tree.heading('content', text='Content')
tree.pack(expand=True, fill='both')

# Start the GUI event loop
root.mainloop()
