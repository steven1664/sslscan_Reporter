# sslscan_Reporter
**Create Word Output for SSLScans**

# Usage

**Perform a scan for a specific host and port**

  ```python3 sslscan_Reporter.py -i 192.168.1.100:443```

**Perform a scan based on hosts listed in a file, no cert info is displayed with an outfile specified**

```python3 sslscan_Reporter.py -f hosts.txt -n -o ./fileScan_nocertinfo.docx```

**Perform a scan based on nmap gnmap output**

```python3 sslscan_Reporter.py -g nmapscan.gnmap -o ./nmapScan_Output.docx```
