Билд в exe файл осуществляется командой:
pyinstaller -y --clean
--additional-hooks-dir extra-hooks
--hiddenimport pulp main.py --onefile
--collect-data pulp
