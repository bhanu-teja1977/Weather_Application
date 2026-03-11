# Python Weather Application

## Overview
The Python Weather Application is a simple project that retrieves real-time weather information using a public weather API. It allows users to check weather conditions such as temperature, humidity, wind speed, and overall weather description for any city. The application demonstrates how Python can interact with external APIs, process JSON data, and display useful information in a clear format.

## Features
- Fetch real-time weather data using a weather API
- Display temperature, humidity, wind speed, and weather condition
- Search weather by city name
- Simple command-line interface
- Efficient handling of API responses and errors

## Tech Stack
- Python
- Requests Library
- OpenWeatherMap API (or any weather API)
- JSON Data Handling

## Project Workflow
1. The user enters the name of a city.
2. The application sends an API request to the weather service.
3. The weather API returns the data in JSON format.
4. The program extracts important information such as temperature, humidity, wind speed, and weather description.
5. The processed data is displayed in a readable format for the user.

## Project Structure
```

weather-app/
│
├── weather.py
├── requirements.txt
├── README.md
└── config.py

```

## Installation

### 1. Clone the Repository
```

git clone [https://github.com/yourusername/python-weather-app.git](https://github.com/yourusername/python-weather-app.git)
cd python-weather-app

```

### 2. Install Required Libraries
```

pip install -r requirements.txt

```

### 3. Get API Key
Create an account and obtain a free API key from:
https://openweathermap.org/api

## Configuration
Add your API key inside the Python script.

```

API_KEY = "your_api_key_here"

```

## Running the Application
Run the Python script using:

```

python weather.py

```

Enter the city name when prompted and the application will display the weather details.

## Example Output
```

Enter city name: Hyderabad

Weather in Hyderabad
Temperature: 30°C
Humidity: 65%
Wind Speed: 3.5 m/s
Condition: Clear Sky

```

## Future Improvements
- Add a graphical user interface using Tkinter or PyQt
- Display multi-day weather forecasts
- Add location-based automatic weather detection
- Convert the application into a web or mobile app

## Learning Outcomes
- Understanding how to work with REST APIs
- Parsing and handling JSON data
- Using Python libraries for HTTP requests
- Building real-world API-based applications

## License
This project is open-source and available for learning and educational purposes.
```
