#!/usr/bin/python3
"""lists all cities of that state."""
import MySQLdb
import sys



if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.name\
            FROM cities LEFT JOIN states\
            ON states.id = cities.state_id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC", (sys.argv[4],))
    rows = c.fetchall()
    print(", ".join([row[0] for row in rows]))

    c.close()
    db.close()
