# vNUNES17 / Dirforce

### Python script for bruteforce of directories and files in web applications.

- By default, use the python 3 interpreter path, you can change to the python path on your machine. change the field -- "#!/usr/bin/python3"

- #### Easy to use:

  - Clone the repository.
  
  - use "chmod +x" for Permission to run (For Linux users)
  
  - use: ./dirforce -d *domain* -w *wordlist*
  
  - use: -f *filetype* -- If you want to do a brute force on files with defined extensions
  
    - Example: ./dirforce -d http://site.com -w wordlist -f *txt*  
      - OUTPUT: "[+] FOUND: http://site.com/robots.txt"  
  
  - ### IMPORTANT: Always use "http://" before the domain.

