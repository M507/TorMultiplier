import time
import requests
import TorMultiplier
import subprocess
import os



list_of_sockets = []


def execute(command):
    pid=os.fork()
    if pid==0:
        # new process
        os.system(command)
        exit()

def getPID(i):
    pid =""
    while len(pid) < 4:
        command = "cat data/pids/"+str(i)+".pid"
        result = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE)
        out, err = result.communicate()
        pid = out
    return pid

def create_a_process(command,i):
    if len(command) > 0:
        execute(command+" > /dev/null ;echo $! > data/pids/"+str(i)+".pid")



    return -1

# def isAlive(p):
#     poll = p.poll()
#     if poll == None:
#         # p.subprocess is alive
#         print(p.pid," is alive")
#     else:
#         print(p.pid," is dead")



def create_sockets(number):
    socks_port=9051
    for i in range(1,number+1):
        command = "tor --PidFile tor"+str(i)+".pid --SocksPort "+str(socks_port)+" --DataDirectory data/tor"+str(i)+" "
        execute("mkdir data/tor"+str(i))
        pid = create_a_process(command,i)
        list_of_sockets.append([socks_port,pid])
        socks_port+=1
    time.sleep(5)
    return list_of_sockets


def clean_processes():
    for process in list_of_sockets:
        pid = process[1]
        execute("kill "+str(pid))


def kill_a_socket(pid,port):
    try:
        if pid > 0:
            var =pid.kill
            return 1
    except:
        print("Couldnt kill %i",pid)
        return -1
    try:
        if port > 0:
            for process in list_of_sockets:
                if process[0] == port:
                    var = process[1].kill
            return 1
    except:
        print("Couldnt kill process in port %i",port)
        return -1




def get_tor_session(port_number):
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:'+str(port_number),
                       'https': 'socks5://127.0.0.1:'+str(port_number)}
    return session



def printIP(session):
    print(session.get("http://httpbin.org/ip").text.split(":")[1].split('"')[1]+" Located in ",end="")
    print(session.get("https://mylocation.org/").text.split("Country")[1].split("<td>")[1].split("</td>")[0])

def fun(number):
    # Get them
    if len(list_of_sockets) <=  0:
        print("Length is 0")
        # Create sockets
        create_sockets(int(number))
    # Print IPs
    input("Start? >")
    for sockets in list_of_sockets:
        try:
            port = sockets[0]
            print("Connecting using port: ",port)
            session = get_tor_session(port)
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

