# windows11_clone.py

import tkinter as tk
from tkinter import ttk
import datetime

class Windows11Clone:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Windows 11 25H2 Clone")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.configure(bg='black')

        # Style
        self.style = ttk.Style()
        available_themes = self.style.theme_names()
        if 'vista' in available_themes:
            self.style.theme_use('vista')
        elif 'xpnative' in available_themes:
            self.style.theme_use('xpnative')
        elif 'clam' in available_themes:
            self.style.theme_use('clam')

        # Desktop
        self.desktop = tk.Canvas(self.root, bg='black', highlightthickness=0)
        self.desktop.pack(fill=tk.BOTH, expand=True)

        # Desktop icons
        self.create_desktop_icon("This PC", 30, 30, self.open_this_pc)
        self.create_desktop_icon("Recycle Bin", 30, 110, self.open_recycle_bin)
        self.create_desktop_icon("Documents", 30, 190, self.open_documents)

        # Taskbar
        self.taskbar = tk.Frame(self.root, bg='black', height=40)
        self.taskbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.taskbar.pack_propagate(False)

        # Left side (Start, Search, Task View, Widgets)
        left_frame = tk.Frame(self.taskbar, bg='black')
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)

        # Start button
        self.start_btn = tk.Label(left_frame, text='󰣇', font=('Segoe UI', 14),
                                  fg='#1E90FF', bg='black', cursor='hand2')
        self.start_btn.pack(side=tk.LEFT, padx=5)
        self.start_btn.bind('<Button-1>', self.toggle_start_menu)

        # Search
        self.search_btn = tk.Label(left_frame, text='🔍', font=('Segoe UI', 12),
                                   fg='#1E90FF', bg='black', cursor='hand2')
        self.search_btn.pack(side=tk.LEFT, padx=8)
        self.search_btn.bind('<Button-1>', self.toggle_search)

        # Task View
        self.taskview_btn = tk.Label(left_frame, text='🗖', font=('Segoe UI', 12),
                                     fg='#1E90FF', bg='black', cursor='hand2')
        self.taskview_btn.pack(side=tk.LEFT, padx=8)
        self.taskview_btn.bind('<Button-1>', self.toggle_task_view)

        # Widgets
        self.widgets_btn = tk.Label(left_frame, text='󰡔', font=('Segoe UI', 12),
                                    fg='#1E90FF', bg='black', cursor='hand2')
        self.widgets_btn.pack(side=tk.LEFT, padx=8)
        self.widgets_btn.bind('<Button-1>', self.toggle_widgets)

        # Separator (optional)
        ttk.Separator(self.taskbar, orient='vertical').pack(side=tk.LEFT, fill='y', padx=5)

        # Right side (System Tray + Clock)
        right_frame = tk.Frame(self.taskbar, bg='black')
        right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5)

        # System tray icons
        tray_icons = ['🔊', '📶', '🔋', '🔔']  # volume, network, battery, notification
        self.tray_labels = []
        for icon in tray_icons:
            lbl = tk.Label(right_frame, text=icon, font=('Segoe UI', 12),
                           fg='#1E90FF', bg='black', cursor='hand2')
            lbl.pack(side=tk.LEFT, padx=4)
            self.tray_labels.append(lbl)

        # Bind notification icon to open action center
        self.tray_labels[3].bind('<Button-1>', self.toggle_action_center)

        # Clock (clickable)
        self.clock_label = tk.Label(right_frame, font=('Segoe UI', 10),
                                    fg='#1E90FF', bg='black', cursor='hand2')
        self.clock_label.pack(side=tk.LEFT, padx=8)
        self.clock_label.bind('<Button-1>', self.toggle_calendar)
        self.update_clock()

        # Popup references
        self.start_menu = None
        self.search_popup = None
        self.taskview_popup = None
        self.widgets_popup = None
        self.action_center_popup = None
        self.calendar_popup = None
        self.all_apps_visible = False

        self.root.mainloop()

    # Desktop icon helpers (unchanged)
    def create_desktop_icon(self, name, x, y, command):
        icon = tk.Label(self.desktop, text='📁', font=('Segoe UI', 24),
                        bg='black', fg='#1E90FF', cursor='hand2')
        self.desktop.create_window(x, y, window=icon, anchor='nw')
        icon.bind('<Double-Button-1>', lambda e: command())

        text = tk.Label(self.desktop, text=name, font=('Segoe UI', 8),
                        bg='black', fg='#1E90FF', cursor='hand2')
        self.desktop.create_window(x+10, y+45, window=text, anchor='n')
        text.bind('<Double-Button-1>', lambda e: command())

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
        msg.configure(bg='black')
        tk.Label(msg, text=message, font=('Segoe UI', 10),
                 bg='black', fg='#1E90FF').pack(expand=True)
        tk.Button(msg, text="OK", command=msg.destroy,
                  bg='black', fg='#1E90FF', activebackground='gray',
                  activeforeground='#1E90FF').pack(pady=10)

    def update_clock(self):
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p").lstrip('0')
        self.clock_label.config(text=time_str)
        self.root.after(1000, self.update_clock)

    # --- Popup management ---
    def close_all_popups(self, exclude=None):
        for popup in [self.start_menu, self.search_popup, self.taskview_popup,
                      self.widgets_popup, self.action_center_popup, self.calendar_popup]:
            if popup and popup != exclude and popup.winfo_exists():
                popup.destroy()
        # Reset references if they were destroyed
        if exclude != self.start_menu: self.start_menu = None
        if exclude != self.search_popup: self.search_popup = None
        if exclude != self.taskview_popup: self.taskview_popup = None
        if exclude != self.widgets_popup: self.widgets_popup = None
        if exclude != self.action_center_popup: self.action_center_popup = None
        if exclude != self.calendar_popup: self.calendar_popup = None

    def toggle_start_menu(self, event):
        self.close_all_popups(exclude=self.start_menu)
        if self.start_menu and self.start_menu.winfo_exists():
            self.start_menu.destroy()
            self.start_menu = None
        else:
            self.show_start_menu()

    def toggle_search(self, event):
        self.close_all_popups(exclude=self.search_popup)
        if self.search_popup and self.search_popup.winfo_exists():
            self.search_popup.destroy()
            self.search_popup = None
        else:
            self.show_search()

    def toggle_task_view(self, event):
        self.close_all_popups(exclude=self.taskview_popup)
        if self.taskview_popup and self.taskview_popup.winfo_exists():
            self.taskview_popup.destroy()
            self.taskview_popup = None
        else:
            self.show_task_view()

    def toggle_widgets(self, event):
        self.close_all_popups(exclude=self.widgets_popup)
        if self.widgets_popup and self.widgets_popup.winfo_exists():
            self.widgets_popup.destroy()
            self.widgets_popup = None
        else:
            self.show_widgets()

    def toggle_action_center(self, event):
        self.close_all_popups(exclude=self.action_center_popup)
        if self.action_center_popup and self.action_center_popup.winfo_exists():
            self.action_center_popup.destroy()
            self.action_center_popup = None
        else:
            self.show_action_center()

    def toggle_calendar(self, event):
        self.close_all_popups(exclude=self.calendar_popup)
        if self.calendar_popup and self.calendar_popup.winfo_exists():
            self.calendar_popup.destroy()
            self.calendar_popup = None
        else:
            self.show_calendar()

    # --- Popup implementations ---
    def show_start_menu(self):
        self.start_menu = tk.Toplevel(self.root)
        self.start_menu.overrideredirect(True)
        self.start_menu.geometry("280+50+200")
        self.start_menu.configure(bg='black')

        main = tk.Frame(self.start_menu, bg='black')
        main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(main, text="Start", font=('Segoe UI', 14, 'bold'),
                 fg='#1E90FF', bg='black').pack(anchor='w', pady=(0,10))

        tk.Label(main, text="Pinned", font=('Segoe UI', 10),
                 fg='#1E90FF', bg='black').pack(anchor='w')

        pinned_apps = ["Settings", "File Explorer", "Microsoft Store", "Calculator", "Notepad"]
        for app in pinned_apps:
            btn = tk.Button(main, text=app, bg='black', fg='#1E90FF',
                            activebackground='gray', activeforeground='#1E90FF',
                            bd=0, padx=10, pady=5, anchor='w')
            btn.pack(fill=tk.X, pady=2)

        ttk.Separator(main, orient='horizontal').pack(fill=tk.X, pady=10)

        self.all_apps_btn = tk.Button(main, text="▼ All apps", bg='black', fg='#1E90FF',
                                       activebackground='gray', activeforeground='#1E90FF',
                                       bd=0, padx=10, pady=5, anchor='w',
                                       command=self.toggle_all_apps)
        self.all_apps_btn.pack(fill=tk.X, pady=2)

        self.all_apps_frame = tk.Frame(main, bg='black')
        self.all_apps_frame.pack(fill=tk.BOTH, expand=True)

        # Click outside to close (simplified)
        self.start_menu.bind('<Button-1>', lambda e: self.start_menu.destroy())

    def toggle_all_apps(self):
        if self.all_apps_visible:
            for widget in self.all_apps_frame.winfo_children():
                widget.destroy()
            self.all_apps_btn.config(text="▼ All apps")
            self.all_apps_visible = False
        else:
            self.populate_all_apps()
            self.all_apps_btn.config(text="▲ All apps")
            self.all_apps_visible = True

    def populate_all_apps(self):
        canvas = tk.Canvas(self.all_apps_frame, bg='black', highlightthickness=0)
        scrollbar = tk.Scrollbar(self.all_apps_frame, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='black')

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

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

    def show_search(self):
        self.search_popup = tk.Toplevel(self.root)
        self.search_popup.overrideredirect(True)
        self.search_popup.geometry("300x200+100+150")
        self.search_popup.configure(bg='black')

        tk.Label(self.search_popup, text="Search", font=('Segoe UI', 14, 'bold'),
                 fg='#1E90FF', bg='black').pack(pady=10)

        entry = tk.Entry(self.search_popup, bg='#333', fg='#1E90FF',
                         insertbackground='#1E90FF', font=('Segoe UI', 10))
        entry.pack(padx=10, pady=5, fill=tk.X)
        entry.insert(0, "Type here to search...")
        entry.bind('<FocusIn>', lambda e: entry.delete(0, tk.END))

        tk.Label(self.search_popup, text="Recent searches will appear here",
                 font=('Segoe UI', 8), fg='#1E90FF', bg='black').pack(pady=10)

        self.search_popup.bind('<Button-1>', lambda e: self.search_popup.destroy())

    def show_task_view(self):
        self.taskview_popup = tk.Toplevel(self.root)
        self.taskview_popup.overrideredirect(True)
        self.taskview_popup.geometry("400x200+100+100")
        self.taskview_popup.configure(bg='black')

        tk.Label(self.taskview_popup, text="Task View", font=('Segoe UI', 14, 'bold'),
                 fg='#1E90FF', bg='black').pack(pady=10)

        # Mock thumbnails
        thumbs_frame = tk.Frame(self.taskview_popup, bg='black')
        thumbs_frame.pack(pady=10)

        for i in range(3):
            thumb = tk.Frame(thumbs_frame, bg='#1E90FF', width=100, height=60)
            thumb.pack(side=tk.LEFT, padx=5)
            tk.Label(thumb, text=f"Desktop {i+1}", bg='#1E90FF', fg='black').place(relx=0.5, rely=0.5, anchor='center')

        self.taskview_popup.bind('<Button-1>', lambda e: self.taskview_popup.destroy())

    def show_widgets(self):
        self.widgets_popup = tk.Toplevel(self.root)
        self.widgets_popup.overrideredirect(True)
        self.widgets_popup.geometry("350x250+200+100")
        self.widgets_popup.configure(bg='black')

        tk.Label(self.widgets_popup, text="Widgets", font=('Segoe UI', 14, 'bold'),
                 fg='#1E90FF', bg='black').pack(pady=10)

        # Weather widget
        weather_frame = tk.Frame(self.widgets_popup, bg='#1E90FF', width=300, height=80)
        weather_frame.pack(pady=5, padx=10, fill=tk.X)
        weather_frame.pack_propagate(False)
        tk.Label(weather_frame, text="☀️ 72°F", font=('Segoe UI', 12),
                 bg='#1E90FF', fg='black').pack(expand=True)

        # News widget
        news_frame = tk.Frame(self.widgets_popup, bg='#1E90FF', width=300, height=60)
        news_frame.pack(pady=5, padx=10, fill=tk.X)
        news_frame.pack_propagate(False)
        tk.Label(news_frame, text="Breaking: Tkinter still awesome!",
                 font=('Segoe UI', 10), bg='#1E90FF', fg='black').pack(expand=True)

        self.widgets_popup.bind('<Button-1>', lambda e: self.widgets_popup.destroy())

    def show_action_center(self):
        self.action_center_popup = tk.Toplevel(self.root)
        self.action_center_popup.overrideredirect(True)
        self.action_center_popup.geometry("280x300+320+150")
        self.action_center_popup.configure(bg='black')

        tk.Label(self.action_center_popup, text="Action Center", font=('Segoe UI', 12, 'bold'),
                 fg='#1E90FF', bg='black').pack(pady=5)

        # Quick actions
        actions = ["Wi-Fi", "Bluetooth", "Airplane Mode", "Night Light", "VPN"]
        actions_frame = tk.Frame(self.action_center_popup, bg='black')
        actions_frame.pack(pady=10)

        for i, action in enumerate(actions):
            btn = tk.Button(actions_frame, text=action, bg='#1E90FF', fg='black',
                            width=10, height=2)
            btn.grid(row=i//2, column=i%2, padx=2, pady=2)

        # Notifications
        tk.Label(self.action_center_popup, text="Notifications", font=('Segoe UI', 10),
                 fg='#1E90FF', bg='black').pack(anchor='w', padx=10)
        notif_frame = tk.Frame(self.action_center_popup, bg='#1E90FF', height=60)
        notif_frame.pack(padx=10, pady=5, fill=tk.X)
        tk.Label(notif_frame, text="No new notifications", bg='#1E90FF', fg='black').pack(expand=True)

        self.action_center_popup.bind('<Button-1>', lambda e: self.action_center_popup.destroy())

    def show_calendar(self):
        self.calendar_popup = tk.Toplevel(self.root)
        self.calendar_popup.overrideredirect(True)
        self.calendar_popup.geometry("250x200+350+150")
        self.calendar_popup.configure(bg='black')

        now = datetime.datetime.now()
        month_year = now.strftime("%B %Y")
        tk.Label(self.calendar_popup, text=month_year, font=('Segoe UI', 12, 'bold'),
                 fg='#1E90FF', bg='black').pack(pady=5)

        # Simple calendar grid (just a placeholder)
        days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
        cal_frame = tk.Frame(self.calendar_popup, bg='black')
        cal_frame.pack(pady=5)

        for i, day in enumerate(days):
            tk.Label(cal_frame, text=day, fg='#1E90FF', bg='black',
                     font=('Segoe UI', 8)).grid(row=0, column=i, padx=5)

        # Show today's date
        tk.Label(self.calendar_popup, text=f"Today: {now.strftime('%B %d, %Y')}",
                 font=('Segoe UI', 9), fg='#1E90FF', bg='black').pack(pady=5)

        self.calendar_popup.bind('<Button-1>', lambda e: self.calendar_popup.destroy())

if __name__ == "__main__":
    Windows11Clone()
