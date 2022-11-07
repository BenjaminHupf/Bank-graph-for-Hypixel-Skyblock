# Hypixel-SkyBlock - Banking graph - Made with ♥ by TechLife (https://github.com/TachLaif)
# Last update: 07.11.2022
#
# This work is made available under the GNU General Public License v3.0.
# More informations about the license can be found at
# https://www.gnu.org/licenses/gpl-3.0.html

import requests
import pickle
import time
import os
import matplotlib.pyplot as plt

apiKey = '[YOUR HYPIXEL API KEY HERE]'
playerUUID = '[YOUR MINECRAFT PLAYER UUID HERE]'

def generateGraph(key: str, uuid: str):
    if os.path.isfile('data/balanceHistory.dat') and os.path.isfile('data/timeHistory.dat'):
        with open('data/balanceHistory.dat', 'rb') as f:
            balanceHistory = pickle.load(f)
        with open('data/timeHistory.dat', 'rb') as f:
            timeHistory = pickle.load(f)
    else:
        balanceHistory = []
        timeHistory = []
    
    data = requests.get(
        url = 'https://api.hypixel.net/skyblock/profiles',
        params = {
            'key': key, 
            'uuid': uuid 
        }
    ).json()

    try:
        filteredData = data['profiles'][1]['banking']['balance']
        timeString = time.strftime('%Y.%m.%d-%H:%M', time.localtime())

        balanceHistory.append(float(filteredData))
        timeHistory.append(timeString)
        plt.plot(timeHistory, balanceHistory, color='red')
        plt.xlabel('Time')
        plt.ylabel('Balance')
        plt.title('Hypixel Skyblock - Bank Balance History')
        plt.grid(True)
        plt.xticks(timeHistory, timeHistory, rotation=90)
        plt.tight_layout()
        plt.savefig('diagram.png')

        with open('data/balanceHistory.dat', 'wb') as f:
            pickle.dump(balanceHistory, f)
        with open('data/timeHistory.dat', 'wb') as f:
            pickle.dump(timeHistory, f)
    except:
        generateGraph(key, uuid)
if __name__ == '__main__':
    generateGraph(apiKey, playerUUID)