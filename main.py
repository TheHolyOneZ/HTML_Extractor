import os
import time
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog

def extract_css_js_from_html(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract CSS and JS
    css_code = ""
    js_code = ""

    # Find all style tags and extract their contents
    style_tags = soup.find_all('style')
    for tag in style_tags:
        css_code += tag.string if tag.string else ""

    # Find all script tags and extract their contents
    script_tags = soup.find_all('script')
    for tag in script_tags:
        if tag.string:  # Only extract inline scripts (ignore external sources)
            js_code += tag.string

    # Remove style and script tags from the original HTML
    for tag in style_tags:
        tag.decompose()
    for tag in script_tags:
        tag.decompose()

    # Return the modified HTML, CSS, and JS
    new_html = str(soup)
    return new_html, css_code, js_code

def save_files(new_html, css_code, js_code):
    # Save the new HTML file with links to external files using UTF-8 encoding
    with open('index.html', 'w', encoding='utf-8') as html_file:
        # Update the HTML to link to external CSS and JS files
        updated_html = new_html.replace(
            '<head>', 
            '<head>\n    <link rel="stylesheet" type="text/css" href="styles.css">'
        ).replace(
            '</body>', 
            '    <script src="scripts.js"></script>\n</body>'
        )
        html_file.write(updated_html)

    with open('styles.css', 'w', encoding='utf-8') as css_file:
        css_file.write(css_code)
    
    with open('scripts.js', 'w', encoding='utf-8') as js_file:
        js_file.write(js_code)

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  

    file_path = filedialog.askopenfilename(
        title="Select the HTML file",
        filetypes=[("HTML files", "*.html"), ("All files", "*.*")]
    )

    return file_path

def display_overlay_window():
    overlay = tk.Tk()
    overlay.title("Overlay Window")
    overlay.geometry("300x100+500+250")  
    overlay.configure(bg='white')  

    overlay.attributes("-topmost", True)  
    overlay.attributes("-transparentcolor", 'white')  
    overlay.overrideredirect(True)  

    label = tk.Label(overlay, text="TheZ on Top", font=('Helvetica', 24), fg='red', bg='white')
    label.pack(expand=True)

    overlay.after(2000, overlay.destroy)  
    overlay.mainloop()  

def main():
    display_overlay_window()

    
    choice = input("Would you like to select a file using the file explorer? (y/n): ").strip().lower()

    if choice == 'y':
        file_path = open_file_dialog()
        if not file_path:
            print("No file selected, exiting...")
            return
    else:
        file_path = input("Enter the full path to the HTML file: ").strip()
        if not os.path.isfile(file_path):
            print(f"File '{file_path}' does not exist.")
            return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    new_html, css_code, js_code = extract_css_js_from_html(html_content)
    save_files(new_html, css_code, js_code)

    print("Process complete: HTML, CSS, and JS have been separated and saved.")

if __name__ == "__main__":
    main()
