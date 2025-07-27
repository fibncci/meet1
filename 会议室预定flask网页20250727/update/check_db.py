import sqlite3
#### 此文件 为查看 数据库的情况

conn = sqlite3.connect("instance/meeting_rooms.db")
cursor = conn.cursor()

# 获取所有表名
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("📋 所有表：", tables)

# 查看每个表的结构
for table in tables:
    print(f"\n表结构：{table[0]}")
    cursor.execute(f"PRAGMA table_info({table[0]});")
    for col in cursor.fetchall():
        print(col)

conn.close()


# (meet1) D:\JupyterRoot\A\华为\会议室预定flask网页20250727>python check_db.py
# 📋 所有表： [('role',), ('equipment',), ('room',), ('user',), ('room_equipment',), ('reservation',), ('maintenance',), ('reservation_document',)]

# 表结构：role
# (0, 'id', 'INTEGER', 1, None, 1)
# (1, 'name', 'VARCHAR(20)', 1, None, 0)

# 表结构：equipment
# (0, 'id', 'INTEGER', 1, None, 1)
# (1, 'name', 'VARCHAR(50)', 1, None, 0)

# 表结构：room
# (0, 'id', 'INTEGER', 1, None, 1)
# (1, 'name', 'VARCHAR(50)', 1, None, 0)
# (2, 'location', 'VARCHAR(100)', 1, None, 0)
# (3, 'capacity', 'INTEGER', 1, None, 0)
# (4, 'description', 'TEXT', 0, None, 0)
# (5, 'is_active', 'BOOLEAN', 0, None, 0)

# 表结构：user
# (0, 'id', 'INTEGER', 1, None, 1)
# (1, 'username', 'VARCHAR(50)', 1, None, 0)
# (2, 'email', 'VARCHAR(100)', 1, None, 0)
# (3, 'password_hash', 'VARCHAR(128)', 0, None, 0)
# (4, 'department', 'VARCHAR(100)', 0, None, 0)
# (5, 'phone', 'VARCHAR(20)', 0, None, 0)
# (6, 'role_id', 'INTEGER', 1, None, 0)

# 表结构：room_equipment
# (0, 'id', 'INTEGER', 1, None, 1)
# (1, 'room_id', 'INTEGER', 1, None, 0)
# (2, 'equipment_id', 'INTEGER', 1, None, 0)
# (3, 'quantity', 'INTEGER', 0, None, 0)

# 表结构：reservation
# (0, 'id', 'INTEGER', 1, None, 1)
# (1, 'title', 'VARCHAR(100)', 1, None, 0)
# (2, 'date', 'DATE', 1, None, 0)
# (3, 'start_time', 'TIME', 1, None, 0)
# (4, 'end_time', 'TIME', 1, None, 0)
# (5, 'attendees', 'INTEGER', 1, None, 0)
# (6, 'description', 'TEXT', 0, None, 0)
# (7, 'status', 'VARCHAR(20)', 0, None, 0)
# (8, 'created_at', 'DATETIME', 0, None, 0)
# (9, 'user_id', 'INTEGER', 1, None, 0)
# (10, 'room_id', 'INTEGER', 1, None, 0)

# 表结构：maintenance
# (0, 'id', 'INTEGER', 1, None, 1)
# (1, 'room_id', 'INTEGER', 1, None, 0)
# (2, 'start_date', 'DATE', 1, None, 0)
# (3, 'end_date', 'DATE', 1, None, 0)
# (4, 'reason', 'TEXT', 1, None, 0)
# (5, 'created_by', 'INTEGER', 1, None, 0)
# (6, 'created_at', 'DATETIME', 0, None, 0)

# 表结构：reservation_document
# (0, 'id', 'INTEGER', 1, None, 1)
# (1, 'filename', 'VARCHAR(255)', 1, None, 0)
# (2, 'stored_filename', 'VARCHAR(255)', 1, None, 0)
# (3, 'file_type', 'VARCHAR(50)', 0, None, 0)
# (4, 'file_size', 'INTEGER', 0, None, 0)
# (5, 'upload_time', 'DATETIME', 0, None, 0)
# (6, 'reservation_id', 'INTEGER', 1, None, 0)
# (7, 'uploaded_by', 'INTEGER', 1, None, 0)
