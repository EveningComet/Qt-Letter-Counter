from PySide6.QtWidgets import QTextEdit

class TextEntry(QTextEdit):
    """
    Responsible for storing the user's input.
    """

    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Please enter text...")
        self.setContentsMargins(10, 10, 10, 10)
