Linking Database Stuff

Getting FastAPI running: uvicorn sql_app.main:app --reload
My website stuff is accessible here: http://127.0.0.1:8000/docs#/default/main__get

what is primary key?

Create SQLAlchemy models from the Base class (i believe i have done this)
    copying down every piece of relevant code
    engine = create_engine('sqlite:///ihub.db')  THIS GETS RUN IN SQL_APP DIRECTORY, NOT IN THE LEVEL HIGHER
    Base = declarative_base()  
    Session = sessionmaker(bind=engine) 
    Session.configure(bind=engine)  
    session = Session() 
    dog = session.query(Comp).first()  
    print(dog.author)

CURRENT SPOT: I have my database tentatively hooked up to FastAPI through SQLAlchemy, and now I think I need to come up with a basic form that can be used
to be query, which is then POSTED, and I need a GET that returns those and displays
them in a browser? I think I need to understand the various pages of sql_app on a more bare bones level, and remove extraneous lines, and figure out HOW TO DISPLAY RESULTS IN A WEB PAGE (probably go back to 122 project code)

Note: the databasae found at "baudouin/data/toms.db" does not have an author column,
so I have omitted it from "philodbnames"
Note: your most up to date db is ihub.db and the table is called test
    database created off copy of clean_query.csv called tester.csv

Querying each database 
    1. Open ipython3
    2. Import extracter.py
    3. Run extracter.extract_metadata(databases)
        Note: input variable should be a list of directories within intertextual hub
        that you want to query 
    4. Run clean_csv(csv_file)

At this point, you will have a file "query_results.csv", which contains all query
results from the various databases, and once it is cleaned, it is called clean_query.csv

I account for databases with missing authors, but still have not figured out how to handle sub-sections found in dictionaries or encyclopedias

https://stackoverflow.com/questions/26837998/pandas-replace-nan-with-blank-empty-string
https://stackoverflow.com/questions/17683228/how-to-replace-all-null-values-with-n-a-in-a-sqlite-table

pandas.to_datetime(df['year']], format='%Y')
    this is how you convert the year into a datetime 
if you recreate database from the original query across all dbs, make sure that the philo_id is converted
into string/objects 
Converting my df into sql (df.to_sql('test', conn, if_exists='replace', index=False) )
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html

Basic SQLite3 commands for using DB in Python:
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print c.fetchone()

Adding an Index (2 Docs and a Medium tutorial)
https://www.sqlitetutorial.net/sqlite-primary-key/
https://www.sqlitetutorial.net/sqlite-index/
https://medium.com/@JasonWyatt/squeezing-performance-from-sqlite-indexes-indexes-c4e175f3c346

Connecting SQLite to Flask/FastAPI
https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
https://fastapi.tiangolo.com/tutorial/sql-databases/
    docs on SQLAlch: https://docs.sqlalchemy.org/en/13/core/engines.html


Connecting Flask to Gunicorn and Nginx
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
    Explanation of why this web server combo
    https://serverfault.com/questions/331256/why-do-i-need-nginx-and-something-like-gunicorn
    https://docs.python-guide.org/scenarios/web/

Adding in a client-facing web app (2 guides)
https://realpython.com/the-ultimate-flask-front-end/
http://zike.io/posts/Full-Stack-Beginner-s-Guide-Flask-React-SQLAlchemy/

Additional Resources
https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs

Useful SQL query:
select author, title, year, philo_id from toms where philo_type="doc";
