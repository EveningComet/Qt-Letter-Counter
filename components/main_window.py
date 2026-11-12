from PySide6.QtWidgets import (
        QVBoxLayout, QLabel, QMainWindow, QWidget
    )

from components.results_box import ResultsBox
from components.text_entry import TextEntry

class MainWindow(QMainWindow):
    """
    The component responsible for displaying the program to the user.
    """

    WINDOW_TITLE = "Qt Letter Counter"
    ENGLISH_ALPHABET = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
        "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
        "W", "X", "Y", "Z"
    ]


    def __init__(self):
        super().__init__()

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setMinimumSize(480, 480)

        central_layout = QVBoxLayout()
        central_layout.setSpacing(10)
        self.text_entry  = TextEntry()
        self.results_box = ResultsBox()
        central_layout.addWidget(self.text_entry)
        central_layout.addWidget(self.results_box)

        self.text_entry.textChanged.connect(self._on_text_changed)

        central_widget = QWidget()
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)
        
        print("main_window :: Properly initialized")

    def _on_text_changed(self) -> None:
        """
        When the text changes within the entry, pass that
        information along to the results. It will display
        all the letters that appear.
        """

        user_entry = self.text_entry.toPlainText().strip()
        if user_entry == "":
            self.results_box.setText("")
            print("main_window :: text_entry is empty. Doing nothing.")
        
        else:
            letters_and_count = {}
            for letter in self.ENGLISH_ALPHABET:
                letters_and_count[letter] = 0
            for user_letter in user_entry:
                for letter in self.ENGLISH_ALPHABET:
                    if letter.lower() == user_letter.lower():
                        letters_and_count[letter] += 1

            result = ""
            for letter in letters_and_count.keys():
                if letters_and_count[letter] != 0:
                    result += "%s: %s\n" % (
                        letter, letters_and_count[letter]
                    )

            # Tell the results to display
            self.results_box.display_results(result)