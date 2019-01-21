import time
import requests
import TorMultiplier
import subprocess
import os

list_of_sockets = []


"""
Prints the socket's IP and locate.
"""
def printIP(session):
    print(session.get("http://httpbin.org/ip").text.split(":")[1].split('"')[1]+" Located in ",end="")
    print(session.get("https://mylocation.org/").text.split("Country")[1].split("<td>")[1].split("</td>")[0])

"""

"""
def fun(number):
    # Get them
    if len(list_of_sockets) <=  0:
        print("Length is 0")
        # Create sockets
        TorMultiplier.create_sockets(int(number))
    # Print IPs
    input("Start? >")
    for sockets in list_of_sockets:
        try:
            port = sockets[0]
            print("Connecting using port: ",port)
            session = TorMultiplier.get_tor_session(port)
            printIP(session)
        except:
            print("R")
    #clean_processes()
    print("\n Real public IP :")
    # Prints your normal public IP
    printIP(requests)


def main():
    fun(10)


if __name__ == '__main__':
    main()

