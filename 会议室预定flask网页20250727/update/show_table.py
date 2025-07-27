import sqlite3
import pandas as pd
### (meet1) D:\JupyterRoot\A\华为\会议室预定flask网页20250727>
#  python show_table.py
conn = sqlite3.connect("instance/meeting_rooms.db")
cursor = conn.cursor()

# 查看所有表名
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for table in tables:
    table_name = table[0]
    print(f"\n--- {table_name} ---")
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    print(df)

conn.close()


# 步骤如下：
# 1、安装 SQLite 浏览工具（任选其一）
# DB Browser for SQLite

# 2、使用 Python 自带的 sqlite3 模块也可以
# Python 脚本查看表数据
# 如果你在项目根目录（有 instance/meeting_rooms.db）下，可使用如下代码查看所有表

# 3、结果输出示例
# 执行后你会看到控制台中每张表的内容，比如：
# 
# 

# (meet1) D:\JupyterRoot\A\华为\会议室预定flask网页20250727>python show_table.py

# --- role ---
#    id   name
# 0   1  admin
# 1   2   user

# --- equipment ---
#    id    name
# 0   1     投影仪
# 1   2    电子白板
# 2   3  视频会议系统
# 3   4    音响系统
# 4   5      电视
# 5   6      空调

# --- room ---
#    id  name location  capacity description  is_active
# 0   1  会议室A       1楼        10       小型会议室          1
# 1   2  会议室B       2楼        20       中型会议室          1
# 2   3  会议室C       3楼         5       小型洽谈室          1
# 3   4  会议室D       4楼        50       大型会议室          1

# --- user ---
#    id username              email                                      password_hash department       phone  role_id
# 0   1    admin  admin@example.com  pbkdf2:sha256:260000$xZp1JSJkjgx1KoO3$cbb165da...        管理部  1234567890        1

# --- room_equipment ---
#     id  room_id  equipment_id  quantity
# 0    1        1             1         1
# 1    2        1             2         1
# 2    3        1             6         1
# 3    4        2             1         1
# 4    5        2             2         1
# 5    6        2             3         1
# 6    7        2             4         1
# 7    8        2             6         1
# 8    9        3             5         1
# 9   10        3             6         1
# 10  11        4             1         1
# 11  12        4             2         1
# 12  13        4             3         1
# 13  14        4             4         1
# 14  15        4             6         1

# --- reservation ---
#    id  title        date       start_time  ...     status                  created_at user_id room_id
# 0   1  养猫的讨论  2025-05-27  10:30:00.000000  ...   canceled  2025-05-26 12:26:23.722080       1       3
# 1   2  华为605  2025-07-28  10:00:00.000000  ...  confirmed  2025-07-27 13:49:18.574661       1       1

# [2 rows x 11 columns]

# --- maintenance ---
# Empty DataFrame
# Columns: [id, room_id, start_date, end_date, reason, created_by, created_at]
# Index: []

# --- reservation_document ---
# Empty DataFrame
# Columns: [id, filename, stored_filename, file_type, file_size, upload_time, reservation_id, uploaded_by]
# Index: []
