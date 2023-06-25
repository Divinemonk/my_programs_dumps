#!/usr/bin/env python3

# [brrtp]: Burp Raw Requests To Python
# [dev]  : A Divinemonk creation!
# [desc] : Convert Burp raw requests to python requests
# [usage]: python3 brrtp.py <burp_raw_request_file>


import sys

# Read the file
with open(sys.argv[1], 'r') as f:
    data = f.read() 

# Split the file into headers and body
headers, body = data.split('\n\n')

# Filtering HEADERS
# Split the headers into a list
headers = headers.split('\n')

# Split the first line of the headers into a list
first_line = headers[0].split(' ')

# Get the method, second part of the url and protocol
method = first_line[0]
url = first_line[1]
protocol = first_line[2]

# Remove the first line from the headers
headers.pop(0)

# From the headers, remove the 'Host' header and 
# add its value as first (domain) part  of the url
for header in headers:
    if 'Host' in header:
        url = 'http://' + header.split(': ')[1] + url
        headers.remove(header)
        break

# Remove the first line from the headers
headers.pop(0)

# Create a dictionary of headers
headers_dict = {}
for header in headers:
    header = header.split(': ')
    headers_dict[header[0]] = header[1]

# Filtering BODY
# if body is not in json format, convert it to json
if not body.startswith('{'):
    body = body.replace('\n', '')
    body = body.replace('\r', '')
    body = body.replace(' ', '')
    body = body.replace('=', '":"')
    body = body.replace('&', '","')
    body = '{"' + body + '"}'
    body = body.replace('""', '"')


# Save the python requests code in a variable
python_requests = f"""import requests

url = '{url}'
headers = {headers_dict}
data = {body}
response = requests.request('{method}', url, headers=headers, data=data)
"""

# Print the python requests code
print(python_requests)

# Write the python requests code to a file (same name as the burp raw request file)
with open(sys.argv[1].split('.')[0] + '.py', 'w') as f:
    f.write(python_requests)