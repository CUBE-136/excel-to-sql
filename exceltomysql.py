import openpyxl
import mysql.connector
# ワークシート読み込み
wb = openpyxl.load_workbook('music_chart2022.xlsx')

# セル用のリスト
values = [[] for i in range(74)]

# シート読み込み&リスト挿入
ws = wb.worksheets[13]
for row in range(2, 76):
    for column in range(1, 3):
        nowcell = ws.cell(row, column).value
        values[row - 2].append(nowcell)
print(values)

# SQLへのリスト挿入
cnx = None

try:
    cnx = mysql.connector.connect(
        user='name',  # ユーザー名
        password='password',  # パスワード
        host='localhost',  # ホスト名(IPアドレス）
        database='music'  # データベース名
    )

    cursor = cnx.cursor()

    sql = ('''
    INSERT INTO `artist` 
        (`artist`, `nationality`)
    VALUES 
        (%s, %s)
    ''')

    cursor.executemany(sql, values)
    cnx.commit()

    print(f"{cursor.rowcount} records inserted.")

    cursor.close()

except Exception as e:
    print(f"Error Occurred: {e}")

finally:
    if cnx is not None and cnx.is_connected():
        cnx.close()
