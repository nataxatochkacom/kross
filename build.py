# build.py

import sys
import subprocess

if len(sys.argv) < 2:
    print("Использование: python build.py [desktop|web]")
    sys.exit(1)

target = sys.argv[1]

if target == "desktop":
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--windowed",
        "gui_main.py"
    ])

elif target == "web":
    print("Web/WASM версия запускается через браузер")
    print("Откройте файл index.html через HTTP сервер, например:")
    print("python3 -m http.server")


else:
    print("Неизвестная цель сборки")
