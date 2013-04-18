# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'vcexportmanager.pyw'],
             pathex=['d:\\Users\\lgsatellital\\Documents\\02-msys\\D00737824\\src\\vcexportmanager\\src'])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\vcexportmanager', 'vcexportmanager.exe'),
          debug=False,
          strip=True,
          upx=True,
          console=False )
coll = COLLECT( exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=True,
               upx=True,
               name=os.path.join('dist', 'vcexportmanager'))
app = BUNDLE(coll,
             name=os.path.join('dist', 'vcexportmanager.app'))
