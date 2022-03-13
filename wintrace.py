import socket


try:
    import os, sys, json, requests
    import rich
except:
    import subprocess
    subprocess.call(["pip", "install", "rich"], stdout = open(os.devnull, "w"), stderr = subprocess.STDOUT)
    import sys
    os.system(" ".join(sys.argv))
if "python" == sys.argv[0]:
    if "-m" != sys.argv[2]:
        ip = sys.argv[2]
    else:
        ip = requests.get("https://api.ipify.org").text
else:
    if "m" != sys.argv[1]:
        ip = sys.argv[1]
    else:
        ip = requests.get("https://api.ipify.org").text
import requests
info = requests.get('http://ip-api.com/json/'+ip).json()
print(info)
if info["status"] == "success":
    rich.print("""[bold red]
  __      _____ _  _ _____ ___    _   ___ ___ 
  \ \    / /_ _| \| |_   _| _ \  /_\ / __| __|
   \ \/\/ / | || .` | | | |   / / _ \ (__| _| 
    \_/\_/ |___|_|\_| |_| |_|_\/_/ \_\___|___|
    [/bold red]
    [bold red]
    ------[/bold red] [green]Ip Information[/green] [bold red]------[/bold red]\n
    [yellow]IP Address[/yellow]    >   """+ip+"""
    [yellow]Country   [/yellow]    >   [green]"""+info["country"]+"""[/green]
    [yellow]Region    [/yellow]    >   [green]"""+info["regionName"]+"""[/green]
    [yellow]City      [/yellow]    >   [green]"""+info["city"]+"""[/green]
    [yellow]Latitude  [/yellow]    >   [green]"""+str(info["lat"])+"""[/green]
    [yellow]Longitude [/yellow]    >   [green]"""+str(info["lon"])+"""[/green]
    [yellow]Google Maps[/yellow]   >   [green]"""+"http://maps.google.com/maps?q="+str(info["lat"])+","+str(info["lon"])+"""[/green]
    [yellow]Time zone [/yellow]    >   [green]"""+info["timezone"]+"""[/green]
    [yellow]ISP       [/yellow]    >   [green]"""+info["isp"]+"""[/green]
    [yellow]Organization[/yellow]  >   [green]"""+info["org"]+"""[/green]
    [yellow]ASN         [/yellow]  >   [green]"""+info["as"]+"""[/green]
    """)
else:
    rich.print("""[bold red]
  __      _____ _  _ _____ ___    _   ___ ___ 
  \ \    / /_ _| \| |_   _| _ \  /_\ / __| __|
   \ \/\/ / | || .` | | | |   / / _ \ (__| _| 
    \_/\_/ |___|_|\_| |_| |_|_\/_/ \_\___|___|
    [/bold red]
    [bold red]
  ----[/bold red] [yellow]FAILED TO RETRIEVE IP INFORMATION[/yellow] [bold red]-----[/bold red]\n
  [red]JSON[/red]  >  """+str(info)+"""
    """)