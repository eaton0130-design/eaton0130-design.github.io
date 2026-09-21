import os
from datetime import datetime

# 設定你要掃描的資料夾路徑（'.' 代表目前腳本所在的資料夾）
target_folder = '.'

for root, dirs, files in os.walk(target_folder):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            
            # 讀取原本的檔案內容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 檢查是否已經有 Front Matter，避免重複加入
            if content.startswith('---\n') or content.startswith('---\r\n'):
                print(f"跳過（已有 Front Matter）: {file}")
                continue
            
            # 取得不含副檔名的檔名，作為預設 title
            title = os.path.splitext(file)[0]
            # 取得目前的日期
            current_date = datetime.now().strftime('%Y-%m-%d')
            
            # 定義你要加入的 Front Matter 內容
            front_matter = f"""---
title: "{title}"
date: {current_date}
draft: false
tags: []
---

"""
            # 將 Front Matter 組合並寫回檔案
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(front_matter + content)
                
            print(f"已成功加入: {file}")
