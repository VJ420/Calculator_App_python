import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, QLabel, QSlider
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt

class VisualizationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Visualization')
        self.setGeometry(400, 100, 600, 600)

        self.layout = QVBoxLayout()

        shapes = ["Circle", "Square", "Rectangle", "Quadrilateral"]

        for shape in shapes:
            button = QPushButton(shape)
            button.clicked.connect(lambda _, s=shape: self.draw_shape(s))
            button.setStyleSheet('font-size: 24px; padding: 10px; margin: 5px; border-radius: 5px; background-color: #FF5733; color: white;')
            self.layout.addWidget(button)

        self.setLayout(self.layout)

    def draw_shape(self, shape):
        plt.close()
        fig, ax = plt.subplots()

        if shape == "Circle":
            circle = plt.Circle((0.5, 0.5), 0.4, color='r')
            ax.add_artist(circle)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.set_aspect('equal', adjustable='box')
            ax.set_title("Circle")

        elif shape == "Square":
            square = plt.Rectangle((0.2, 0.2), 0.6, 0.6, color='b')
            ax.add_artist(square)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.set_aspect('equal', adjustable='box')
            ax.set_title("Square")

        elif shape == "Rectangle":
            rectangle = plt.Rectangle((0.1, 0.3), 0.8, 0.4, color='g')
            ax.add_artist(rectangle)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.set_aspect('equal', adjustable='box')
            ax.set_title("Rectangle")

        elif shape == "Quadrilateral":
            x = [0.2, 0.4, 0.6, 0.8]
            y = [0.2, 0.6, 0.8, 0.4]
            quadrilateral = plt.Polygon(list(zip(x, y)), color='y')
            ax.add_artist(quadrilateral)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.set_aspect('equal', adjustable='box')
            ax.set_title("Quadrilateral")

        ax.axis('off')
        plt.show()

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(400, 100, 600, 600)

        self.layout = QVBoxLayout()
        self.result_display = QLineEdit()
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setStyleSheet('font-size: 30px; padding: 10px; margin-bottom: 10px; border: 2px solid black; border-radius: 5px; background-color: black; color: white;')
        self.layout.addWidget(self.result_display)

        self.add_buttons()

        self.slider_layout = QHBoxLayout()
        self.slider_label = QLabel("Slide for basic visualization: ")
        self.slider_layout.addWidget(self.slider_label)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setMinimum(0)
        self.slider.setMaximum(1)
        self.slider.valueChanged.connect(self.show_visualization_window)
        self.slider_layout.addWidget(self.slider)
        self.layout.addLayout(self.slider_layout)

        self.setLayout(self.layout)

    def add_buttons(self):
        button_grid = [
            ['sin', 'cos', 'tan', '(', ')'],
            ['7', '8', '9', '/', '√'],
            ['4', '5', '6', '*', 'log'],
            ['1', '2', '3', '-', 'exp'],
            ['C', '0', '=', '+', 'Clear']
        ]

        for row in button_grid:
            h_layout = QHBoxLayout()
            for text in row:
                button = QPushButton(text)
                button.setStyleSheet('padding: 15px; margin: 10px; font-size: 24px; border-radius: 5px; background-color: #FF5733; color: white; border: 2px solid black;')
                button.clicked.connect(lambda _, t=text: self.on_button_clicked(t))
                h_layout.addWidget(button)
            self.layout.addLayout(h_layout)

    def on_button_clicked(self, text):
        if text == '=':
            self.calculate_result()
        elif text == 'C':
            self.clear_display()
        elif text == 'Clear':
            self.clear_history()
        else:
            self.result_display.setText(self.result_display.text() + text)

    def clear_display(self):
        self.result_display.clear()

    def clear_history(self):
        self.result_display.clear()

    def calculate_result(self):
        try:
            result = eval(self.result_display.text())
            self.result_display.setText(str(result))
        except Exception as e:
            print("Error:", e)

    def show_visualization_window(self, value):
        if value == 1:
            self.vis_window = VisualizationWindow()
            self.vis_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
