# gui_window.py

from PySide6.QtWidgets import (
    QWidget, QTextEdit, QPushButton,
    QVBoxLayout, QMessageBox, QLabel
)

from gui_runner import run_program
from gui_memory import MemoryTable


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("УВМ — GUI версия")
        self.resize(900, 700)

        self.editor = QTextEdit()
        self.editor.setPlaceholderText(
            "; Введите программу на ассемблере\n"
            "LOAD_CONST 0, 10\n"
            "LOAD_CONST 1, 0\n"
        )

        self.run_button = QPushButton("Ассемблировать и запустить")
        self.run_button.clicked.connect(self.on_run)

        self.memory_label = QLabel("Дамп памяти:")

        self.memory_table = MemoryTable()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Программа на ассемблере:"))
        layout.addWidget(self.editor)
        layout.addWidget(self.run_button)
        layout.addWidget(self.memory_label)
        layout.addWidget(self.memory_table)

        self.setLayout(layout)

    def on_run(self):
        source = self.editor.toPlainText()

        try:
            memory = run_program(source)
            self.memory_table.update_memory(memory)
        except Exception as e:
            QMessageBox.critical(
                self,
                "Ошибка",
                str(e)
            )
