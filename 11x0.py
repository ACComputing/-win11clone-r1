# windows11_clone.py

import tkinter as tk
from tkinter import ttk
import datetime

class Windows11Clone:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Windows 11 Clone")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
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

        # Desktop area (canvas for flexible positioning)
        self.desktop = tk.Canvas(self.root, bg='#E6F0FA', highlightthickness=0)
        self.desktop.pack(fill=tk.BOTH, expand=True)

        # Create interactive desktop icons
        self.create_desktop_icon("This PC", 30, 30, self.open_this_pc)
        self.create_desktop_icon("Recycle Bin", 30, 110, self.open_recycle_bin)
        self.create_desktop_icon("Documents", 30, 190, self.open_documents)

        # Taskbar
        self.taskbar = tk.Frame(self.root, bg='#202020', height=40)
        self.taskbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.taskbar.pack_propagate(False)

        center_frame = tk.Frame(self.taskbar, bg='#202020')
        center_frame.pack(expand=True)

        # Start button (Windows logo)
        self.start_btn = tk.Label(center_frame, text='󰣇', font=('Segoe UI', 14),
                                  fg='white', bg='#202020', cursor='hand2')
        self.start_btn.pack(side=tk.LEFT, padx=10)
        self.start_btn.bind('<Button-1>', self.toggle_start_menu)

        # Other taskbar icons (non‑functional placeholders)
        icons = ['🔍', '🗖', '󰡔', '󰎗']
        for icon in icons:
            lbl = tk.Label(center_frame, text=icon, font=('Segoe UI', 12),
                           fg='white', bg='#202020')
            lbl.pack(side=tk.LEFT, padx=8)

        # Clock
        self.clock_label = tk.Label(self.taskbar, font=('Segoe UI', 10),
                                    fg='white', bg='#202020')
        self.clock_label.pack(side=tk.RIGHT, padx=10, pady=8)
        self.update_clock()

        # Start menu (initially hidden)
        self.start_menu = None
        self.all_apps_visible = False   # track whether "All apps" is expanded

        self.root.mainloop()

    def create_desktop_icon(self, name, x, y, command):
        """Place an interactive desktop icon with text."""
        icon = tk.Label(self.desktop, text='📁', font=('Segoe UI', 24),
                        bg='#E6F0FA', fg='#2C3E50', cursor='hand2')
        self.desktop.create_window(x, y, window=icon, anchor='nw')
        icon.bind('<Double-Button-1>', lambda e: command())

        text = tk.Label(self.desktop, text=name, font=('Segoe UI', 8),
                        bg='#E6F0FA', fg='#2C3E50', cursor='hand2')
        self.desktop.create_window(x+10, y+45, window=text, anchor='n')
        text.bind('<Double-Button-1>', lambda e: command())

    # Placeholder functions for desktop icons
    def open_this_pc(self):
        self.show_message("This PC", "This would open File Explorer.")

    def open_recycle_bin(self):
        self.show_message("Recycle Bin", "This would open the Recycle Bin.")

    def open_documents(self):
        self.show_message("Documents", "This would open your Documents folder.")

    def show_message(self, title, message):
        msg = tk.Toplevel(self.root)
        msg.title(title)
        msg.geometry("300x150")
        msg.resizable(False, False)
        msg.configure(bg='#f0f0f0')
        tk.Label(msg, text=message, font=('Segoe UI', 10), bg='#f0f0f0').pack(expand=True)
        tk.Button(msg, text="OK", command=msg.destroy, bg='#0078D4', fg='white',
                  activebackground='#005A9E', activeforeground='white').pack(pady=10)

    def update_clock(self):
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p").lstrip('0')
        self.clock_label.config(text=time_str)
        self.root.after(1000, self.update_clock)

    def toggle_start_menu(self, event):
        """Show or hide the start menu."""
        if self.start_menu and self.start_menu.winfo_exists():
            self.start_menu.destroy()
            self.start_menu = None
        else:
            self.show_start_menu()

    def show_start_menu(self):
        """Create the start menu popup with pinned apps and an 'All apps' section."""
        self.start_menu = tk.Toplevel(self.root)
        self.start_menu.overrideredirect(True)
        self.start_menu.geometry("280+50+200")  # width 280, height will adjust
        self.start_menu.configure(bg='#2D2D2D')

        # Main container
        main = tk.Frame(self.start_menu, bg='#2D2D2D')
        main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Header
        tk.Label(main, text="Start", font=('Segoe UI', 14, 'bold'),
                 fg='white', bg='#2D2D2D').pack(anchor='w', pady=(0,10))

        # Pinned apps section
        tk.Label(main, text="Pinned", font=('Segoe UI', 10),
                 fg='#AAAAAA', bg='#2D2D2D').pack(anchor='w')

        pinned_apps = ["Settings", "File Explorer", "Microsoft Store", "Calculator", "Notepad"]
        for app in pinned_apps:
            btn = tk.Button(main, text=app, bg='black', fg='#1E90FF',
                            activebackground='gray', activeforeground='#1E90FF',
                            bd=0, padx=10, pady=5, anchor='w')
            btn.pack(fill=tk.X, pady=2)

        # Separator
        ttk.Separator(main, orient='horizontal').pack(fill=tk.X, pady=10)

        # "All apps" button (toggle)
        self.all_apps_btn = tk.Button(main, text="▼ All apps", bg='black', fg='#1E90FF',
                                       activebackground='gray', activeforeground='#1E90FF',
                                       bd=0, padx=10, pady=5, anchor='w',
                                       command=self.toggle_all_apps)
        self.all_apps_btn.pack(fill=tk.X, pady=2)

        # Frame that will contain the scrollable all‑apps list (initially empty)
        self.all_apps_frame = tk.Frame(main, bg='#2D2D2D')
        self.all_apps_frame.pack(fill=tk.BOTH, expand=True)
        # We'll populate it only when expanded

        # Click anywhere outside to close (simplified: click on start menu background)
        self.start_menu.bind('<Button-1>', lambda e: self.start_menu.destroy())

    def toggle_all_apps(self):
        """Expand or collapse the all‑apps list."""
        if self.all_apps_visible:
            # Collapse: remove all widgets from the all_apps_frame
            for widget in self.all_apps_frame.winfo_children():
                widget.destroy()
            self.all_apps_btn.config(text="▼ All apps")
            self.all_apps_visible = False
        else:
            # Expand: populate with a scrollable list of many apps
            self.populate_all_apps()
            self.all_apps_btn.config(text="▲ All apps")
            self.all_apps_visible = True

    def populate_all_apps(self):
        """Create a scrollable canvas with many application names."""
        # Create a canvas with a scrollbar
        canvas = tk.Canvas(self.all_apps_frame, bg='#2D2D2D', highlightthickness=0)
        scrollbar = tk.Scrollbar(self.all_apps_frame, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#2D2D2D')

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # List of common Windows apps (short list for demonstration)
        all_apps_list = [
            "3D Viewer", "Alarms & Clock", "Calculator", "Calendar", "Camera",
            "Cortana", "Feedback Hub", "Get Help", "Groove Music", "Maps",
            "Messaging", "Microsoft Edge", "Microsoft Store", "Movies & TV",
            "News", "OneDrive", "OneNote", "Paint", "Paint 3D", "People",
            "Photos", "Power Automate", "Quick Assist", "Settings", "Skype",
            "Snip & Sketch", "Solitaire Collection", "Sound Recorder",
            "Sticky Notes", "Tips", "To Do", "Voice Recorder", "Weather",
            "Windows Security", "WordPad", "Xbox", "Your Phone"
        ]

        for app in all_apps_list:
            btn = tk.Button(scrollable_frame, text=app, bg='black', fg='#1E90FF',
                            activebackground='gray', activeforeground='#1E90FF',
                            bd=0, padx=10, pady=5, anchor='w')
            btn.pack(fill=tk.X, pady=1)

if __name__ == "__main__":
    Windows11Clone()
