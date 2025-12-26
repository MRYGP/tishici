# -*- coding: utf-8 -*-
import os
import shutil
import glob

target_dir = "参考文档和资料"

# 使用glob找到包含特殊字符的文件
files = [
    glob.glob('*六段式熔炉*')[0] if glob.glob('*六段式熔炉*') else None,
    glob.glob('*认知引力理论*')[0] if glob.glob('*认知引力理论*') else None
]

for filename in files:
    if filename and os.path.exists(filename):
        try:
            target_path = os.path.join(target_dir, os.path.basename(filename))
            shutil.move(filename, target_path)
            print(f"Moved: {filename}")
        except Exception as e:
            print(f"Failed: {filename} - {e}")

