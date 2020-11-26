#!/usr/bin/python3

import requests,socket,argparse

def Arg_parse():
    parser = argparse.ArgumentParser(description='Python script for brute force in web directories')
    parser.add_argument("-d", "--domain", help="The domain for brute force (Include HTTP schema)", type=str, required=True)
    parser.add_argument("-w", "--wordlist", help="Wordlist or path to the wordlist", type=str, required=True)
    parser.add_argument("-f", "--filetype", help="select brute force on a specific file type", type=str)
    args = parser.parse_args()
    return args


def declaring_Variables(args):    
    args = Arg_parse()
    global host
    global wordlist
    global filetype
    global file
    filetype = args.filetype
    host = args.domain
    wordlist = args.wordlist
    

def Dns_resolution(host):
    host_replace = host.replace("http://", '')
    print(f" [DNS] {host_replace} ---> {socket.gethostbyname(host_replace)}")

def Brute_force(host, wordlist, filetype):
        try:   
            
            archive = open(wordlist,'r')

            if filetype is not None :
                print(" [+] Starting Bruteforce (FILETYPE) ")
                
                for dir in archive:
                    dir_strip = dir.strip()
                    url_request = (f"{host}/{dir_strip}.{filetype}")
                    req = requests.get(url_request)
                    if req.status_code == 200:
                        print(f' [+] FOUND: {host}/{dir_strip}.{filetype}')
                    else:
                        pass
            
            else:
                print(" [+] Starting Bruteforce ")
                
                for dir in archive:
                    dir_strip = dir.strip()
                    url_request = host + "/" + dir_strip
                    req = requests.get(url_request)

                    if req.status_code == 200:
                        print(' [+] FOUND: ' + host + "/" + dir_strip)
                    elif req.status_code == 403:
                        print(' [+] FOUND (FORBIDDEN): ' + host + "/" + dir_strip)
                    else:
                        pass
        except:
            pass


def main(dns, bruteforce, variables):
    variables(Arg_parse)
    dns(host)
    bruteforce(host, wordlist, filetype)    


if __name__ == "__main__":
    try:
        main(Dns_resolution, Brute_force, declaring_Variables)
    except KeyboardInterrupt:
        pass
