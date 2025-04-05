import requests
import sqlite3

# Fetch JSON from NASA APOD API
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=2"
response = requests.get(url)
planets = response.json()  # List of APOD entries

# Connect to local database
conn = sqlite3.connect("apod.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS apod")
cursor.execute("CREATE TABLE apod (title TEXT, date TEXT, url TEXT)")

# Insert data
cursor.executemany("INSERT INTO apod VALUES (?, ?, ?)", 
                   [(p["date"], p["title"], p["url"]) for p in planets])
conn.commit()

# Show as table
cursor.execute("SELECT * FROM apod")
print(f"{'Date':<12} {'Title':<30} {'URL'}")
print("-" * 70)
for date, title, url in cursor.fetchall():
    print(f"{date:<12} {title:<30} {url[:30]}...")
conn.close()
# Learned: SQLite can store NASA APOD data in a table