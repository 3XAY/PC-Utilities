#Import packages
from tkinter import * #GUI
import time #Delays
import pyautogui #Macros

# Initialize screen
screen = Tk()
screen.geometry("1000x400")

#Set Button Defaults
btnHeight = 2
btnWidth = 10
btnX = 75
btnY = 75

#Methods
def openDiskClean():
	exit

def openDefrag():
	exit

def openUpdate():
	exit

def openPowerPlan():
	exit

def openCrystalDiskInfo():
	exit

def runSfc():
	exit

def runMemtest():
	exit

def runFurmark():
	exit

def runCinebench():
	exit

def openAnim():
	exit
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

#Refresh screen
screen.mainloop()