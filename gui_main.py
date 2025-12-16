# gui_main.py

import sys
from PySide6.QtWidgets import QApplication
from gui_window import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    if sys.platform != "emscripten":
        sys.exit(app.exec())
    else:
        app.exec()


if __name__ == "__main__":
    main()
