from modules import *
import argparse
import sys


def createreport(scanoutput):
    if args.nocertinfo:
        if args.outfile:
            createreport = wordOutput_nocert.create_document(scanoutput, args.outfile)
            print("Report Created: " + createreport)
        else:
            createreport = wordOutput_nocert.create_document(scanoutput)
            print("Report Created: " + createreport)
    else:
        if args.outfile:
            createreport = wordOutput.create_document(scanoutput, args.outfile)
            print("Report Created: " + createreport)
        else:
            createreport = wordOutput.create_document(scanoutput)
            print("Report Created: " + createreport)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Provide a file with a list of IPs or hosts to scan", nargs="+")
    parser.add_argument("-i", "--hosts", help="Provide a a list of IPs or hosts to scan", nargs="+")
    parser.add_argument("-o", "--outfile", help="Provide name for the created scan output file")
    parser.add_argument("-n", "--nocertinfo", help="Do not include Certificate Information column in report output", action='store_true')
    parser.add_argument("-x", "--xml", help="Provide an Nmap XML scan to parse and scan", nargs="+")
    parser.add_argument("-r", "--review", help="Provide a file or files with sslscan output to review", nargs="+")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    if args.file:
        sslout = sslscanner.sslscanner_files(args.file)
        scanoutput = sslscanOutput.getfile_scaninfo(sslout)
        createreport(scanoutput)

    if args.hosts:
        sslout = sslscanner.sslscanner_hosts(args.hosts)
        scanoutput = sslscanOutput.getfile_scaninfo(sslout)
        createreport(scanoutput)

    if args.xml:
        nmapout = nmapParser.parsenmap(args.xml)
        sslout = sslscanner.sslscanner_hosts(nmapout)
        scanoutput = sslscanOutput.getfile_scaninfo(sslout)
        createreport(scanoutput)

    if args.review:
        scanoutput = sslscanOutput.getfile_scaninfo(args.review)
        createreport(scanoutput)
