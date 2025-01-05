# This document is for development purposes

### Required Python modules
- PyQt5
- os
- winreg
- subprocess
- auto-py-to-exe
- QT Designer (Included with PyQt5)


### How to compile the `.py` file to an executable
1. Run: `auto-py-to-exe`
2. Select the `main.py` file in the Script location
3. Choose one file
4. Choose console based
5. In advanced, enable the following:
    - --name = `PC-Utilities`
    - --clean = `Enable`
    - Windows specific options ==> --uac-admin = `Enable`
6. Click `Convert .py to .exe`


### How to modify the UI
1. Type `designer` into the terminal and the QT Designer app should open
2. Open the `PC-UtilitiesGUI.ui` file
3. Modify it
4. Save the file


### How to apply the UI to the `.py` file
1. Type `pyuic5 -x PC-UtilitiesGUI.ui -o output.py`
2. Copy the methods from the `main.py` file into the the `output.py` file
3. Copy the `runCommand` method from `main.py` and the following code block (`self.retranslateUi(screen)` to `QtCore.QMetaObject.connectSlotsByName(screen)`) and replace it in the same location in `output.py`. A tool like [diffchecker](https://www.diffchecker.com/text-compare/) can help.
4. Copy everything from `output.py` to the `main.py` file
5. Delete the warning at the top
6. Delete `output.py`