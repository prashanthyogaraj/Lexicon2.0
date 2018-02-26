import paramiko
import socket
import time
import re
from paramiko import SSHClient
import os


def server_login(server_ip,password):
    # server_ip = '10.126.141.112'
    username = 'admin'
    # password = 'Cisco123'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print("Connecting to server %s" % server_ip)
        error_status = ssh.connect(server_ip, username=username, password=password, timeout=60, allow_agent=False,
                                   look_for_keys=False)
        print "error status is",error_status
        if error_status is None:
            print("SSH login successful for IP %s" % server_ip)
            time.sleep(10)
            connect = ssh.invoke_shell()
            return connect
    except paramiko.AuthenticationException:
        print("Authentication Error for server:%s" % server_ip)
    except paramiko.BadHostKeyException:
        print("Server's host key could not be verified")
    except paramiko.SSHException:
        print("Error connecting or establishing  SSH session")
    except socket.error:
        print("Connection Error for IP:%s" % server_ip)
    except Exception as e:
        print(str(e))

def get_adapter_detail(server_ip,password):
    server_detail=[]
    connect = server_login(server_ip,password)
    connect.send('scope chassis\n')
    time.sleep(10)
    stdout = connect.send('show pci-adapter detail | no-more\n')
    time.sleep(10)
    detail = connect.recv(99999)
    out = str(detail.decode('utf-8')).split("\n")
    for i in out:
        # for i in final_out:
        slot_pattern = "Slot (.*):"
        FW_pattern = "Firmware Version: (.*)"
        Prd_pattern = "Product Name: (.*)"
        slot_match = re.search(slot_pattern, i)
        fw_match = re.search(FW_pattern, i)
        prd_match = re.search(Prd_pattern, i)
        if slot_match:
            server_detail.append(slot_match.group(1)+"\n")
            # print "slot is", slot_match.group(1)
        if fw_match:
            server_detail.append(fw_match.group(1))
            # print "firmware version is", fw_match.group(1)
        if prd_match:
            server_detail.append(prd_match.group(1))
            # print "product is", prd_match.group(1)
        else:
            pass
    return server_detail

if __name__ == "__main__":
    get_adapter_detail()






