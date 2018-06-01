# sslscan_Reporter
Create Word Output for SSLScans

#Example scans 


#Perform a scan for a specific host
python3 sslscan_Reporter.py -i www.badssl.com 

#Perform a scan based on hosts listed in a file, no cert info is displayed with an outfile specified
python3 sslscan_Reporter.py -f hosts.txt -n -o ./fileScan_nocertinfo.docx

#Perform a scan based on nmap XML output in two different files with an outfile specified
python3 sslscan_Reporter.py -x nmapscan1.xml nmapscan2.xml -o ./nmapScan_Output.docx


#Help for usage

usage: sslscan_Reporter.py [-h] [-f FILE [FILE ...]] [-i HOSTS [HOSTS ...]]
                           [-o OUTFILE] [-n] [-x XML [XML ...]]
                           [-r REVIEW [REVIEW ...]]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE [FILE ...], --file FILE [FILE ...]
                        Provide a file with a list of IPs or hosts to scan
  -i HOSTS [HOSTS ...], --hosts HOSTS [HOSTS ...]
                        Provide a a list of IPs or hosts to scan
  -o OUTFILE, --outfile OUTFILE
                        Provide name for the created scan output file
  -n, --nocertinfo      Do not include Certificate Information column in
                        report output
  -x XML [XML ...], --xml XML [XML ...]
                        Provide an Nmap XML scan to parse and scan
  -r REVIEW [REVIEW ...], --review REVIEW [REVIEW ...]
                        Provide a file or files with sslscan output to review
