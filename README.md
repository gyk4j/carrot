# car
Crop And Resize

# Development Workstation Setup

```shell
py -m venv car
.\car\Scripts\activate.bat
py -m pip install pyinstaller
```

# Build
```shell
cd car
pyinstaller -w main.py
pyinstaller --onefile -w main.py
```
