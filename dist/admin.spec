# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['admin.py', 'Adminbutton.png', 'Adminbutton.png', 'backbutton.png', 'exitbutton.png', 'halo_shield.png', 'leveler.png', 'nextbutton.png', 'nextt.png', 'questions_answers.json', 'user_awareness1.png', 'user_responses.json', 'start.png', 'UserXP.py'],
             pathex=['C:\\Users\\david\\OneDrive\\Documents\\Python Scripts\\SANS SURVEY APP UPDATE V2\\dist'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='admin',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='halo_shield.ico')
