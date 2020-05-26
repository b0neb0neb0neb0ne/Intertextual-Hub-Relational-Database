import os
import sqlite3
import csv

directories = os.listdir()
philodbnames = ["marat", "frantext18thc", "frc", "ap", "Gldsmth18cfr", "hubeccofr"]

query_results = open('query_results2.csv', 'w')
my_file = csv.writer(query_results)
column_names = ["author", "title", "year", "philo_id"]
my_file.writerow(column_names)

def extract_metadata(databases, path):
    for i in databases:
        path += i + '/data/toms.db'
        if os.path.exists(path):
            conn = sqlite3.connect(path)
            c = conn.cursor()
            c.execute('SELECT author, title, year, philo_id FROM toms WHERE philo_type="doc"')
            data = c.fetchall()
            my_file.writerows(data)
            conn.close()
    return

def clean_up_in_pandas(csv_file):

    df = pandas.read_csv(csv_file)
    df['year'] = pandas.to_datetime(df['year'], format='%Y')
    return df
