#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
takes 3 arguments: mysql username, mysql password and database name (no argument validation needed)
Result sorted in ascending order by states.id
"""

import sys
import MySQLdb


def N_states():
    """defining func"""

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user='root', passwd='14298uppah', db='hbtn_0e_0_usa')
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name FROM `states` WHERE name LIKE 'N%' ORDER BY id ASC")
    [print(state) for state in cur.fetchall()]
    cur.close()
    conn.close()


if __name__ == '__main__':
    N_states()
