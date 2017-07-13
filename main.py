import os
import regex as re
import subprocess as subprocess

from builtins import range

(temp1,temp2)= subprocess.getstatusoutput('env|grep ^HOME')
userpath =  temp2[5:]
if os.path.exists( userpath + '/.homeassistant/home-assistant.log' ):
    logfile = open( userpath + '/.homeassistant/home-assistant.log' )
    print( 'Find home-assistant.log successfully!' )
elif os.path.exists( './home-assistant.log' ):
     logfile = open( userpath + '/.homeassistant/home-assistant.log' )
     print( 'Find home-assistant.log successfully!' )
else:
    print ('I can\'t find homeassistant.log, you should go to homeassisant directory ')


#Enter your group name
group_name = input(
        "You'll transplant a group of RM/RM2-commands from your E-control to homeassistant \nNow define a group name at homeassistant: ")
a = 1
while a:
    if re.match(r"^[\u4E00-\u9FA5A-Za-z0-9_-]+$", group_name):
        a = 0
        print ('Correct!')
    else:
        print('\nhint:Wrong format! You could even try Chinese but no space or incommon symbol!\n')
        group_name = input("Now try again: ")

#Enter broadlink IP
ip = input("Tell me your ip address about broadlink rm/rm2/rmpro: ")
if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$", ip):
    ip_addr = ip.replace('.', '_')
    print ('Correct!')
else:
    print ('\nYou are abandoned since you ca\'t acquaint yourself with what the IP address looks like, farewell!')

#create switch funtion
def create_switch(switch_number, ip_addr, datas):
    return '  fox_controls_' + str(
        switch_number) + ' :\n#    alias: ' + 'delete\# and give a new name by yourself' + '\n    sequence:\n      - service: broadlink.send_packet_' + ip_addr + '\n        data:\n          packet: #' + 'send a packet' + '\n            -\"' + datas + '"'

#create group funtion
def ini_group():
    a = 'fox_view:\n  view: true\n  name: '+ group_name+'\n  entities:\n  - group.group_foxswitch'
def addintogroup(switch_number):
    return 'group_foxswitch:\ngroup_tv:\n  view: false\n  name: TV\n  entities:\n  - script.fox_controls_'+str(
        switch_number)





