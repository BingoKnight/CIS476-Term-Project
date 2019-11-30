import sqlite3
from sqlite3 import Error

def create_connection(db_file):
  conn = None
  try:
    conn = sqlite3.connect(db_file)
  except Error as e:
    print(e)

  return conn

def remove_flights(conn):
  cursor = conn.cursor()
  rowcount = cursor.execute("DELETE FROM flight_flightmodel").rowcount
  conn.commit()
  cursor.execute("VACUUM")
  
  print(str(rowcount) + ' rows deleted from flight_flightmodel')

def main():
  database = r"backend\db.sqlite3"
  conn = create_connection(database)

  print('Are you sure you want to delete the \'flight_flightmodel\' table (Y/N)')
  answer = input()

  if answer.lower() == 'y':
    remove_flights(conn)
  else:
    print('Delete canceled')

main()