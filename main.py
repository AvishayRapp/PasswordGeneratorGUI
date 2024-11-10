import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Generator')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # Label to display the current selected password length
        self.length_label = QLabel('Password Length: 16', self)
        layout.addWidget(self.length_label)

        # Slider to select the password length
        self.length_slider = QSlider(Qt.Horizontal, self)
        self.length_slider.setMinimum(8)
        self.length_slider.setMaximum(64)
        self.length_slider.setValue(16)
        self.length_slider.valueChanged.connect(self.update_label)
        layout.addWidget(self.length_slider)

        # Button to generate the password
        generate_button = QPushButton('Generate Password', self)
        generate_button.clicked.connect(self.generate_password)
        layout.addWidget(generate_button)

        self.setLayout(layout)

    def update_label(self, value):
        self.length_label.setText(f'Password Length: {value}')

    def generate_password(self):
        # Get the selected password length from the slider
        password_length = self.length_slider.value()

        # Define the characters to use in the password
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate a random password of the selected length
        password = ''.join(random.choice(characters) for _ in range(password_length))

        # Display the password in a messagebox
        self.show_password_messagebox(password)

    def show_password_messagebox(self, password):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Generated Password')
        msg_box.setText(f'Your password is:\n\n{password}')

        # Add a "Copy password to Clipboard" button
        copy_button = QPushButton('Copy password to Clipboard')
        copy_button.clicked.connect(lambda: self.copy_to_clipboard(password))
        msg_box.addButton(copy_button, QMessageBox.ActionRole)

        # Add an "OK" button
        msg_box.addButton(QMessageBox.Ok)

        # Adjust the width of the messagebox to fit the password
        msg_box.setStyleSheet("QLabel{min-width: 300px;}")

        msg_box.exec_()

    def copy_to_clipboard(self, password):
        clipboard = QApplication.clipboard()
        clipboard.setText(password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())