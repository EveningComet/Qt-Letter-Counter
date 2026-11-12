from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QProxyStyle

class CustomStyle(QProxyStyle):
    """
    Manages the custom theme for the program.
    """

    def __init__(self):
        super().__init__()

    def get_standard_palette(self) -> QPalette:
        palette = super().standardPalette()
        bckgrnd_clr = "#282A36"
        text_color  = "#F8F8F2" 

        palette.setColor(QPalette.ColorRole.Window, QColor(bckgrnd_clr))
        palette.setColor(QPalette.ColorRole.Base, bckgrnd_clr)
        palette.setColor(QPalette.ColorRole.Text, text_color)
        palette.setColor(QPalette.ColorRole.Highlight, "#CFCFDE")
        palette.setColor(QPalette.ColorRole.HighlightedText, "#6C664B")
        
        return palette