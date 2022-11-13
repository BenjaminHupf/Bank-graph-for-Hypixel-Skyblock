# Hypixel-SkyBlock - Banking graph - Made with ♥ by TechLife (https://github.com/TachLaif)
# Last update: 13.11.2022
#
# This work is made available under the GNU Affero General Public License v3.0.
# More informations about the license can be found at
# https://www.gnu.org/licenses/agpl-3.0

import requests
import pickle
import time
import os
import matplotlib.pyplot as plt

apiKey = '[YOUR HYPIXEL API KEY HERE]'
playerUUID = '[YOUR MINECRAFT PLAYER UUID HERE]'

def generateGraph(key: str, uuid: str, darkmode = False):
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
        filteredData = data['profiles'][0]['banking']['balance'] # Change the number ( [0] ) to specify your SkyBlock Account
        timeString = time.strftime('%Y.%m.%d-%H:%M', time.localtime())
        balanceHistory.append(float(filteredData))
        timeHistory.append(timeString)
        if darkmode:
            plt.style.use('dark_background')
        plt.plot(timeHistory, balanceHistory, color='red')
        plt.xlabel('Time')
        plt.ylabel('Balance')
        plt.title('Hypixel Skyblock - Bank Balance History')
        plt.grid(True)
        plt.xticks(timeHistory, timeHistory, rotation=90)
        plt.tight_layout()
        plt.savefig('graph.png')
        with open('data/balanceHistory.dat', 'wb') as f:
            pickle.dump(balanceHistory, f)
        with open('data/timeHistory.dat', 'wb') as f:
            pickle.dump(timeHistory, f)
    except (KeyError):
        print('Program ran into a KeyError')
        print('Hypixel API did not sent the required banking data.')
        print('If it does not work in a few moments, terminate the program and check if you have the Banking API enabled in Hypixel SkyBlock')
        generateGraph(key, uuid)
    except (IndexError):
        print('Program ran into an IndexError')
        print('Please make sure that you have used the right SkyBlock Profile Number')

if __name__ == '__main__':
    generateGraph(apiKey, playerUUID)