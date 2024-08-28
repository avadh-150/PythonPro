import folium.map
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
 #use for show in map as like google map 
from opencage.geocoder import OpenCageGeocode

# import opencage
key = "1023ba1fdb564f78985f8d1bb8573435"
number = input("Enter the your phone number with country code.. ")

check_num = phonenumbers.parse(number) #  the number is parse in phonenumber ....parse() function is used... 
num_location = geocoder.description_for_number(check_num,"en")  # print the country
print(f"Country is :",num_location)

# isp = phonenumbers.parse(number)
print(carrier.name_for_number(check_num,"en"))# it is give the current your service provider...

# key API of ma p 
geocoder = OpenCageGeocode(key)

# parsen as a string .
query = str(num_location)

# get the latitude and longtitude coordinates
result = geocoder.geocode(query)
print(result)

# latitude
lat = result[0]['geometry']['lat']

# longtitude
lng = result[0]['geometry']['lng']

# and then print it coordinates/........
print(lat,lng)

map_location= folium.Map(location=(lat,lng),zoom_status=9) #show in the map by putting coordinates
folium.Marker([lat,lng],popup=num_location).add_to(map_location)
map_location.save("location.html")
 



