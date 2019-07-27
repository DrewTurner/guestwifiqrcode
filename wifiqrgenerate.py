#! python3
import pyqrcode

ssid = "YOURSSID"
security = "WPA|WEP"
password = "WIRELESSPASSCODE"

qr = pyqrcode.create(f'WIFI:S:{ssid};T:{security};P:{password};;')
qr.png('wificode.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
