# Import module 
import sqlite3 
import pandas as pd
  
# Connecting to sqlite 
conn = sqlite3.connect('employee.db') 

# Creating a cursor object using the  
# cursor() method 
cursor = conn.cursor() 

# Creating table 
# table ="""CREATE TABLE EMPLOYEE(EMPLOYEE_ID INT(5),FIRST_NAME VARCHAR(255), LAST_NAME VARCHAR(255),EMAIL VARCHAR(255), 
# PHONE_NUMBER VARCHAR(255),HIRE_DATE DATE,JOB_ID VARCHAR(255),SALARY INT(15),COMMISSION_PCT VARCHAR(255),MANAGER_ID INT(5),DEPARTMENT_ID INT(5));"""
# cursor.execute(table) 

 
# Queries to INSERT records. 

# load the data into a Pandas DataFrame
employee = pd.read_csv('C:\LLM\LLMA2_Chat\End-to-end-SQL-Chatbot-using-Llam2\sqlite_scripts\data\employee.csv')
# write the data to a sqlite table
employee.to_sql('EMPLOYEE_DATA', conn, if_exists='append', index = False)

order = pd.read_csv('C:\LLM\LLMA2_Chat\End-to-end-SQL-Chatbot-using-Llam2\sqlite_scripts\data\order.csv')
# write the data to a sqlite table
order.to_sql('EMPLOYEE_ORDER', conn, if_exists='append', index = False)

# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM EMPLOYEE_ORDER''') 
for row in data: 
    print(row) 

# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM EMPLOYEE_DATA''') 
for row in data: 
    print(row) 

  
# Commit your changes in the database     
conn.commit() 
  
# Closing the connection 
conn.close()