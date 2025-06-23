import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "excludes": ["unittest"],
    "includes": ["pyvips"],
    "include_files": [
        "lib64/libvips/libglib-2.0-0.dll",
        "lib64/libvips/libgobject-2.0-0.dll",
        "lib64/libvips/libvips-42.dll",
        "lib64/libvips/libvips-cpp-42.dll",
    ],
    # "bin_path_includes": ["lib64/libvips"],
    # "bin_includes": [
        # "libglib-2.0-0.dll",
        # "libgobject-2.0-0.dll",
        # "libvips-42.dll",
        # "libvips-cpp-42.dll",
    # ],
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="carrot",
    version="0.0.1",
    description="carrot",
    options={"build_exe": build_exe_options},
    executables=[Executable("src/carrot/carrot.py", base=base)],
)