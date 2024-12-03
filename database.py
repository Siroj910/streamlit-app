import sqlite3
from datetime import datetime, timedelta

def get_schedules():
    # Connect to the database
    conn = sqlite3.connect('lecture_reminder.db')
    cursor = conn.cursor()

    # Query to fetch schedules
    cursor.execute('SELECT time, theme FROM lectures WHERE date = ?', [(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')])

    rows = cursor.fetchall()
    conn.close()
    return rows

