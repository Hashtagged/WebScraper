import tkinter as tk
from tkinter import scrolledtext
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Create the main window
window = tk.Tk()
window.title("WebScraper")

# Create the entry box
entry_box = tk.Entry(window, width=60)
entry_box.pack(side="top", fill="x")

# Function to parse data from the website
def parse_data():
    url = entry_box.get()
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Extract all the content from the website
    for tag in soup.find_all():
        scrolled_text.insert(tk.END, tag.text)
    
# Create the buttons
reset_button = tk.Button(window, text="Reset", command=lambda: scrolled_text.delete(1.0, tk.END))
reset_button.pack(side="left")

clear_button = tk.Button(window, text="Clear", command=lambda: entry_box.delete(0, tk.END))
clear_button.pack(side="left")

enter_button = tk.Button(window, text="Enter", command=parse_data)
enter_button.pack(side="right")

exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.pack(side="right")

# Create the scrolled text box
scrolled_text = scrolledtext.ScrolledText(window, width=100, height=70)
scrolled_text.pack()

# Start the window
window.mainloop()
