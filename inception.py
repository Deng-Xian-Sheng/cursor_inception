import os
import platform
import subprocess
import tempfile
import shutil

def open_editor_and_get_input():
    with tempfile.NamedTemporaryFile(delete=False, mode='w+', suffix='.txt') as tmp:
        tmp_path = tmp.name

    try:
        system_type = platform.system()

        if system_type == 'Darwin':
            # macOS 使用 open
            subprocess.run(['open', tmp_path])
        elif system_type == 'Linux':
            # Linux 优先使用 xdg-open，再尝试 gio open
            if shutil.which('xdg-open'):
                subprocess.run(['xdg-open', tmp_path])
            elif shutil.which('gio'):
                subprocess.run(['gio', 'open', tmp_path])
            else:
                raise OSError("No suitable text editor launcher found (xdg-open or gio).")
        elif system_type == 'Windows':
            subprocess.run(['notepad', tmp_path])
        else:
            raise OSError(f"Unsupported OS: {system_type}")

        input("编辑器已打开，请编辑文件并保存后按 Enter 键继续...")

        with open(tmp_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print("\n用户输入的内容：\n")
            print(content)
    finally:
        os.unlink(tmp_path)

if __name__ == '__main__':
    open_editor_and_get_input()
