# 极简英语单词学习器 / Simple Vocabulary Trainer

一个简洁、易用的桌面英语单词学习应用程序。

A minimalist and user-friendly desktop application for learning English vocabulary.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-blue.svg)

## ✨ 特性 / Features

- 🎯 **简洁界面** - 极简设计，专注学习
- 📚 **自定义词库** - 支持导入自己的单词列表
- 🔄 **智能复习** - 可设置复习周期
- 🎲 **随机学习** - 随机显示单词，避免记忆顺序
- ⚙️ **灵活设置** - 可调整窗口大小、显示模式等
- 📁 **多格式支持** - 支持多种分隔符和编码格式

## 🚀 快速开始 / Quick Start

### 方式一：直接运行 exe（Windows用户）

1. 下载 `dist/英语学习器_极简版.exe`
2. 双击运行即可

### 方式二：从源码运行

```bash
# 克隆仓库
git clone https://github.com/yourusername/simple-vocab-trainer.git
cd simple-vocab-trainer

# 运行程序
python main.py
```

## 📖 使用说明 / Usage

### 单词文件格式

支持以下分隔符之一：
- 制表符（Tab）：`word	meaning`
- 空格：`word  meaning`
- 分号：`word;meaning`
- 竖线：`word|meaning`

示例文件（cet4.txt）：
```
access	v. 获取 n. 接近，入口
project	n. 工程；课题、作业
intention	n. 打算，意图
strategy	n. 策略，战略
```

### 功能说明

1. **导入按钮** - 导入自定义单词文件
2. **设置按钮** - 打开设置窗口
   - 复习天数：设置复习周期（1-30天）
   - 显示单词释义：控制是否显示释义
   - 窗口大小：自定义窗口宽度和高度
3. **上一个/下一个** - 浏览单词（下一个为随机）

## 🛠️ 技术栈 / Tech Stack

- **Python 3.6+**
- **Tkinter** - GUI界面
- **PyInstaller** - 打包成exe

## 📦 打包说明 / Build

如需自己打包成exe：

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包
python -m PyInstaller --onefile --windowed --name "英语学习器_极简版" --add-data "data;data" main.py --clean
```

生成的exe文件在 `dist` 目录下。

## 📝 项目结构 / Project Structure

```
simple-vocab-trainer/
├── main.py              # 主程序
├── data/
│   └── cet4.txt        # CET-4词汇数据
├── dist/               # 打包后的exe文件
├── README.md           # 项目说明
├── LICENSE             # 许可证
└── .gitignore          # Git忽略文件
```

## 🤝 贡献 / Contributing

欢迎提交 Issue 和 Pull Request！

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 许可证 / License

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 致谢 / Acknowledgments

- CET-4词汇数据来源于公开资源
- 感谢所有贡献者

---

**Enjoy Learning! 📚✨**
