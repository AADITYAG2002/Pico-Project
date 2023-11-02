import socket

led_state = False
bot_response = ""
auth = False

def web_server():
    global auth, led_state, bot_response

    addr =  socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('listening on : ', addr)

    while True:
        client, client_addr = s.accept()
        raw_request = client.recv(1024)
        raw_request = raw_request.decode("utf-8")
        # print(raw_request)

        request_parts = raw_request.split()
        http_method = request_parts[0]
        request_url = request_parts[1]

        print("url: ", request_url)
        
        if request_url.find("/led") != -1:
            led_state = not led_state

        elif request_url.find("/user") != -1:
            input_list = request_url.split('=')
            bot_response = input_list[1].replace('+', ' ')

        elif request_url.find("/login") != -1 :
            cred = request_url[7:].split('&')
            # print(cred)
            username, password = cred[0][6:], cred[1][6:]
        
            if username == "admin" and password == "admin":
                auth = True

        else:
            pass


        led_state_text = "OFF"
        if led_state:
            led_state_text = "ON"

        if auth:
            with open("home.html") as file:
                html = file.read()
                html = html.replace('**ledState**', led_state_text)
                html = html.replace('**reply**', bot_response)
        
        else:
            with open("login.html") as file:
                html = file.read()

        client.send(html.encode('utf-8'))
        client.close()


def main():
    web_server()
    
if __name__ == '__main__':
    main()