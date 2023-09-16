import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
import math
import matplotlib.pyplot as plt
import numpy as np

class QuadraticSolverApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create widgets
        self.label_a = QLabel('Enter coefficient a:')
        self.input_a = QLineEdit()

        self.label_b = QLabel('Enter coefficient b:')
        self.input_b = QLineEdit()

        self.label_c = QLabel('Enter coefficient c:')
        self.input_c = QLineEdit()

        self.solve_button = QPushButton('Solve Quadratic Equation')

        # Connect the button click event to the solver function
        self.solve_button.clicked.connect(self.solveQuadratic)

        # Create label to display the quadratic equation
        self.label_equation = QLabel()

        # Set the quadratic equation label text
        self.label_equation.setText('ax^2 + bx + c = 0')

        # Set the size of the window
        self.setGeometry(100, 100, 400, 400)  # (x position, y position, width, height)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_equation)  # Add the label here
        self.label_equation.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_a)
        layout.addWidget(self.input_a)
        layout.addWidget(self.label_b)
        layout.addWidget(self.input_b)
        layout.addWidget(self.label_c)
        layout.addWidget(self.input_c)
        
        layout.addWidget(self.solve_button)

        self.setLayout(layout)


    def solveQuadratic(self):
        a = float(self.input_a.text())
        b = float(self.input_b.text())
        c = float(self.input_c.text())

        solutions = self.solve_quadratic(a, b, c)
        x1 = None
        x2 = None  # Define x1 and x2 here to avoid UnboundLocalError

        if solutions is not None:
            if isinstance(solutions, tuple):
                x1, x2 = solutions
                print(f"The solutions are x1 = {x1} and x2 = {x2}")

                # Generate x-values for each quadrant
                x_values_quad1 = np.linspace(-10, x1, 100)
                x_values_quad2 = np.linspace(x1, x2, 100)
                x_values_quad3 = np.linspace(x2, 10, 100)

                # Calculate corresponding y-values using the quadratic function for each quadrant
                y_quad1 = a * x_values_quad1**2 + b * x_values_quad1 + c
                y_quad2 = a * x_values_quad2**2 + b * x_values_quad2 + c
                y_quad3 = a * x_values_quad3**2 + b * x_values_quad3 + c

                # Create the plot of the quadratic function
                plt.plot(x_values_quad1, y_quad1, label=f'{a}x^2 + {b}x + {c}', color='blue')
                plt.plot(x_values_quad2, y_quad2, color='blue')
                plt.plot(x_values_quad3, y_quad3, color='blue')

                # Mark the solutions
                plt.scatter([x1, x2], [0, 0], color='red', label='Solutions')
                
                # Add text annotations for solutions
                plt.text(x1, 0.5, f'x1 = {x1}', color='green', fontsize=10, ha='center')
                plt.text(x2, 0.5, f'x2 = {x2}', color='green', fontsize=10, ha='center')
            else:
                print(f"The solution is x = {solutions}")

                # Generate x-values for each quadrant
                x_values_quad1 = np.linspace(-10, solutions, 100)
                x_values_quad4 = np.linspace(solutions, 10, 100)

                # Calculate corresponding y-values using the quadratic function for each quadrant
                y_quad1 = a * x_values_quad1**2 + b * x_values_quad1 + c
                y_quad4 = a * x_values_quad4**2 + b * x_values_quad4 + c

                # Create the plot of the quadratic function
                plt.plot(x_values_quad1, y_quad1, label=f'{a}x^2 + {b}x + {c}', color='blue')
                plt.plot(x_values_quad4, y_quad4, color='blue')

                # Mark the solution
                plt.scatter([solutions], [0], color='red', label='Solution')
                
                # Add text annotation for solution
                plt.text(solutions, 0.5, f'x = {solutions}', color='green', fontsize=10, ha='center')

            plt.xlabel('x')
            plt.ylabel('f(x)')
            if x1 is not None and x2 is not None:
                plt.title(f'Solutions: x1 = {x1}, x2 = {x2} | {a}x^2 + {b}x + {c}')
            else:
                plt.title(f'Solution: x = {solutions} | {a}x^2 + {b}x + {c}')
            
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.legend()
            plt.grid(True)
            plt.show()
        else:
            QMessageBox.warning(self, "No Solutions", "No real solutions")

    def solve_quadratic(self, a, b, c):
        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            return x1, x2
        elif discriminant == 0:
            x = -b / (2*a)
            return x
        else:
            return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QuadraticSolverApp()
    ex.setWindowTitle('Quadratic Solver')
    ex.show()
    sys.exit(app.exec_())
