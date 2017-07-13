import os
import sys
import regex as re
import subprocess as subprocess

from builtins import range
print ('THE PROGRAM JUST FOR NEWBIEs\n')
(temp1,temp2)= subprocess.getstatusoutput('env|grep ^HOME')
userpath =  temp2[5:]
if os.path.exists( userpath + '/.homeassistant/home-assistant.log' ):

#find the homeassistant successfully
    logfile = open( userpath + '/.homeassistant/home-assistant.log' )
    hasspath = userpath + '/.homeassistant/'
    print( 'Find home-assistant.log successfully!' )

#stay at the directory of homeassistant already
elif os.path.exists( './home-assistant.log' ):
     logfile = open( userpath + '/.homeassistant/home-assistant.log' )
     hasspath = './'
     print( 'Find home-assistant.log successfully!' )

#error
else:
    print ('Program can\'t find homeassistant.log, you should stay at .homeassisant directory and run again')
    sys.exit(0)

#Enter your group name
group_name = input(
        "You'll transplant a group of RM/RM2-commands from your E-control to homeassistant \nNow define a group name at homeassistant: ")
a = 1
while a:
    if re.match(r"^[\u4E00-\u9FA5A-Za-z0-9_-]+$", group_name):
        print ('\nCorrect!')
        a = 0
    else:
        print('\nhint:Wrong format! You could even try Chinese but no space or incommon symbol!')
        group_name = input("\nNow try again: ")

#Enter broadlink IP
a = 1
while a:
    ip = input("\nTell me your ip address about broadlink rm/rm2/rmpro: ")
    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$", ip):
        ip_addr = ip.replace('.', '_')
        print ('\nCorrect!\n')
        a = 0
    else:
        print ('\nYou are abandoned since you can\'t acquaint yourself with what the IP address looks like, Kidding...try again ')

#got datas from home-assistant.log
f_log=open(hasspath+'home-assistant.log','r')

#create group file
f_group=open(hasspath+'foxgroup.yaml','a')

#create script file
f_script=open(hasspath+'foxscript.yaml','a')


#create switch funtion
def create_script(switch_number, ip_addr, datas):
    return '  fox_controls_' + str(
        switch_number) + ' :\n#    alias: ' + 'delete\# and give a new name by yourself' + '\n    sequence:\n      - service: broadlink.send_packet_' + ip_addr + '\n        data:\n          packet: #' + 'send a packet' + '\n            -\"' + datas + '"'

#create group funtion
def ini_group():
    a = 'fox_view:\n  view: true\n  name: '+ group_name+'\n  entities:\n  - group.group_foxswitch'
def addintogroup(switch_number):
    return 'group_foxswitch:\ngroup_tv:\n  view: false\n  name: TV\n  entities:\n  - script.fox_controls_'+str(
        switch_number)





