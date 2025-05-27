import sqlite3
import os

# 数据库路径
db_path = os.path.expanduser("~/.config/Cursor/User/globalStorage/state.vscdb")

# 要查找和更新的 key
target_key = "aicontext.personalContext"

# 要追加的文本内容
append_text = """

在任何时候，出现以下几种情况的时，应在命令行中执行：`python -c "print('\\n'.join(line for line in iter(input, ':wq')))"`：
1. 你已经完成用户请求的一部分响应后；
2. 你计划结束这一次响应前；
3. 存在歧义或多种方案，希望用户提供更多信息时；
4. 当你认为存在新的可能性和改进时。
该命令用于与用户实时沟通。请将命令的标准输出作为用户反馈，继续响应。"""

def update_context_value():
    # 连接数据库
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # 查询当前的值
        cursor.execute("SELECT value FROM ItemTable WHERE key=?", (target_key,))
        row = cursor.fetchone()
        if row:
            current_value = row[0]
            new_value = current_value + append_text
            # 更新记录
            cursor.execute("UPDATE ItemTable SET value=? WHERE key=?", (new_value, target_key))
            conn.commit()
            print("已成功更新 value 字段。")
        else:
            print(f"未找到 key 为 '{target_key}' 的记录。")
    finally:
        conn.close()

if __name__ == "__main__":
    update_context_value()
