#Read the file and break it into a dictionary, file should be in format branch, vlan, subnet, netmask
file = open("branchstuffs.txt","r")
pod = {}

router_type = int(raw_input("1.Cisco L3\n2.Brocade L3?\n3.Cisco L2\n4.Brocade L2\n"))
link_type = raw_input("pri or sec?\n")
	
#adding a random comment typicall usless	
if router_type == 1:
    for line in file:
        branch = line.split()
        branch_number = branch[0]
        vlan_id = branch[1]
        subnet = branch[2][:-1]+"1"
        netmask = branch[3]
        pod[branch_number] = vlan_id,subnet,netmask 
        print "vlan %s\n name br%s-%s\n" %(vlan_id,branch_number,link_type)
        print "interface vlan %s\n no shutdown\n ip address %s %s\n ip router ospf 1 area 0.0.0.0 area 0\n" % (vlan_id,subnet,netmask)
	

#Format I need this in for cisco_router
#
#  vlan xxx
#  interface Vlan xxx
#
#  no shutdown
#  ip address xxx.xxx.xxx.xxx xxx.xxx.xxx.xxx
#  ip router ospf 1 area 0.0.0.0


elif router_type == 2:
    for line in file:
        branch = line.split()
        branch_number = branch[0]
        vlan_id = branch[1]
        subnet = branch[2][:-1]+"1"
        netmask = branch[3]
        pod[branch_number] = vlan_id,subnet,netmask 
        print "vlan %s name br%s-%s\n router-interface ve %s\n" %(vlan_id,branch_number,link_type,vlan_id)
        print "interface ve %s\n enable\n ip address %s %s\n" % (vlan_id,subnet,netmask)
	


#Format I need this in for brocade_router
#  vlan xxx name xxx by port
#  router-interface ve xxx
# 
#  interface ve xxx
#  ip address xxx.xxx.xxx.xxx xxx.xxx.xxx.xxx

elif router_type == 3:
    for line in file:
        branch = line.split()
        branch_number = branch[0]
        vlan_id = branch[1]
        subnet = branch[2][:-1]+"1"
        netmask = branch[3]
        pod[branch_number] = vlan_id,subnet,netmask 
        print "vlan %s\n name br%s-%s\n" %(vlan_id,branch_number,link_type)
        
#Format I need this in for cisco_router
#
#  vlan xxx
#  interface Vlan xxx

elif router_type == 4:
    for line in file:
        branch = line.split()
        branch_number = branch[0]
        vlan_id = branch[1]
        subnet = branch[2][:-1]+"1"
        netmask = branch[3]
        pod[branch_number] = vlan_id,subnet,netmask 
        print "vlan %s name br%s-%s\n router-interface ve %s\n" %(vlan_id,branch_number,link_type,vlan_id)
        

#Format I need this in for brocade_router
#  vlan xxx name xxx by port
#  router-interface ve xxx
