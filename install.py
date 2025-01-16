#Installs PC-Utilities and the required software
import subprocess #Allows me to run commands
import sys #For errors
from os import path #See if file/path exists

#Installer method, tries to run a command in powershell, throws an error and gracefully stops on failure
def installStep(message, command, error):
	print(message)
	try:
		subprocess.run(["powershell", command], shell=False, check=True)
		print("DONE")
	except:
		sys.exit(error)

#Header
print("This program will start installing PC-Utilities and the required software")
print("It may take a while, please be patient")

#PC-Utilities setup
if path.exists('PC-Utilities'): #Make sure folder isn't already installed
	print("PC-Utilities folder already exists, please delete it before installing again\nPress any key to quit...")
	blank = input()
	sys.exit()
installStep("Creating PC-Utilities folder...", "md PC-Utilities", "ERROR: Unable to create the PC-Utilities folder, make sure there isn't an existing folder with the same name")
installStep("Downloading the PC-Utilities app...", "curl https://github.com/3XAY/PC-Utilities/releases/latest/download/PC-Utilities.exe -o PC-Utilities/PC-Utilities.exe", "ERROR: Unable to download the PC-Utilities app, check your internet connection")

#Cinebench
installStep("Downloading Cinebench... (This may take a while...)", "curl.exe -L -H 'Referer: https://www.maxon.net/en/downloads/cinebench-2024-downloads?srsltid=AfmBOoqLm_qswxE1fhcxoQflvImG2Vk98d12JYq3e2n3xoIDYX5S6764' https://mx-app-blob-prod.maxon.net/mx-package-production/website/windows/maxon/cinebench/Cinebench2024_win_x86_64.zip -o PC-Utilities/Cinebench.zip", "ERROR: Unable to download Cinebench, check your internet connection") #Uses Internet Archive link by Maxon
installStep("Extracting Cinebench...", "Expand-Archive -Force PC-Utilities/Cinebench.zip PC-Utilities/CinebenchPortable", "ERROR: Unable to extract Cinebench")

#Furmark
installStep("Downloading Furmark...", "curl https://geeks3d.com/dl/get/771 -o PC-Utilities/Furmark.zip", "ERROR: Unable to download Furmark, check your internet connection")
installStep("Extracting Furmark...", "Expand-Archive -Force PC-Utilities/Furmark.zip PC-Utilities/FurMarkPortable", "ERROR: Unable to extract Furmark")

#HWInfo
installStep("Downloading HWInfo...", "curl https://www.sac.sk/download/utildiag/hwi_820.zip -o PC-Utilities/HWInfo.zip", "ERROR: Unable to download HWInfo, check your internet connection") #Downloads from Slovakia
installStep("Extracting HWInfo...", "Expand-Archive -Force PC-Utilities/HWInfo.zip PC-Utilities/HardwareInfoPortable", "ERROR: Unable to extract HWInfo")

#CrystalDiskInfo
installStep("Downloading CrystalDiskInfo", "curl.exe -L https://sourceforge.net/projects/crystaldiskinfo/files/9.5.0/CrystalDiskInfo9_5_0.zip/download -o PC-Utilities/CDI.zip", "ERROR: Unable to download CrystalDiskInfo, check your internet connection")
installStep("Extracting CrystalDiskInfo...", "Expand-Archive -Force PC-Utilities/CDI.zip PC-Utilities/CrystalDiskInfoPortable", "ERROR: Unable to extract CrystalDiskInfo")

#CrystalDiskMark
installStep("Downloading CrystalDiskMark", "curl.exe -L https://sourceforge.net/projects/crystaldiskmark/files/8.0.6/CrystalDiskMark8_0_6.zip/download -o PC-Utilities/CDM.zip", "ERROR: Unable to download CrystalDiskMark, check your internet connection")
installStep("Extracting CrystalDiskMark...", "Expand-Archive -Force PC-Utilities/CDM.zip PC-Utilities/CrystalDiskMarkPortable", "ERROR: Unable to extract CrystalDiskMark")

#Clean up temporary files + save space
installStep("Cleaning up files (1/11)...", "del PC-Utilities/Cinebench.zip", "ERROR: Unable to clean up files")
installStep("Cleaning up files (2/11)...", "del PC-Utilities/Furmark.zip", "ERROR: Unable to clean up files")
installStep("Cleaning up files (3/11)...", "del PC-Utilities/HWInfo.zip", "ERROR: Unable to clean up files")
installStep("Cleaning up files (4/11)...", "del PC-Utilities/CDI.zip", "ERROR: Unable to clean up files")
installStep("Cleaning up files (5/11)...", "del PC-Utilities/CDM.zip", "ERROR: Unable to clean up files")
installStep("Cleaning up files (6/11)...", "del PC-Utilities/HardwareInfoPortable/HWiNFO_ARM64.exe", "ERROR: Unable to clean up files")
installStep("Cleaning up files (7/11)...", "del PC-Utilities/HardwareInfoPortable/HWiNFO32.exe", "ERROR: Unable to clean up files")
installStep("Cleaning up files (8/11)...", "del PC-Utilities/CrystalDiskInfoPortable/DiskInfo32.exe", "ERROR: Unable to clean up files")
installStep("Cleaning up files (9/11)...", "del PC-Utilities/CrystalDiskInfoPortable/DiskInfoA64.exe", "ERROR: Unable to clean up files")
installStep("Cleaning up files (10/11)...", "del PC-Utilities/CrystalDiskMarkPortable/DiskMark32.exe", "ERROR: Unable to clean up files")
installStep("Cleaning up files (11/11)...", "del PC-Utilities/CrystalDiskMarkPortable/DiskMarkA64.exe", "ERROR: Unable to clean up files")

#End
print("Installation complete, press any key to exit")
blank = input()
