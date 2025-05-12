# 🌦️ Weather Dashboard

A beginner-friendly full-stack weather app built with:

- **Python (Flask)** — Backend server & API logic  
- **SQLite + SQLAlchemy** — Database to store recent search history  
- **JavaScript (Vanilla)** — Frontend logic using `fetch()`  
- **HTML/CSS** — UI layout and styling  
- **OpenWeatherMap API** — Real-time weather data

---

## 🚀 Features

- 🔍 Search for weather by city
- 💾 Stores recent 5 searches in SQLite
- 🌐 Responsive frontend with live weather display
- 🔒 API key protected (optionally with `.env`)

---

## 🛠️ Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/weather_dashboard.git
cd weather_dashboard

2. Create and activate virtual enviroment 
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

3. Install dependencies 
pip install -r requirements.txt

4. Set your OpenWeatherMap API key in app.py

5. Run the flask server 
cd backend
python app.py

6. Open the frontend/index.html in your browser