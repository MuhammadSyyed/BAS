create_students_table = '''CREATE TABLE STUDENTS
                        (ROLL_NO TEXT PRIMARY KEY,
                        GR_NO INTEGER NOT NULL,
                        STUDENT_NAME TEXT NOT NULL,
                        FATHER_NAME TEXT NOT NULL,
                        FATHER_PHN INTEGER NOT NULL,
                        MOTHER_PHN INTEGER NOT NULL,
                        STUDENT_PHN INTEGER NOT NULL,
                        ADDRESS TEXT NOT NULL,
                        SCHOOL_NAME TEXT NOT NULL,
                        S_GROUP TEXT NOT NULL,
                        NINTH_PERCENTAGE TEXT NOT NULL,
                        MATRIC_PERCENTAGE TEXT NOT NULL,
                        AVERAGE_PERCENTAGE TEXT NOT NULL);'''


create_result_table = '''CREATE TABLE RESULTS
                        (ROLL_NO TEXT NOT NULL,
                        STUDENT_NAME TEXT NOT NULL,
                        MONTH INTEGER NOT NULL,
                        PHY FLOAT NOT NULL,
                        PHY_MM FLOAT NOT NULL,
                        CHEM FLOAT NOT NULL,
                        CHEM_MM FLOAT NOT NULL,
                        MATH_BIO FLOAT NOT NULL,
                        MATH_BIO_MM FLOAT NOT NULL,
                        ENG FLOAT NOT NULL,
                        ENG_MM FLOAT NOT NULL,
                        URDU FLOAT NOT NULL,
                        URDU_MM FLOAT NOT NULL,
                        ISL FLOAT NOT NULL,
                        ISL_MM FLOAT NOT NULL,
                        OBT_TOTAL FLOAT NOT NULL,
                        MAX_MARKS FLOAT NOT NULL,
                        PERCENTAGE INTEGER NOT NULL,
                        REMARKS TEXT NOT NULL,
                        GRADE TEXT NOT NULL);'''

create_course_table = '''CREATE TABLE COURSE
                        (SUBJECT_ID TEXT PRIMARY KEY,
                        SUBJECT_NAME TEXT NOT NULL,
                        MONTH TEXT NOT NULL,
                        UNITS_PLANNED NOT NULL,
                        UNITS_COVERED NOT NULL);'''

create_bio_table = '''CREATE TABLE BIO(
                    S_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    ROLL_NO TEXT NOT NULL,
                    STUDENT_NAME TEXT NOT NULL);'''

create_attendance_table = '''CREATE TABLE ATTENDANCE
                        (ROLL_NO TEXT NOT NULL,
                        STUDENT_NAME TEXT NOT NULL,
                        DATE_ DATE NOT NULL,
                        REPORTING_TIME TEXT NOT NULL,
                        DEPARTURE_TIME NOT NULL);
'''
