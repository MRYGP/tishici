# -*- coding: utf-8 -*-
"""
提交简化后的更改
"""
import subprocess
import os

os.chdir(r'e:\提示词')

# Git add
print("Adding all changes...")
subprocess.run(['git', 'add', '-A'], capture_output=True)
print("Done")

# Git commit
commit_message = """refactor: simplify structure - keep only 4 core prompts

- Remove 01-商业学习系统 directory structure
- Create Commercial-Case-Analysis-Prompts folder
- Move 4 core prompts to new folder:
  - Claude-案例拆解提示词v1.0.md
  - Claude-模型提炼提示词v1.0.md
  - Claude-洞察归纳提示词v1.0.md
  - Cursor-文档生成指令v1.0.md
- Restore README.md to previous version
"""

print("Committing...")
result = subprocess.run(['git', 'commit', '-m', commit_message], 
                       capture_output=True, text=True, encoding='utf-8', errors='ignore')
if result.returncode == 0:
    print("Commit successful!")
else:
    print("Commit output:", result.stdout if result.stdout else "No output")

print("\nDone! Structure simplified.")

