# 上传到 GitHub 指南

## 准备工作

### 1. 需要上传的文件
```
✅ main.py              - 主程序（已添加完整注释）
✅ README.md            - 项目说明文档
✅ LICENSE              - MIT许可证
✅ .gitignore           - Git忽略文件
✅ requirements.txt     - 依赖说明
✅ data/cet4.txt        - CET-4词汇数据
```

### 2. 不需要上传的文件（已在 .gitignore 中）
```
❌ build/               - 构建临时文件
❌ dist/                - 打包后的exe文件
❌ *.spec               - PyInstaller配置文件
❌ *.docx               - Word文档
❌ __pycache__/         - Python缓存
```

## 上传步骤

### 方法一：使用 GitHub Desktop（推荐新手）

1. 下载并安装 [GitHub Desktop](https://desktop.github.com/)
2. 登录你的GitHub账号
3. 点击 File → Add Local Repository
4. 选择 `c:\Users\KING\Desktop\英语插件` 文件夹
5. 点击 "Publish repository"
6. 输入仓库名称：`simple-vocab-trainer`
7. 添加描述（可选）
8. 取消勾选 "Keep this code private"（如果想公开）
9. 点击 "Publish repository"

### 方法二：使用命令行

```bash
# 1. 进入项目目录
cd "c:\Users\KING\Desktop\英语插件"

# 2. 初始化 Git 仓库
git init

# 3. 添加所有文件
git add .

# 4. 提交
git commit -m "Initial commit: Simple Vocabulary Trainer v1.0"

# 5. 在GitHub网站创建新仓库后，关联远程仓库
git remote add origin https://github.com/你的用户名/simple-vocab-trainer.git

# 6. 推送到GitHub
git branch -M main
git push -u origin main
```

### 方法三：直接在 GitHub 网站上传

1. 登录 [GitHub](https://github.com)
2. 点击右上角 "+" → "New repository"
3. 输入仓库名：`simple-vocab-trainer`
4. 添加描述：`一个简洁的桌面英语单词学习应用 / A minimalist vocabulary learning app`
5. 选择 Public（公开）或 Private（私有）
6. 不要勾选 "Initialize this repository with a README"
7. 点击 "Create repository"
8. 在新页面选择 "uploading an existing file"
9. 拖拽文件到浏览器上传

## 上传后的工作

### 1. 添加 Release（发布版本）

1. 在仓库页面点击 "Releases" → "Create a new release"
2. Tag version: `v1.0`
3. Release title: `v1.0 - 首次发布 / Initial Release`
4. 上传 `dist/英语学习器_极简版.exe` 作为附件
5. 点击 "Publish release"

### 2. 添加主题标签（Topics）

建议添加以下标签：
- `vocabulary-trainer`
- `english-learning`
- `python`
- `tkinter`
- `desktop-app`
- `learning-tool`

### 3. 添加项目描述

在仓库首页点击齿轮图标，添加：
```
一个简洁的桌面英语单词学习应用 | A minimalist vocabulary learning app
```

## 仓库地址示例

上传成功后，你的项目地址应该是：
```
https://github.com/你的用户名/simple-vocab-trainer
```

## 分享项目

可以通过以下方式分享：
- 直接分享仓库链接
- 在 README.md 中添加使用截图
- 添加到你的个人主页
- 发布到相关社区

## 注意事项

1. ✅ 确保 `.gitignore` 正确配置，避免上传临时文件
2. ✅ 检查代码中是否有敏感信息（密码、密钥等）
3. ✅ 确保 LICENSE 文件存在
4. ✅ README.md 内容完整、格式正确
5. ✅ 代码注释清晰完整

## 后续维护

### 更新代码
```bash
git add .
git commit -m "描述你的更改"
git push
```

### 创建新版本
每次重大更新后，创建新的 Release 并上传新的 exe 文件。

---

祝你的项目成功！🎉
