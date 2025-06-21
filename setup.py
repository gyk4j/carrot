from cx_Freeze import setup

build_exe_options = {
    "excludes": ["unittest"],
    "includes": ["pyvips"],
    "include_files": [
        "lib64/libvips"
    ],
    "zip_include_packages": ["tkinter"],    
}

setup(
    name="carrot",
    version="0.0.1",
    description="carrot",
    options={"build_exe": build_exe_options},
    executables=[{"script": "src/carrot/carrot.py", "base": "gui"}],
)
