"""
获取指定目录下文件的名称
"""

import os

count = 0
for files in os.listdir(r"C:\Users\Zen\Desktop\实训\505day2"):
    print(files)
    count += 1
print("总共",count,"个")