from libnmap.parser import NmapParser


def parsenmap(files1):
    fileout_list = []

    for file1 in files1:
        nmap_report = NmapParser.parse_fromfile(file1)

        list443 = []
        list1 = [ a.address for a in nmap_report.hosts if (a.get_open_ports()) and 443 in [b[0] for b in a.get_open_ports()] ]
        for x in list1:
            list443.append(x+":443")

        list8443 = []
        list2 = [ a.address for a in nmap_report.hosts if (a.get_open_ports()) and 8443 in [b[0] for b in a.get_open_ports()] ]
        for x in list2:
            list8443.append(x+":8443")

        mergedlist = list443 + list8443
        mergedlist.sort()
        for host in mergedlist:
            fileout_list.append(host)

    return fileout_list
