# Chat Search Application

## Overview

The Chat Search Application is a Python-based GUI tool designed for searching through chat conversations. It allows users to load chat data from a ZIP file, store the data in a local SQLite database, and perform text-based searches on the conversations.

## Features

- **File Browsing**: Browse and select ZIP files containing chat data in JSON format.
- **Data Extraction**: Automatically extract JSON files from the selected ZIP file.
- **SQLite Database Integration**: Store and manage extracted chat data in a SQLite database.
- **Search Functionality**: Perform text searches across all stored chat conversations.
- **Results Display**: View search results in a tabular format within the GUI.

## Prerequisites

- Python 3.x
- Tkinter (usually comes with Python)
- SQLite3 (comes with Python)

## Setup

1. Ensure Python 3.x is installed on your system.
2. Clone or download this repository to your local machine.
3. Navigate to the directory containing the application.

## Usage

1. Run the application script:

   python chat_search_app.py
Use the "Browse ZIP File" button to select a ZIP file containing JSON-formatted chat data.
After the data is extracted and loaded, enter a search term in the search bar.
Click the "Search" button to display the conversations containing the search term in the results table.
The table will show conversation IDs and a snippet of the content for each match.
Limitations
The application currently supports only ZIP files containing JSON-formatted chat data.
Large datasets may affect performance during data extraction and searching.
Future Enhancements
Implement advanced search options (e.g., regular expressions, specific field searches).
Optimize performance for large datasets.
Enhance the user interface for better user experience.
License
This project is open-source and available under the MIT License.


### Notes on the README:

- **Content**: The README includes sections on the overview, features, prerequisites, setup, usage, limitations, future enhancements, and licensing.
- **Usage Instructions**: Detailed steps for running and using the application are provided.
- **Enhancements and Limitations**: This section outlines potential areas for future development and current limitations.
- **License**: The license is mentioned at the end. You should include an actual `LICENSE` file in your project if you distribute it. 

This README should be placed in the root directory of your project, and you can name it `README.md`. It will serve as the main documentation for users and contributors to your application.
