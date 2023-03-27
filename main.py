# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PCcleaningutilitygui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4


from PyQt5 import QtCore, QtGui, QtWidgets #GUI
from time import sleep #Delays
from pyautogui import typewrite, press, hotkey #Macros
from os import startfile #opening app


waitTime = 2.5



#Methods
def openDiskClean():
	print("\nOpening disk cleanup")
	startfile("C:\WINDOWS\system32\cleanmgr.exe")
	print("Opened disk cleanup\nClean any junk files")

def openDefrag():
	print("\nOpening defrag")
	startfile("C:\WINDOWS\system32\dfrgui.exe")
	print("Opened defrag\nDefrag / retrim HDDs / SSDs")

def openUpdate():
	print("\nOpening Windows Update")
	press("win")
	sleep(waitTime)
	typewrite("Windows Update")
	sleep(waitTime)
	press("enter")
	print("Opened Windows Update\nInstall updates, including optional ones")

def activateUltPower():
	print("\nOpening cmd")
	startfile("C:\WINDOWS\system32\cmd.exe")
	print("Opened cmd\nType 'powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61'\nChange the power plan using the 'Power Plan' button")

def openPowerPlan():
	print("\nOpening power plan settings")
	press("win")
	sleep(waitTime)
	typewrite("Choose a power plan")
	sleep(waitTime)
	press("enter")
	print("Opened power plan settings\nChange power plan as needed")

def openCrystalDiskInfo():
	print("\nOpening CrystalDiskInfo")
	startfile("CrystalDiskInfoPortable\CrystalDiskInfoPortable.exe")
	print("Opened CrystalDiskInfo\nCheck storage health")

def runSfc():
	print("\nOpening cmd")
	startfile("C:\WINDOWS\system32\cmd.exe")
	print("Opened cmd\nType 'sfc /scannow'\nRepair system files")

def runMemtest():
	print("\nOpening Windows Memory Diagnostic")
	startfile("C:\WINDOWS\system32\MdSched.exe")
	print("Opened Windows Memory Diagnostic\nFor results, open event viewer\nRight-click on 'System' under 'Windows Logs'\nPress find\nType: 'MemoryDiagnostics-Results'")

def runFurmark():
	print("\nOpening Furmark")
	startfile("FurMarkPortable\FurMark.exe")
	print("Opened Furmark\nRun the highest resolution benchmark possible")

def runCinebench():
	print("\nOpening Cinebench R23")
	startfile("CinebenchPortable\Cinebench.exe")
	print("Opened Cinebench R23\nRun benchmarks")

def openAnim():
	print("\nOpening regedit")
	startfile("C:\WINDOWS\\regedit.exe")
	print("Opened regedit\n'Go to Computer\HKEY_CURRENT_USER\Control Panel\Desktop'\nFind 'MenuShowDelay\nSet value to '200'\nRestart computer")

def openHWInfo():
	print("\nOpening HWInfo64")
	startfile("HardwareInfoPortable\HWiNFO64.exe")
	print("Opened HWInfo 64\nCheck any hardware stats")

def	openStartupApps():
	print("\nOpening task manager")
	hotkey("ctrl", "shift", "esc")
	print("Opened task manager\nGo to startup tab and disable unwanted apps")

def openMsConfig():
	print("\nOpening System Configuration")
	startfile("C:\WINDOWS\system32\msconfig.exe")
	print("Opened System Configuration\nEnsure 'Normal Startup' is selected\nSwitch to 'Boot' tab\nRemove any unwanted OS'")

def openProgramUninstaller():
	print("\nOpening uninstaller")
	press("win")
	sleep(waitTime)
	typewrite("Add or remove programs")
	sleep(waitTime)
	press("enter")
	print("Opened uninstaller\nUninstall unwanted apps")


class Ui_screen(object):
    def setupUi(self, screen):
        screen.setObjectName("screen")
        screen.setWindowModality(QtCore.Qt.NonModal)
        screen.setEnabled(True)
        screen.resize(625, 610)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        screen.setPalette(palette)
        screen.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(screen)
        self.centralwidget.setObjectName("centralwidget")
        self.warning = QtWidgets.QLabel(self.centralwidget)
        self.warning.setGeometry(QtCore.QRect(40, 570, 551, 16))
        self.warning.setScaledContents(False)
        self.warning.setAlignment(QtCore.Qt.AlignCenter)
        self.warning.setObjectName("warning")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 601, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.btnGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.btnGrid.setContentsMargins(0, 0, 0, 0)
        self.btnGrid.setObjectName("btnGrid")
        self.PowerPlanBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PowerPlanBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #333333;\n"
"    border-radius: 17px;\n"
"    padding: 10px 20px;\n"
"    font-size: 11px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"")
        self.PowerPlanBtn.setObjectName("PowerPlanBtn")
        self.btnGrid.addWidget(self.PowerPlanBtn, 1, 1, 1, 1)
        self.CrystalDiskInfoBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CrystalDiskInfoBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #333333;\n"
"    border-radius: 17px;\n"
"    padding: 10px 20px;\n"
"    font-size: 11px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"")
        self.CrystalDiskInfoBtn.setObjectName("CrystalDiskInfoBtn")
        self.btnGrid.addWidget(self.CrystalDiskInfoBtn, 1, 2, 1, 1)
        self.sfcBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sfcBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #333333;\n"
"    border-radius: 17px;\n"
"    padding: 10px 20px;\n"
"    font-size: 11px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"")
        self.sfcBtn.setObjectName("sfcBtn")
        self.btnGrid.addWidget(self.sfcBtn, 2, 0, 1, 1)
        self.FurmarkBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.FurmarkBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #333333;\n"
"    border-radius: 17px;\n"
"    padding: 10px 20px;\n"
"    font-size: 11px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"")
        self.FurmarkBtn.setObjectName("FurmarkBtn")
        self.btnGrid.addWidget(self.FurmarkBtn, 2, 2, 1, 1)
        self.SysConfigBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SysConfigBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #333333;\n"
"    border-radius: 17px;\n"
"    padding: 10px 20px;\n"
"    font-size: 11px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"")
        self.SysConfigBtn.setObjectName("SysConfigBtn")
        self.btnGrid.addWidget(self.SysConfigBtn, 4, 0, 1, 1)
        self.CinebenchBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CinebenchBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #333333;\n"
"    border-radius: 17px;\n"
"    padding: 10px 20px;\n"
"    font-size: 11px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"")
        self.CinebenchBtn.setObjectName("CinebenchBtn")
        self.btnGrid.addWidget(self.CinebenchBtn, 3, 0, 1, 1)
        self.DefragBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.DefragBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #333333;\n"
"    border-radius: 17px;\n"
"    padding: 10px 20px;\n"
"    font-size: 11px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"")
        self.DefragBtn.setObjectName("DefragBtn")
        self.btnGrid.addWidget(self.DefragBtn, 0, 1, 1, 1)
        self.AnimationBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.AnimationBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #333333;\n"
"    border-radius: 17px;\n"
"    padding: 10px 20px;\n"
"    font-size: 11px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"")
        self.AnimationBtn.setObjectName("AnimationBtn")
        self.btnGrid.addWidget(self.AnimationBtn, 3, 1, 1, 1)
        self.UltPowerPlanBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.UltPowerPlanBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #333333;\n"
"    border-radius: 17px;\n"
"    padding: 10px 20px;\n"
"    font-size: 11px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"")
        self.UltPowerPlanBtn.setObjectName("UltPowerPlanBtn")
        self.btnGrid.addWidget(self.UltPowerPlanBtn, 1, 0, 1, 1)
        self.memtestBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.memtestBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #333333;\n"
"    border-radius: 17px;\n"
"    padding: 10px 20px;\n"
"    font-size: 11px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"")
        self.memtestBtn.setObjectName("memtestBtn")
        self.btnGrid.addWidget(self.memtestBtn, 2, 1, 1, 1)
        self.WindowsUpdateBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.WindowsUpdateBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #333333;\n"
"    border-radius: 17px;\n"
"    padding: 10px 20px;\n"
"    font-size: 11px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"")
        self.WindowsUpdateBtn.setObjectName("WindowsUpdateBtn")
        self.btnGrid.addWidget(self.WindowsUpdateBtn, 0, 2, 1, 1)
        self.HWInfoBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.HWInfoBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #333333;\n"
"    border-radius: 17px;\n"
"    padding: 10px 20px;\n"
"    font-size: 11px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"")
        self.HWInfoBtn.setObjectName("HWInfoBtn")
        self.btnGrid.addWidget(self.HWInfoBtn, 3, 2, 1, 1)
        self.DiskCleanBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.DiskCleanBtn.setPalette(palette)
        self.DiskCleanBtn.setMouseTracking(False)
        self.DiskCleanBtn.setAutoFillBackground(False)
        self.DiskCleanBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #333333;\n"
"    border-radius: 17px;\n"
"    padding: 10px 20px;\n"
"    font-size: 11px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"")
        self.DiskCleanBtn.setCheckable(False)
        self.DiskCleanBtn.setAutoDefault(False)
        self.DiskCleanBtn.setDefault(False)
        self.DiskCleanBtn.setFlat(False)
        self.DiskCleanBtn.setObjectName("DiskCleanBtn")
        self.btnGrid.addWidget(self.DiskCleanBtn, 0, 0, 1, 1)
        self.UninstallAppsBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.UninstallAppsBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #333333;\n"
"    border-radius: 17px;\n"
"    padding: 10px 20px;\n"
"    font-size: 11px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"")
        self.UninstallAppsBtn.setObjectName("UninstallAppsBtn")
        self.btnGrid.addWidget(self.UninstallAppsBtn, 4, 2, 1, 1)
        self.StartupApps = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.StartupApps.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #333333;\n"
"    border-radius: 17px;\n"
"    padding: 10px 20px;\n"
"    font-size: 11px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"")
        self.StartupApps.setObjectName("StartupApps")
        self.btnGrid.addWidget(self.StartupApps, 4, 1, 1, 1)
        screen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(screen)
        self.statusbar.setObjectName("statusbar")
        screen.setStatusBar(self.statusbar)

        self.retranslateUi(screen)
        self.DiskCleanBtn.clicked.connect(openDiskClean)
        self.DefragBtn.clicked.connect(openDefrag)
        self.WindowsUpdateBtn.clicked.connect(openUpdate)
        self.UltPowerPlanBtn.clicked.connect(activateUltPower)
        self.PowerPlanBtn.clicked.connect(openPowerPlan)
        self.CrystalDiskInfoBtn.clicked.connect(openCrystalDiskInfo)
        self.sfcBtn.clicked.connect(runSfc)
        self.memtestBtn.clicked.connect(runMemtest)
        self.FurmarkBtn.clicked.connect(runFurmark)
        self.CinebenchBtn.clicked.connect(runCinebench)
        self.AnimationBtn.clicked.connect(openAnim)
        self.HWInfoBtn.clicked.connect(openHWInfo)
        self.SysConfigBtn.clicked.connect(openMsConfig)
        self.StartupApps.clicked.connect(openStartupApps)
        self.UninstallAppsBtn.clicked.connect(openProgramUninstaller)
        QtCore.QMetaObject.connectSlotsByName(screen)
        screen.setTabOrder(self.DiskCleanBtn, self.DefragBtn)
        screen.setTabOrder(self.DefragBtn, self.WindowsUpdateBtn)
        screen.setTabOrder(self.WindowsUpdateBtn, self.UltPowerPlanBtn)
        screen.setTabOrder(self.UltPowerPlanBtn, self.PowerPlanBtn)
        screen.setTabOrder(self.PowerPlanBtn, self.CrystalDiskInfoBtn)
        screen.setTabOrder(self.CrystalDiskInfoBtn, self.sfcBtn)
        screen.setTabOrder(self.sfcBtn, self.memtestBtn)
        screen.setTabOrder(self.memtestBtn, self.FurmarkBtn)
        screen.setTabOrder(self.FurmarkBtn, self.CinebenchBtn)
        screen.setTabOrder(self.CinebenchBtn, self.AnimationBtn)
        screen.setTabOrder(self.AnimationBtn, self.HWInfoBtn)
        screen.setTabOrder(self.HWInfoBtn, self.SysConfigBtn)

    def retranslateUi(self, screen):
        _translate = QtCore.QCoreApplication.translate
        screen.setWindowTitle(_translate("screen", "PC Cleaning Utility (Custom made)"))
        self.warning.setText(_translate("screen", "Created by 3XAY. This software is not responsible for any harm caused to any computers."))
        self.PowerPlanBtn.setText(_translate("screen", "Power Plan"))
        self.CrystalDiskInfoBtn.setText(_translate("screen", "CrystalDiskInfo"))
        self.sfcBtn.setText(_translate("screen", "sfc"))
        self.FurmarkBtn.setText(_translate("screen", "FurMark"))
        self.SysConfigBtn.setText(_translate("screen", "Sys config"))
        self.CinebenchBtn.setText(_translate("screen", "Cinebench"))
        self.DefragBtn.setText(_translate("screen", "Defrag"))
        self.AnimationBtn.setText(_translate("screen", "Animation"))
        self.UltPowerPlanBtn.setText(_translate("screen", "Ultimate Power Plan"))
        self.memtestBtn.setText(_translate("screen", "memtest"))
        self.WindowsUpdateBtn.setText(_translate("screen", "Windows Update"))
        self.HWInfoBtn.setText(_translate("screen", "HWInfo"))
        self.DiskCleanBtn.setText(_translate("screen", "Disk Clean"))
        self.UninstallAppsBtn.setText(_translate("screen", "Uninstall apps"))
        self.StartupApps.setText(_translate("screen", "Startup Apps"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen = QtWidgets.QMainWindow()
    ui = Ui_screen()
    ui.setupUi(screen)
    screen.show()
    sys.exit(app.exec_())
