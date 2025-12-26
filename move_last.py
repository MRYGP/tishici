# -*- coding: utf-8 -*-
import os
import shutil
import glob
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

target_dir = "参考文档和资料"

# 找到最后一个文件
files = glob.glob('*认知引力理论*')
for filename in files:
    if os.path.exists(filename) and not filename.startswith('参考文档和资料'):
        try:
            target_path = os.path.join(target_dir, os.path.basename(filename))
            shutil.move(filename, target_path)
            print("Moved:", filename)
        except Exception as e:
            print("Failed:", str(e))

