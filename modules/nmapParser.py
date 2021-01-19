def parsenmap(files1):
    fileout_list = []
    for file1 in files1:
        with open(file1, 'r') as f:
            for line in f:
                if 'Ports: ' in line:
                    host = line.split()[1]
                    data = line.split('Ports: ')[1]
                    ports = data.split(', ')
                    for x in ports:
                        if 'https' in x or 'ssl' in x:
                            port = x.split('/')[0]
                            fileout_list.append(host + ':' + port)
    return fileout_list
