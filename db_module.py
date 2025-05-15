import psycopg2
import os

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('LDM_DB', 'ldm_db'),
        user=os.getenv('LDM_USER', 'ldm_user'),
        password=os.getenv('LDM_PASS', 'ldm_pass'),
        host=os.getenv('LDM_HOST', 'localhost'),
        port=os.getenv('LDM_PORT', 5432)
    )
    return conn

def fetch_engagements():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT status, client_engagement, date, major_urgent_callouts, slack_link
        FROM engagements
        ORDER BY date DESC
    ''')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

