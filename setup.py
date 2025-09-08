import sys
from cx_Freeze import setup, Executable

sys.path.append("src/carrot")

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    # "replace_paths": [("*","src/")],
    "packages": ["model", "view", "controller"],
    "excludes": ["unittest"],
    "includes": ["pyvips"],
    "include_files": [
        "lib64/libvips/libglib-2.0-0.dll",
        "lib64/libvips/libgobject-2.0-0.dll",
        "lib64/libvips/libvips-42.dll",
        "lib64/libvips/libvips-cpp-42.dll",
        ("res/ico/file_exit.png", "_internal/res/ico/file_exit.png"),
        ("res/ico/file_exit_24.png", "_internal/res/ico/file_exit_24.png"),
        ("res/ico/file_export.png", "_internal/res/ico/file_export.png"),
        ("res/ico/file_export_24.png", "_internal/res/ico/file_export_24.png"),
        ("res/ico/file_new.png", "_internal/res/ico/file_new.png"),
        ("res/ico/file_new_24.png", "_internal/res/ico/file_new_24.png"),
        ("res/ico/file_open.png", "_internal/res/ico/file_open.png"),
        ("res/ico/file_open_24.png", "_internal/res/ico/file_open_24.png"),
        ("res/ico/file_save.png", "_internal/res/ico/file_save.png"),
        ("res/ico/file_saveas.png", "_internal/res/ico/file_saveas.png"),
        ("res/ico/file_saveas_24.png", "_internal/res/ico/file_saveas_24.png"),
        ("res/ico/file_save_24.png", "_internal/res/ico/file_save_24.png"),
        ("res/ico/go_back.png", "_internal/res/ico/go_back.png"),
        ("res/ico/go_back_16.png", "_internal/res/ico/go_back_16.png"),
        ("res/ico/go_back_24.png", "_internal/res/ico/go_back_24.png"),
        ("res/ico/go_forward.png", "_internal/res/ico/go_forward.png"),
        ("res/ico/go_forward_24.png", "_internal/res/ico/go_forward_24.png"),
        ("res/ico/help_about_24.png", "_internal/res/ico/help_about_24.png"),
        ("res/ico/help_about_32.png", "_internal/res/ico/help_about_32.png"),
        ("res/ico/help_view.png", "_internal/res/ico/help_view.png"),
        ("res/ico/help_view_24.png", "_internal/res/ico/help_view_24.png"),
        ("res/ico/selection_contract.png", "_internal/res/ico/selection_contract.png"),
        ("res/ico/selection_contract_24.png", "_internal/res/ico/selection_contract_24.png"),
        ("res/ico/selection_expand.png", "_internal/res/ico/selection_expand.png"),
        ("res/ico/selection_expand_24.png", "_internal/res/ico/selection_expand_24.png"),
        ("res/ico/selection_mark.png", "_internal/res/ico/selection_mark.png"),
        ("res/ico/selection_mark_24.png", "_internal/res/ico/selection_mark_24.png"),
        ("0.jpg", "_internal/0.jpg"),
        ("1.jpg", "_internal/1.jpg"),
        ("2.jpg", "_internal/2.jpg"),
        ("3.jpg", "_internal/3.jpg"),
        ("4.jpg", "_internal/4.jpg"),
        ("5.jpg", "_internal/5.jpg"),
        ("6.jpg", "_internal/6.jpg"),
        ("7.jpg", "_internal/7.jpg"),
        ("8.jpg", "_internal/8.jpg"),
    ],
    # "bin_path_includes": ["lib64/libvips"],
    # "bin_includes": [
        # "libglib-2.0-0.dll",
        # "libgobject-2.0-0.dll",
        # "libvips-42.dll",
        # "libvips-cpp-42.dll",
    # ],
    "silent": True,
    "silent_level": 1,
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="carrot",
    version="0.0.1",
    description="carrot",
    options={"build_exe": build_exe_options},
    executables=[Executable("src/carrot/app.py", base=base)],
)