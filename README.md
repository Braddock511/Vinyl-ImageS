# Vinyl image processing

The "Vinyl ImageS" application helps users determine the title, genre, label, where it's from, release year, and optionally the value of the vinyl records from the uploaded image. As a user, you can upload a photo of the vinyl record and select the condition of the vinyl from the drop-down menu.
All data is taken from the discogs website: discogs.com

# Configuration
  
  1. Complete all environment in application/compose.yml (https://docs.imagekit.io/api-reference/api-introduction, https://azure.microsoft.com/pl-pl/products/app-service/api/, https://www.discogs.com/developers)
  2. In terminal -> cd application, docker-compose up --build
  3. The application should run on localhost:8080

# Used tools

- Docker 20.10.16
- Model OCR from Azure API
- ImageKit API
- Discogs API 
- Selenium scraper
- FastAPI to own API
- PostgreSQL database
- Vue.js to create interface