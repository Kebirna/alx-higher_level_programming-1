#!/usr/bin/python3

import sys
import MySQLdb


def list_state():
    """  lists all states from the database hbtn_0e_0_usa"""

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]
    cur.close()
    conn.close()


if __name__ == "__main__":
    list_state()


