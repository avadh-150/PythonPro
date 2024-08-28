import folium
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

# Your OpenCage API key
key = "1023ba1fdb564f78985f8d1bb8573435"

# Input phone number
number = input("Enter your phone number with country code: ")

# Parse the phone number
check_num = phonenumbers.parse(number)

# Get location and service provider
num_location = geocoder.description_for_number(check_num, "en")
print(f"Location: {num_location}")

service_provider = carrier.name_for_number(check_num, "en")
print(f"Service Provider: {service_provider}")

# Initialize OpenCage Geocoder
geocoder = OpenCageGeocode(key)

# Geocode the location description
result = geocoder.geocode(num_location)

if result and len(result) > 0:
    # Get latitude and longitude
    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']
    
    print(f"Latitude: {lat}, Longitude: {lng}")
    
    # Create a map centered around the coordinates
    map_location = folium.Map(location=[lat, lng], zoom_start=9)
    
    # Add a marker for the location
    folium.Marker([lat, lng], popup=num_location).add_to(map_location)
    
    # Save the map to an HTML file
    map_location.save("location.html")
    print("Map has been saved to location.html")
else:
    print("Geocoding failed. No results found.")
