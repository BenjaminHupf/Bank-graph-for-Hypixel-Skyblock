# Bank graph for Hypixel SkyBlock
<a href="https://www.python.org/downloads/release/python-3110/"><img src="https://img.shields.io/badge/python-3.11.0-success?style=for-the-badge&logo=python&logoColor=white"></img></a>
<img src="https://img.shields.io/badge/Last%20update-04.11.2023-blue?style=for-the-badge"></img>
[<img src="https://img.shields.io/github/license/BenjaminHupf/Bank-graph-for-Hypixel-Skyblock?style=for-the-badge">](LICENSE.md)

## Description
Bank graph for Hypixel SkyBlock is a small program which I wrote to get the bank account balance of my coop SkyBlock world and print it to a graph to visualize our progress.

**You can also use <a href="https://github.com/BenjaminHupf/Discord-bot-for-SkyBlock-graph">Discord bot for SkyBlock graph</a> to make a Discord bot which uses this program and generates a graph when you type a command in Discord.**

## Table of Contents
- <a href="#description">Description</a>
- <a href="#table-of-contents">Table of Contents</a>
- <a href="#how-to-install">How to install</a>
  - <a href="#installing-the-libraries">Installing the libraries</a>
  - <a href="#how-to-get-a-hypixel-api-key">How to get the Hypixel API key</a>
  - <a href="#installing-bank-graph">Installing Bank graph</a>
- <a href="#how-to-use">How to use</a>
  - <a href="#setup-in-hypixel">Setup in Hypixel</a>
  - <a href="#customize-program">Customize program</a>
  - <a href="#run-the-program">Run the program</a>
- <a href="#how-it-works">How it works</a>
- <a href="#tests-and-results">Tests and results</a>
- <a href="#license-and-credits">License and credits</a>

## How to install
The bank graph program requires:
- <a href="https://www.python.org/downloads/release/python-3107/">Python 3.11.0</a>
- <a href="https://pypi.org/project/requests/">requests</a>
- <a href="https://pypi.org/project/matplotlib/">matplotlib</a>
- pickle
- time
- os
- A Hypixel API Key

### Installing the libraries
The libraries **pickle**, **time** and **os** are pre-installed with Python.

The remaining libraries can be installed with pip using this command:

```cmd
pip install requests matplotlib
```

You can also install them with __requirements.txt__.

### How to get a Hypixel API key

To get an API key you have to go to the following website: <a href="https://developer.hypixel.net">https://developer.hypixel.net</a>. On this side you have to login to your account (or create a new one), afterwards you can generate an API Key, which is needed to reach the Hypixel API, make sure to save it to make sure you do not loose it and NEVER give it to somebody else.

### Installing Bank graph

To install this program simply download this repository as a .zip file and unpack it in a folder.

## How to use

### Setup in Hypixel

First of all, you need to enable the Banking API in Hypixel.

To do that you have to join the profile you want this program to work on and open your SkyBlock Menu with the Nether Star in you hotbar. In there you have to open the Settings (Picture 1).

<img src="https://user-images.githubusercontent.com/104715363/200687460-27ce3e0d-0401-42da-b7b6-c621f2057e66.png"><br>
**Picture 1 - SkyBlock Menu**

From the settings page you have to navigate to your island settings (Picture 2).

<br><br><img src="https://user-images.githubusercontent.com/104715363/200687463-8b11c015-f7d9-4fff-804e-44bdf8c3fc69.png"><br>
**Picture 2 - Settings**

Then you can activate the Banking API by clicking on the icon below the gold ingot (Picture 3). Make sure that the icon is green because otherwise the Hypixel API will not give the required informations needed for the program to work.

<br><br><img src="https://user-images.githubusercontent.com/104715363/200687836-c9fc47cb-80a4-4370-8fef-5c2fdda6bece.png"><br>
**Picture 3 - Settings - Island Settings**

### Customize program

When you open __main.py__ with an editor of your choice you will see the following part of the program:

```python
apiKey = '[YOUR HYPIXEL API KEY HERE]'
playerUsername = '[YOUR MINECRAFT USERNAME HERE]'
```

Where you have to put your <a href="#how-to-get-a-hypixel-api-key">Hypixel API key</a> and the name of the Minecraft Account you have your SkyBlock profile on.

Additionally, you need to specify the SkyBlock-Account you want for the program to get the data from. For this you need to change the number ( [0] ) in this line:
  
```python
filteredData = data['profiles'][0]['banking']['balance']
```

You can get this number by subtracting 1 from the Slot number of your SkyBlock-Account.

Example:
- SkyBlock Slot 1 -> 1 - 1 = 0
- SkyBlock Slot 3 -> 3 - 1 = 2

Note: Hypixel changed something about how the API works, so for our profile the number randomly changed (don't ask me how or why), so if you have multiple accounts and the program fails to get the banking data or gathers the data from a wrong account, try another number. 

You can also turn on dark mode by adding __True__ or __darkmode = True__ as third parameter in __generateGraph()__. Examples:

```python
generateGraph(apiKey, playerUsername, True)
```

OR

```python
generateGraph(apiKey, playerUsername, darkmode = True)
```

### Run the program

After running the program you should see that one new file was created in the main directory of the program and two new files in the data folder. 

The two files in the data directory store your previously recorded bank balances and the timestamps they were recorded. You should leave these files alone, unless you want to restart the graph, then you just have to delete these files. 

The file in the main directory is your graph. If you ran the program only once you will not see much in it, but if you rerun the program when the balance of your bank account in SkyBlock changed, you will see that the graph now actually contains a graph.

**Especially when you run the program for the first time or when you changed something in the program, you should watch the terminal because some error messages might be printed there.**

## How it works

This program is desinged in a way which allows you to incorporate it in one of your own programs. 
You can also get <a href="https://github.com/BenjaminHupf/Discord-bot-for-SkyBlock-graph">Discord bot for SkyBlock graph</a> which is another program I wrote which uses this program to generate and send the graph to you when you type a command in Discord.

When you start the program it first checks if the files __balanceHistory.dat__ and __timeHistory.dat__ exist in the data folder. 
When they exist the program loads these files as they contain your previous Bank data informations otherwise it will create new files to save your bank history. 

Then it connects to the Mojyng API using your player name to recieve your UUID.
After that it connects to the Hypixel API to recieve the SkyBlock data of the player with the just recieved UUID and then it filters the recieved json file so that it just adds the balance to the __balanceHistory.dat__. During that process it also gets the current time (Format: YYYY.MM.DD-hh:mm) and saves to to __timeHistory.dat__.

Using these data it creates a graph and saves it as __graph.png__ to the main directory. Please be aware that this file will be overwritten everytime you rerun the program, so if you like a graph make sure that you copy-paste it to somewhere else.

A generated graph looks like this:

Light Mode:
<br><img src="https://user-images.githubusercontent.com/104715363/201547883-00fbcd53-cf8e-4bea-92ef-97ae5b6d120e.png">

Dark Mode:
<br><img src="https://user-images.githubusercontent.com/104715363/201775400-7bb453d5-f84f-4c35-a39c-ee02e54fb6d5.png">

## Tests and results

Tested in __Python 3.10.7__ and __Python 3.11.0__, but I recommend __Python 3.11.0__ as it contains some optimizations allowing for faster code.

## License and credits

This work is made available under the **[GNU Affero General Public License v3.0](LICENSE.md)**.

Project made by **<a href="https://github.com/BenjaminHupf">Benjamin Hupf</a>**.
