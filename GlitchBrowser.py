import tkinter as tk
from tkinter import ttk
import webbrowser
from urllib.parse import quote

class GlitchBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("Glitch Browser")
        
        # Search engine options
        self.search_engines = {
            "Google": "https://www.google.com/search?q=",
            "DuckDuckGo": "https://duckduckgo.com/?q=",
            "Bing": "https://www.bing.com/search?q=",
            "Wikipedia": "https://wikipedia.org/wiki/Special:Search/"
        }
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Search engine selector
        self.engine_var = tk.StringVar(value="Google")
        engine_label = ttk.Label(self.root, text="Search Engine:")
        engine_label.pack(pady=5)
        
        engine_menu = ttk.Combobox(self.root, textvariable=self.engine_var, 
                                 values=list(self.search_engines.keys()),
                                 state="readonly")
        engine_menu.pack(pady=5)
        
        # Search entry
        self.search_entry = ttk.Entry(self.root, width=50)
        self.search_entry.pack(pady=10)
        
        # Search button
        search_button = ttk.Button(self.root, text="Search",
                                 command=self.perform_search)
        search_button.pack(pady=5)
        
    def perform_search(self):
        query = self.search_entry.get()
        if query:
            engine = self.engine_var.get()
            base_url = self.search_engines[engine]
            search_url = base_url + quote(query)
            webbrowser.open(search_url)

def main():
    root = tk.Tk()
    root.geometry("400x200")
    app = GlitchBrowser(root)
    root.mainloop()

if __name__ == "__main__":
    main()