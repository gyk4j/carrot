# car

*Crop And Resize* is a Python script to crop and resize JPEG photos using the 
high-speed [libvips](https://www.libvips.org/) image processing library with 
low memory needs.

Currently, it is only packaged and tested for Windows platform, but there is 
nothing platform-specific. Linux build and instructions can be produced and 
tested if needed. 

# Developer Guide

## Setup

```shell
py -m venv car
.\car\Scripts\activate.bat
pip install build
pip install pyinstaller
pip install "pyvips[binary]"

# Download/copy pre-compiled DLLs for libvips
mkdir .\car\lib64
copy car\venv\Lib\site-packages\libvips-42-a64e1348d8f8d46219492aea226fbd74.dll lib64\libvips-42.dll
curl -O https://github.com/libvips/libvips/releases/download/v8.10.5/vips-dev-w64-all-8.10.5.zip
unzip -d %TEMP% vips-dev-w64-all-8.10.5.zip
copy %TEMP%\vips-dev-8.10\bin\*.dll .\car\lib64\
```

## Build Python Wheel Package
```shell
py -m build
```

Check that files are produced:

1. `dist\car-x.x.x.tar.gz`
2. `car-x.x.x-py3-none-any.whl`

## Build PyInstaller Package 
```shell
cd car
#pyinstaller -w main.py
#pyinstaller --onefile -w main.py
#pyinstaller -w --add-binary="lib64:." --add-data="test.jpg:." main.py
pyinstaller main.spec
```

Check that one of the files are produced:

1. `dist\car\car.exe`
2. `dist\car.exe`

## Run
```shell
.\dist\main\main.exe
.\dist\main.exe
```
