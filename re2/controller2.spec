# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['controller2.py','controller.py','controller3.py','UI.py','UI2.py','UI3.py','yolo_img.py','read_img.py','main2.py'],
    pathex=[],
    binaries=[],
    datas=[('yolov7-tiny_last2.weights','.'),('yolov7-tiny.cfg','.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='controller2',
    debug=False,
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
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='controller2',
)
