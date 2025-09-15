#!/bin/sh

# Requires `source .venv/Scripts/activate` to set the virtual environment.

call_pyinstaller()
{
    pyinstaller --noconfirm --log-level WARN pyinstaller.spec
    
    if [ $? -gt 0 ]
    then
        error
    fi
    
    if [ -e dist/carrot/carrot.exe ]
    then
        ./dist/carrot/carrot.exe &
    fi
}

call_cx_Freeze()
{  
    py setup.py build
    
    if [ $? -gt 0 ]
    then
        error
    fi
    
    if [ -e build/exe.win-amd64-3.8/carrot.exe ]
    then
        ./build/exe.win-amd64-3.8/carrot.exe &
    fi
}

error()
{
    echo "An error occurred."
}

call_pyinstaller
call_cx_Freeze
