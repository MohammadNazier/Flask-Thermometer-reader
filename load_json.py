import json
import pathlib

json_file1 = pathlib.Path("devices.json").read_text()
data = json.loads(json_file1)
#print(data['data'])
def read_json():
    mac_ad = []
    room_name = []
    for n in data['data']:
        mac_ad.append(n["mac_address"])
        room_name.append(n['room'])
        #print(n["mac_address"])
    return [mac_ad, room_name]


#example to test this lib
'''
mac_ad , room = read_json()
for eath in range(len(mac_ad)):
    print(mac_ad[eath]+ " " + room[eath])
'''
