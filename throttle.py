#!/usr/bin/env python
# encoding: utf-8
"""
throttle.py

Created by Aaron on 2011-08-23
"""
import transmissionrpc

node_list = []              # List of Transmission clients currently managed by the script.

def main():
    print "\nWelcome to TurtleMode!\n"
    list_nodes()
    while(True):
        choice = raw_input("0-list nodes, 1-add node, 2-del node, 3-manual turtle, 4-turtle OFF all ")
        if choice is '0':
            list_nodes()
        elif choice is '1':
            add_node()
        elif choice is '2':
            del_node()
        elif choice is '3':
            turtle_all()
        elif choice is '4':
            full_speed_all()

def turtle_all():
    """Force all nodes into turtle mode"""
    if len(node_list) is 0:
        print "ERROR: No nodes currently."
    else:
        for node in node_list:
            node.turtle_on

def full_speed_all():
	""""""
	if len(node_list) is 0:
		print "No nodes currently."
	else:
		for node in node_list:
			node.turtle_off

def list_nodes():
    """List the nodes currently managed by the script."""
    i = 0
    if len(node_list) is 0:
        print "No nodes currently."
    else:
        for node in node_list:
            print "%s | %r" % (i, node)
            i+=1

def scan():
    """Scan the priority addresses to see if they're online."""
    pass

def add_node():
    """Add a transmission client address to remotely manage."""
    node_address = raw_input("Address: ")
    portnum = raw_input("Port Number: ")
    username = raw_input("User Name: ")
    password = raw_input("Password: ")
    client = Node(node_address, portnum, username, password)
    node_list.append(client)

def del_node():
    """Remove a transmission node from being managed."""
    list_nodes()        # show user what nodes are currently managed so they can select.
    delete_index = raw_input("Which entry to delete? (use index): ")
    try:
        delete_index = int(delete_index)
    except:
        print 'Please enter a valid integer'
        exit(1)
    del node_list[delete_index]
    print "Node deleted."

class Node:
    """Represents a machine to administer."""
    tc = None
    node_address = ""

    def __init__(self, add, portnum, username, passw):
        """TODO: more consistent naming"""
        Node.tc = transmissionrpc.Client(add, port=portnum, user=username, password=passw)
        #self.tc = transmissionrpc.Client(add, port=portnum, user=username, password=passw)
        Node.node_address = add
        print "Client < %s > added." % add
    
    def __str__(self):
        """Build readable output."""
        return str(Node.node_address)

    def __repr__(self):
        return Node.node_address
    
    def turtle_on():
        """Turn ON the speed-limiting mode."""
        Node.tc.set_session(timeout=None, alt_speed_time_enabled=1)

    def turtle_off():
        """Turn OFF the speed-limiting mode."""
        Node.tc.set_session(timeout=None, alt_speed_enabled=False)

if __name__ == '__main__':
    main()