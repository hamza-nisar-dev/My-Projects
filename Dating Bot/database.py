import sqlite3
conn = sqlite3.connect('user.db')
conn.execute('''CREATE TABLE COMPANY
         (
          ID   NOT NULL,
          username  NOT NULL,
          date_birth   NOT NULL,
          body_type  NOT NULL,
          height  NOT NULL,
          race NOT NULL,
          weight  NOT NULL,
          verification_numbers  NOT NULL,
          report_numbers  NOT NULL,
          account_type  NOT NULL,
          contact_info NOT NULL
         );''')
conn.close()
conn = sqlite3.connect('post.db')
conn.execute('''CREATE TABLE COMPANY
         (
          ID   NOT NULL,
          Country   NULL,
          town  NULL,
          area  NOT NULL,
          wlf  NOT NULL,          
          Age  INT NOT NULL,
          Height FLOAT NOT NULL,
          weight  FLOAT NOT NULL,
          race NOT NULL,
          bt  NOT NULL,
          lf  NOT NULL,
          pos  NOT NULL,
          Tribe  NOT NULL,
          member NOT NULL,
          reports NOT NULL
         );''')
conn.close()

conn = sqlite3.connect('age.db')
conn.execute('''CREATE TABLE COMPANY
         (
         ID   NOT NULL,
         range NOT NULL
         );''')
conn.close()

conn = sqlite3.connect('filters.db')
conn.execute('''CREATE TABLE COMPANY
         (
          ID   NOT NULL,
          Country  NOT NULL,
          Age   NOT NULL,
          Height  NOT NULL,
          weight  NOT NULL,
          race NOT NULL,
          bt  NOT NULL,
          lf  NOT NULL,
          pos  NOT NULL,
          Tribe  NOT NULL
         );''')
conn.close()

conn = sqlite3.connect('proh.db')
conn.execute('''CREATE TABLE COMPANY
         (
         ID   NOT NULL,
         feat  NOT NULL
         );''')
conn.close()
conn = sqlite3.connect('report.db')
conn.execute('''CREATE TABLE COMPANY
         (
         id   text    NOT NULL,
         report   text    NOT NULL,
         report_by text    NOT NULL
         );''')
conn.close()

conn = sqlite3.connect('verify.db')
conn.execute('''CREATE TABLE COMPANY
         (
         id   text    NOT NULL,
         verify_by   text    NOT NULL
         );''')
conn.close()