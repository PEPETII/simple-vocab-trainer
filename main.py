#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
极简英语单词学习工具
Simple Vocabulary Trainer

一个简洁的桌面英语单词学习应用，支持导入自定义单词列表。
A minimalist desktop application for learning English vocabulary with custom word list support.

作者: PEPETII
版本: 1.0
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import random
import os


class SimpleVocabTrainer:
    """
    单词学习器主类
    Main vocabulary trainer class with GUI interface
    """
    def __init__(self):
        """初始化应用程序 / Initialize the application"""
        self.root = tk.Tk()
        self.words = []  # 单词列表 / Word list
        self.current_index = 0  # 当前单词索引 / Current word index
        self.history = []  # 浏览历史 / Browse history
        self.show_meaning = True  # 是否显示释义 / Show meaning toggle
        self.review_days = 7  # 复习周期(天) / Review cycle in days
        self.window_width = 350  # 窗口宽度 / Window width
        self.window_height = 250  # 窗口高度 / Window height
        
        self.setup_window()
        self.create_widgets()
        self.load_default_words()
    
    def setup_window(self):
        """设置窗口属性和居中显示 / Setup window properties and center it"""
        self.root.title("英语单词学习器")
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.resizable(False, False)
        
        # 窗口居中 / Center the window
        x = (self.root.winfo_screenwidth() - self.window_width) // 2
        y = (self.root.winfo_screenheight() - self.window_height) // 2
        self.root.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")
    
    def create_widgets(self):
        """创建所有UI组件 / Create all UI widgets"""
        # 顶部按钮
        top_frame = ttk.Frame(self.root)
        top_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(top_frame, text="设置", command=self.open_settings).pack(side=tk.LEFT)
        ttk.Button(top_frame, text="导入", command=self.import_file).pack(side=tk.LEFT, padx=(10, 0))
        
        # 单词显示区
        word_frame = ttk.LabelFrame(self.root, text="单词")
        word_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.word_label = ttk.Label(word_frame, font=("Arial", 16, "bold"), anchor=tk.CENTER)
        self.word_label.pack(pady=10)
        
        self.meaning_label = ttk.Label(word_frame, font=("Arial", 10), anchor=tk.CENTER, wraplength=300)
        self.meaning_label.pack(pady=(0, 10))
        
        # 底部按钮
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(btn_frame, text="上一个", command=self.prev_word).pack(side=tk.LEFT)
        ttk.Button(btn_frame, text="下一个", command=self.next_word).pack(side=tk.LEFT, padx=(10, 0))
    
    def load_default_words(self):
        """
        加载默认单词文件
        Load default word file from multiple possible locations
        """
        data_paths = [
            "data/cet4.txt",
            "cet4.txt", 
            os.path.join(os.path.dirname(__file__), "data", "cet4.txt"),
            os.path.join(os.path.dirname(__file__), "cet4.txt")
        ]
        
        for path in data_paths:
            if os.path.exists(path):
                if self.load_words_from_file(path):
                    return
        
        # 如果找不到文件，使用内置单词
        self.words = [
            {"word": "access", "meaning": "v. 获取 n. 接近，入口"},
            {"word": "project", "meaning": "n. 工程；课题、作业"},
            {"word": "intention", "meaning": "n. 打算，意图"},
            {"word": "strategy", "meaning": "n. 策略，战略"},
            {"word": "primary", "meaning": "adj. 主要的，基本的"}
        ]
        self.update_display()
    
    def load_words_from_file(self, file_path):
        """
        从文件加载单词数据
        Load word data from file
        
        支持的格式 / Supported formats:
        - 制表符分隔: word\tmeaning
        - 空格分隔: word  meaning
        - 分号分隔: word;meaning
        - 竖线分隔: word|meaning
        
        支持的编码 / Supported encodings: UTF-8, GBK
        
        Args:
            file_path: 文件路径 / File path
            
        Returns:
            bool: 加载是否成功 / Success status
        """
        try:
            # 尝试UTF-8
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except:
            try:
                # 尝试GBK
                with open(file_path, 'r', encoding='gbk') as f:
                    lines = f.readlines()
            except:
                return False
        
        self.words = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 尝试不同分隔符
            parts = None
            for sep in ['\t', '  ', ';', '|']:
                if sep in line:
                    parts = line.split(sep, 1)
                    break
            
            if parts and len(parts) >= 2:
                word = parts[0].strip()
                meaning = parts[1].strip()
                if word and meaning:
                    self.words.append({"word": word, "meaning": meaning})
        
        if self.words:
            self.current_index = 0
            self.history = [0]
            self.update_display()
            return True
        return False
    
    def update_display(self):
        """更新界面显示当前单词 / Update UI to display current word"""
        if not self.words:
            self.word_label.config(text="没有单词")
            self.meaning_label.config(text="")
            return
        
        word_data = self.words[self.current_index]
        self.word_label.config(text=word_data["word"])
        
        if self.show_meaning:
            self.meaning_label.config(text=word_data["meaning"])
        else:
            self.meaning_label.config(text="[在设置中开启显示释义]")
    
    def next_word(self):
        """随机显示下一个单词 / Display next random word"""
        if not self.words:
            return
        
        self.current_index = random.randint(0, len(self.words) - 1)
        self.history.append(self.current_index)
        if len(self.history) > 50:  # 限制历史记录
            self.history.pop(0)
        self.update_display()
    
    def prev_word(self):
        """返回上一个单词 / Go back to previous word"""
        if len(self.history) <= 1:
            return
        
        self.history.pop()
        self.current_index = self.history[-1]
        self.update_display()
    
    def open_settings(self):
        """打开设置窗口 / Open settings window"""
        settings_win = tk.Toplevel(self.root)
        settings_win.title("设置")
        settings_win.geometry("300x220")
        settings_win.resizable(False, False)
        settings_win.transient(self.root)
        settings_win.grab_set()
        
        frame = ttk.Frame(settings_win, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # 复习天数设置
        ttk.Label(frame, text="复习天数:").grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        days_var = tk.StringVar(value=str(self.review_days))
        ttk.Spinbox(frame, from_=1, to=30, width=8, textvariable=days_var).grid(row=0, column=1, padx=(10, 0), pady=(0, 10))
        
        # 显示释义
        show_var = tk.BooleanVar(value=self.show_meaning)
        ttk.Checkbutton(frame, text="显示单词释义", variable=show_var).grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=(0, 15))
        
        # 窗口大小
        ttk.Label(frame, text="宽度:").grid(row=2, column=0, sticky=tk.W)
        width_var = tk.StringVar(value=str(self.window_width))
        ttk.Spinbox(frame, from_=250, to=600, width=8, textvariable=width_var).grid(row=2, column=1, padx=(10, 0), pady=(0, 10))
        
        ttk.Label(frame, text="高度:").grid(row=3, column=0, sticky=tk.W)
        height_var = tk.StringVar(value=str(self.window_height))
        ttk.Spinbox(frame, from_=200, to=500, width=8, textvariable=height_var).grid(row=3, column=1, padx=(10, 0), pady=(0, 15))
        
        def save_settings():
            try:
                self.review_days = int(days_var.get())
                self.show_meaning = show_var.get()
                self.window_width = int(width_var.get())
                self.window_height = int(height_var.get())
                
                # 应用窗口大小
                self.root.geometry(f"{self.window_width}x{self.window_height}")
                
                self.update_display()
                messagebox.showinfo("设置", "设置已保存")
                settings_win.destroy()
            except:
                messagebox.showerror("错误", "请输入有效数值")
        
        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=4, column=0, columnspan=2)
        ttk.Button(btn_frame, text="保存", command=save_settings).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(btn_frame, text="取消", command=settings_win.destroy).pack(side=tk.LEFT)
    
    def import_file(self):
        """导入自定义单词文件 / Import custom word file"""
        file_path = filedialog.askopenfilename(
            title="选择单词文件",
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
        )
        
        if file_path and self.load_words_from_file(file_path):
            messagebox.showinfo("成功", "文件导入成功！")
        elif file_path:
            messagebox.showerror("错误", "文件格式不正确")
    
    def run(self):
        """启动主循环 / Start the main event loop"""
        self.root.mainloop()


if __name__ == "__main__":
    app = SimpleVocabTrainer()
    app.run()
    
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = SimpleVocabTrainer()
    app.run()