# sslscan_Reporter
Create Word Output for SSLScans

#Example scans 


#Perform a scan for a specific host

  python3 sslscan_Reporter.py -i www.badssl.com 

#Perform a scan based on hosts listed in a file, no cert info is displayed with an outfile specified

  python3 sslscan_Reporter.py -f hosts.txt -n -o ./fileScan_nocertinfo.docx

#Perform a scan based on nmap XML output in two different files with an outfile specified

  python3 sslscan_Reporter.py -x nmapscan1.xml nmapscan2.xml -o ./nmapScan_Output.docx
