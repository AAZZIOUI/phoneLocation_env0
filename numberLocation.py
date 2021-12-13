# %% [markdown]
# STEPS TO CREATE THIS CLOSED JUPYTER ENVIRONMENT:
# 
# inspired by: https://www.digitalocean.com/community/tutorials/how-to-set-up-jupyter-notebook-with-python-3-on-ubuntu-18-04
# 
# 
#     1. Go TO your workspace folder: WS
#     2. $ mkdir ~/my_project_dir
#     3. $ virtualenv my_project_env
#     4. source my_project_env/bin/activate
#     5. CTRL+Shift+P to open "Command palette" which you can find also in section "View"
#     6. find "Create New Jupyter Notebook" and click on it.
#     7. save it in the location you want in the chosen environment
#     8. to deactivate a python Environment: $ deactivate
# 
# 

# %%
#pip install phonenumbers

# %%
#pip install folium

# %%
#pip install opencage

# %% [markdown]
# Now our code starts:

# %%
number = "+919876543210"

# The key is from my account in https://opencagedata.com/ 

key='10dxxxxxxxxxxxxxxxxxxxxxxxxxx'

# %%
import phonenumbers
from phonenumbers import geocoder, carrier
import folium

theNumber = phonenumbers.parse(number, 'CH')

numberLocation = geocoder.description_for_number(theNumber, 'en')
carrier = carrier.name_for_number(theNumber, 'en')
valid = phonenumbers.is_valid_number(theNumber)

#print("The number is: ",theNumber)
#print("numberLocation is: ", numberLocation)
#print("Service provider is: ", carrier)
#print(valid)

# %%
from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(numberLocation)

results = geocoder.geocode(query)

#print(results)

# %%
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

#print("latitude:", lat)
#print("longitude:", lng)

# %%
myMap = folium.Map(location=[lat,lng] , zoom_start=9)
folium.Marker([lat,lng], popup=numberLocation).add_to(myMap)

myMap.save("numberLocation.html")


