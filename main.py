#Import packages
from tkinter import Label, Tk, Button #GUI
from time import sleep #Delays
from pyautogui import typewrite, press, hotkey #Macros
from os import startfile #opening apps

#Set Defaults
btnHeight = 2
btnWidth = 10
btnX = 75
btnY = 75
waitTime = 2.5
screenBgColor = "#141414"
bgBtnColorInactive = "#0f0f0f"
bgBtnColorActive = "#0d0d0d"
BtnTextColorActive = "#c4c4c4"
textColor = "white"

# Initialize screen
screen = Tk()
screen.geometry("1000x400")
screen.title("PC Cleaning Utility (Custom made)")
screen.configure(background=screenBgColor)

#Create text
warning = Label(screen, text = "Created by 3XAY. This software is not responsible for any harm caused to any computers.", bg=screenBgColor, fg=textColor)
warning.place(x=0, y=375)

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


#Buttons
DiskClean = Button(screen, text="Disk Clean", bg=bgBtnColorInactive, fg=textColor, command=openDiskClean, height=btnHeight, width=btnWidth, borderwidth=0, activebackground=bgBtnColorActive, activeforeground=BtnTextColorActive)
DiskClean.place(x=btnX, y=btnY)

Defrag = Button(screen, text="Defrag", bg=bgBtnColorInactive, fg=textColor, command=openDefrag, height=btnHeight, width=btnWidth, borderwidth=0, activebackground=bgBtnColorActive, activeforeground=BtnTextColorActive)
Defrag.place(x=btnX + 100, y=btnY)

WindowsUpdate = Button(screen, text="Windows Update", bg=bgBtnColorInactive, fg=textColor, command=openUpdate, height=btnHeight, width=btnWidth + 3, borderwidth=0, activebackground=bgBtnColorActive, activeforeground=BtnTextColorActive)
WindowsUpdate.place(x=btnX + 200, y=btnY)

UltPower = Button(screen, text="Ultimate Power Plan", bg=bgBtnColorInactive, fg=textColor, command=activateUltPower, height=btnHeight, width=btnWidth + 5, borderwidth=0, activebackground=bgBtnColorActive, activeforeground=BtnTextColorActive)
UltPower.place(x=btnX + 325, y=btnY)

PowerPlan = Button(screen, text="Power Plan", bg=bgBtnColorInactive, fg=textColor, command=openPowerPlan, height=btnHeight, width=btnWidth, borderwidth=0, activebackground=bgBtnColorActive, activeforeground=BtnTextColorActive)
PowerPlan.place(x=btnX + 475, y=btnY)

chkStorage = Button(screen, text="CrystalDiskInfo", bg=bgBtnColorInactive, fg=textColor, command=openCrystalDiskInfo, height=btnHeight, width=btnWidth + 3, borderwidth=0, activebackground=bgBtnColorActive, activeforeground=BtnTextColorActive)
chkStorage.place(x=btnX + 575, y=btnY)

sfc = Button(screen, text="sfc", bg=bgBtnColorInactive, fg=textColor, command=runSfc, height=btnHeight, width=btnWidth - 3, borderwidth=0, activebackground=bgBtnColorActive, activeforeground=BtnTextColorActive)
sfc.place(x=btnX + 700, y=btnY)

memtest = Button(screen, text="memtest", bg=bgBtnColorInactive, fg=textColor, command=runMemtest, height=btnHeight, width=btnWidth, borderwidth=0, activebackground=bgBtnColorActive, activeforeground=BtnTextColorActive)
memtest.place(x=btnX + 775, y=btnY)

furmark = Button(screen, text="Furmark", bg=bgBtnColorInactive, fg=textColor, command=runFurmark, height=btnHeight, width=btnWidth, borderwidth=0, activebackground=bgBtnColorActive, activeforeground=BtnTextColorActive)
furmark.place(x=btnX, y=btnY + 100)

cinebench = Button(screen, text="Cinebench", bg=bgBtnColorInactive, fg=textColor, command=runCinebench, height=btnHeight, width=btnWidth, borderwidth=0, activebackground=bgBtnColorActive, activeforeground=BtnTextColorActive)
cinebench.place(x=btnX + 100, y=btnY + 100)

animTimes = Button(screen, text="Animation",bg=bgBtnColorInactive, fg=textColor, command=openAnim, height=btnHeight, width=btnWidth, borderwidth=0, activebackground=bgBtnColorActive, activeforeground=BtnTextColorActive)
animTimes.place(x=btnX + 200, y=btnY + 100)

hwInfo = Button(screen, text="HWInfo", bg=bgBtnColorInactive, fg=textColor, command=openHWInfo, height=btnHeight, width=btnWidth, borderwidth=0, activebackground=bgBtnColorActive, activeforeground=BtnTextColorActive)
hwInfo.place(x=btnX + 300, y=btnY + 100)

msConfig = Button(screen, text="Sys Config", bg=bgBtnColorInactive, fg=textColor, command=openMsConfig, height=btnHeight, width=btnWidth, borderwidth=0, activebackground=bgBtnColorActive, activeforeground=BtnTextColorActive)
msConfig.place(x=btnX + 400, y=btnY + 100)

uninstaller = Button(screen, text="Uninstall apps", bg=bgBtnColorInactive, fg=textColor, command=openProgramUninstaller, height=btnHeight, width=btnWidth, borderwidth=0, activebackground=bgBtnColorActive, activeforeground=BtnTextColorActive)
uninstaller.place(x=btnX + 500, y=btnY + 100)

#Refresh screen
screen.mainloop()