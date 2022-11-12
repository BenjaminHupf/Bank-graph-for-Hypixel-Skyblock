# Bank graph for Hypixel Skyblock
<a href="https://www.python.org/downloads/release/python-3107/"><img src="https://img.shields.io/badge/python-3.10.7-success?style=for-the-badge&logo=python&logoColor=white"></img></a>
<img src="https://img.shields.io/badge/Last%20update-12.11.2022-blue?style=for-the-badge"></img>
<a href="https://www.gnu.org/licenses/agpl-3.0"><img src="https://img.shields.io/github/license/TachLaif/Banking-graph-for-Hypixel-Skyblock?style=for-the-badge"></img></a>

## Description
Bank graph for Hypixel Skyblock is a small program which I wrote to get the bank account balance of my coop SkyBlock world and print it to a graph to visualize our progress.

## Table of Contents
- <a href="#description">Description</a>
- <a href="#table-of-contents">Table of Contents</a>
- <a href="#how-to-install">How to install</a>
  - <a href="#installing-the-libraries">Installing the libraries</a>
  - <a href="#how-to-get-a-hypixel-api-key">How to get the Hypixel API key</a>
  - <a href="#how-to-get-your-minecraft-player-uuid">How to get your Minecraft Player UUID</a>
  - <a href="#installing-bank-graph">Installing Bank graph</a>
- <a href="#how-to-use">How to use</a>
  - <a href="#setup-in-hypixel">Setup in Hypixel</a>
  - <a href="#customize-program">Customize program</a>
  - <a href="#run-the-program">Run the program</a>
- <a href="#how-it-works">How it works</a>
- <a href="problems-and-future-plans">Problems and future plans</a>
- <a href="#license-and-credits">License and credits</a>

## How to install
The bank graph program requires:
- <a href="https://www.python.org/downloads/release/python-3107/">Python 3.10.7</a>
- <a href="https://pypi.org/project/requests/">requests</a>
- <a href="https://pypi.org/project/matplotlib/">matplotlib</a>
- pickle
- time
- os
- A Hypixel API Key
- Your Minecraft Player UUID

### Installing the libraries
The libraries **pickle**, **time** and **os** are pre-installed with Python.

The remaining libraries can be installed with pip using this command:

```cmd
pip install requests matplotlib
```

### How to get a Hypixel API key

To get an API key you have to join <a href="https://hypixel.net">mc.hypixel.net</a> and type the following command in the chat:

```
/api
```

This command will generate you an API key in the chat which you need to reach the Hypixel API, so save it to make sure that you do not lose it and NEVER give it to somebody else.


### How to get your Minecraft Player UUID

To find your Minecraft Player UUID go to a page like <a href="https://minecraftuuid.com">minecraftuuid.com</a> and put in your username and it will show you your Player UUID which you should save for later.

You have to use the same username on which you have your SkyBlock profiles.

### Installing Bank graph

To install this program simply download this repository as a .zip file and unpack it in a folder.

## How to use

### Setup in Hypixel

First of all, you need to enable the Banking API in Hypixel.

To do that you have to join the profile you want this program to work on and open your SkyBlock Menu with the Nether Star in you hotbar. In there you have to open the Settings (Picture 1).

<img src="https://user-images.githubusercontent.com/104715363/200687460-27ce3e0d-0401-42da-b7b6-c621f2057e66.png"><br>
**Picture 1 - SkyBlock Menu**

From the settings page you have to navigae to your island settings (Picture 2).

<br><br><img src="https://user-images.githubusercontent.com/104715363/200687463-8b11c015-f7d9-4fff-804e-44bdf8c3fc69.png"><br>
**Picture 2 - Settings**

Then you can activate the Banking API by clicking on the icon below the gold ingot (Picture 3). Make sure that the icon is green because otherwise the Hypixel API will not give the required informations needed for the program to wirk.

<br><br><img src="https://user-images.githubusercontent.com/104715363/200687836-c9fc47cb-80a4-4370-8fef-5c2fdda6bece.png"><br>
**Picture 3 - Settings - Island Settings**

### Customize program

When you open __main.py__ with an editor of your choice you will see the following part of the program:

```python
apiKey = '[YOUR HYPIXEL API KEY HERE]'
playerUUID = '[YOUR MINECRAFT PLAYER UUID HERE]'
```

Where you have to put your <a href="#how-to-get-a-hypixel-api-key">Hypixel API key</a> and your <a href="#how-to-get-your-minecraft-player-uuid">Minecraft player UUID.</a>

Additionally, you need to specify the SkyBlock-Account you want for the program to get the data from. For this you need to change the number ( [0] ) in this line:
  
```python
filteredData = data['profiles'][0]['banking']['balance']
```

You can get this number by subtracting 1 from the Slot number of your SkyBlock-Account.

Example:
- SkyBlock Slot 1 -> 1 - 1 = 0
- SkyBlock Slot 3 -> 3 - 1 = 2

### Run the program

After running the program you should see that one new file was created in the main directory of the program and two new files in the data folder. 

The two files in the data directory store your previously recorded bank balances and the timestamps they were recorded. You should leave these files alone, unless you want to restart the graph, then you just have to delete these files. 

The file in the main directory is your graph. If you ran the program only once you will not see much in it, but if you rerun the program when the balance of your bank account in SkyBlock changed, you will see that the graph now actually contains a graph.

**Especially when you run the program for the first time or when you changed something in the program, you should watch the terminal because some error messages might be printed there.**

## How it works

This program is desinged in a way which allows you to incorporate it in one of your own programs. 
In the future I plan on uploading a new repository which will be a simple Discord bot that connects to this program and sends the graph to you when you type a command.

When you start the program it first checks if the files __balanceHistory.dat__ and __timeHistory.dat__ exist in the data folder. 
When they exist the program loads these files as they contain your previous Bank data informations otherwise it will create new files to save your bank history. 

After that it connects to the Hypixel API to recieve the SkyBlock data of the player with the predefined UUID and then it filters the recieved json file so that it just adds the balance to the __balanceHistory.dat__. During that process it also gets the current time (Format: YYYY.MM.DD-hh:mm) and saves to to __timeHistory.dat__.

Using these data it creates a graph and saves it as __graph.png__ to the main directory. Please be aware that this file will be overwritten everytime you rerun the program, so if you like a graph make sure that you copy-paste it to somewhere else.

A generated graph looks like this:
<br><img src="https://user-images.githubusercontent.com/104715363/201477175-a0e04f39-2798-48e7-be75-205a74220944.png">

## Problems and future plans

- [ ] **Bug**: When there are too many entries the labels on the x-Axis will overlap each other.
- [x] **Improvement idea**: Add multiple different except ways to allow for better error handling.
- [ ] **Visual change**: Add a dark mode.

## License and credits

This work is made available under the **GNU Affero General Public License v3.0**.

Project made by <a href="https://github.com/TachLaif">TechLife</a>.
<br><br><a href="https://discord.com"><img src="https://img.shields.io/badge/TechLife-4447-informational?style=for-the-badge&logo=discord&logoColor=white"></a><br><a href="https://twitter.com/_Tech4Life_"><img src="https://img.shields.io/badge/Twitter-@__Tech4Life__-informational?style=for-the-badge&logo=twitter&logoColor=white"></a><br><a href="https://www.buymeacoffee.com/TechLife"><img src="https://img.shields.io/badge/Buy%20me%20a-coffee-red?style=for-the-badge&logo=buymeacoffee&logoColor=white" title="I like coffee!"></a>
