# SQLite 数据库 meeting_rooms.db，下面我会根据你提供的字段结构说明你如何：

# ✅ 修改 room 表：
# 包括：
# 删除会议室 C、D；
# 新增一个会议室：id=10, name=华为A, location=6楼A, capacity=20, description=中型会议室, is_active=1。
# 

import sqlite3
print("修改开始")
### (meet1) D:\JupyterRoot\A\华为\会议室预定flask网页20250727>
#  python update_db.py
# 连接数据库
conn = sqlite3.connect("instance/meeting_rooms.db")
cursor = conn.cursor()

# 1. 删除会议室 C、D（根据 name）
cursor.execute("DELETE FROM room WHERE name IN ('会议室C', '会议室D')")

# 2. 插入新的会议室记录
cursor.execute("""
    INSERT INTO room (id, name, location, capacity, description, is_active)
    VALUES (?, ?, ?, ?, ?, ?)
""", (10, '华为A', '6楼A', 20, '中型会议室', 1))

# 提交更改并关闭连接
conn.commit()
conn.close()
print("修改成功")
