#Import packages
from tkinter import * #GUI
import time #Delays
import pyautogui #Macros
import os #opening apps

# Initialize screen
screen = Tk()
screen.geometry("1000x400")
screen.title("Windows Debug (Custom made)")

#Create text
warning = Label(screen, text = "Created by 3XAY. This software is not responsible for any harm caused to any computers.")
warning.place(x=0, y=375)

#Set Defaults
btnHeight = 2
btnWidth = 10
btnX = 75
btnY = 75
waitTime = 2.5

#Methods
def openDiskClean():
	print("")
	print("Opening disk cleanup")
	os.startfile("C:\WINDOWS\system32\cleanmgr.exe")
	print("Opened disk cleanup")

def openDefrag():
	print("")
	print("Opening defrag")
	os.startfile("C:\WINDOWS\system32\dfrgui.exe")
	print("Opened defrag")

def openUpdate():
	print("")
	print("Opening Windows Update")
	pyautogui.press("win")
	time.sleep(waitTime)
	pyautogui.typewrite("Windows Update")
	time.sleep(waitTime)
	pyautogui.press("enter")
	print("Opened Windows Update")

def openPowerPlan():
	print("")
	print("Opening power plan settings")
	pyautogui.press("win")
	time.sleep(waitTime)
	pyautogui.typewrite("Choose a power plan")
	time.sleep(waitTime)
	pyautogui.press("enter")
	print("Opened power plan settings")

def openCrystalDiskInfo():
	print("")
	print("Opening CrystalDiskInfo")
	os.startfile("CrystalDiskInfoPortable\CrystalDiskInfoPortable.exe")
	print("Opened CrystalDiskInfo")

def runSfc():
	print("")
	print("Opening cmd")
	os.startfile("C:\WINDOWS\system32\cmd.exe")
	print("Opened cmd")
	print("Type 'sfc /scannow'")

def runMemtest():
	print("")
	print("Opening Windows Memory Diagnostic")
	os.startfile("C:\WINDOWS\system32\MdSched.exe")
	print("Opened Windows Memory Diagnostic")

def runFurmark():
	print("")
	print("Opening Furmark")
	os.startfile("FurMarkPortable\FurMark.exe")
	print("Opened Furmark")

def runCinebench():
	print("")
	print("Opening Cinebench R23")
	os.startfile("CinebenchPortable\Cinebench.exe")
	print("Opened Cinebench R23")

def openAnim():
	print("")
	print("Opening regedit")
	os.startfile("C:\WINDOWS\\regedit.exe")
	print("Opened regedit")
	print('Go to "Computer\HKEY_CURRENT_USER\Control Panel\Desktop"')
	print("Find 'MenuShowDelay'")
	print("set value to '200'")
	print("restart computer")

def openHWInfo():
	print("")
	print("Opening HWInfo64")
	os.startfile("HardwareInfoPortable\HWiNFO64.exe")
	print("Opened HWInfo 64")

#Buttons
DiskClean = Button(screen, text="Disk Clean", bg='white', command=openDiskClean, height=btnHeight, width=btnWidth)
DiskClean.place(x=btnX, y=btnY)

Defrag = Button(screen, text="Defrag", bg='white', command=openDefrag, height=btnHeight, width=btnWidth)
Defrag.place(x=btnX + 100, y=btnY)

WindowsUpdate = Button(screen, text="Windows Update", bg='white', command=openUpdate, height=btnHeight, width=btnWidth + 3)
WindowsUpdate.place(x=btnX + 200, y=btnY)

PowerPlan = Button(screen, text="Power Plan", bg='white', command=openPowerPlan, height=btnHeight, width=btnWidth)
PowerPlan.place(x=btnX + 325, y=btnY)

chkStorage = Button(screen, text="CrystalDiskInfo", bg='white', command=openCrystalDiskInfo, height=btnHeight, width=btnWidth + 3)
chkStorage.place(x=btnX + 425, y=btnY)

sfc = Button(screen, text="sfc", bg='white', command=runSfc, height=btnHeight, width=btnWidth - 3)
sfc.place(x=btnX + 550, y=btnY)

memtest = Button(screen, text="memtest", bg='white', command=runMemtest, height=btnHeight, width=btnWidth)
memtest.place(x=btnX + 625, y=btnY)

furmark = Button(screen, text="Furmark", bg='white', command=runFurmark, height=btnHeight, width=btnWidth)
furmark.place(x=btnX + 725, y=btnY)

cinebench = Button(screen, text="Cinebench", bg='white', command=runCinebench, height=btnHeight, width=btnWidth)
cinebench.place(x=btnX, y=btnY + 100)

animTimes = Button(screen, text="Animation", bg='white', command=openAnim, height=btnHeight, width=btnWidth)
animTimes.place(x=btnX + 100, y=btnY + 100)

hwInfo = Button(screen, text="HWInfo", bg='white', command=openHWInfo, height=btnHeight, width=btnWidth)
hwInfo.place(x=btnX + 200, y=btnY + 100)


#Refresh screen
screen.mainloop()