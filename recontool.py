import os,time


domain = input("Domain Input: ")


os.system("subfinder -d {} -o subfinder.txt -v".format(domain))
time.sleep(5)
os.system("assetfinder -subs-only {} > assetfinder.txt".format(domain))
time.sleep(5)
os.system("sublist3r -d {} -o sublist3r.txt".format(domain))
time.sleep(5)
os.system("cat subfinder.txt assetfinder.txt sublist3r.txt | sort -u > subdomains.txt") #get unique values to text file.
time.sleep(5)
os.system("httpx -l subdomains.txt -o activesubdomains.txt -threads 200 -status-code -follow-redirects")
