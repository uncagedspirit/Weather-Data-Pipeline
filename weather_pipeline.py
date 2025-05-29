import os
from dotenv import load_dotenv
import requests
import psycopg2
from datetime import datetime

load_dotenv()  

API_KEY = os.getenv('API_KEY')
CITY = os.getenv('CITY')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather():
    response = requests.get(URL)
    data = response.json()
    return {
        'city': CITY,
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description'],
        'timestamp': datetime.now()
    }

def insert_into_db(weather):
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO weather (city, temperature, humidity, description, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    """, (weather['city'], weather['temperature'], weather['humidity'],
          weather['description'], weather['timestamp']))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    data = fetch_weather()
    insert_into_db(data)
