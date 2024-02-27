"""
    Name: polyangle_tkinter.py
    Author: Jed Felker
    Created: 12/4/22
    Purpose: GUI version of polyangle
"""

# Import the tkinter module
from tkinter import *
# Override tk widgets with themed ttk widgets if available
from tkinter.ttk import *

class PolyAngle:
    # A class level tuple that holds polygon names
    POLYGON_NAMES = (
        'Triangle', 'Quadrilateral', 'Pentagon', 'Hexagon',
        'Heptagon', 'Octagton', 'Nonagon', 'Decagon', 
        'Hendecagon', 'Dodecagon', 'Tridecagon', 'Tetradecagon',
        'Pentadecagon', 'Hexadecagon', 'Heptadecagon', 
        'Octadecagon', 'Enneadecagon', 'Icosagon'
    )

    def __init__(self):
        """
            Define the object initialize method
        """
        # Create the root window
        self.root = Tk()
        self.root.title("PolyAngle")

        # Add icon to window corner
        # Search the web fro free thermometer.ico files
        # self.root.iconbitmap("thermometer.ico")

        # Prevent window from resizing
        self.root.resizable(False, False)

        # Create the GUI widgets in a seperate method
        self.create_widgets()

        # Call the mainloop method to start program
        self.root.mainloop()

    def create_widgets(self):
        # Create main label frame to hold widgets
        self.main_frame = LabelFrame(
            self.root,                              # Assign to parent window
            text="Enter Polygon Sides",    # Text for the frame
            relief=GROOVE                           # Decorative border
        )

        self.output_frame = LabelFrame(
            self.root,                              # Assign to parent window
            text="Enter Polygon Sides",    # Text for the frame
            relief=GROOVE                           # Decorative border
        )

        # Set padding between frame and window
        self.main_frame.grid_configure(padx=20, pady=20)

        # Set padding for all widgets inside the frame
        for widget in self.main_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)
        
        # Set padding between frame and window
        self.output_frame.grid_configure(padx=20, pady=20)

        # Set padding for all widgets inside the frame
        for widget in self.output_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)

        self.enter_sides = Entry(
            self.main_frame,  # Assign to parent frame
            width=15          # Width in characters
        )

        self.side_len = Entry(
            self.main_frame,  # Assign to parent frame
            width=15          # Width in characters
        )

        self.enter_sides.grid(row=0, column=1)
        self.side_len.grid(row=1, column=1)


        self.calculate_angles = Button(
            self. main_frame,            # Assign to parent frame
            text="Calculate Angles",     # Text shown on button
            # Connect convert method to button click
            command=self.calculateAngles
        )

        self.calculate_angles.grid(row=2, columnspan=2)

        self.lbl_numsides = Label(
            self.main_frame,     # Assign to parent frame
            text="Enter # of Sides:",
            width=15,            # Width in characters
            relief=FLAT,       # Decorative border
            justify=CENTER
        )

        self.lbl_lensides = Label(
            self.main_frame,     # Assign to parent frame
            text="Enter Length of \nSides:",
            width=15,            # Width in characters
            relief=FLAT,       # Decorative border
            justify=CENTER
        )

        self.lbl_polygon = Label(
            self.output_frame,     # Assign to parent frame
            width=30,            # Width in characters
            relief=GROOVE       # Decorative border
        )

        self.lbl_interior = Label(
            self.output_frame,     # Assign to parent frame
            width=30,            # Width in characters
            relief=GROOVE       # Decorative border
        )

        self.lbl_exterior = Label(
            self.output_frame,     # Assign to parent frame
            width=30,            # Width in characters
            relief=GROOVE       # Decorative border
        )

        self.lbl_perimeter = Label(
            self.output_frame,     # Assign to parent frame
            width=30,            # Width in characters
            relief=GROOVE       # Decorative border
        )

        self.lbl_numsides.grid(row=0, column=0)
        self.lbl_lensides.grid(row=1, column=0)
        self.lbl_interior.grid(row=1, columnspan=2)
        self.lbl_exterior.grid(row=2, columnspan=2)
        self.lbl_polygon.grid(row=0, columnspan=2)
        self.lbl_perimeter.grid(row=3, columnspan=2)

    def calculateAngles(self):
        self.POLYGON_NAMES
        self._sides = float(self.enter_sides.get())
        self._length = float(self.side_len.get())
        self._interior = (self._sides - 2) * 180 / self._sides
        self._exterior = 360 / self._sides
        self._perimeter = self._sides * self._length
        if self._sides == 3:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[0]}")
        elif self._sides == 4:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[1]}")
        elif self._sides == 5:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[2]}")
        elif self._sides == 6:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[3]}")
        elif self._sides == 7:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[4]}")
        elif self._sides == 8:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[5]}")
        elif self._sides == 9:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[6]}")
        elif self._sides == 10:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[7]}")
        elif self._sides == 11:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[8]}")
        elif self._sides == 12:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[9]}")
        elif self._sides == 13:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[10]}")
        elif self._sides == 14:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[11]}")
        elif self._sides == 15:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[12]}")
        elif self._sides == 16:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[13]}")
        elif self._sides == 17:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[14]}")
        elif self._sides == 18:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[15]}")
        elif self._sides == 19:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[16]}")
        elif self._sides == 20:
            self.lbl_polygon.configure(text=f"Polygon: {self.POLYGON_NAMES[17]}")
        self.lbl_interior.configure(text=f"Interior angle: {self._interior:,.2f}°")
        self.lbl_exterior.configure(text=f"Exterior angle: {self._exterior:,.2f}°")
        self.lbl_perimeter.configure(text=f"Perimeter: {self._perimeter}")
polyangle = PolyAngle()