import socket

def check_network_connection():
    try:
        # Try to resolve Google's domain name using DNS lookup
        socket.gethostbyname('www.google.com')
        return True
    except socket.error:
        pass
    return False

if check_network_connection():
    print('Network connection 3 third party is active.')
else:
    print('Network connection 3 third party is down.')
