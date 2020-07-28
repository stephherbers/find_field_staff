import pickle
import pandas as pd
import geopandas
import matplotlib.pyplot as plt
import math

#return dict of lat and long based on city name
def find_lat_and_long(location_data, city_name):
    return location_data[city_name.lower()]

def find_field_locations(location_data, email_array):
    field_locations = {'Email': [], 'Time': [], 'Location': [], 'Latitude': [], 'Longitude': []}
    for email in email_array:
        field_locations["Email"].append(email[0])
        field_locations["Time"].append(email[1])
        field_locations["Location"].append(email[2])
        lat_and_long = find_lat_and_long(location_data, email[2])
        field_locations["Latitude"].append(lat_and_long["lat"])
        field_locations["Longitude"].append(lat_and_long["long"])
    return field_locations

#finds furthest distance in km and location
def find_furthest_from_home(field_locations, home_loc_dic):
    largest_current_distance = -1
    furthest_person_index = -1
    EARTH_RADIUS = 6378
    home_lat = math.radians(float(home_loc_dic["lat"]))
    home_long = math.radians(float(home_loc_dic["long"]))
    latitudes = field_locations['Latitude']
    longitudes = field_locations['Longitude']
    for i in range(len(latitudes)):
        staff_lat = math.radians(float(latitudes[i]))
        staff_lon = math.radians(float(longitudes[i]))
        difference_in_lat = staff_lat - home_lat
        difference_in_long = staff_lon - home_long
        a = math.sin(difference_in_lat / 2)**2 + math.cos(home_lat) * math.cos(staff_lat) * math.sin(difference_in_long / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = EARTH_RADIUS * c
        if distance > largest_current_distance:
            largest_current_distance = distance
            furthest_person_index = i
    return largest_current_distance, field_locations['Location'][furthest_person_index]



def main():
    processed_email_array =  pickle.load( open("processed_email_array.p", "rb"))
    location_data =  pickle.load( open("processed_location_data.p", "rb"))
    field_locations = find_field_locations(location_data, processed_email_array)

    cambridge_loc = {"lat": '42.33704', "long": '-71.20922'}
    furthest_distance, furthest_location = find_furthest_from_home(field_locations, cambridge_loc)

    superlative = "The furthest Employee from our Cambridge Office is " + str(int(furthest_distance)) + "km away located in " + furthest_location


    df = pd.DataFrame(field_locations, columns= ['Email', 'Time', 'Location', 'Latitude', 'Longitude'])
    df.to_csv (r'field_staff_locations.csv', index = False, header=True)

    gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))

    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    ax = world.plot(color='white', edgecolor='black')
    ax.set_title(superlative)
    gdf.plot(ax=ax, color='blue')

    plt.show() #displays world map




main()
