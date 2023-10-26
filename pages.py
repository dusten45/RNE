from layout import Layouts
from button import Button
from PyQt6.QtWidgets import QSizePolicy, QGridLayout

class Pages(Layouts):
    def __init__(self):
        super().__init__()

        btnFilePath = Button(lambda: self.changePage(0), '')
        btnData = Button(lambda: self.changePage(1), '')
        btnInfo = Button(lambda: self.changePage(2), '')
        btnHome = Button(lambda: self.changePage(3), '')

        btnFilePath.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        btnData.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        btnInfo.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        btnHome.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.pgSide = QGridLayout()
        self.pgSide.addWidget(btnFilePath, 0, 0)
        self.pgSide.addWidget(btnData, 1, 0)
        self.pgSide.addWidget(btnInfo, 2, 0)
        self.pgSide.addWidget(btnHome, 3, 0)

        self.changePage(3)

    def changePage(self, page):
        layout = QGridLayout()
        layout.addLayout(self.pgSide, 0, 0)

        if page == 0:
            layout.addLayout(self.pgFilePath, 0, 1)

        elif page == 1:
            layout.addLayout(self.pgData, 0, 1)

        elif page == 2:
            layout.addLayout(self.pgInfo, 0, 1)

        else:
            layout.addLayout(self.pgHome, 0, 1)

        self.setLayout(layout)