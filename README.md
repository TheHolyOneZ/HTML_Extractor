
# HTML Extractor: Split HTML, CSS, and JS

This Python script extracts inline CSS and JavaScript from an HTML file and saves them into separate `styles.css` and `scripts.js` files. It then modifies the original HTML to link to the external CSS and JS files. It also includes an interactive overlay that appears when the script starts.

## Features:
- Extracts inline CSS and JavaScript from HTML files.
- Saves the CSS and JS into separate files.
- Modifies the original HTML to link to the new CSS and JS files.
- Displays an overlay with a "TheZ on Top" message before starting the extraction process.

## Requirements:
- Python 3.x
- `beautifulsoup4` library (for parsing HTML)

### Installation:
1. Make sure Python 3.x is installed on your machine.
2. Install the required dependencies by running:
   ```bash
   pip install beautifulsoup4
   ```

### Usage:
1. Run the script in your terminal or command prompt:
   ```bash
   python main.py
   ```

2. The script will ask whether you want to open a file dialog to select an HTML file or provide a file path manually.

3. Once the HTML file is selected, the script extracts the CSS and JS, saves them into separate files, and updates the HTML accordingly.

### Example Output:
- `index.html` - Modified HTML file with links to `styles.css` and `scripts.js`.
- `styles.css` - Extracted CSS.
- `scripts.js` - Extracted JavaScript.

## Interactive Button

Click below to join the Discord server:

[![Join Our Discord Server](https://img.shields.io/badge/Join_Discord_Server-7289DA?style=for-the-badge&logo=discord)](https://discord.com/invite/zsGTqgnsmK)


Replace `YOUR_SERVER_INVITE` with your actual Discord server invite link.

---

### Notes:
- The script works by parsing the HTML file, finding all inline CSS and JavaScript, and saving them in separate files.
- The `overlay` window with "TheZ on Top" is shown for 2 seconds when the script starts.

---



