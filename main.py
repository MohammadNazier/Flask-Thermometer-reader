
from flask import Flask #need to install 
from lywsd03mmc import Lywsd03mmcClient #need to install
from load_json import read_json
from time import gmtime, strftime

app = Flask(__name__)

@app.route("/temp")
def temperature():
    mac_ads, room = read_json()
    all_text = ""
    for eath in range(len(mac_ads)):
        header = ('<p>'+room[eath]+'    '+'<p>'+mac_ads[eath]+'<br><br>')
        mac_ad = (mac_ads[eath])
        client = Lywsd03mmcClient(mac_ad)
        client.connect()
        data = client.data
        all_text = all_text + "<br>"+strftime("%Y-%m-%d %H:%M:%S", gmtime())+ header + ('Temperature: ' + str(data.temperature) +' <br> '
                    +'Humidity: ' + str(data.humidity)+' <br> '+'Battery: ' + str(data.battery)+' <br> '
                    +'Display units: ' + client.units)+'<br>__________________________'

    return all_text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8333, threaded = True, debug = True) #try app.ran() if you wont run tha app localy 

