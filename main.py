import subprocess
import optparse
import re

'''
subprocess -> kod icerisinde, terminalde (veya command promptta) komut calistirir gibi bilgisayarimiza komut vermeye
yariyor. ornegin ls komutunu acip terminalde calistirir gibi kod icerisinde calistirabiliyorum.

optparse -> terminal icinde kullanicidan input almaya yariyor.

bu ikisini de oldukca fazla kullanacagiz ileriki programlarda da.

scapy.all -> ag icinde paketleri okumamiza, yazmamiza yardimci olan bir kutuphane o da
'''


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="change the mac")

    return parse_object.parse_args()

def change_mac_address(user_interface, user_mac_address):

    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])

def check_mac_address(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig) #string dondermiyor
    print(ifconfig)

    if new_mac:
        return new_mac.group(0)  #yazmamizin sebebi string haline getirmemizdir. 0 ise ilk bu formatta olani aliyor
    else:
        return None

print("MyMacChanger started!")

(user_input, arguments) = get_user_input()
change_mac_address(user_input.interface, user_input.mac_address)
finally_mac = check_mac_address(user_input.interface)

if finally_mac == user_input.mac_address:
    print("Success!")
else:
    print("Error!")
