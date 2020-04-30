import os
import sqlite3
import csv

directories = os.listdir()
philodbnames = ["marat", "frantext18thc", "baudouin", "frc", "ap", "Gldsmth18cfr", "hubeccofr"]

query_results = open('query_results.csv', 'w')
my_file = csv.writer(query_results)
column_names = ["author", "title", "year", "philo_id"]
my_file.writerow(column_names)

def extract_metadata(databases):
    for i in databases:
        path = i + '/data/toms.db'
        if os.path.exists(path):
            conn = sqlite3.connect(path)
            c = conn.cursor()
            c.execute('SELECT author, title, year, philo_id FROM toms WHERE philo_type="doc"')
            data = c.fetchall()
            my_file.writerows(data)
            conn.close()
    return
