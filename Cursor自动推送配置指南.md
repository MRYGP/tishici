# Cursor自动推送配置指南

## 方法1：使用Git Hooks（推荐）

### 方案A：Post-Commit Hook（提交后自动推送）

**创建文件**：`.git/hooks/post-commit`

```bash
#!/bin/sh
# 自动推送脚本
git push origin main
```

**Windows PowerShell版本**（`.git/hooks/post-commit`）：
```powershell
#!/usr/bin/env pwsh
git push origin main
```

**设置执行权限**（Linux/Mac）：
```bash
chmod +x .git/hooks/post-commit
```

### 方案B：Pre-Push Hook（推送前检查）

**创建文件**：`.git/hooks/pre-push`

```bash
#!/bin/sh
# 推送前自动检查编码
git config --global core.quotepath false
git config --global i18n.commitencoding utf-8
git config --global i18n.logoutputencoding utf-8
```

---

## 方法2：使用Git配置（自动推送）

### 配置Git自动推送

```bash
# 设置自动推送（每次commit后自动push）
git config --global push.autoSetupRemote true
git config --global push.default simple
```

### 创建别名（快捷命令）

```bash
# 创建"提交并推送"的别名
git config --global alias.cp "!f() { git commit -m \"$1\" && git push; }; f"

# 使用方式：
# git cp "提交信息"
```

---

## 方法3：使用Cursor的Git集成

### Cursor设置

1. **打开Cursor设置**：`Ctrl+,` 或 `Cmd+,`
2. **搜索"Git"**
3. **启用以下选项**：
   - `Git: Auto Fetch` - 自动获取远程更新
   - `Git: Auto Stash` - 自动暂存更改
   - `Git: Enable` - 启用Git集成

### Cursor命令面板

使用快捷键：
- `Ctrl+Shift+P` (Windows) 或 `Cmd+Shift+P` (Mac)
- 输入 "Git: Push" 或 "Git: Sync"

---

## 方法4：使用PowerShell脚本（Windows）

### 创建自动推送脚本

**文件**：`auto-push.ps1`

```powershell
# 自动推送脚本
param(
    [string]$message = "Auto commit and push"
)

# 配置编码
git config --global core.quotepath false
git config --global i18n.commitencoding utf-8
git config --global i18n.logoutputencoding utf-8

# 添加所有更改
git add .

# 提交
git commit -m $message

# 推送
git push origin main

Write-Host "✅ 推送完成！" -ForegroundColor Green
```

**使用方法**：
```powershell
.\auto-push.ps1 "提交信息"
```

---

## 方法5：使用Git别名（最简单）

### 创建"提交并推送"别名

```bash
# 创建别名
git config --global alias.acp '!f() { git add -A && git commit -m "$1" && git push; }; f'

# 使用方式：
# git acp "提交信息"
```

### 创建"快速推送"别名

```bash
# 只推送，不提交
git config --global alias.p 'push origin main'

# 使用方式：
# git p
```

---

## 方法6：Cursor任务配置（.vscode/tasks.json）

**创建文件**：`.vscode/tasks.json`

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Git: Add, Commit & Push",
            "type": "shell",
            "command": "git add . && git commit -m '${input:commitMessage}' && git push origin main",
            "problemMatcher": [],
            "presentation": {
                "reveal": "always",
                "panel": "new"
            }
        },
        {
            "label": "Git: Push Only",
            "type": "shell",
            "command": "git push origin main",
            "problemMatcher": [],
            "presentation": {
                "reveal": "always"
            }
        }
    ],
    "inputs": [
        {
            "id": "commitMessage",
            "type": "promptString",
            "description": "请输入提交信息"
        }
    ]
}
```

**使用方法**：
- `Ctrl+Shift+P` → 输入 "Tasks: Run Task" → 选择 "Git: Add, Commit & Push"

---

## 方法7：使用Git Credential Helper（避免重复输入token）

### 配置Credential Helper

```bash
# Windows
git config --global credential.helper wincred

# 或者使用store（将token保存到文件）
git config --global credential.helper store
```

### 使用Token（已配置）

Token已配置到远程URL，无需重复输入。

---

## 🎯 推荐方案

### 最简单：使用Git别名

```bash
# 一键配置
git config --global alias.acp '!f() { git add -A && git commit -m "$1" && git push origin main; }; f'

# 使用
git acp "feat: 更新内容"
```

### 最自动化：使用Post-Commit Hook

创建 `.git/hooks/post-commit` 文件，每次commit后自动push。

### 最灵活：使用Cursor任务

配置 `.vscode/tasks.json`，通过命令面板执行。

---

## ⚠️ 注意事项

1. **自动推送的风险**：
   - 可能推送未完成的代码
   - 建议只在特定分支使用
   - 或添加检查机制

2. **网络问题**：
   - 如果网络不稳定，自动推送可能失败
   - 建议添加重试机制

3. **Token安全**：
   - Token已配置在URL中
   - 注意不要将包含token的URL提交到代码库
   - 建议使用Git Credential Helper

---

## 🔧 故障排除

### 如果自动推送失败

1. **检查网络连接**：
   ```bash
   ping github.com
   ```

2. **检查远程配置**：
   ```bash
   git remote -v
   ```

3. **手动推送测试**：
   ```bash
   git push origin main
   ```

4. **查看详细错误**：
   ```bash
   git push origin main -v
   ```

---

## 📝 完整配置示例

### 一键配置脚本（Windows PowerShell）

```powershell
# 配置Git自动推送
git config --global core.quotepath false
git config --global i18n.commitencoding utf-8
git config --global i18n.logoutputencoding utf-8
git config --global push.autoSetupRemote true
git config --global alias.acp '!f() { git add -A && git commit -m "$1" && git push origin main; }; f'
git config --global alias.p 'push origin main'

Write-Host "✅ Git自动推送配置完成！" -ForegroundColor Green
Write-Host "使用方式：git acp '提交信息' 或 git p" -ForegroundColor Yellow
```

保存为 `setup-auto-push.ps1` 并运行即可。
