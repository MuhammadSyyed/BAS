import time
from datetime import datetime
import pandas as pd
import sqlite3
import schemas
from utils import dict_factory, save_response
connection = sqlite3.connect("TI_CampusI.db")
cursor = connection.cursor()

# RESULT TABLE QUERIES


def insert_all(all_data):
    data_list = all_data.loc[0:, :].values
    data_list = [tuple(x) for x in data_list]
    try:
        conn = sqlite3.connect('TI_CampusI.db')
        conn.executemany(
            'INSERT INTO RESULTS VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);', data_list)
        conn.commit()
        conn.close()
    except Exception as e:
        print("insert_rooms_list Database Error", str(e))


def get_student_data_by_id(id):
    try:
        conn = sqlite3.connect('TI_CampusI.db')
        conn.row_factory = dict_factory
        query = f"Select ROLL_NO,STUDENT_NAME from BIO WHERE S_ID = '{id}' "
        cursor = conn.execute(query)
        data = cursor.fetchone()
        conn.close()
        print(data["ROLL_NO"], data["STUDENT_NAME"])
        return data["ROLL_NO"], data["STUDENT_NAME"]
    except Exception as e:
        print("get_student_data_by_id Database Error", str(e))


def get_student_data(roll_no, month):
    try:
        conn = sqlite3.connect('TI_CampusI.db')
        conn.row_factory = dict_factory
        query = f"Select * from RESULTS where ROLL_NO = '{roll_no}' "
        if month == 'all':
            pass
        else:
            query += f''' and MONTH={month}'''
        cursor = conn.execute(query
                              )
        data = cursor.fetchall()
        conn.close()
        return data
    except Exception as e:
        print("Database Error", str(e))


def get_all_monthly_result(month):
    try:
        conn = sqlite3.connect('TI_CampusI.db')
        conn.row_factory = dict_factory
        query = f"Select * from RESULTS where MONTH = '{month}' "
        cursor = conn.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
    except Exception as e:
        print("Database Error", str(e))


# STUDENTS TABLE QUERIES

def get_student_details(id):
    try:
        conn = sqlite3.connect('TI_CampusI.db')
        conn.row_factory = dict_factory
        query = f"Select ROLL_NO,NAME from STUDENTS WHERE ROLL_NO = 'T9-{id}' "
        cursor = conn.execute(query)
        data = cursor.fetchone()
        conn.close()
        return data["ROLL_NO"], data["NAME"]
    except Exception as e:
        print("get_student_details Database Error", str(e))

# ATTENDANCE TABLE QUERIES


def check_arrival(id, date):
    try:
        conn = sqlite3.connect('TI_CampusI.db')
        conn.row_factory = dict_factory
        query = f"Select * from ATTENDANCE where DATE_ = '{date}' and ROLL_NO like '{id}' "
        cursor = conn.execute(query)
        data = cursor.fetchone()
        print(data)
        conn.close()
        return data
    except Exception as e:
        print("Database Error", str(e))


def mark_attendance(roll_no, name, date_, time_):
    try:
        conn = sqlite3.connect('TI_CampusI.db', check_same_thread=True)
        conn.execute(f'''
        INSERT OR REPLACE INTO ATTENDANCE (ROLL_NO,STUDENT_NAME,DATE_,REPORTING_TIME,DEPARTURE_TIME)
            VALUES ('{roll_no}','{name}','{date_}','{time_}','');''')
        conn.commit()
        conn.close()
    except Exception as e:
        print("mark_attendance Database Error", str(e))


def mark_departure(roll_no, date, departure_time):
    try:
        conn = sqlite3.connect('TI_CampusI.db')
        conn.execute(f'''
        UPDATE ATTENDANCE SET DEPARTURE_TIME = '{departure_time}' WHERE  ROLL_NO = '{roll_no}' AND DATE_ = '{date}' ;''')
        conn.commit()
        conn.close()
    except Exception as e:
        print("mark_departure Database Error", str(e))


def insert_student_data(roll_no, name):
    try:
        conn = sqlite3.connect('TI_CampusI.db')
        conn.execute(
            f'''INSERT INTO BIO (ROLL_NO,STUDENT_NAME) VALUES ('{roll_no}','{name}');''')
        conn.commit()
        conn.close()
    except Exception as e:
        print("insert_student_data Database Error", str(e))


def get_presents(date):
    try:
        conn = sqlite3.connect('TI_CampusI.db')
        conn.row_factory = dict_factory
        query = f"Select * from ATTENDANCE where date_ = '{date}' "
        cursor = conn.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
    except Exception as e:
        print("Database Error", str(e))


def get_absents(presents):
    presents = [student["ROLL_NO"] for student in presents]
    presents = tuple(presents)
    if len(presents) == 1:
        presents = f"('{presents[0]}')"
    try:
        conn = sqlite3.connect('TI_CampusI.db')
        conn.row_factory = dict_factory
        query = f"Select * from BIO where ROLL_NO NOT IN {presents} "
        cursor = conn.execute(query)
        absents = cursor.fetchall()
        conn.close()
        return absents
    except Exception as e:
        print("Database Error", str(e))


if __name__ == '__main__':
    pass

    print(get_absents('02/16/2023'))
    # Creating Tables

    # # cursor.execute(schemas.create_students_table)
    # # cursor.execute(schemas.create_result_table)
    # # cursor.execute(schemas.create_course_table)
    # cursor.execute(schemas.create_attendance_table)
    # cursor.execute(schemas.create_bio_table)

    # Inserting all old data

    # dataset=pd.read_excel('./others/database.xlsx',sheet_name='RESULT')
    # # insert_all(dataset)

    # Testing functions

    # save_response(get_student_data('T9-18','all'),'get_student_data')
    # save_response(get_all_monthly_result('202210'),"get_all_monthly_result")
    # print(get_student_data_by_id(12))
