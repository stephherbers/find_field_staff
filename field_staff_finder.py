import re


# processes location txt file and outputs location_dict : {"city_name": {"lat":  "long": }}
def process_location_data(file_name):
    location_dict = {}
    lat_and_long_dict = {}
    file = open(file_name, "r")
    for line in file:
        city_names = set(re.findall(r',([a-zA-Z ]+)', line))
        lat_and_long = re.findall(r'[0-9]+\.[0-9]*', line)
        try:
            lat_and_long_dict["lat"] = lat_and_long[0]
            lat_and_long_dict["long"] = lat_and_long[1]
        except:
            pass #not proper lat or long found for this line
        for city in city_names:
            location_dict[city] = lat_and_long_dict
    return location_dict





def main():
    location_data = process_location_data("cities15000.txt")



main()
