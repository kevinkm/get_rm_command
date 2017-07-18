####Original author: KEVIN.km####
import os
import subprocess as subprocess
import sys
import re

print( 'THE PROGRAM JUST FOR NEWBIEs\n\n' )
(num1, path1) = subprocess.getstatusoutput( 'env|grep ^HOME' )
userpath = path1[5:]
if os.path.exists( userpath + '/.homeassistant/home-assistant.log' ):

    # find the homeassistant successfully
    hasspath = userpath + '/.homeassistant/'
    print( 'Find home-assistant.log successfully!' )

# already stay at the directory of homeassistant
elif os.path.exists( './home-assistant.log' ):
    hasspath = './'
    print( 'Already stay at the directory of home-assistant!' )

# error
else:
    print( 'Program can\'t find home-assistant.log, you should stay at .homeassisant directory and run again' )
    sys.exit( 0 )


#########################  initial OK Program starts, one global var: hasspath  #############################

# Building four global functions: create_script, ini_group, addintogroup, check_group
def check_foxgroup_num():
    fp = open( hasspath+'foxgroup.yaml', 'r' )
    line = fp.readlines()
    a = re.findall( r'(?<=script.fox_controls_).*', line[-1] )
    fp.close()
    if a:
        print( '\nAlready has ' + (
        ''.join( a )) + ' elements in foxgroup.yaml, the new command will begin with the next number ' + str(int( ''.join( a ) ) + 1 ) +'\n')
        return int( ''.join( a ) )+1
    else:
        return 0

# create group funtion
def ini_group():
    f = open( hasspath + 'foxgroup.yaml', 'a' )
    a = 'fox_view:\n  view: true\n  name: ' + group_name + '\n  entities:\n  - group.group_foxswitch\ngroup_foxswitch:\n  view: false\n  name: ' + group_name + '\n  entities:\n'
    f.write( a )
    f.close()

# create switch funtion
def create_script(SWITCH_NUMBER, ip_addr, datas):
    return '  fox_controls_' + str(
        switch_number ) + ' :\n#    alias: ' + 'delete# and give a new name by yourself' + '\n    sequence:\n      - service: broadlink.send_packet_' + ip_addr + '\n        data:\n          packet: #' + 'send a packet' + '\n            - \"' + datas + '"\n'


def addintogroup(switch_number):
    return '  - script.fox_controls_' + str(switch_number) + '\n'


# firstly, prepare for getting user's group name and broadlink IP address

# Enter your group name as a var: group_name
if not os.path.exists( hasspath + 'foxgroup.yaml' ):
    group_name = input(
        "You'll transplant a group of RM/RM2-commands from your E-control to homeassistant \nNow define a group name at homeassistant: " )
    a = 1
    while a:
        if re.match( r"^[\u4E00-\u9FA5A-Za-z0-9_-]+$", group_name ):
            print( '\nCorrect!' )
            a = 0
        else:
            print( '\nhint:Wrong format! You could even try Chinese but no space or incommon symbol!' )
            group_name = input( "\nNow try again: " )
else:
    print ('\nYou may have group name.\n')

# Get broadlink IP as a var: ip_addr

loop0 = '1'
f1_log=open('configuration.yaml' )
while loop0:
    loop0 = f1_log.readline()
    b = re.findall( r'(?<=    host: ).*', loop0 )
    if len( b ) > 0:
        host = ''.join( b )  # CLASS: list to string
        print('\nGet your broadlink ip is: ' + host )
        ip_addr=host
        loop0 = loop0 in 'a'


# a = 1
# while a:
#     ip = input( "\nTell me your ip address about broadlink rm/rm2/rmpro: " )
#     if re.match( r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$", ip ):
#         ip_addr = ip.replace( '.', '_' )
#         a = 0
#         print( '\nCorrect!\n' )
#     else:
#         print(
#             '\nYou are abandoned since you can\'t acquaint yourself with what the IP address looks like, Kidding...try again ' )

# got datas from home-assistant.log as a var: rm_datas
if not os.path.exists( hasspath + 'foxgroup.yaml' ):
    ini_group()
f_group = open( hasspath + 'foxgroup.yaml', 'a' )
f_script = open( hasspath + 'foxscript.yaml', 'a' )
f_log = open( hasspath + 'home-assistant.log', 'r' )

loop1 = '1'
command_count=0
switch_number = check_foxgroup_num()
while loop1:
    loop1 = f_log.readline()
    b = re.findall( r'(?<=Recieved packet is: ).*', loop1 )
    print( b )
    if len( b ) > 0:
        rm_datas = ''.join( b )  # CLASS: list to string
        print( rm_datas )
        # Append switches to group file and # script file
        f_script.write( create_script( switch_number, ip_addr, rm_datas ) )
        f_group.write( addintogroup( switch_number ) )
        switch_number = switch_number + 1
        command_count=command_count+1

f_group.close()
f_script.close()
f_log.close()
print(str(command_count)+ ' commands are done!')

####Original author: KEVIN.km####