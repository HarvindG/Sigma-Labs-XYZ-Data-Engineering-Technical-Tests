# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Correct link: https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode=WC2B6EX

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

"""
[
    {
        "name": "Central London Employment Tribunal",
        "lat": 51.5158158439741,
        "lon": -0.118745425821452,
        "number": null,
        "cci_code": null,
        "magistrate_code": null,
        "slug": "central-london-employment-tribunal",
        "types": [
            "Tribunal"
        ],
        "address": {
            "address_lines": [
                "Victory House",
                "30-34 Kingsway"
            ],
            "postcode": "WC2B 6EX",
            "town": "London",
            "type": "Visiting"
        },
        "areas_of_law": [
            {
                "name": "Employment",
                "external_link": "https%3A//www.gov.uk/courts-tribunals/employment-tribunal",
                "display_url": "<bound method AreaOfLaw.display_url of <AreaOfLaw: Employment>>",
                "external_link_desc": "Information about the Employment Tribunal"
            }
        ],
        "displayed": true,
        "hide_aols": false,
        "dx_number": "141420 Bloomsbury 7",
        "distance": 1.29
    },
    etc
]
"""

# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type

import csv
import requests

COURT_API_URL = "https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode="


def extract_customer_info(filename: str) -> list[dict]:
    """Extract customer information from csv file and return list of all people"""

    customer_data = []
    with open(filename, 'r') as people_file:
        reader = csv.reader(people_file)
        for row in reader:
            customer_data.append(
                {'name': row[0], 'type of court desired': row[2], 'home postcode': row[1]})
    customer_data.pop(0)

    return customer_data


def get_all_nearby_courts(person: dict) -> list[dict]:
    """Return list of all courts near to customer postcode"""

    response = requests.get(COURT_API_URL + person['home postcode'])
    return response.json()


def find_single_nearest_court(people_data: list[dict]) -> list[dict]:
    """Return single nearest court that matches search type for each person in person list"""

    for person in people_data:

        # Get all nearby courts
        json = get_all_nearby_courts(person)

        distances = []
        relevant_courts = []

        # Refine search to courts where type is matching desired court type
        for court in json:
            if person['type of court desired'] in court['types']:
                relevant_courts.append(court)
                distances.append(court['distance'])

        # Determine shortest distance of all courts of correct type
        shortest_distance = min(distances)

        # construct output json
        for court in relevant_courts:
            if court['distance'] == shortest_distance:

                if not court['dx_number']:
                    court_dx_num = 'Unavailable'
                else:
                    court_dx_num = court['dx_number']

                person.update({'nearest court': court['name'], 'dx_number': court_dx_num,
                              'distance to nearest court': court['distance']})

    return people_data


if __name__ == "__main__":
    # [TODO]: write your answer here

    customer_info = extract_customer_info('people.csv')

    court_search_results = find_single_nearest_court(customer_info)

    print(court_search_results)
