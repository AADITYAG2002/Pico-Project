import network
import socket
import time
import network

ssid = 'VISHAL HOME '
password = '9816034485vg'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wifis = wlan.scan()
for wifi in wifis:
    print('=> ', wifi)

wlan.connect(ssid, password)
for _ in range(10):
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0])
    print('subnet mask = ' + status[1])
    print('gateway = ' + status[2])
    print('dns server = ' + status[3])
