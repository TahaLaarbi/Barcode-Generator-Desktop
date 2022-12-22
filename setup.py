#BENACEUR TAHA ELARABI

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

target = Executable(
    script="main.py",
    icon="icons/icon.ico"
    )
"""
compress=False,
copyDependentFiles=True,
appendScriptToExe=True,
appendScriptToLibrary=False,
"""
    

setup(
    name="Barcode Studio",
    version="1.0",
    description="Barcode Studio",
    author="BENACEU TAHA ELARABI",
    #options={"BarcodeStudio_exe": options},
    executables=[target]
    )
