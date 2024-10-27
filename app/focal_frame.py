from typing import Tuple
from PySide6 import QtWidgets
from PySide6.QtWidgets import QHeaderView, QTableWidgetItem
from ui.window import Ui_MainWindow
from app.utils import calculate_angles, calculate_frames

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self) -> None:
        """Initialize the main window and set up the UI."""
        super().__init__()

        self.setWindowTitle("Focal Frame")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setVisible(False)

        self.setup_sensor_combo_box()

        self.add_values_to_table()

        self.ui.spinBox.valueChanged.connect(self.add_values_to_table)
        self.ui.comboBox.currentIndexChanged.connect(self.add_values_to_table)
        self.ui.doubleSpinBox.valueChanged.connect(self.add_values_to_table)


    def setup_sensor_combo_box(self) -> None:
        """Set up the sensor formats in the combo box."""
        sensor_formats = {
            "MF": "44 x 33",
            "FF": "36 x 24",
            "S35": "24.89 x 18.66",
            "MFT": "17.3 x 13",
            "S16": "12.5 x 7"
        }

        for sensor, dimensions in sensor_formats.items():
            self.ui.comboBox.addItem(f"{sensor}: {dimensions}")


    def add_values_to_table(self) -> None:
        """Add calculated values to the table based on current inputs."""
        focal_length, (sensor_width, sensor_height), distance = self.get_all_values()
        angle_horizontal_rad, angle_vertical_rad, angle_horizontal_deg, angle_vertical_deg = calculate_angles(focal_length, sensor_width, sensor_height)
        frame_width, frame_height = calculate_frames(angle_horizontal_rad, angle_vertical_rad, distance)
        
        self.ui.tableWidget.setRowCount(0)
        row_position = 0
        self.ui.tableWidget.insertRow(row_position)

        self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(f"{angle_horizontal_deg:.2f}"))
        self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(f"{angle_vertical_deg:.2f}"))
        self.ui.tableWidget.setItem(row_position, 2, QTableWidgetItem(f"{frame_width:.2f}"))
        self.ui.tableWidget.setItem(row_position, 3, QTableWidgetItem(f"{frame_height:.2f}"))


    def get_focal_length(self) -> int:
        """Retrieve the focal length from the spin box."""
        return self.ui.spinBox.value()


    def get_sensor_size(self) -> Tuple[float, float]:
        """Retrieve the sensor width and height from the combo box."""
        sensor_text = self.ui.comboBox.currentText()
        sensor_values = sensor_text.split(":")[1].strip()
        width, height = map(float, sensor_values.split(" x "))
        return width, height


    def get_distance(self) -> float:
        """Retrieve the distance from the double spin box."""
        return self.ui.doubleSpinBox.value()


    def get_all_values(self) -> Tuple[int, Tuple[float, float], float]:
        """Retrieve all relevant values as a tuple."""
        focal_length = self.get_focal_length()
        width, height = self.get_sensor_size()
        distance = self.get_distance()
        return focal_length, (width, height), distance
