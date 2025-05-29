## Real-Time Weather Data Pipeline

- An ETL pipeline to fetch and store real-time weather data into a PostgreSQL database.

### Tools Used
- Python
- OpenWeatherMap API
- PostgreSQL
- Requests
- python-dotenv

### Project Structure
```
weather-data-pipeline/ 
├── weather_pipeline.py  (Main logic)    
├── requirements.txt     (Dependencies list) 
├── schema.sql           (SQL table schema)  
├── .gitignore           (Files to ignore)   
└── README.md            (Documentation)     
```

### Features
- Fetches real-time weather for a selected city.
- Parses and cleans temperature, humidity, and description.
- Inserts clean data into PostgreSQL with timestamp.

### Setup

1. Clone the repo:
   git clone https://github.com/uncagedspirit/weather-data-pipeline.git
   cd weather-data-pipeline

2. Create a .env file in the root folder with:
   API_KEY=your_openweathermap_api_key
   CITY=Pune
   DB_NAME=weather_db
   DB_USER=your_db_username
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432

3. Install dependencies:
   pip install -r requirements.txt

4. Set up PostgreSQL:
   - Create weather_db database.
   - Run schema.sql to create the weather table.

5. Run the script:
   python weather_pipeline.py

