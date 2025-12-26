# -*- coding: utf-8 -*-
import os
import shutil
import sys

# 设置输出编码为UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 创建目标文件夹
target_dir = "参考文档和资料"
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 需要移动的文件列表
files_to_move = [
    "双循环说明书.md",
    "Token优化系统.md",
    "CEET理论体系最终整合与标准化SOP.md",
    r'CEET理论打磨的"六段式熔炉"SOP v2.0.md',
    "CST理论消化与认知OS内化——双循环引导系统升级版8.8日.md",
    "原始提示词参考文档.md",
    r'认知引力理论"旗舰论文重构终极指令 v2.0.md',
    "文档分类分析报告.md",
    "重复文档分析报告.md",
    "提示词系统化升级方案.md",
    "（20230801）精品提示词分享-无水印版.pdf",
    "精品提示词分享（0725）.pdf",
    "提示词工程师公开课.pdf"
]

# 移动文件
moved = []
failed = []

for filename in files_to_move:
    if os.path.exists(filename):
        try:
            target_path = os.path.join(target_dir, filename)
            shutil.move(filename, target_path)
            moved.append(filename)
            print(f"OK: {filename}")
        except Exception as e:
            failed.append((filename, str(e)))
            print(f"FAIL: {filename} - {e}")
    else:
        print(f"NOT FOUND: {filename}")

print(f"\nTotal: {len(moved)} moved, {len(failed)} failed")

