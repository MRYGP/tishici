# -*- coding: utf-8 -*-
"""
执行最终的Git提交
"""
import subprocess
import os

os.chdir(r'e:\提示词')

# Git add
print("Adding files...")
result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
if result.returncode == 0:
    print("Files added successfully")
else:
    print("Error:", result.stderr)

# Git commit
commit_message = """refactor: 重组目录结构，新增商业学习系统

- 创建01-商业学习系统一级目录
- 完成"张潇雨商业案例课改编"项目完整架构
- 新增4个核心提示词（案例拆解、模型提炼、洞察归纳、文档生成）
- 创建完整的三层系统（Claude分析 → Cursor文档 → GitHub知识库）
- 补充15个README和索引文件
- 更新仓库根目录README

目录结构：
- 01-商业学习系统/张潇雨商业案例课改编/
  - 00_系统指令/（4个核心提示词）
  - 01_案例库/（按行业/模型/生命周期分类）
  - 02_模型库/（战略/运营/财务模型）
  - 03_洞察库/（跨案例洞察/行业趋势）
  - 04_原著笔记/
  - 05_学习记录/
"""

print("\nCommitting...")
result = subprocess.run(['git', 'commit', '-m', commit_message], 
                       capture_output=True, text=True, encoding='utf-8', errors='ignore')
if result.returncode == 0:
    print("Commit successful!")
    print(result.stdout)
else:
    if "nothing to commit" in result.stdout:
        print("Nothing to commit")
    else:
        print("Error:", result.stderr)
        print("Output:", result.stdout)

print("\nDone! Commit completed, push not executed (waiting for user confirmation)")

