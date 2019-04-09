import socket
import sys

TCP_PORT = 7777
BUFFER_SIZE = 1024
HOST_NAME = 'palindromer-bd7e0fc867d57915.elb.us-east-1.amazonaws.com'

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket created"
except socket.error as err:
    print "socket creation failed with error %s" %(err)

try:
    HOST_IP = socket.gethostbyname(HOST_NAME)
except socket.gaierror:
    print "Error resolving host"
    sys.exit()

s.connect((HOST_IP, TCP_PORT))

data = s.recv(BUFFER_SIZE)
send_back = ""
solution = ""
is_solution = False
while data:
    for word in data.split():
        if is_solution:
           solution += word
        if word == '!!!':
           is_solution = True
        l = 0
        r = len(word) - 1
        palindrome = ""
        while l <= r:
            if word[l] != word[r]:
                palindrome = False
                break
            l, r = l + 1, r - 1
        if palindrome != False:
            send_back += word + ' '
    s.send(send_back[:-1] + '\n')
    send_back = ""
    data = s.recv(BUFFER_SIZE)
s.close()
print(solution)
