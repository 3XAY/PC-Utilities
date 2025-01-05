# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PC-UtilitiesGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.11


from PyQt5 import QtCore, QtGui, QtWidgets
from os import startfile, system #opening apps / running commands
import winreg, subprocess

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
	system("C:\Windows\System32\control.exe /name Microsoft.WindowsUpdate")
	print("Opened Windows Update\nInstall updates, including optional ones")

def activateUltPower():
	print("\nRunning powercfg command")
	system("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
	print("\nRan powercfg command\nChange the power plan using the 'Power Plan' button")

def openPowerPlan():
	print("\nOpening power plan settings")
	startfile("C:\Windows\System32\powercfg.cpl")
	print("Opened power plan settings\nChange power plan as needed")

def openCrystalDiskInfo():
	print("\nOpening CrystalDiskInfo")
	try:
		startfile("CrystalDiskInfoPortable\CrystalDiskInfoPortable.exe")
		print("Opened CrystalDiskInfo\nCheck storage health")
	except:
		print("ERROR: Couldn't open CrystalDiskInfo")
		print("Check your file structure at https://github.com/3XAY/PC-Utilities in the README.md file, under the File Structure section")

def runSfc():
	print("\nRunning sfc (this may take some time)")
	system("sfc /scannow")
	print("\nRan sfc\nRepaired system files")

def runMemtest():
	print("\nOpening Windows Memory Diagnostic")
	startfile("C:\WINDOWS\system32\MdSched.exe")
	print("Opened Windows Memory Diagnostic\nFor results, open event viewer\nRight-click on 'System' under 'Windows Logs'\nPress find\nType: 'MemoryDiagnostics-Results'")

def runFurmark():
	print("\nOpening Furmark")
	try:
		startfile("FurMarkPortable\FurMark.exe")
		print("Opened Furmark\nRun the highest resolution benchmark possible")
	except:
		print("ERROR: Couldn't open Furmark")
		print("Check your file structure at https://github.com/3XAY/PC-Utilities in the README.md file, under the File Structure section")
	
	

def runCinebench():
	print("\nOpening Cinebench")
	try:
		startfile("CinebenchPortable\Cinebench.exe")
		print("Opened Cinebench R23\nRun benchmarks")
	except:
		print("ERROR: Couldn't open Cinebench")
		print("Check your file structure at https://github.com/3XAY/PC-Utilities in the README.md file, under the File Structure section")
	

def openAnim():
	print("\nOpening registry...")
	try:
		key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, winreg.KEY_ALL_ACCESS)
		print("Currently set to: " + str(winreg.QueryValueEx(key, "MenuShowDelay")))
		print("Changing value to 200...")
		try:
			winreg.SetValueEx(key, "MenuShowDelay", 0, winreg.REG_SZ, "200")
			winreg.CloseKey(key)
			print("Animation delay is set to 200ms")
		except:
			print("ERROR: Unable to write to registry, try running in Administrator mode")
	except:
		print("ERROR: Unable to read current value, try running in Administrator mode")
	print("You can manually modify the key at Computer/HKEY_CURRENT_USER/Control Panel/Desktop and change the MenuShowDelay value in milliseconds")
	print("Don't forget to restart the computer for the changes to take effect")

def openHWInfo():
	print("\nOpening HWInfo64")
	try:
		startfile("HardwareInfoPortable\HWiNFO64.exe")
		print("Opened HWInfo 64\nCheck any hardware stats")
	except:
		print("ERROR: Couldn't open HWInfo64")
		print("Check your file structure at https://github.com/3XAY/PC-Utilities in the README.md file, under the File Structure section")
	

def	openStartupApps():
	print("\nOpening Task Manager")
	subprocess.run(["powershell", "taskmgr /startup"], shell=True)
	print("Opened startup apps tab in Task Manager")

def openMsConfig():
	print("\nOpening System Configuration")
	startfile("C:\WINDOWS\system32\msconfig.exe")
	print("Opened System Configuration\nEnsure 'Normal Startup' is selected\nSwitch to 'Boot' tab\nRemove any unwanted OS'")

def openProgramUninstaller():
	print("\nOpening Installed Apps")
	subprocess.run(["powershell", "start ms-settings:appsfeatures-app"], shell=True)
	print("Opened Installed Apps\nUninstall apps from here")

def openCrystalDiskMark():
	print("\nOpening CrystalDiskMark")
	try:
		startfile("CrystalDiskMarkPortable\CrystalDiskMarkPortable.exe")
		print("Opened CrystalDiskMark\nBenchmark Storage Devices")
	except:
		print("ERROR: Couldn't open CrystalDiskMark")
		print("Check your file structure at https://github.com/3XAY/PC-Utilities in the README.md file, under the File Structure section")

def	openTaskManager():
	print("\nOpening Task Manager")
	startfile("C:\WINDOWS\system32\Taskmgr.exe")
	print("Opened Task Manager\nMonitor system components")

def openRestorePoint():
    print("\nOpening System Properties")
    startfile("C:\WINDOWS\system32\SystemPropertiesProtection.exe")
    print("Opened System Properties\nCreate a Restore Point to undo any major system changes")

#runCommand method is on line 991


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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 641, 611))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabBar::tab:selected {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background-color: #1f1f1f;\n"
"    color: white;\n"
"}\n"
"")
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.sysTab = QtWidgets.QWidget()
        self.sysTab.setStyleSheet("background-color: #1f1f1f;\n"
"border: none;\n"
"")
        self.sysTab.setObjectName("sysTab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.sysTab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 601, 561))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.btnGrid_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.btnGrid_2.setContentsMargins(0, 0, 0, 0)
        self.btnGrid_2.setObjectName("btnGrid_2")
        self.CrystalDiskMarkBtn_7 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.CrystalDiskMarkBtn_7.setStyleSheet("QPushButton {\n"
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
        self.CrystalDiskMarkBtn_7.setObjectName("CrystalDiskMarkBtn_7")
        self.btnGrid_2.addWidget(self.CrystalDiskMarkBtn_7, 11, 1, 1, 1)
        self.PowerPlanBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.PowerPlanBtn_2.setStyleSheet("QPushButton {\n"
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
        self.PowerPlanBtn_2.setObjectName("PowerPlanBtn_2")
        self.btnGrid_2.addWidget(self.PowerPlanBtn_2, 1, 1, 1, 1)
        self.UltPowerPlanBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.UltPowerPlanBtn_2.setStyleSheet("QPushButton {\n"
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
        self.UltPowerPlanBtn_2.setObjectName("UltPowerPlanBtn_2")
        self.btnGrid_2.addWidget(self.UltPowerPlanBtn_2, 1, 0, 1, 1)
        self.DefragBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.DefragBtn_2.setStyleSheet("QPushButton {\n"
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
        self.DefragBtn_2.setObjectName("DefragBtn_2")
        self.btnGrid_2.addWidget(self.DefragBtn_2, 0, 2, 1, 1)
        self.DiskCleanBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
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
        self.DiskCleanBtn_2.setPalette(palette)
        self.DiskCleanBtn_2.setMouseTracking(False)
        self.DiskCleanBtn_2.setAutoFillBackground(False)
        self.DiskCleanBtn_2.setStyleSheet("QPushButton {\n"
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
        self.DiskCleanBtn_2.setCheckable(False)
        self.DiskCleanBtn_2.setAutoDefault(False)
        self.DiskCleanBtn_2.setDefault(False)
        self.DiskCleanBtn_2.setFlat(False)
        self.DiskCleanBtn_2.setObjectName("DiskCleanBtn_2")
        self.btnGrid_2.addWidget(self.DiskCleanBtn_2, 0, 1, 1, 1)
        self.CrystalDiskMarkBtn_6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.CrystalDiskMarkBtn_6.setStyleSheet("QPushButton {\n"
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
        self.CrystalDiskMarkBtn_6.setObjectName("CrystalDiskMarkBtn_6")
        self.btnGrid_2.addWidget(self.CrystalDiskMarkBtn_6, 0, 0, 1, 1)
        self.UninstallAppsBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.UninstallAppsBtn_2.setStyleSheet("QPushButton {\n"
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
        self.UninstallAppsBtn_2.setObjectName("UninstallAppsBtn_2")
        self.btnGrid_2.addWidget(self.UninstallAppsBtn_2, 1, 2, 1, 1)
        self.WindowsUpdateBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.WindowsUpdateBtn_2.setStyleSheet("QPushButton {\n"
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
        self.WindowsUpdateBtn_2.setObjectName("WindowsUpdateBtn_2")
        self.btnGrid_2.addWidget(self.WindowsUpdateBtn_2, 2, 0, 1, 1)
        self.StartupApps_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.StartupApps_2.setStyleSheet("QPushButton {\n"
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
        self.StartupApps_2.setObjectName("StartupApps_2")
        self.btnGrid_2.addWidget(self.StartupApps_2, 2, 1, 1, 1)
        self.AnimationBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.AnimationBtn_2.setStyleSheet("QPushButton {\n"
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
        self.AnimationBtn_2.setObjectName("AnimationBtn_2")
        self.btnGrid_2.addWidget(self.AnimationBtn_2, 2, 2, 1, 1)
        self.sfcBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.sfcBtn_2.setStyleSheet("QPushButton {\n"
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
        self.sfcBtn_2.setObjectName("sfcBtn_2")
        self.btnGrid_2.addWidget(self.sfcBtn_2, 3, 0, 1, 1)
        self.memtestBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.memtestBtn_2.setStyleSheet("QPushButton {\n"
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
        self.memtestBtn_2.setObjectName("memtestBtn_2")
        self.btnGrid_2.addWidget(self.memtestBtn_2, 3, 1, 1, 1)
        self.SysConfigBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.SysConfigBtn_2.setStyleSheet("QPushButton {\n"
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
        self.SysConfigBtn_2.setObjectName("SysConfigBtn_2")
        self.btnGrid_2.addWidget(self.SysConfigBtn_2, 3, 2, 1, 1)
        self.warning_2 = QtWidgets.QLabel(self.sysTab)
        self.warning_2.setGeometry(QtCore.QRect(40, 570, 551, 16))
        self.warning_2.setStyleSheet("color: white;\n"
"")
        self.warning_2.setScaledContents(False)
        self.warning_2.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_2.setObjectName("warning_2")
        self.tabWidget.addTab(self.sysTab, "")
        self.benchTab = QtWidgets.QWidget()
        self.benchTab.setStyleSheet("background-color: #1f1f1f;\n"
"border: none;\n"
"")
        self.benchTab.setObjectName("benchTab")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.benchTab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 0, 601, 561))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.btnGrid_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.btnGrid_3.setContentsMargins(0, 0, 0, 0)
        self.btnGrid_3.setObjectName("btnGrid_3")
        self.CrystalDiskMarkBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.CrystalDiskMarkBtn_2.setStyleSheet("QPushButton {\n"
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
        self.CrystalDiskMarkBtn_2.setObjectName("CrystalDiskMarkBtn_2")
        self.btnGrid_3.addWidget(self.CrystalDiskMarkBtn_2, 2, 2, 1, 1)
        self.FurmarkBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.FurmarkBtn_2.setStyleSheet("QPushButton {\n"
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
        self.FurmarkBtn_2.setObjectName("FurmarkBtn_2")
        self.btnGrid_3.addWidget(self.FurmarkBtn_2, 0, 2, 1, 1)
        self.CinebenchBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.CinebenchBtn_2.setStyleSheet("QPushButton {\n"
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
        self.CinebenchBtn_2.setObjectName("CinebenchBtn_2")
        self.btnGrid_3.addWidget(self.CinebenchBtn_2, 1, 2, 1, 1)
        self.warning_3 = QtWidgets.QLabel(self.benchTab)
        self.warning_3.setGeometry(QtCore.QRect(40, 570, 551, 16))
        self.warning_3.setStyleSheet("color: white;\n"
"")
        self.warning_3.setScaledContents(False)
        self.warning_3.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_3.setObjectName("warning_3")
        self.tabWidget.addTab(self.benchTab, "")
        self.monitorTab = QtWidgets.QWidget()
        self.monitorTab.setStyleSheet("background-color: #1f1f1f;\n"
"border: none;\n"
"")
        self.monitorTab.setObjectName("monitorTab")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.monitorTab)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 0, 601, 561))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.btnGrid_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.btnGrid_4.setContentsMargins(0, 0, 0, 0)
        self.btnGrid_4.setObjectName("btnGrid_4")
        self.HWInfoBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.HWInfoBtn_2.setStyleSheet("QPushButton {\n"
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
        self.HWInfoBtn_2.setObjectName("HWInfoBtn_2")
        self.btnGrid_4.addWidget(self.HWInfoBtn_2, 0, 0, 1, 1)
        self.StartupApps_3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.StartupApps_3.setStyleSheet("QPushButton {\n"
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
        self.StartupApps_3.setObjectName("StartupApps_3")
        self.btnGrid_4.addWidget(self.StartupApps_3, 0, 1, 1, 1)
        self.memtestBtn_3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.memtestBtn_3.setStyleSheet("QPushButton {\n"
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
        self.memtestBtn_3.setObjectName("memtestBtn_3")
        self.btnGrid_4.addWidget(self.memtestBtn_3, 1, 1, 1, 1)
        self.CrystalDiskInfoBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.CrystalDiskInfoBtn_2.setStyleSheet("QPushButton {\n"
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
        self.CrystalDiskInfoBtn_2.setObjectName("CrystalDiskInfoBtn_2")
        self.btnGrid_4.addWidget(self.CrystalDiskInfoBtn_2, 1, 0, 1, 1)
        self.warning_4 = QtWidgets.QLabel(self.monitorTab)
        self.warning_4.setGeometry(QtCore.QRect(40, 570, 551, 16))
        self.warning_4.setStyleSheet("color: white;\n"
"")
        self.warning_4.setScaledContents(False)
        self.warning_4.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_4.setObjectName("warning_4")
        self.tabWidget.addTab(self.monitorTab, "")
        self.storageTab = QtWidgets.QWidget()
        self.storageTab.setStyleSheet("background-color: #1f1f1f;\n"
"border: none;\n"
"")
        self.storageTab.setObjectName("storageTab")
        self.warning_5 = QtWidgets.QLabel(self.storageTab)
        self.warning_5.setGeometry(QtCore.QRect(40, 570, 551, 16))
        self.warning_5.setStyleSheet("color: white;\n"
"")
        self.warning_5.setScaledContents(False)
        self.warning_5.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_5.setObjectName("warning_5")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.storageTab)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 0, 601, 561))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.btnGrid_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.btnGrid_5.setContentsMargins(0, 0, 0, 0)
        self.btnGrid_5.setObjectName("btnGrid_5")
        self.DiskCleanBtn_3 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
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
        self.DiskCleanBtn_3.setPalette(palette)
        self.DiskCleanBtn_3.setMouseTracking(False)
        self.DiskCleanBtn_3.setAutoFillBackground(False)
        self.DiskCleanBtn_3.setStyleSheet("QPushButton {\n"
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
        self.DiskCleanBtn_3.setCheckable(False)
        self.DiskCleanBtn_3.setAutoDefault(False)
        self.DiskCleanBtn_3.setDefault(False)
        self.DiskCleanBtn_3.setFlat(False)
        self.DiskCleanBtn_3.setObjectName("DiskCleanBtn_3")
        self.btnGrid_5.addWidget(self.DiskCleanBtn_3, 0, 0, 1, 1)
        self.DefragBtn_3 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.DefragBtn_3.setStyleSheet("QPushButton {\n"
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
        self.DefragBtn_3.setObjectName("DefragBtn_3")
        self.btnGrid_5.addWidget(self.DefragBtn_3, 0, 1, 1, 1)
        self.CrystalDiskInfoBtn_3 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.CrystalDiskInfoBtn_3.setStyleSheet("QPushButton {\n"
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
        self.CrystalDiskInfoBtn_3.setObjectName("CrystalDiskInfoBtn_3")
        self.btnGrid_5.addWidget(self.CrystalDiskInfoBtn_3, 1, 0, 1, 1)
        self.CrystalDiskMarkBtn_4 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.CrystalDiskMarkBtn_4.setStyleSheet("QPushButton {\n"
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
        self.CrystalDiskMarkBtn_4.setObjectName("CrystalDiskMarkBtn_4")
        self.btnGrid_5.addWidget(self.CrystalDiskMarkBtn_4, 1, 1, 1, 1)
        self.tabWidget.addTab(self.storageTab, "")
        self.cmdTab = QtWidgets.QWidget()
        self.cmdTab.setStyleSheet("background-color: #1f1f1f;\n"
"border: none;\n"
"")
        self.cmdTab.setObjectName("cmdTab")
        self.commandButton = QtWidgets.QPushButton(self.cmdTab)
        self.commandButton.setGeometry(QtCore.QRect(150, 200, 321, 35))
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
        self.commandButton.setPalette(palette)
        self.commandButton.setMouseTracking(False)
        self.commandButton.setAutoFillBackground(False)
        self.commandButton.setStyleSheet("QPushButton {\n"
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
        self.commandButton.setCheckable(False)
        self.commandButton.setAutoDefault(False)
        self.commandButton.setDefault(False)
        self.commandButton.setFlat(False)
        self.commandButton.setObjectName("commandButton")
        self.commandTextbox = QtWidgets.QLineEdit(self.cmdTab)
        self.commandTextbox.setGeometry(QtCore.QRect(40, 30, 551, 121))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.commandTextbox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.commandTextbox.setFont(font)
        self.commandTextbox.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.commandTextbox.setAutoFillBackground(False)
        self.commandTextbox.setStyleSheet("background-color: #000000; color: white; border-radius: 17px;")
        self.commandTextbox.setDragEnabled(False)
        self.commandTextbox.setObjectName("commandTextbox")
        self.tabWidget.addTab(self.cmdTab, "")
        screen.setCentralWidget(self.centralwidget)

        #runCommand method
        def runCommand():
            system(self.commandTextbox.text())

        self.retranslateUi(screen)
        self.tabWidget.setCurrentIndex(0)
        self.DiskCleanBtn_2.clicked.connect(openDiskClean)
        self.DefragBtn_2.clicked.connect(openDefrag)
        self.WindowsUpdateBtn_2.clicked.connect(openUpdate)
        self.PowerPlanBtn_2.clicked.connect(openPowerPlan)
        self.sfcBtn_2.clicked.connect(runSfc)
        self.UninstallAppsBtn_2.clicked.connect(openProgramUninstaller)
        self.memtestBtn_2.clicked.connect(runMemtest)
        self.SysConfigBtn_2.clicked.connect(openMsConfig)
        self.StartupApps_2.clicked.connect(openStartupApps)
        self.FurmarkBtn_2.clicked.connect(runFurmark)
        self.CrystalDiskMarkBtn_2.clicked.connect(openCrystalDiskMark)
        self.CinebenchBtn_2.clicked.connect(runCinebench)
        self.memtestBtn_3.clicked.connect(runMemtest)
        self.CrystalDiskInfoBtn_2.clicked.connect(openCrystalDiskInfo)
        self.StartupApps_3.clicked.connect(openTaskManager)
        self.HWInfoBtn_2.clicked.connect(openHWInfo)
        self.DiskCleanBtn_3.clicked.connect(openDiskClean)
        self.DefragBtn_3.clicked.connect(openDefrag)
        self.CrystalDiskInfoBtn_3.clicked.connect(openCrystalDiskInfo)
        self.CrystalDiskMarkBtn_4.clicked.connect(openCrystalDiskMark)
        self.CrystalDiskMarkBtn_6.clicked.connect(openRestorePoint)
        self.UltPowerPlanBtn_2.clicked.connect(activateUltPower)
        self.AnimationBtn_2.clicked.connect(openAnim)
        self.CrystalDiskMarkBtn_7.clicked.connect(openTaskManager)
        self.commandButton.clicked.connect(runCommand)
        QtCore.QMetaObject.connectSlotsByName(screen)

    def retranslateUi(self, screen):
        _translate = QtCore.QCoreApplication.translate
        screen.setWindowTitle(_translate("screen", "PC Utilities (Made by 3XAY)"))
        self.CrystalDiskMarkBtn_7.setText(_translate("screen", "Task Manager"))
        self.PowerPlanBtn_2.setText(_translate("screen", "Power Plan"))
        self.UltPowerPlanBtn_2.setText(_translate("screen", "Ultimate Power Plan"))
        self.DefragBtn_2.setText(_translate("screen", "Defrag"))
        self.DiskCleanBtn_2.setText(_translate("screen", "Disk Clean"))
        self.CrystalDiskMarkBtn_6.setText(_translate("screen", "Restore Point"))
        self.UninstallAppsBtn_2.setText(_translate("screen", "Uninstall apps"))
        self.WindowsUpdateBtn_2.setText(_translate("screen", "Windows Update"))
        self.StartupApps_2.setText(_translate("screen", "Startup Apps"))
        self.AnimationBtn_2.setText(_translate("screen", "Windows Animation Speed"))
        self.sfcBtn_2.setText(_translate("screen", "sfc"))
        self.memtestBtn_2.setText(_translate("screen", "Memory Diagnostics"))
        self.SysConfigBtn_2.setText(_translate("screen", "Sys config"))
        self.warning_2.setText(_translate("screen", "Created by 3XAY. This software is not responsible for any harm caused to any computers."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sysTab), _translate("screen", "System"))
        self.CrystalDiskMarkBtn_2.setText(_translate("screen", "CrystalDiskMark"))
        self.FurmarkBtn_2.setText(_translate("screen", "FurMark"))
        self.CinebenchBtn_2.setText(_translate("screen", "Cinebench"))
        self.warning_3.setText(_translate("screen", "Created by 3XAY. This software is not responsible for any harm caused to any computers."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.benchTab), _translate("screen", "Benchmarking"))
        self.HWInfoBtn_2.setText(_translate("screen", "HWInfo"))
        self.StartupApps_3.setText(_translate("screen", "Task Manager"))
        self.memtestBtn_3.setText(_translate("screen", "Memory Diagnostics"))
        self.CrystalDiskInfoBtn_2.setText(_translate("screen", "CrystalDiskInfo"))
        self.warning_4.setText(_translate("screen", "Created by 3XAY. This software is not responsible for any harm caused to any computers."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.monitorTab), _translate("screen", "Monitoring"))
        self.warning_5.setText(_translate("screen", "Created by 3XAY. This software is not responsible for any harm caused to any computers."))
        self.DiskCleanBtn_3.setText(_translate("screen", "Disk Clean"))
        self.DefragBtn_3.setText(_translate("screen", "Defrag"))
        self.CrystalDiskInfoBtn_3.setText(_translate("screen", "CrystalDiskInfo"))
        self.CrystalDiskMarkBtn_4.setText(_translate("screen", "CrystalDiskMark"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.storageTab), _translate("screen", "Storage"))
        self.commandButton.setText(_translate("screen", "Enter Command"))
        self.commandTextbox.setPlaceholderText(_translate("screen", "Enter a Windows command here..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cmdTab), _translate("screen", "Commands"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen = QtWidgets.QMainWindow()
    ui = Ui_screen()
    ui.setupUi(screen)
    screen.show()
    sys.exit(app.exec_())
