import pickle
import re

# processes location txt file and outputs location_dict : {"city_name": {"lat":  "long": }}
def process_location_data(file_name):
    location_dict = {}
    file = open(file_name, "r")
    for line in file:
        lat_and_long_dict = {}
        city_names_line = re.split('\d+', line)[1]
        city_names = set(re.findall(r'[a-zA-Z -\']+', city_names_line))
        lat_and_long = re.findall(r'[0-9]+\.[0-9]*', line)
        try:
            lat_and_long_dict["lat"] = lat_and_long[0]
            lat_and_long_dict["long"] = lat_and_long[1]
        except:
            pass #not proper lat or long found for this line
        for city in city_names:
            city = city.lower()
            location_dict[city] = lat_and_long_dict
    file.close()
    return location_dict


def main():
    location_data = process_location_data("cities15000.txt")
    pickle.dump(location_data, open( "processed_location_data.p", "wb"))



main()
