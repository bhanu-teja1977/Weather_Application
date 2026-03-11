Python Weather Application
Overview

The Python Weather Application is a lightweight project that retrieves real-time weather information using a public weather API and displays key weather parameters in a simple and user-friendly format. The application helps users quickly check weather conditions such as temperature, humidity, wind speed, and general climate status for any location.

This project demonstrates how Python can be used to interact with external APIs, process JSON responses, and present useful data in a structured manner.

Features

Fetches real-time weather data from a weather API

Displays temperature, humidity, wind speed, and weather conditions

Allows users to search weather by city name

Simple and clean command-line interface

Handles API responses and errors efficiently

Tech Stack

Python

Requests Library

Weather API (e.g., OpenWeatherMap)

JSON Data Handling

Project Workflow

The user enters the city name.

The application sends a request to the weather API.

The API returns weather data in JSON format.

The program extracts required parameters such as:

Temperature

Humidity

Weather description

Wind speed

The processed data is displayed to the user in a readable format.

Project Structure
weather-app/
│
├── weather.py          # Main Python script
├── requirements.txt    # Required dependencies
├── README.md           # Project documentation
└── config.py           # API key configuration (optional)
Installation
1. Clone the Repository
git clone https://github.com/yourusername/python-weather-app.git
cd python-weather-app
2. Install Dependencies
pip install -r requirements.txt
3. Get API Key

Create a free account and obtain an API key from:

https://openweathermap.org/api

Configuration

Add your API key in the script:

API_KEY = "your_api_key_here"
Running the Application

Run the Python script:

python weather.py

Enter the city name when prompted to view weather details.

Example Output
Enter city name: Hyderabad

Weather in Hyderabad:
Temperature: 30°C
Humidity: 65%
Wind Speed: 3.5 m/s
Condition: Clear Sky
Future Enhancements

GUI using Tkinter or PyQt

Weather forecast for multiple days

Location-based weather detection

Mobile or web interface

Learning Outcomes

Working with REST APIs

Parsing JSON data

Using Python libraries for HTTP requests

Building real-world data-driven applications

License

This project is open-source and available under the MIT License.
