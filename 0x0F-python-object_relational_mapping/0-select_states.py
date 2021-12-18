#!/usr/bin/python3

import sys
import MySQLdb

def list_states():
    """lists all states from the database hbtn_0e_0_usa"""

    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute('SELECT * FROM `states`')
    [print(state) for state in cur.fetchall()]

if __name__ == '__main__':
    list_states()
