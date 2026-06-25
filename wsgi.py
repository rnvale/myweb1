# Render.com 部署使用该文件
# 命令: gunicorn backend.app:app

import sys
import os

# 将项目根目录添加到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
