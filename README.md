# weather-Forcasting-app



## Features
- Get real-time weather data (daily and 5-day forecasts)
- Search by latitude/longitude, city/country, or place name
- Clean and simple user interface (Django templates & CSS)
- Python utility functions for temperature, wind, and time zone conversion
- API key security using a `.env` file
- Session management for user selections



## Technologies Used
- Python 3
- Django
- HTML, CSS
- OpenWeatherMap API



## Getting Started

### Prerequisites
- Python 3.x
- pip
- (Optional) Virtualenv for isolated environment

### Installation Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/dwivediajit01/weather-Forcasting-app.git
   cd weather-Forcasting-app/weatherApp
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On Linux/Mac
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Create a `.env` file** in the root directory and add your OpenWeatherMap API key:
   ```env
   OPENWEATHER_API_KEY=your_api_key_here
   ```
5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
7. **Open your browser** and go to `http://127.0.0.1:8000/`



## Project Structure (Simplified)
```
weatherApp/
├── manage.py
├── static/
├── templates/
├── weather_app/
│   ├── views.py
│   ├── urls.py
│   ├── utils_conversion.py
│   └── ...
├── weatherApp/
│   ├── settings.py
│   └── ...
```



## Security
- API keys are stored securely using a `.env` file and are not committed to version control.



## Author
Ajit Dwivedi
