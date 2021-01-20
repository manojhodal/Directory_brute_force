#!/usr/bin/env python

# To Doscover Hidden Directories by bruteforcing with a wordlist
# subdomain.txt is the file containing different subdomains
# common.txt is the file containing list of directories to be checked




import requests  
import os
import sys

# Line of code to iterate each subdomain

with open("subdomain.txt", "r") as wordlist_file:
	for url in wordlist_file:
		

# Function to capture response
	
		def request(url):
			try:
				return requests.get("https://" + url)
			except requests.exceptions.ConnectionError:
				pass


# Line of code to iterate each word of common.txt as directory


		with open("word_list.txt","r") as wordlist_file:
			for line in wordlist_file:
				word = line.strip()
				test_url = url.strip() + "/" + word
				print(test_url)
				response = request(test_url)
				if response :
					print "[+] Discovered URL ----> " + test_url




########################## END
