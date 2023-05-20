import mysql.connector

cnx = None

try:
    cnx = mysql.connector.connect(
        user='name',  # ユーザー名
        password='password',  # パスワード
        host='localhost',  # ホスト名(IPアドレス）
        database='music'  # データベース名
    )

    cursor = cnx.cursor()

    # SQL命令文

    sql = '''
    create table artist (
        `artist` varchar(100) not null , 
        `nationality` varchar(20) not null, 
        primary key(`artist`),
    ) engine = InnoDB;


    create table `music`.`song` (
        `song` varchar(100) not null , 
        `artist` varchar(100) not null, 
        `genre` varchar(30) not null, 
        primary key(`song`),
        foreign key(`artist`) references artist(`artist`)
    ) engine = InnoDB;

    create table `music`.`global` (
        `rank` int not null , 
        `song` varchar(100) not null, 
        primary key(`rank`),
        foreign key(`song`) references song(`song`)
    ) engine = InnoDB;

    create table `japan` like `global`;
    create table `usa` like `global`;
    create table `china` like `global`;
    create table `uk` like `global`;
    create table `france` like `global`;
    create table `brazil` like `global`;
    create table `india` like `global`;
    create table `germany` like `global`;
    create table `italy` like `global`;
    create table `canada` like `global`;
    create table `korea` like `global`;
    '''
    cursor.execute(sql)

    cursor.execute("SHOW TABLES", multi=True)
    print(cursor.fetchall())

    cursor.close()

except Exception as e:
    print(f"Error Occurred: {e}")

finally:
    if cnx is not None and cnx.is_connected():
        cnx.close()