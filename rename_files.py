import os
import re
from pathlib import Path

# 已接受資料夾 - 添加 ~ 標記
accepted_dir = Path('已接受')
for file in accepted_dir.rglob('*'):
    if file.is_file() and file.name.startswith('['):
        # 如果檔名已經包含 -X 就跳過
        if  '-X' in file.name:
            continue
        
        # 從 [情緒] 改為 [情緒-X]~
        match = re.match(r'^\[([^\]]+)\](.+)$', file.name)
        if match:
            emotion, rest = match.groups()
            new_name = f'[{emotion}-X]~{rest}'
            new_path = file.parent / new_name
            
            print(f'重新命名: {file.name} -> {new_name}')
            try:
                file.rename(new_path)
            except Exception as e:
                print(f'錯誤: {e}')

# 待嘗試資料夾 - 只添加 -X
try_dir = Path('待嘗試')
for file in try_dir.rglob('*'):
    if file.is_file():
        # 如果檔名已經包含 -X 就跳過
        if '-X' in file.name:
            continue
        
        # 從 [情緒] 改為 [情緒-X]
        match = re.match(r'^\[([^\]]+)\](.+)$', file.name)
        if match:
            emotion, rest = match.groups()
            new_name = f'[{emotion}-X]{rest}'
            new_path = file.parent / new_name
            
            print(f'重新命名: {file.name} -> {new_name}')
            try:
                file.rename(new_path)
            except Exception as e:
                print(f'錯誤: {e}')
        elif not file.name.startswith('['):
            # 處理沒有標籤的檔案
            print(f'需要手動分類: {file.name}')

print('\n完成!')

