# windows11_clone.py

import tkinter as tk
from tkinter import ttk
import datetime
import time

class Windows11Clone:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Windows 11 Clone")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Set the desktop background color (similar to default Windows 11)
        self.root.configure(bg='#E6F0FA')
        
        # Try to use a modern ttk theme
        self.style = ttk.Style()
        available_themes = self.style.theme_names()
        if 'vista' in available_themes:
            self.style.theme_use('vista')
        elif 'xpnative' in available_themes:
            self.style.theme_use('xpnative')
        elif 'clam' in available_themes:
            self.style.theme_use('clam')
        
        # Create desktop icons area (using a Canvas for flexible positioning)
        self.desktop = tk.Canvas(self.root, bg='#E6F0FA', highlightthickness=0)
        self.desktop.pack(fill=tk.BOTH, expand=True)
        
        # Add some desktop icons
        self.create_desktop_icon("This PC", 30, 30)
        self.create_desktop_icon("Recycle Bin", 30, 110)
        self.create_desktop_icon("Documents", 30, 190)
        
        # Create taskbar at the bottom
        self.taskbar = tk.Frame(self.root, bg='#202020', height=40)
        self.taskbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.taskbar.pack_propagate(False)  # Prevent shrinking
        
        # Center container for taskbar icons
        center_frame = tk.Frame(self.taskbar, bg='#202020')
        center_frame.pack(expand=True)
        
        # Start button (Windows logo)
        self.start_btn = tk.Label(center_frame, text='󰣇', font=('Segoe UI', 14), fg='white', bg='#202020', cursor='hand2')
        self.start_btn.pack(side=tk.LEFT, padx=10)
        self.start_btn.bind('<Button-1>', self.show_start_menu)
        
        # Search icon
        search_icon = tk.Label(center_frame, text='🔍', font=('Segoe UI', 12), fg='white', bg='#202020')
        search_icon.pack(side=tk.LEFT, padx=8)
        
        # Task view icon
        taskview_icon = tk.Label(center_frame, text='🗖', font=('Segoe UI', 12), fg='white', bg='#202020')
        taskview_icon.pack(side=tk.LEFT, padx=8)
        
        # Widgets icon
        widgets_icon = tk.Label(center_frame, text='󰡔', font=('Segoe UI', 12), fg='white', bg='#202020')
        widgets_icon.pack(side=tk.LEFT, padx=8)
        
        # Chat icon (Teams)
        chat_icon = tk.Label(center_frame, text='󰎗', font=('Segoe UI', 12), fg='white', bg='#202020')
        chat_icon.pack(side=tk.LEFT, padx=8)
        
        # Clock on the right side of taskbar
        self.clock_label = tk.Label(self.taskbar, font=('Segoe UI', 10), fg='white', bg='#202020')
        self.clock_label.pack(side=tk.RIGHT, padx=10, pady=8)
        self.update_clock()
        
        # Start menu (hidden initially)
        self.start_menu = None
        
        # Run the app
        self.root.mainloop()
    
    def create_desktop_icon(self, name, x, y):
        """Place a simple desktop icon with text."""
        # Icon placeholder (could use images, but here just a colored square)
        icon = tk.Label(self.desktop, text='📁', font=('Segoe UI', 24), bg='#E6F0FA', fg='#2C3E50')
        icon_window = self.desktop.create_window(x, y, window=icon, anchor='nw')
        # Text label
        text = tk.Label(self.desktop, text=name, font=('Segoe UI', 8), bg='#E6F0FA', fg='#2C3E50')
        text_window = self.desktop.create_window(x+10, y+45, window=text, anchor='n')
    
    def update_clock(self):
        """Update the taskbar clock every second."""
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p").lstrip('0')
        self.clock_label.config(text=time_str)
        self.root.after(1000, self.update_clock)
    
    def show_start_menu(self, event):
        """Display a simple start menu popup."""
        # If start menu already exists, toggle it
        if self.start_menu and self.start_menu.winfo_exists():
            self.start_menu.destroy()
            self.start_menu = None
            return
        
        # Create a toplevel window for start menu (simplified)
        self.start_menu = tk.Toplevel(self.root)
        self.start_menu.overrideredirect(True)  # Remove window decorations
        self.start_menu.geometry("200x300+50+200")  # Position near start button
        self.start_menu.configure(bg='#2D2D2D')
        
        # Add some placeholder content
        title = tk.Label(self.start_menu, text="Start", font=('Segoe UI', 12, 'bold'), 
                         fg='white', bg='#2D2D2D')
        title.pack(pady=10)
        
        apps = ["Settings", "File Explorer", "Microsoft Store", "Calculator", "Notepad"]
        for app in apps:
            # Fix: change background to black, foreground to bright blue
            btn = tk.Button(self.start_menu, text=app, 
                            bg='black', fg='#1E90FF',  # Black background, DodgerBlue text
                            activebackground='gray', activeforeground='#1E90FF',  # Optional hover colors
                            bd=0, padx=10, pady=5, anchor='w')
            btn.pack(fill=tk.X, padx=5, pady=2)
        
        # Click outside to close (simplified: click anywhere on start menu to close)
        self.start_menu.bind('<Button-1>', lambda e: self.start_menu.destroy())

if __name__ == "__main__":
    Windows11Clone()
