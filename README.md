# Vinyl image processing

The "Vinyl ImageS" application helps users determine the title, genre, label, where it's from, release year, and optionally the value of the vinyl records from the uploaded image. As a user, you can upload a photo of the vinyl record and select the condition of the vinyl from the drop-down menu
All data is taken from the discogs website: discogs.com

# Configuration
  
  1. Download and configure all required libraries and tools listed in requirements
  2. Enable the postgresql service and in database.py -> SQLALCHEMY_DATABASE_URL = "postgresql://{user}:{password}@{host}:{port}/{database}"
  3. In database.py -> fill in the blanks in data_to_insert
  4. To enable the interface, in the application folder, type "npm run dev" in the console, the application will run on localhost

# Used tools

- Model OCR from Azure API
- ImageKit API
- Discogs API 
- Selenium scraper
- FastAPI to own API
- PostgreSQL database
- Vue.js to create interface


