#assign importfile to the name of the text file that you want to create

import_file= "data/login.txt"

#assign ip address to a list of ipa ddreses that are allowed to access the restricted information

ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"

# Create a `with` statement to write to the text file 
with open(import_file, "w") as file:
    file.write(ip_addresses)
#create a  WITH statment to read in the text file 
with open(import_file, "r") as file:
    text = file.read()
print(text)