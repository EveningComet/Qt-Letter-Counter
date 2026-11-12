# This file is what is used to make the program run
import sys

from PySide6.QtWidgets import QApplication
from components.main_window import MainWindow
from custom_style import CustomStyle


if __name__ == "__main__":
    _style = CustomStyle()
    app = QApplication(sys.argv)
    app.setStyle(_style)
    app.setPalette(_style.get_standard_palette())
    
    window = MainWindow()
    window.show()

    # The program reached this point without any problems,
    # so it may now run
    sys.exit(app.exec())