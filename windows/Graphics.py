import sys
from collections import defaultdict

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

WHITELIST_COLOR = "#ffffff"
OTHER_COLOR = "#0000000"


class BarGraph(QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.setWindowTitle("App Time Totals")

        layout = QVBoxLayout(self)

        # Create a Matplotlib figure and axis
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)

        # Create the timeline
        self.plot_timeline(data)

        # Create canvas and add to layout
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

    def plot_timeline(self, data):
        # Calculate total time per app using a defaultdict
        app_time = defaultdict(int)
        for item in data:
            app_time[item["appName"].replace(".exe", "")] += item["time"]

        # Prepare data for plotting
        apps = list(app_time.keys())
        total_times = list(app_time.values())

        # Create a timeline as a vertical bar graph
        bar_width = 0.4
        x_pos = range(len(apps))  # Set x positions for each app

        # Plot the bars for each app
        self.ax.bar(x_pos, total_times, width=bar_width)

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
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)

        # Create the Pie chart
        self.plot_pie_chart(data)

        # Create canvas and add to layout
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

    def plot_pie_chart(self, data):
        # Aggregate total time per app
        app_time = {}
        for item in data:
            app_name = item["appName"].replace(".exe", "")
            app_time[app_name] = app_time.get(app_name, 0) + item["time"]

        total_time = sum(app_time.values())  # Total duration for all apps
        if total_time == 0:
            return  # Avoid division by zero

        labels = app_time.keys()
        sizes = app_time.values()
        colors = plt.cm.Paired.colors[: len(sizes)]  # Generate distinct colors

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


class TimelineGraph(QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.setWindowTitle("App Timeline View")

        layout = QVBoxLayout(self)

        # Create a Matplotlib figure and axis
        self.fig = Figure()
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

            # Draw the segment: use 'current_time' as the starting point for this segment
            self.ax.barh(0, time, left=current_time, height=0.5, label=app_name)

            # Add the text label in the middle of the segment
            self.ax.text(
                current_time + time / 2,
                0,
                app_name,
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


class GraphicsStatsWindow(QMainWindow):
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Focus Mode Summary")
        self.setStatusBar(None)

        # Initialize a QWidget to host the layouts
        widget = QWidget(self)
        self.setCentralWidget(widget)

        # Create a QVBoxLayout to stack all the graphs vertically
        layout = QVBoxLayout(widget)

        # Create the individual graph views
        self.bar_graph = BarGraph(data)
        self.pie_graph = PieGraph(data)
        self.timeline_view = TimelineGraph(data)

        # Add each graph to the layout
        layout.addWidget(self.bar_graph)
        layout.addWidget(self.pie_graph)
        layout.addWidget(self.timeline_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Sample Data (App usage with timestamps)
    sample_data = [
        {"appName": "Code.exe", "time": 7},
        {"appName": "firefox.exe", "time": 12},
        {"appName": "Code.exe", "time": 10},
        {"appName": "chrome.exe", "time": 8},
        {"appName": "Code.exe", "time": 5},
    ]

    window = GraphicsStatsWindow(sample_data)
    window.show()
    sys.exit(app.exec_())
