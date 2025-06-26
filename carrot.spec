# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    [
        'src/carrot/app.py',
        'src/carrot/controller/controller.py',
        'src/carrot/model/model.py',
        'src/carrot/view/imageview.py',
        'src/carrot/view/menu.py',
        'src/carrot/view/menubar.py',
        'src/carrot/view/menuitem.py',
        'src/carrot/view/statusbar.py',
        'src/carrot/view/statusbarpane.py',
        'src/carrot/view/toolbar.py',
        'src/carrot/view/toolbarbutton.py',
        'src/carrot/view/tooltip.py',
        'src/carrot/view/view.py',
        'src/carrot/view/window.py',
    ],
    pathex=['./src/carrot'],
    binaries=[("lib64/libvips", ".")],
    datas=
    [
        ('res/ico/*.png', 'res/ico'),
        ('*.jpg', '.'),
    ],
    hiddenimports=
    [
        'controller.controller',
        'model.model',
        'view.imageview',
        'view.menu',
        'view.menubar',
        'view.menuitem',
        'view.statusbar',
        'view.statusbarpane',
        'view.toolbar',
        'view.toolbarbutton',
        'view.tooltip',
        'view.view',
        'view.window',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='carrot',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='carrot',
)
