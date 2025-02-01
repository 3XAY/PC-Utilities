#Installs PC-Utilities and the required software
from subprocess import run #Allows me to run commands
from sys import exit #For errors
from os import path #See if file/path exists
import requests #Used to loop till the HWInfo URL is found

#Installer method, tries to run a command in powershell, throws an error and gracefully stops on failure
def installStep(message, command, error):
	print(message)
	try:
		run(["powershell", command], shell=False, check=True)
		print("DONE")
	except:
		print(error + "\nEnter any key to exit...")
		blank = input()
		exit(error)

#Header
print("This program will start installing PC-Utilities and the required software")
print("It may take a while, please be patient")
print("If the installer appears to be frozen and you believe that step is completed, press 'CTRL+C' to continue")

#PC-Utilities setup
if path.exists('PC-Utilities'): #Make sure folder isn't already installed
	print("PC-Utilities folder already exists, enter 'Y' to replace, 'N' to continue")
	yn = input()
	yn = yn.lower()
	if(yn == "n"):
		pass
	else:
		installStep("Deleting existing PC-Utilities folder...", "rm PC-Utilities -r -force", "ERROR: Unable to delete the PC-Utilities folder")
		installStep("Creating PC-Utilities folder...", "md PC-Utilities", "ERROR: Unable to create the PC-Utilities folder")
else:
	installStep("Creating PC-Utilities folder...", "md PC-Utilities", "ERROR: Unable to create the PC-Utilities folder")

if path.exists("PC-Utilities/PC-Utilities.exe"):
	installStep("Deleting existing installation of PC-Utilities...", "del PC-Utilities/PC-Utilities.exe", "ERROR: Unable to delete PC-Utilities.exe")
	installStep("Downloading the PC-Utilities app...", "curl https://github.com/3XAY/PC-Utilities/releases/latest/download/PC-Utilities.exe -o PC-Utilities/PC-Utilities.exe", "ERROR: Unable to download the PC-Utilities app, check your internet connection")
else:
	installStep("Downloading the PC-Utilities app...", "curl https://github.com/3XAY/PC-Utilities/releases/latest/download/PC-Utilities.exe -o PC-Utilities/PC-Utilities.exe", "ERROR: Unable to download the PC-Utilities app, check your internet connection")

#Cinebench
if path.exists("PC-Utilities/CinebenchPortable"):
	print("Cinebench is already installed, press 'Y' to re-install, 'N' to keep the current version")
	yn = input()
	yn = yn.lower()
	if(yn == "n"):
		pass
	else:
		installStep("Deleting existing Cinebench installation...", "rm PC-Utilities/CinebenchPortable -r -force", "ERROR: Unable to delete the Cinebench folder")
		installStep("Downloading Cinebench... (This may take a while...)", "curl.exe -L -H 'Referer: https://www.maxon.net/en/downloads/cinebench-2024-downloads?srsltid=AfmBOoqLm_qswxE1fhcxoQflvImG2Vk98d12JYq3e2n3xoIDYX5S6764' https://mx-app-blob-prod.maxon.net/mx-package-production/website/windows/maxon/cinebench/Cinebench2024_win_x86_64.zip -o PC-Utilities/Cinebench.zip", "ERROR: Unable to download Cinebench, check your internet connection") #Uses Internet Archive link by Maxon
		installStep("Extracting Cinebench...", "Expand-Archive -Force PC-Utilities/Cinebench.zip PC-Utilities/CinebenchPortable", "ERROR: Unable to extract Cinebench")
		installStep("Cleaning up files...", "del PC-Utilities/Cinebench.zip", "ERROR: Unable to clean up files")
else:
	installStep("Downloading Cinebench... (This may take a while...)", "curl.exe -L -H 'Referer: https://www.maxon.net/en/downloads/cinebench-2024-downloads?srsltid=AfmBOoqLm_qswxE1fhcxoQflvImG2Vk98d12JYq3e2n3xoIDYX5S6764' https://mx-app-blob-prod.maxon.net/mx-package-production/website/windows/maxon/cinebench/Cinebench2024_win_x86_64.zip -o PC-Utilities/Cinebench.zip", "ERROR: Unable to download Cinebench, check your internet connection") #Uses Internet Archive link by Maxon
	installStep("Extracting Cinebench...", "Expand-Archive -Force PC-Utilities/Cinebench.zip PC-Utilities/CinebenchPortable", "ERROR: Unable to extract Cinebench")
	installStep("Cleaning up files...", "del PC-Utilities/Cinebench.zip", "ERROR: Unable to clean up files")

#Furmark
if path.exists("PC-Utilities/FurMarkPortable"):
	print("Furmark is already installed, press 'Y' to re-install, 'N' to keep the current version")
	yn = input()
	yn = yn.lower()
	if(yn == "n"):
		pass
	else:
		installStep("Deleting existing Furmark installation...", "rm PC-Utilities/FurMarkPortable -r -force", "ERROR: Unable to delete the Furmark folder")
		installStep("Downloading Furmark...", "curl https://geeks3d.com/dl/get/771 -o PC-Utilities/Furmark.zip", "ERROR: Unable to download Furmark, check your internet connection")
		installStep("Extracting Furmark...", "Expand-Archive -Force PC-Utilities/Furmark.zip PC-Utilities/FurMarkPortable", "ERROR: Unable to extract Furmark")
		installStep("Cleaning up files...", "del PC-Utilities/Furmark.zip", "ERROR: Unable to clean up files")
		
else:
	installStep("Downloading Furmark...", "curl https://geeks3d.com/dl/get/771 -o PC-Utilities/Furmark.zip", "ERROR: Unable to download Furmark, check your internet connection")
	installStep("Extracting Furmark...", "Expand-Archive -Force PC-Utilities/Furmark.zip PC-Utilities/FurMarkPortable", "ERROR: Unable to extract Furmark")
	installStep("Cleaning up files...", "del PC-Utilities/Furmark.zip", "ERROR: Unable to clean up files")

#HWInfo
if path.exists("PC-Utilities/HardwareInfoPortable"):
	print("HWInfo is already installed, press 'Y' to re-install, 'N' to keep the current version")
	yn = input()
	yn = yn.lower()
	if(yn == "n"):
		pass
	else:
		installStep("Deleting existing HWInfo installation...", "rm PC-Utilities/HardwareInfoPortable -r -force", "ERROR: Unable to delete the HWInfo folder")
		v=820
		fake = True
		try:
			print("Downloading HWInfo...")
			while fake:
				r = requests.head("https://www.sac.sk/download/utildiag/hwi_" + str(v) + ".zip")
				if r.status_code == requests.codes.ok:
					fake = False
				else:
					v = v+1
			c = "curl https://www.sac.sk/download/utildiag/hwi_" + str(v) + ".zip -o PC-Utilities/HWInfo.zip"
			run(["powershell", c], shell=False, check=True)
			print("DONE")
		except:
			print("ERROR: Unable to download HWInfo, this is likely due to my code, please leave an issue in the repo\nEnter any key to exit...")
			blank = input()
			exit("ERROR: Unable to download HWInfo, this is likely due to my code, please leave an issue in the repo")
		installStep("Extracting HWInfo...", "Expand-Archive -Force PC-Utilities/HWInfo.zip PC-Utilities/HardwareInfoPortable", "ERROR: Unable to extract HWInfo")
		installStep("Cleaning up files (1/3)...", "del PC-Utilities/HWInfo.zip", "ERROR: Unable to clean up files")
		installStep("Cleaning up files (2/3)...", "del PC-Utilities/HardwareInfoPortable/HWiNFO_ARM64.exe", "ERROR: Unable to clean up files")
		installStep("Cleaning up files (3/3)...", "del PC-Utilities/HardwareInfoPortable/HWiNFO32.exe", "ERROR: Unable to clean up files")
		
else:
	v=820
	fake = True
	try:
		print("Downloading HWInfo...")
		while fake:
			r = requests.head("https://www.sac.sk/download/utildiag/hwi_" + str(v) + ".zip")
			if r.status_code == requests.codes.ok:
				fake = False
			else:
				v = v+1
		c = "curl https://www.sac.sk/download/utildiag/hwi_" + str(v) + ".zip -o PC-Utilities/HWInfo.zip"
		run(["powershell", c], shell=False, check=True)
		print("DONE")
	except:
		print("ERROR: Unable to download HWInfo, this is likely due to my code, please leave an issue in the repo\nEnter any key to exit...")
		blank = input()
		exit("ERROR: Unable to download HWInfo, this is likely due to my code, please leave an issue in the repo")
	installStep("Extracting HWInfo...", "Expand-Archive -Force PC-Utilities/HWInfo.zip PC-Utilities/HardwareInfoPortable", "ERROR: Unable to extract HWInfo")
	installStep("Cleaning up files (1/3)...", "del PC-Utilities/HWInfo.zip", "ERROR: Unable to clean up files")
	installStep("Cleaning up files (2/3)...", "del PC-Utilities/HardwareInfoPortable/HWiNFO_ARM64.exe", "ERROR: Unable to clean up files")
	installStep("Cleaning up files (3/3)...", "del PC-Utilities/HardwareInfoPortable/HWiNFO32.exe", "ERROR: Unable to clean up files")
		

#CrystalDiskInfo
if path.exists("PC-Utilities/CrystalDiskInfoPortable"):
	print("CrystalDiskInfo is already installed, press 'Y' to re-install, 'N' to keep the current version")
	yn = input()
	yn = yn.lower()
	if(yn == "n"):
		pass
	else:
		installStep("Deleting existing CrystalDiskInfo installation...", "rm PC-Utilities/CrystalDiskInfoPortable -r -force", "ERROR: Unable to delete the CrystalDiskInfo folder")
		installStep("Downloading CrystalDiskInfo", "curl.exe -L https://sourceforge.net/projects/crystaldiskinfo/files/9.5.0/CrystalDiskInfo9_5_0.zip/download -o PC-Utilities/CDI.zip", "ERROR: Unable to download CrystalDiskInfo, check your internet connection")
		installStep("Extracting CrystalDiskInfo...", "Expand-Archive -Force PC-Utilities/CDI.zip PC-Utilities/CrystalDiskInfoPortable", "ERROR: Unable to extract CrystalDiskInfo")
		installStep("Cleaning up files (1/3)...", "del PC-Utilities/CDI.zip", "ERROR: Unable to clean up files")
		installStep("Cleaning up files (2/3)...", "del PC-Utilities/CrystalDiskInfoPortable/DiskInfo32.exe", "ERROR: Unable to clean up files")
		installStep("Cleaning up files (3/3)...", "del PC-Utilities/CrystalDiskInfoPortable/DiskInfoA64.exe", "ERROR: Unable to clean up files")
		
else:	
	installStep("Downloading CrystalDiskInfo", "curl.exe -L https://sourceforge.net/projects/crystaldiskinfo/files/9.5.0/CrystalDiskInfo9_5_0.zip/download -o PC-Utilities/CDI.zip", "ERROR: Unable to download CrystalDiskInfo, check your internet connection")
	installStep("Extracting CrystalDiskInfo...", "Expand-Archive -Force PC-Utilities/CDI.zip PC-Utilities/CrystalDiskInfoPortable", "ERROR: Unable to extract CrystalDiskInfo")
	installStep("Cleaning up files (1/3)...", "del PC-Utilities/CDI.zip", "ERROR: Unable to clean up files")
	installStep("Cleaning up files (2/3)...", "del PC-Utilities/CrystalDiskInfoPortable/DiskInfo32.exe", "ERROR: Unable to clean up files")
	installStep("Cleaning up files (3/3)...", "del PC-Utilities/CrystalDiskInfoPortable/DiskInfoA64.exe", "ERROR: Unable to clean up files")

#CrystalDiskMark
if path.exists("PC-Utilities/CrystalDiskMarkPortable"):
	print("CrystalDiskMark is already installed, press 'Y' to re-install, 'N' to keep the current version")
	yn = input()
	yn = yn.lower()
	if(yn == "n"):
		pass
	else:
		installStep("Deleting existing CrystalDiskMark installation...", "rm PC-Utilities/CrystalDiskMarkPortable -r -force", "ERROR: Unable to delete the CrystalDiskMark folder")
		installStep("Downloading CrystalDiskMark", "curl.exe -L https://sourceforge.net/projects/crystaldiskmark/files/8.0.6/CrystalDiskMark8_0_6.zip/download -o PC-Utilities/CDM.zip", "ERROR: Unable to download CrystalDiskMark, check your internet connection")
		installStep("Extracting CrystalDiskMark...", "Expand-Archive -Force PC-Utilities/CDM.zip PC-Utilities/CrystalDiskMarkPortable", "ERROR: Unable to extract CrystalDiskMark")
		installStep("Cleaning up files (1/3)...", "del PC-Utilities/CDM.zip", "ERROR: Unable to clean up files")
		installStep("Cleaning up files (2/3)...", "del PC-Utilities/CrystalDiskMarkPortable/DiskMark32.exe", "ERROR: Unable to clean up files")
		installStep("Cleaning up files (3/3)...", "del PC-Utilities/CrystalDiskMarkPortable/DiskMarkA64.exe", "ERROR: Unable to clean up files")
		
else:	
	installStep("Downloading CrystalDiskMark", "curl.exe -L https://sourceforge.net/projects/crystaldiskmark/files/8.0.6/CrystalDiskMark8_0_6.zip/download -o PC-Utilities/CDM.zip", "ERROR: Unable to download CrystalDiskMark, check your internet connection")
	installStep("Extracting CrystalDiskMark...", "Expand-Archive -Force PC-Utilities/CDM.zip PC-Utilities/CrystalDiskMarkPortable", "ERROR: Unable to extract CrystalDiskMark")
	installStep("Cleaning up files (1/3)...", "del PC-Utilities/CDM.zip", "ERROR: Unable to clean up files")
	installStep("Cleaning up files (2/3)...", "del PC-Utilities/CrystalDiskMarkPortable/DiskMark32.exe", "ERROR: Unable to clean up files")
	installStep("Cleaning up files (3/3)...", "del PC-Utilities/CrystalDiskMarkPortable/DiskMarkA64.exe", "ERROR: Unable to clean up files")

#End
print("Installation complete, press any key to exit")
blank = input()