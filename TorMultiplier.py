import time
import subprocess
import os


"""
Executes a command
"""
def execute(command):
    pid=os.fork()
    if pid==0:
        # new process
        os.system(command)
        exit()

"""
Gets a PID using i which is the socket's ID.
"""
def getPID(i):
    pid =""
    while len(pid) < 4:
        command = "cat data/pids/"+str(i)+".pid"
        result = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE)
        out, err = result.communicate()
        pid = out
    return pid

"""
Executes a command, and saves it's process ID in "pids" folder.
"""
def create_a_process(command,i):
    if len(command) > 0:
        execute(command+" > /dev/null ;echo $! > data/pids/"+str(i)+".pid")
    return -1

"""
Checks if a process is alive.
"""
def isAlive(process):
    pass

"""
Creates a number of socket according to "number" parameter.
"""
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

"""
Kills all the processes in list_of_sockets list.
"""
def clean_processes():
    for process in list_of_sockets:
        pid = process[1]
        execute("kill "+str(pid))

"""
It kills just one process/socket.
"""
def kill_a_socket(pid,port):
    try:
        if pid > 0:
            execute("kill "+pid)
            print("killed "+pid)
            return 1
    except:
        print("Couldn kill ",pid)
        return -1
    try:
        if port > 0:
            for process in list_of_sockets:
                if process[0] == port:
                    execute("kill "+process[1])
                    print("killed "+process[1])
            return 1
    except:
        print("Couldn't kill process in port ",port)
        return -1

"""
Connects to a proxy.
"""
def get_tor_session(port_number):
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:'+str(port_number),
                       'https': 'socks5://127.0.0.1:'+str(port_number)}
    return session
