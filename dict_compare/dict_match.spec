# -*- mode: python -*-

block_cipher = None


a = Analysis(['dict_match.py', 'xls_process.py', 'cj_pic.py', 'pic_gen.py'],
             pathex=['C:\\Users\\Administrator\\Desktop\\cj_small_progs\\dict_compare'],
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
          name='dict_match',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
