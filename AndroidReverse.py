# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AndroidReverse.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AndroidReversePanel(object):
    def setupUi(self, AndroidReversePanel):
        AndroidReversePanel.setObjectName("AndroidReversePanel")
        AndroidReversePanel.setEnabled(True)
        AndroidReversePanel.resize(812, 538)
        AndroidReversePanel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/sword.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AndroidReversePanel.setWindowIcon(icon)
        AndroidReversePanel.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.PanelLayout = QtWidgets.QWidget(AndroidReversePanel)
        self.PanelLayout.setObjectName("PanelLayout")
        self.PanelLayoutVerticalLayout = QtWidgets.QVBoxLayout(self.PanelLayout)
        self.PanelLayoutVerticalLayout.setObjectName("PanelLayoutVerticalLayout")
        self.DeviceSelect = QtWidgets.QHBoxLayout()
        self.DeviceSelect.setObjectName("DeviceSelect")
        self.DeviceList = QtWidgets.QComboBox(self.PanelLayout)
        self.DeviceList.setStyleSheet("height:20px;")
        self.DeviceList.setEditable(False)
        self.DeviceList.setCurrentText("")
        self.DeviceList.setObjectName("DeviceList")
        self.DeviceSelect.addWidget(self.DeviceList)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.DeviceSelect.addItem(spacerItem)
        self.PanelLayoutVerticalLayout.addLayout(self.DeviceSelect)
        self.PanelTabs = QtWidgets.QTabWidget(self.PanelLayout)
        self.PanelTabs.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}")
        self.PanelTabs.setIconSize(QtCore.QSize(20, 20))
        self.PanelTabs.setObjectName("PanelTabs")
        self.AndroidTab = ConsoleTab()
        self.AndroidTab.setObjectName("AndroidTab")
        self.AndroidTabGridLayout = QtWidgets.QGridLayout(self.AndroidTab)
        self.AndroidTabGridLayout.setObjectName("AndroidTabGridLayout")
        self.ActivityInput = QtWidgets.QLineEdit(self.AndroidTab)
        self.ActivityInput.setObjectName("ActivityInput")
        self.AndroidTabGridLayout.addWidget(self.ActivityInput, 4, 1, 1, 1)
        self.InfoButtons = QtWidgets.QHBoxLayout()
        self.InfoButtons.setObjectName("InfoButtons")
        self.GetAppInfo = QtWidgets.QPushButton(self.AndroidTab)
        self.GetAppInfo.setEnabled(True)
        self.GetAppInfo.setStyleSheet("")
        self.GetAppInfo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/activity.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GetAppInfo.setIcon(icon1)
        self.GetAppInfo.setIconSize(QtCore.QSize(20, 20))
        self.GetAppInfo.setObjectName("GetAppInfo")
        self.InfoButtons.addWidget(self.GetAppInfo)
        self.StartDebug = QtWidgets.QPushButton(self.AndroidTab)
        self.StartDebug.setEnabled(True)
        self.StartDebug.setStyleSheet("")
        self.StartDebug.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pic/debug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StartDebug.setIcon(icon2)
        self.StartDebug.setIconSize(QtCore.QSize(20, 20))
        self.StartDebug.setObjectName("StartDebug")
        self.InfoButtons.addWidget(self.StartDebug)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.InfoButtons.addItem(spacerItem1)
        self.LocalPort = QtWidgets.QLineEdit(self.AndroidTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LocalPort.sizePolicy().hasHeightForWidth())
        self.LocalPort.setSizePolicy(sizePolicy)
        self.LocalPort.setMaximumSize(QtCore.QSize(60, 16777215))
        self.LocalPort.setStyleSheet("height:20px;")
        self.LocalPort.setMaxLength(100)
        self.LocalPort.setObjectName("LocalPort")
        self.InfoButtons.addWidget(self.LocalPort)
        self.RemotePort = QtWidgets.QLineEdit(self.AndroidTab)
        self.RemotePort.setMaximumSize(QtCore.QSize(60, 16777215))
        self.RemotePort.setStyleSheet("height:20px;")
        self.RemotePort.setMaxLength(100)
        self.RemotePort.setObjectName("RemotePort")
        self.InfoButtons.addWidget(self.RemotePort)
        self.AdbForward = QtWidgets.QPushButton(self.AndroidTab)
        self.AdbForward.setEnabled(True)
        self.AdbForward.setStyleSheet("")
        self.AdbForward.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pic/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AdbForward.setIcon(icon3)
        self.AdbForward.setIconSize(QtCore.QSize(20, 20))
        self.AdbForward.setObjectName("AdbForward")
        self.InfoButtons.addWidget(self.AdbForward)
        self.AndroidTabGridLayout.addLayout(self.InfoButtons, 3, 1, 1, 1)
        self.AppInfoText = AndroidTextEdit(self.AndroidTab)
        self.AppInfoText.setEnabled(True)
        self.AppInfoText.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.AppInfoText.setToolTip("")
        self.AppInfoText.setStatusTip("")
        self.AppInfoText.setReadOnly(True)
        self.AppInfoText.setObjectName("AppInfoText")
        self.AndroidTabGridLayout.addWidget(self.AppInfoText, 5, 1, 1, 1)
        self.CommandInput = ShellCommandLineEdit(self.AndroidTab)
        self.CommandInput.setObjectName("CommandInput")
        self.AndroidTabGridLayout.addWidget(self.CommandInput, 6, 1, 1, 1)
        self.ActivityInput.raise_()
        self.CommandInput.raise_()
        self.AppInfoText.raise_()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("pic/android.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PanelTabs.addTab(self.AndroidTab, icon4, "")
        self.FridaTab = ConsoleTab()
        self.FridaTab.setObjectName("FridaTab")
        self.gridLayout = QtWidgets.QGridLayout(self.FridaTab)
        self.gridLayout.setObjectName("gridLayout")
        self.FridaTabPanelLayout = QtWidgets.QVBoxLayout()
        self.FridaTabPanelLayout.setObjectName("FridaTabPanelLayout")
        self.FridaButtonsLayout = QtWidgets.QGridLayout()
        self.FridaButtonsLayout.setObjectName("FridaButtonsLayout")
        self.FridaStop = QtWidgets.QPushButton(self.FridaTab)
        self.FridaStop.setStyleSheet("")
        self.FridaStop.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("pic/frida-stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FridaStop.setIcon(icon5)
        self.FridaStop.setIconSize(QtCore.QSize(20, 20))
        self.FridaStop.setObjectName("FridaStop")
        self.FridaButtonsLayout.addWidget(self.FridaStop, 0, 2, 1, 1)
        self.FridaDebug = QtWidgets.QPushButton(self.FridaTab)
        self.FridaDebug.setSizeIncrement(QtCore.QSize(1, 1))
        self.FridaDebug.setStyleSheet("")
        self.FridaDebug.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("pic/frida-debug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FridaDebug.setIcon(icon6)
        self.FridaDebug.setIconSize(QtCore.QSize(20, 20))
        self.FridaDebug.setObjectName("FridaDebug")
        self.FridaButtonsLayout.addWidget(self.FridaDebug, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.FridaButtonsLayout.addItem(spacerItem2, 0, 6, 1, 1)
        self.FridaAttachWay = QtWidgets.QRadioButton(self.FridaTab)
        self.FridaAttachWay.setChecked(False)
        self.FridaAttachWay.setObjectName("FridaAttachWay")
        self.FridaButtonsLayout.addWidget(self.FridaAttachWay, 0, 3, 1, 1)
        self.FridaPackageList = FridaPackageListComboBox(self.FridaTab)
        self.FridaPackageList.setMaximumSize(QtCore.QSize(150, 16777215))
        self.FridaPackageList.setStyleSheet("height:20px;\n"
"width:80px;")
        self.FridaPackageList.setObjectName("FridaPackageList")
        self.FridaButtonsLayout.addWidget(self.FridaPackageList, 0, 5, 1, 1)
        self.FridaStart = QtWidgets.QPushButton(self.FridaTab)
        self.FridaStart.setStyleSheet("")
        self.FridaStart.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("pic/frida-start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FridaStart.setIcon(icon7)
        self.FridaStart.setIconSize(QtCore.QSize(20, 20))
        self.FridaStart.setObjectName("FridaStart")
        self.FridaButtonsLayout.addWidget(self.FridaStart, 0, 0, 1, 1)
        self.FridaSpawnWay = QtWidgets.QRadioButton(self.FridaTab)
        self.FridaSpawnWay.setChecked(True)
        self.FridaSpawnWay.setObjectName("FridaSpawnWay")
        self.FridaButtonsLayout.addWidget(self.FridaSpawnWay, 0, 4, 1, 1)
        self.FridaTabPanelLayout.addLayout(self.FridaButtonsLayout)
        self.gridLayout.addLayout(self.FridaTabPanelLayout, 0, 0, 1, 1)
        self.FridaEditContainer = QtWidgets.QHBoxLayout()
        self.FridaEditContainer.setObjectName("FridaEditContainer")
        self.FridaEditPage = QtWebEngineWidgets.QWebEngineView(self.FridaTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FridaEditPage.sizePolicy().hasHeightForWidth())
        self.FridaEditPage.setSizePolicy(sizePolicy)
        self.FridaEditPage.setStyleSheet("border:1px;border-color:gray;border-style:solid;")
        self.FridaEditPage.setObjectName("FridaEditPage")
        self.FridaEditContainer.addWidget(self.FridaEditPage)
        self.FridaConsole = QtWidgets.QTextEdit(self.FridaTab)
        self.FridaConsole.setStyleSheet("")
        self.FridaConsole.setObjectName("FridaConsole")
        self.FridaEditContainer.addWidget(self.FridaConsole)
        self.gridLayout.addLayout(self.FridaEditContainer, 1, 0, 1, 1)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("pic/tag-r.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PanelTabs.addTab(self.FridaTab, icon8, "")
        self.PanelLayoutVerticalLayout.addWidget(self.PanelTabs)
        AndroidReversePanel.setCentralWidget(self.PanelLayout)
        self.menubar = QtWidgets.QMenuBar(AndroidReversePanel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuDDMS = QtWidgets.QMenu(self.menu)
        self.menuDDMS.setObjectName("menuDDMS")
        self.menuIDA = QtWidgets.QMenu(self.menu)
        self.menuIDA.setObjectName("menuIDA")
        self.menuFrida = QtWidgets.QMenu(self.menu)
        self.menuFrida.setObjectName("menuFrida")
        AndroidReversePanel.setMenuBar(self.menubar)
        self.SettingDDMS = QtWidgets.QAction(AndroidReversePanel)
        self.SettingDDMS.setObjectName("SettingDDMS")
        self.StartDDMS = QtWidgets.QAction(AndroidReversePanel)
        self.StartDDMS.setObjectName("StartDDMS")
        self.SettingIDAPath = QtWidgets.QAction(AndroidReversePanel)
        self.SettingIDAPath.setObjectName("SettingIDAPath")
        self.StartIDA = QtWidgets.QAction(AndroidReversePanel)
        self.StartIDA.setObjectName("StartIDA")
        self.SettingFridaScript = QtWidgets.QAction(AndroidReversePanel)
        self.SettingFridaScript.setObjectName("SettingFridaScript")
        self.SettingIDAServer = QtWidgets.QAction(AndroidReversePanel)
        self.SettingIDAServer.setObjectName("SettingIDAServer")
        self.StartIDAServer = QtWidgets.QAction(AndroidReversePanel)
        self.StartIDAServer.setObjectName("StartIDAServer")
        self.StartFridaServer = QtWidgets.QAction(AndroidReversePanel)
        self.StartFridaServer.setObjectName("StartFridaServer")
        self.menuDDMS.addAction(self.StartDDMS)
        self.menuDDMS.addSeparator()
        self.menuDDMS.addAction(self.SettingDDMS)
        self.menuIDA.addAction(self.StartIDA)
        self.menuIDA.addAction(self.StartIDAServer)
        self.menuIDA.addSeparator()
        self.menuIDA.addAction(self.SettingIDAPath)
        self.menuIDA.addAction(self.SettingIDAServer)
        self.menuFrida.addAction(self.StartFridaServer)
        self.menuFrida.addSeparator()
        self.menuFrida.addAction(self.SettingFridaScript)
        self.menu.addAction(self.menuDDMS.menuAction())
        self.menu.addAction(self.menuIDA.menuAction())
        self.menu.addAction(self.menuFrida.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(AndroidReversePanel)
        self.DeviceList.setCurrentIndex(-1)
        self.PanelTabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(AndroidReversePanel)

    def retranslateUi(self, AndroidReversePanel):
        _translate = QtCore.QCoreApplication.translate
        AndroidReversePanel.setWindowTitle(_translate("AndroidReversePanel", "Inteaf"))
        self.DeviceList.setPlaceholderText(_translate("AndroidReversePanel", "无连接设备"))
        self.ActivityInput.setPlaceholderText(_translate("AndroidReversePanel", "Debug Activity eg:package/.Activity"))
        self.GetAppInfo.setToolTip(_translate("AndroidReversePanel", "获取当前activity"))
        self.StartDebug.setToolTip(_translate("AndroidReversePanel", "启动调试"))
        self.LocalPort.setPlaceholderText(_translate("AndroidReversePanel", "本地端口"))
        self.RemotePort.setPlaceholderText(_translate("AndroidReversePanel", "手机端口"))
        self.AdbForward.setToolTip(_translate("AndroidReversePanel", "端口转发"))
        self.AppInfoText.setWhatsThis(_translate("AndroidReversePanel", "<html><head/><body><p><br/></p></body></html>"))
        self.CommandInput.setPlaceholderText(_translate("AndroidReversePanel", "ShellCommand"))
        self.PanelTabs.setTabText(self.PanelTabs.indexOf(self.AndroidTab), _translate("AndroidReversePanel", "Android"))
        self.FridaStop.setToolTip(_translate("AndroidReversePanel", "Stop"))
        self.FridaDebug.setToolTip(_translate("AndroidReversePanel", "Debug"))
        self.FridaAttachWay.setText(_translate("AndroidReversePanel", "Attach"))
        self.FridaPackageList.setPlaceholderText(_translate("AndroidReversePanel", "package"))
        self.FridaStart.setToolTip(_translate("AndroidReversePanel", "Start"))
        self.FridaSpawnWay.setText(_translate("AndroidReversePanel", "Spawn"))
        self.PanelTabs.setTabText(self.PanelTabs.indexOf(self.FridaTab), _translate("AndroidReversePanel", "Frida"))
        self.menu.setTitle(_translate("AndroidReversePanel", "设置"))
        self.menuDDMS.setTitle(_translate("AndroidReversePanel", "DDMS设置"))
        self.menuIDA.setTitle(_translate("AndroidReversePanel", "IDA设置"))
        self.menuFrida.setTitle(_translate("AndroidReversePanel", "Frida设置"))
        self.SettingDDMS.setText(_translate("AndroidReversePanel", "配置路径"))
        self.StartDDMS.setText(_translate("AndroidReversePanel", "启动"))
        self.SettingIDAPath.setText(_translate("AndroidReversePanel", "配置程序路径"))
        self.StartIDA.setText(_translate("AndroidReversePanel", "启动IDA"))
        self.SettingFridaScript.setText(_translate("AndroidReversePanel", "配置启动脚本"))
        self.SettingIDAServer.setText(_translate("AndroidReversePanel", "配置启动服务"))
        self.StartIDAServer.setText(_translate("AndroidReversePanel", "启动IDAServer"))
        self.StartFridaServer.setText(_translate("AndroidReversePanel", "启动FridaServer"))
from PyQt5 import QtWebEngineWidgets
from widget.AndroidTextEdit import AndroidTextEdit
from widget.ConsoleTab import ConsoleTab
from widget.FridaPackageListComboBox import FridaPackageListComboBox
from widget.ShellCommandLineEdit import ShellCommandLineEdit
