# Importing Necessary Modules
import requests
import requests_cache
from retry_requests import retry
import openmeteo_requests
import pickle

list_of_weather_data = []
dict_mood = {
    'Energetic': 1,
    'Happy': 2,
    'Calm': 3,
    'Sad': 4
}

# This method will return our actual coordinates using our IP address
def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
    except Exception as e:
        # Displaying the error message
        print("Error fetching location:", e)
        return None, None, None, None

latitude, longitude, city, state = locationCoordinates()
if latitude is not None and longitude is not None:
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["temperature_2m", "is_day", "precipitation", "rain", "snowfall", "cloud_cover"]
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]

    # Current values. The order of variables needs to be the same as requested.
    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    current_is_day = current.Variables(1).Value()
    current_precipitation = current.Variables(2).Value()
    current_cloud_cover = current.Variables(5).Value()

    list_of_weather_data = [current_is_day, current_cloud_cover, current_precipitation]

def get_key_from_value(dict_mood, predicted_mood_EncodedValue):
    for key, value in dict_mood.items():
        if value == predicted_mood_EncodedValue:
            return key
    # If the value is not found, you can handle it accordingly
    return None

# Loading face emotion detection model
weather_model_pickle_file_path = r'C:\Users\njain\OneDrive - Cal State Fullerton\SPRING 2024\CPSC 597 Project\Project\APMBSS\data\models\mood_detection_weather_model.pkl'

with open(weather_model_pickle_file_path, 'rb+') as file:
    mood_detection_weather_model = pickle.load(file)

predicted_mood_EncodedValue = mood_detection_weather_model.predict([list_of_weather_data])[0]

predicted_mood = get_key_from_value(dict_mood, predicted_mood_EncodedValue)
print(predicted_mood)