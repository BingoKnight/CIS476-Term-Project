import sqlite3
from sqlite3 import Error
from random import randint, randrange
from datetime import timedelta, datetime
 
 
def create_connection(db_file):
  conn = None
  try:
    conn = sqlite3.connect(db_file)
  except Error as e:
    print(e)

  return conn

def create_flight(conn, flight):
  sql = ''' INSERT INTO flight_flightmodel(from_state, from_city, depart_date, 
            to_state, to_city, cost, seats) VALUES(?,?,?,?,?,?,?) '''
  cur = conn.cursor()
  cur.execute(sql, flight)
 
def select_state(conn, state_id):
  sql = 'SELECT * FROM location_statemodel WHERE id=?'

  cur = conn.cursor()
  cur.execute(sql, (state_id,))

  return cur.fetchall()[0][1]

def select_city(conn, state_code):
  sql = 'SELECT * FROM location_citymodel WHERE state_code=?'

  cur = conn.cursor()
  cur.execute(sql, (state_code,))
  resultset = cur.fetchall()

  count = len(resultset) - 1
  city_index = randint(0, count)
  return resultset[city_index][2]

def get_depart_date():
  d1 = datetime.strptime('11/30/2019', '%m/%d/%Y')
  d2 = datetime.strptime('11/30/2020', '%m/%d/%Y')

  delta = d2 - d1
  random_time = randrange(delta.days)
  return d1 + timedelta(days=random_time)

def duplicate_flight(conn, flight):
  sql = '''SELECT * FROM flight_flightmodel WHERE from_state=? AND
            from_city=? AND depart_date=? AND to_state=? AND to_city=?'''

  cur = conn.cursor()
  cur.execute(sql, flight)
  return len(cur.fetchall())

def main():
  database = r"backend\db.sqlite3"
  duplicates = 0

  conn = create_connection(database)
  with conn:
    for i in range(500000):
      from_state = select_state(conn, i % 12 + 1)
      from_city = select_city(conn, from_state)
      depart_date = get_depart_date()
      to_state = select_state(conn, randint(1, 12))
      to_city = select_city(conn, to_state)

      if from_state == to_state and from_city == to_city:
        continue    
      
      cost = randint(8, 70) * 10
      seats = randint(3, 6) * 10
      outbound_flight = (from_state, from_city, depart_date, to_state, to_city, cost, seats)

      cost = randint(8, 70) * 10
      seats = randint(3, 6) * 10
      return_date = depart_date + timedelta(days=randint(1,45))
      return_flight = (to_state, to_city, return_date, from_state, from_city, cost, seats)

      create_flight(conn, outbound_flight)
      create_flight(conn, return_flight)

      print(i+1)
  
if __name__ == '__main__':
  main()