# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['home.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Programa git\\pyqt6\\database', 'database'), ('C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Programa git\\pyqt6\\database\\icons', 'database/icons'), ('C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Programa git\\pyqt6\\database\\image', 'database/image'), ('C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Programa git\\pyqt6\\database\\mensagem', 'database/mensagem'), ('C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Programa git\\pyqt6\\database\\template', 'database/template'), ('C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Programa git\\pyqt6\\database\\relatorio', 'database'), ('C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Programa git\\pyqt6\\database\\Nova pasta', 'database/Nova pasta'), ('C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Programa git\\pyqt6\\database\\Nova pasta', 'database/Nova pasta'), ('C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Programa git\\pyqt6\\database\\selenium', 'database/selenium'), ('C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Programa git\\pyqt6\\database\\template', 'database/template'), ('C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Programa git\\pyqt6\\database\\template\\comunicacao_padronizada', 'database/template/comunicacao_padronizada'), ('C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Programa git\\pyqt6\\database\\template\\relatorio_controle_pregao', 'database/template/relatorio_controle_pregao'), ('C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Programa git\\pyqt6\\controle_contratos', 'controle_contratos'), ('C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Programa git\\pyqt6\\controle_contratos\\data_contratos', 'controle_contratos/data_contratos'), ('C:\\Users\\guilh\\OneDrive\\Área de Trabalho\\Programa git\\pyqt6\\controle_contratos\\comunicacao_padronizada', 'controle_contratos/comunicacao_padronizada')],
    hiddenimports=['PyQt6', 'qdarkstyle', 'pdfplumber', 'openpyxl'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='home',
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
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='home',
)
