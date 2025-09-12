@echo off

REM Requires `.venv\Scripts\activate.bat` to set the virtual environment.

call :pyinstaller
call :cx_Freeze
goto end

:pyinstaller
pyinstaller --noconfirm --log-level WARN pyinstaller.spec
if ERRORLEVEL 1 goto error
dir dist\carrot\
if exist "dist\carrot\carrot.exe" "dist\carrot\carrot.exe"
goto end

:cx_Freeze
py setup.py build
if ERRORLEVEL 1 goto error
dir build\exe.win-amd64-3.8\
if exist "build\exe.win-amd64-3.8\carrot.exe" "build\exe.win-amd64-3.8\carrot.exe"
goto end

:error
echo An error occurred.
goto end

:end


