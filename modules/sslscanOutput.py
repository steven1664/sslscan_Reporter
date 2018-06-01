import re


def host_output(file_read):
    htest1 = re.compile(r"Testing SSL server.*?on port.*", re.I).findall(file_read)
    htest2 = ''.join(htest1)
    host_out = htest2.replace('Testing SSL server ', '').replace(" on", '').replace('port', '\nPort').replace('\x1b[32m', '').replace('\x1b[0m', '')
    host_out = re.sub(" using SNI name.*", '', host_out)
    return host_out


def cipher_output(file_read):
    test1 = re.compile(r"Supported.Server.Cipher.*?SSL Certificate", re.S).findall(file_read)
    test2 = ''.join(test1)
    if test2 and not test2.isspace():
        test3 = test2.split('\n')
        del test3[0]
        del test3[-1]
        del test3[-1]
        list1 = []
        for x in test3:
            y = x.replace("Preferred", "•").replace("Accepted", "•")
            y = re.sub("\x1b\[\d*m", "", y)
            y = re.sub("(•\s\s)|(•\s)", "•", y)
            list1.append(y)
        del list1[-1]
        new1 = '\n'.join(list1)
        cipher_out = re.sub("\s\s\s\s\s*?\n", "\n", new1)
        cipher_out = re.sub("\s\s\s\s*?", " ", cipher_out)
        cipher_out = re.sub("\s\s\s*?", " ", cipher_out)
        cipher_out = re.sub("\s\s*?", " ", cipher_out)
        return cipher_out
    else:
        return test2


def cert_output(file_read):
    testcert1 = re.compile(r"SSL Certificate:.*", re.S).findall(file_read)
    testcert2 = ''.join(testcert1)
    testcert2 = re.sub("\x1b\[\d*m", "", testcert2)
    if testcert2 and not testcert2.isspace():
        testcert3 = testcert2.split('\n')
        del testcert3[0]
        del testcert3[-1]
        cert1 = testcert3[3].replace('  ', ' ').replace("Subject:", "•Subject:")
        if "Altnames" in testcert3[4]:
            cert2 = testcert3[5].replace('   ', ' ').replace('Issuer:', "•Issuer:")
        else:
            cert2 = testcert3[4].replace('   ', ' ').replace('Issuer:', "•Issuer:")
        cert3 = testcert3[0].replace("Signature Algorithm:", "•Signature Algorithm:")
        cert4 = testcert3[1].replace('    ', ' ').replace('RSA Key Strength:', "•Key Strength:")
        cert5 = testcert3[-1].replace('Not valid after:', "•Expiration:").replace('  ', ' ')
        return cert1 + "\n" + cert2 + "\n" + cert3 + "\n" + cert4 + "\n" + cert5
    else:
        return testcert2


def getfile_scaninfo(host_files):
    getoutput = {}
    counter = 1
    for file1 in host_files:
        with open(file1, 'r') as f:
            file_read = f.read()
            getoutput["host" + str(counter)] = host_output(file_read)
            getoutput["ciphers" + str(counter)] = cipher_output(file_read)
            getoutput["cert" + str(counter)] = cert_output(file_read)
            counter += 1
    return getoutput
