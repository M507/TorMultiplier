import subprocess
import time
list_of_sockets = []


def create_a_process(command):
    if len(command) > 0:
        print(command)
        result = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE)
        #out, err = result.communicate()
        #print(out)
        return result
    return -1

def create_sockets(number):
    socks_port=9051
    for i in range(number):
        command = "tor --PidFile tor"+str(i)+".pid --SocksPort "+str(socks_port)+" --DataDirectory data/tor"+str(i)+" "
        create_a_process("mkdir data/tor"+str(i))
        process = create_a_process(command)
        # if (process.pid < 0):
        #     print("Process number: %i Task: %i , Failed",str(process.pid),str(i))
        list_of_sockets.append([socks_port,process])
        socks_port+=1
    time.sleep(5)


def get_list_of_sockets():
    return list_of_sockets

def clean_processes():
    for process in list_of_sockets:
        var = process[1].kill
        print(str(process[0])+" is killed")

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
