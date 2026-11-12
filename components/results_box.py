from PySide6.QtGui import QFont
from PySide6.QtWidgets import QTextEdit

class ResultsBox(QTextEdit):
    """
    Responsible for displaying the results of the user's input.
    """

    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setPlaceholderText("Waiting to receive text")
        self.setContentsMargins(10, 10, 10, 10)
        self.setFontWeight(QFont.Bold)


    def display_results(self, results: str) -> None:
        """
        Displays the passed results to the user.
        """

        self.setText(results)