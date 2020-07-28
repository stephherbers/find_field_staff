import pytest
import re

import process_location_data as processor
import field_staff_finder as finder


def test_parser_regular_expression_lat_and_long():
    sample_line = "2794507	Kessel-Lo	Kessel-Lo	Kessel-Loo,Leuven (Kessel-Lo)	50.88549	4.73717	P	PPL	BE		VLG	VBR	24	24062	30215		35	Europe/Brussels	2020-05-25"
    lat_and_long = re.findall(r'[0-9]+\.[0-9]*', sample_line)
    assert ["50.88549", "4.73717"] == lat_and_long


def test_parser_regular_expression_city_line():
    sample_line = "2794507	Kessel-Lo	Kessel-Lo	Kessel-Loo,Leuven (Kessel-Lo)	50.88549	4.73717	P	PPL	BE		VLG	VBR	24	24062	30215		35	Europe/Brussels	2020-05-25"
    city_names_line = re.split('\d+', sample_line)[1]
    assert city_names_line == "\tKessel-Lo\tKessel-Lo\tKessel-Loo,Leuven (Kessel-Lo)\t"

def test_parser_regular_expression_cities_list():
    sample_line = "2794507	Kessel-Lo	Kessel-Lo	Kessel-Loo,Leuven (Kessel-Lo)	50.88549	4.73717	P	PPL	BE		VLG	VBR	24	24062	30215		35	Europe/Brussels	2020-05-25"
    city_names_line = re.split('\d+', sample_line)[1]
    city_names = set(re.findall(r'[a-zA-Z -\']+', city_names_line))
    assert sorted(["Kessel-Lo", "Kessel-Loo", "Leuven "]) == sorted(list(city_names))
