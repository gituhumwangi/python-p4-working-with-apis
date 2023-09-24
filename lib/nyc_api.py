import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        return response.content

    def program_school(self):
        # We use the JSON library to parse the API response into nicely formatted JSON
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])
        return programs_list

# Create an instance of the GetPrograms class
get_programs_instance = GetPrograms()

# Call the methods to retrieve and process data
# 

programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)