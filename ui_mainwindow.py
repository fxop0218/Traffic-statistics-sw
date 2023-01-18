# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(
            "background-color: rgb(71, 71, 71);\n" 'font: 8pt "MS Shell Dlg 2";'
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.leUsername = QLineEdit(self.centralwidget)
        self.leUsername.setObjectName("leUsername")
        self.leUsername.setMaximumSize(QSize(500, 25))

        self.verticalLayout.addWidget(self.leUsername)

        self.lePassword = QLineEdit(self.centralwidget)
        self.lePassword.setObjectName("lePassword")
        self.lePassword.setMaximumSize(QSize(500, 25))
        self.lePassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.lePassword)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bRegister = QPushButton(self.centralwidget)
        self.bRegister.setObjectName("bRegister")
        self.bRegister.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.bRegister)

        self.bLog = QPushButton(self.centralwidget)
        self.bLog.setObjectName("bLog")
        self.bLog.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.bLog)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 19))
        self.menuMain = QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.leUsername.setText("")
        self.leUsername.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Username", None)
        )
        self.lePassword.setText("")
        self.lePassword.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Password", None)
        )
        self.bRegister.setText(
            QCoreApplication.translate("MainWindow", "Registger", None)
        )
        self.bLog.setText(QCoreApplication.translate("MainWindow", "Log", None))
        self.menuMain.setTitle(QCoreApplication.translate("MainWindow", "Main", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))

    # retranslateUi
