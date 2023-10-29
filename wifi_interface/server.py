import socket

addr = ('192.168.1.4', 80)
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on : ', addr)

led_state = False
bot_response = ""
auth = False

def home():
    global led_state, bot_response

    client, client_addr = s.accept()
    raw_request = client.recv(1024)
    raw_request = raw_request.decode("utf-8")
    print(raw_request)

    request_parts = raw_request.split()
    http_method = request_parts[0]
    request_url = request_parts[1]

    print("url: ", request_url)

    if request_url.find("/led") != -1:
        led_state = not led_state

    elif request_url.find("/user") != -1:
        input_list = request_url.split('=')
        bot_response = input_list[1].replace('+', ' ')

    else:
        pass

    led_state_text = "OFF"
    if led_state:
        led_state_text = "ON"


    with open("home.html") as file:
        html = file.read()
    

    html = html.replace('**ledState**', led_state_text)
    html = html.replace('**reply**', bot_response)
    client.send(html.encode('utf-8'))
    client.close()

def login():
    global auth

    username, password = "", ""
    client, client_addr = s.accept()
    raw_request = client.recv(1024)
    raw_request = raw_request.decode("utf-8")
    print(raw_request)

    request_parts = raw_request.split()
    http_method = request_parts[0]
    request_url = request_parts[1]

    print("url: ", request_url)

    if request_url.find("/login") != -1:
        cred = request_url[7:].split('&')
        print(cred)
        username, password = cred[0][6:], cred[1][6:]

    print(username, password)

    if username == "admin" and password == "admin":
        auth = True
        client.close()
        return

    with open("login.html") as file:
        html = file.read()
    
    client.send(html.encode('utf-8'))
    client.close()

def main():
    while True:
        if auth:
            home()
        else:
            login()

if __name__ == '__main__':
    main()