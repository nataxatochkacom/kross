# gui_memory.py

from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt


class MemoryTable(QTableWidget):
    def __init__(self, memory_size=4096):
        super().__init__(memory_size, 2)
        self.setHorizontalHeaderLabels(["Адрес", "Значение"])
        self.verticalHeader().setVisible(False)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setAlternatingRowColors(True)

    def update_memory(self, memory):
        for addr, value in enumerate(memory):
            addr_item = QTableWidgetItem(str(addr))
            value_item = QTableWidgetItem(str(value))

            addr_item.setTextAlignment(Qt.AlignCenter)
            value_item.setTextAlignment(Qt.AlignCenter)

            self.setItem(addr, 0, addr_item)
            self.setItem(addr, 1, value_item)
