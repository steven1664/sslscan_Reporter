import datetime
import os
from subprocess import PIPE, run


def sslscanner_hosts(hosts1):
    fileout_list = []
    for host in hosts1:
        print("Performing SSLScan for: " + host)
        sslscan_command = ["sslscan", "--timeout=1", "--no-heartbleed", "--no-cipher-details", "--no-compression", '--no-renegotiation', '--no-fallback', host.rstrip()]
        result = run(sslscan_command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        filetime = datetime.datetime.now().strftime("_%m_%d_%y_%H_%M_%S")
        fileout = os.getcwd() + '/tmpfiles/sslscan' + str(filetime) + '.txt'
        with open(fileout, 'w') as f:
            f.write(result.stdout)
        fileout_list.append(fileout)
    return fileout_list


def sslscanner_files(files1):
    fileout_list = []
    for file1 in files1:
        with open(file1, 'r') as f:
            for host in f.readlines():
                host = host.rstrip().replace('https://','').replace('http://','')
                print("Performing SSLScan for: " + host)
                sslscan_command = ["sslscan", "--timeout=1", "--no-heartbleed", "--no-cipher-details", "--no-compression", '--no-renegotiation', '--no-fallback', host]
                result = run(sslscan_command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
                filetime = datetime.datetime.now().strftime("_%m_%d_%y_%H_%M_%S")
                fileout = os.getcwd() + '/tmpfiles/sslscan' + str(filetime) + '.txt'
                with open(fileout, 'w') as f:
                    f.write(result.stdout)
                fileout_list.append(fileout)
    return fileout_list
