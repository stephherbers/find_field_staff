import pickle
import pandas as pd
import geopandas

#return dict of lat and long based on city name
def find_lat_and_long(location_data, city_name):
    return location_data[city_name.lower()]

def find_field_locations(location_data, email_array):
    field_locations = {'Email': [], 'Time': [], 'Location': [], 'Latitude': [], 'Longitude': []}

    for email in email_array:
        print(email[2])
        field_locations["Email"].append(email[0])
        field_locations["Time"].append(email[1])
        field_locations["Location"].append(email[2])
        lat_and_long = find_lat_and_long(location_data, email[2])
        print(lat_and_long)
        field_locations["Latitude"].append(lat_and_long["lat"])
        field_locations["Longitude"].append(lat_and_long["long"])
    return field_locations



def main():
    processed_email_array =  pickle.load( open("processed_email_array.p", "rb"))
    location_data =  pickle.load( open("processed_location_data.p", "rb"))
    field_locations = find_field_locations(location_data, processed_email_array)


    df = pd.DataFrame(field_locations, columns= ['Email', 'Time', 'Location', 'Latitude', 'Longitude'])
    df.to_csv (r'field_staff_locations.csv', index = False, header=True)



main()
