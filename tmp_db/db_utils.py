# tmp_db/db_utils.py
import sqlite3
from django.conf import settings

def execute_sql(sql):
    # 获取SQLite数据库文件路径
    db_path = settings.BASE_DIR.joinpath('tmp_db/db.sqlite')

    # 连接到SQLite数据库
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        conn.commit()
        result = {"status": "success", "message": "SQL executed（这只是临时的处理方式，不能上线）"}
    except sqlite3.Error as e:
        conn.rollback()
        result = {"status": "error", "message": str(e)}

    finally:
        cursor.close()
        conn.close()

    return result
