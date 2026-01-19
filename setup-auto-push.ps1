# Git自动推送配置脚本
# 运行此脚本将配置Git自动推送功能

Write-Host "正在配置Git自动推送..." -ForegroundColor Yellow

# 配置编码
git config --global core.quotepath false
git config --global i18n.commitencoding utf-8
git config --global i18n.logoutputencoding utf-8

# 配置自动推送
git config --global push.autoSetupRemote true
git config --global push.default simple

# 创建别名
git config --global alias.acp '!f() { git add -A && git commit -m "$1" && git push origin main; }; f'
git config --global alias.p 'push origin main'
git config --global alias.s 'status'
git config --global alias.l 'log --oneline -10'

Write-Host "`n✅ Git自动推送配置完成！" -ForegroundColor Green
Write-Host "`n可用命令：" -ForegroundColor Cyan
Write-Host "  git acp '提交信息'  - 添加、提交并推送" -ForegroundColor White
Write-Host "  git p                - 仅推送" -ForegroundColor White
Write-Host "  git s                - 查看状态" -ForegroundColor White
Write-Host "  git l                - 查看最近10条提交" -ForegroundColor White
