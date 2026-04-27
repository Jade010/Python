import tkinter as tk
from tkinter import filedialog
import pandas as pd
import random
import time
from collections import Counter
import ttkbootstrap as tb

class RestaurantPickerApp:
    def __init__(self, root):
        # Main window configuration
        self.root = root
        self.root.title("Restaurant Picker")
        self.root.geometry("650x650")
        self.root.resizable(False, False)

        # Data storage
        self.restaurant_df = None # Full dataset
        self.filtered_restaurants = [] # Filtered restaurant names
        self.cities = ["All"] # City dropdown values
        self.types = ["All"] # Type dropdown values

        self.setup_ui()

    def setup_ui(self):
        """Builds the UI components."""

        # Title
        tb.Label(self.root, text="Import Restaurant List", 
                 font=("Arial", 14, "bold")).pack(pady=10)

        # File import section
        import_frame = tb.Frame(self.root, bootstyle="light")
        import_frame.pack(pady=5, padx=20, fill="x")

        # Button for selecting restaurant file
        self.import_button = tb.Button(
            import_frame,
            text="📁 Browse File",
            command=self.browse_file,
            bootstyle="primary-outline"
        )
        self.import_button.pack(side="left", padx=10, pady=10)

        # Displays selected file name
        self.file_label = tb.Label(
            import_frame,
            text="No file selected",
            font=("Arial", 10),
            bootstyle="secondary"
        )
        self.file_label.pack(side="left", padx=10)

        # Filter section
        filter_frame = tb.Frame(self.root, bootstyle="light")
        filter_frame.pack(pady=10, padx=20, fill="x")

        # City filter dropdown
        tb.Label(filter_frame, text="City:", font=("Arial", 11)).pack(side="left", padx=10)
        self.city_var = tk.StringVar(value="All")
        self.city_dropdown = tb.Combobox(
            filter_frame,
            textvariable=self.city_var,
            values=self.cities,
            state="readonly",
            bootstyle="primary",
            width=15
        )
        
        self.city_dropdown.pack(side="left", padx=10)
        self.city_dropdown.bind("<<ComboboxSelected>>", self.filter_restaurants)

        # Type filter dropdown
        tb.Label(filter_frame, text="Type:", font=("Arial", 11)).pack(side="left", padx=10)
        self.type_var = tk.StringVar(value="All")
        self.type_dropdown = tb.Combobox(
            filter_frame,
            textvariable=self.type_var,
            values=self.types,
            state="readonly",
            bootstyle="primary",
            width=25
        )
        self.type_dropdown.pack(side="left", padx=10)
        self.type_dropdown.bind("<<ComboboxSelected>>", self.filter_restaurants)

        # Table to display restaurant data
        self.tree = tb.Treeview(
            self.root,
            columns=("Name", "City", "Type"),
            show="headings",
            bootstyle="info"
        )
        self.tree.heading("Name", text="Restaurant Name")
        self.tree.heading("City", text="City")
        self.tree.heading("Type", text="Type")

        self.tree.column("Name", width=250)
        self.tree.column("City", width=150)
        self.tree.column("Type", width=150)

        self.tree.pack(pady=10, padx=20, fill="both", expand=True)

        # Button to trigger random selection
        self.pick_button = tb.Button(
            self.root,
            text="🎲 Pick Restaurant",
            command=self.pick_restaurant,
            state=tk.DISABLED,
            bootstyle="success"
        )
        self.pick_button.pack(pady=10)

        # Label to display chosen restaurant
        self.selected_restaurant = tk.StringVar()
        self.result_label = tb.Label(
            self.root,
            textvariable=self.selected_restaurant,
            font=("Arial", 16, "bold"),
            bootstyle="danger"
        )
        self.result_label.pack(pady=10)

    def browse_file(self):
        """Opens file dialog and loads Excel data."""
        file_path = filedialog.askopenfilename(
            filetypes=[("Excel Files", "*.xlsx;*.xls")]
        )

        if file_path:
            try:
                # Load Excel file into DataFrame
                self.restaurant_df = pd.read_excel(file_path)

                # Validate required columns
                if {'Name', 'City', 'Type'}.issubset(self.restaurant_df.columns):
                    self.file_label.config(text=file_path.split("/")[-1])

                    self.populate_filters()
                    self.filter_restaurants()
                    self.pick_button.config(state=tk.NORMAL)
                else:
                    self.file_label.config(
                        text="Error: Missing required columns"
                    )
            except Exception as e:
                self.file_label.config(text=f"Error: {e}")

    def populate_filters(self):
        """Populates dropdown filters."""
        self.cities = ["All"] + sorted(
            self.restaurant_df["City"].dropna().unique().tolist()
        )
        self.types = ["All"] + sorted(
            self.restaurant_df["Type"].dropna().unique().tolist()
        )

        self.city_dropdown.config(values=self.cities)
        self.type_dropdown.config(values=self.types)

    def filter_restaurants(self, event=None):
        """Applies filters based on selected City and Type."""
        if self.restaurant_df is not None:
            selected_city = self.city_var.get()
            selected_type = self.type_var.get()

            filtered_df = self.restaurant_df

            if selected_city != "All":
                filtered_df = filtered_df[filtered_df['City'] == selected_city]

            if selected_type != "All":
                filtered_df = filtered_df[filtered_df['Type'] == selected_type]

            self.filtered_restaurants = filtered_df['Name'].tolist()

            self.update_table(filtered_df)

            if filtered_df.empty:
                self.pick_button.config(state=tk.DISABLED)
                self.selected_restaurant.set("No restaurants found.")
            else:
                self.pick_button.config(state=tk.NORMAL)
                self.selected_restaurant.set("")

    def update_table(self, df):
        """Refreshes table display."""
        self.tree.delete(*self.tree.get_children())

        for _, row in df.iterrows():
            self.tree.insert(
                "",
                "end",
                values=(row["Name"], row["City"], row["Type"])
            )

    def pick_restaurant(self):
        """Randomly selects a restaurant with animation."""
        if self.filtered_restaurants:
            self.pick_button.config(state=tk.DISABLED)

            results = []

            for _ in range(10):
                selected = random.choice(self.filtered_restaurants)
                results.append(selected)

                self.selected_restaurant.set(selected)
                self.root.update()
                time.sleep(0.1)

            final_choice = Counter(results).most_common(1)[0][0]

            self.selected_restaurant.set(f"{final_choice}")
            self.pick_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tb.Window(themename="minty")
    app = RestaurantPickerApp(root)
    root.mainloop()