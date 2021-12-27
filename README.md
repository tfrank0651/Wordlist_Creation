# Wordlist Creation
This repo contains various programs that can be used to generate files containing wordlists that may be used by other programs.

# numlist.py
Created for use in CS 5713 - Practical Attack and Defense Techniques. The purpose was to create a wordlist containing all possible permutations of numeric values with length 6-12 digits. I then used this file to break wireless encryption used in the Lab's pcap. I had success with the following programs:
- aircrack-ng
- cowpatty
- john

Numlist.py takes 3 parameters, creates the specified output file containing all possible permutations of the specified lenghts.
1. output file path
2. minimum length of word
3. maximum length of word

# hex_keys.py
Created for use in CS 5323 - Principles of Cybersecurity. Creates a wordlist containing all possible permutations of 64 bit hex values. This program was used to assist in breaking DES encryption.

hex_keys.py takes 1 paramater, generates all permutatiuons and saves in the specified output file.
1. output file path
