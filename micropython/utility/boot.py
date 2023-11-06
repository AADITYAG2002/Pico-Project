import time
import network

ssid = 'Galaxy A52s 5G 9E5C'
password = 'alcz6396'

time.sleep(5)

wlan = network.WLAN(network.STA_IF)
wlan.active(False)
wlan.active(True)
wlan.connect(ssid, password)

#wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# HAndle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status= wlan.ifconfig()
    print('ip = ' + status[0])