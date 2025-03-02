from collections import defaultdict

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QMainWindow, QDialog

WHITELIST_COLOR = "#88C0D0"
OTHER_COLOR = "#4C566A"

class BarGraph(QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.setWindowTitle("App Time Totals")

        layout = QVBoxLayout(self)

        # Create a Matplotlib figure and axis
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot(111)

        # Create the timeline
        self.plot_timeline(data)

        # Create canvas and add to layout
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

    def plot_timeline(self, data):
        # Calculate total time per app using a defaultdict
        app_time = defaultdict(int)
        app_whitelist = {}  # Dictionary to store whitelisted status of each app

        for item in data:
            app_name = item["appName"].replace(".exe", "")
            app_time[app_name] += item["time"]
            app_whitelist[app_name] = item.get("whitelisted", False)

        # Prepare data for plotting
        apps = list(app_time.keys())
        total_times = list(app_time.values())

        # Create a timeline as a vertical bar graph
        bar_width = 0.4
        x_pos = range(len(apps))  # Set x positions for each app

        # Assign colors based on whitelist status
        colors = [
            WHITELIST_COLOR if app_whitelist.get(app, False) else OTHER_COLOR
            for app in apps
        ]

        # Plot the bars for each app with the appropriate color
        self.ax.bar(x_pos, total_times, width=bar_width, color=colors)

        # Set labels and title
        self.ax.set_xticks(x_pos)
        self.ax.set_xticklabels(apps, rotation=0, ha="right")
        self.ax.set_ylabel("Total Time (seconds)")
        self.ax.set_title("Total Time per App")

        # Make the timeline nice and clean
        self.ax.set_ylim(
            0, max(total_times) + 5
        )  # Add some extra space at the top for visualization


class PieGraph(QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.setWindowTitle("App Usage Percentages")

        layout = QVBoxLayout(self)

        # Create a Matplotlib figure and axis
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot(111)

        # Create the Pie chart
        self.plot_pie_chart(data)

        # Create canvas and add to layout
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

    def plot_pie_chart(self, data):
        # Aggregate total time per app
        app_time = {}
        app_whitelist = {}  # Dictionary to store whitelisted status of each app

        # Process data to aggregate total time and store whitelist info
        for item in data:
            app_name = item["appName"].replace(".exe", "")
            app_time[app_name] = app_time.get(app_name, 0) + item["time"]
            app_whitelist[app_name] = item.get("whitelisted", False)

        total_time = sum(app_time.values())  # Total duration for all apps
        if total_time == 0:
            return  # Avoid division by zero

        labels = list(app_time.keys())
        sizes = list(app_time.values())

        # Assign colors based on whitelist status
        colors = [
            WHITELIST_COLOR if app_whitelist.get(app, False) else OTHER_COLOR
            for app in labels
        ]

        # Plot the pie chart
        wedges, texts, autotexts = self.ax.pie(
            sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors
        )

        # Adjust text properties
        for text in texts + autotexts:
            text.set_fontsize(12)

        self.ax.axis(
            "equal"
        )  # Equal aspect ratio ensures that pie is drawn as a circle.


class TimelineGraph(QMainWindow):
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Matplotlib Timeline View with Text in Segments")

        # Initialize a QWidget to host the matplotlib canvas
        widget = QWidget(self)
        self.setCentralWidget(widget)

        layout = QVBoxLayout(widget)

        # Create a Matplotlib figure and axis
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot(111)

        # Create the timeline
        self.plot_timeline(data)

        # Create canvas and add to layout
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

    def plot_timeline(self, data):
        # Starting point for drawing the segments on the timeline
        current_time = 0

        # Loop through the data and plot each app's time as a segment on the timeline
        for item in data:
            app_name = item["appName"].replace(".exe", "")
            time = item["time"]

            # Check if the app is whitelisted
            whitelisted = item.get("whitelisted", False)
            color = WHITELIST_COLOR if whitelisted else OTHER_COLOR

            # Draw the segment: use 'current_time' as the starting point for this segment
            self.ax.barh(
                0,
                time,
                left=current_time,
                height=0.5,
                color=color,
                label=app_name,
            )

            # Add the text label in the middle of the segment
            self.ax.text(
                current_time + time / 2,
                0,
                f"{app_name}\n({time}s)",
                ha="center",
                va="center",
                color="white",
            )

            # Update the current time to be the end of the last segment
            current_time += time

        # Set the labels and title
        self.ax.set_xlabel("Time (seconds)")
        self.ax.set_title("App Usage Timeline")

        # Set the y-axis to be constant, as we only need one horizontal line
        self.ax.set_ylim(-1, 1)
        self.ax.get_yaxis().set_visible(
            False
        )  # Hide the y-axis as it's not necessary here

        # Set the x-axis limit to ensure enough space for the timeline
        self.ax.set_xlim(
            0, current_time + 5
        )  # Adding some extra space at the end for visualization


class GraphicsStatsWindow(QDialog):
    def __init__(self, data=[{
        'appName': 'Code.exe', 'time': 3, 'whitelisted': False
    }]):
        super().__init__()

        self.setWindowTitle("Focus Mode Summary")

        # Initialize a QWidget to host the layouts
        #widget = QWidget(self)
        #self.setCentralWidget(widget)

        # Create a QVBoxLayout to stack all the graphs vertically
        self.layout = QVBoxLayout()

        # Create the individual graph views
        self.bar_graph = BarGraph(data)
        self.pie_graph = PieGraph(data)
        self.timeline_view = TimelineGraph(data)

        # Add each graph to the layout
        self.layout.addWidget(self.bar_graph)
        self.layout.addWidget(self.pie_graph)
        self.layout.addWidget(self.timeline_view)
        self.setLayout(self.layout)