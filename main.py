# Copyright (C) 2022 - TechLife
#
# Bank graph for Hypixel SkyBlock (https://github.com/TachLaif/Bank-graph-for-Hypixel-Skyblock)
# - Made with ♥ by TechLife (https://github.com/TachLaif)
# Last update: 19.11.2022
#
# This work is made available under the GNU Affero General Public License v3.0.
# More informations about the license can be found at:
# https://www.gnu.org/licenses/agpl-3.0

import requests
import pickle
import time
import os
import matplotlib.pyplot as plt

apiKey = '[YOUR HYPIXEL API KEY HERE]'
playerUsername = '[YOUR MINECRAFT USERNAME HERE]'

def generateGraph(key: str, username: str, darkmode = False):
    if os.path.isfile('data/balanceHistory.dat') and os.path.isfile('data/timeHistory.dat'):
        with open('data/balanceHistory.dat', 'rb') as f:
            balanceHistory = pickle.load(f)
        with open('data/timeHistory.dat', 'rb') as f:
            timeHistory = pickle.load(f)
    else:
        balanceHistory = []
        timeHistory = []
    
    try:
        uuid = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{username}').json()['id']
        print(uuid)
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
            title_color = 'black'
            if darkmode:
                plt.figure(facecolor = '#1E1E1E')
                ax = plt.axes()
                ax.set_facecolor('#1E1E1E')
                ax.xaxis.label.set_color('white')
                ax.yaxis.label.set_color('white')
                ax.tick_params(axis = 'x', colors = 'white')
                ax.tick_params(axis = 'y', colors = 'white')
                ax.spines['left'].set_color('white')
                ax.spines['top'].set_color('white')
                ax.spines['right'].set_color('white')
                ax.spines['bottom'].set_color('white')
                title_color = 'white'
            plt.plot(timeHistory, balanceHistory, color='red')
            plt.xlabel('Time')
            plt.ylabel('Balance')
            plt.title('Hypixel Skyblock - Bank Balance History', color = title_color)
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
    
    
    except:
        print(f'Could not find UUID of username {username}. Please make sure it is spelled correctly.')

    

if __name__ == '__main__':
    generateGraph(apiKey, playerUsername)
