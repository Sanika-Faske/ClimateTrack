# 🌦️ ClimateTrack - Weather App

ClimateTrack is a Django-based web application that provides real-time weather information for cities around the world.  
It fetches weather data using an API and displays it in a clean, responsive UI.  

---

## 🚀 Live Demo
🔗 [View Project on Render]((https://climatetrack.onrender.com/))

---

## 📌 Features
- 🌍 Search weather by city name  
- 🌡️ Displays temperature, humidity, and weather conditions  
- 📱 Mobile-friendly responsive UI  
- ⚡ Fast deployment with Render  

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, Bootstrap (optional)  
- **Database:** SQLite (default) / PostgreSQL (optional for production)  
- **Deployment:** Render  
- **Others:** Gunicorn, Whitenoise  

---

## ⚙️ Setup & Installation
1. Clone the repository:
   
   git clone https://github.com/your-username/your-repo.git
   cd ClimateTrack

2. Create a virtual environment & activate it:

    python -m venv venv
    source venv/bin/activate   # (Linux/Mac)
    venv\Scripts\activate      # (Windows)


3. Install dependencies:

    pip install -r requirements.txt


4. Run migrations:

    python manage.py migrate


5. Start the server:

    python manage.py runserver
