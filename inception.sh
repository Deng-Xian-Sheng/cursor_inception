#!/bin/bash

# 封装Python脚本到Shell脚本中
PYTHON_SCRIPT=$(cat <<'EOF'
import os
import platform
import subprocess
import tempfile

def open_editor_and_get_input():
    with tempfile.NamedTemporaryFile(delete=False, mode='w+', suffix='.txt') as tmp:
        tmp_path = tmp.name

    try:
        system_type = platform.system()
        if system_type in ['Linux', 'Darwin']:
            editor = os.environ.get('EDITOR', 'vim')
            subprocess.run([editor, tmp_path])
        elif system_type == 'Windows':
            subprocess.run(['notepad', tmp_path])
        else:
            raise OSError(f"Unsupported OS: {system_type}")

        with open(tmp_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print("\n用户输入的内容：\n")
            print(content)
    finally:
        os.unlink(tmp_path)

if __name__ == '__main__':
    open_editor_and_get_input()
EOF
)

# 执行Python代码
python3 -c "$PYTHON_SCRIPT"
