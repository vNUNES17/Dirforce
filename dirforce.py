#!/usr/bin/python3

import requests,socket,argparse,sys

def Dns_resolution(host):
    host_replace = host.replace("http://", '')
    print(f" [DNS] {host_replace} ---> {socket.gethostbyname(host_replace)}")

def Brute_force(host, wordlist):
        try:   
            archive = open(wordlist,'r')
        
            print(" [+] Starting Bruteforce ")
        
            for dir in archive:
                dir_strip = dir.strip()
                url_request = host + "/" + dir_strip + "/"
                req = requests.get(url_request)

                if req.status_code == 200:
                    print(' [+] FOUND: ' + host + "/" + dir_strip + "/")
                elif req.status_code == 403:
                    print(' [+] FOUND (FORBIDDEN): ' + host + "/" + dir_strip + "/")
                else:
                    pass
        except:
            pass
            

def Arg_parse():
    parser = argparse.ArgumentParser(description='Python script for brute force in web directories')
    parser.add_argument("-d", "--domain", help="The domain for brute force (Include HTTP schema)", type=str, required=True)
    parser.add_argument("-w", "--wordlist", help="Wordlist or path to the wordlist", type=str, required=True)
    args = parser.parse_args()
    return args

def main(Dns_resolution, Brute_force, Arg_parse):
    args = Arg_parse()
    host = args.domain
    wordlist = args.wordlist
    Dns_resolution(host)
    Brute_force(host, wordlist)    


if __name__ == "__main__":
    try:
        main(Dns_resolution, Brute_force, Arg_parse)
    except KeyboardInterrupt:
        pass
