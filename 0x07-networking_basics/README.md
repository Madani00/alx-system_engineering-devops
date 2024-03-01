# task 0
### What is the OSI model?
* 1.Set of specifications that network hardware manufacturers must respect
* 2.The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
* 3.The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology
### How is the OSI model organized?
* 1.Alphabetically
* 2.From the lowest to the highest level
* 3.Randomly

# task 1
### What type of network a computer in local is connected to?

* 1.Internet
* 2.WAN
* 3.LAN
### What type of network could connect an office in one building to another office in a building a few streets away?

* 1.Internet
* 2.WAN
3 3.LAN
### What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?

* 1.Internet
* 2.WAN
* 3.LAN

# task 2
### What is a MAC address?

* 1.The name of a network interface
* 2.The unique identifier of a network interface
* 3.A network interface
### What is an IP address?

* 1.Is to devices connected to a network what postal address is to houses
* 2.The unique identifier of a network interface
* 3.Is a number that network devices use to connect to networks



# task 3
### Which statement is correct for the TCP box:
* 1.It is a protocol that is transferring data in a slow way but surely
* 2.It is a protocol that is transferring data in a fast way and might loss data along in the process
### Which statement is correct for the UDP box:
* 1.It is a protocol that is transferring data in a slow way but surely
* 2.It is a protocol that is transferring data in a fast way and might loss data along in the process
### Which statement is correct for the TCP worker:
* 1.Have you received boxes x, y, z?
* 2.May I increase the rate at which I am sending you boxes?

# task 4
Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.

If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.

While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:

22 for SSH
80 for HTTP
443 for HTTPS
Note that a specific IP + port = socket.

Write a Bash script that displays listening ports:

That only shows listening sockets
That shows the PID and name of the program to which each socket belongs
```yaml
Example:

sylvain@ubuntu$ sudo ./4-TCP_and_UDP_ports
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 *:sunrpc                *:*                     LISTEN      518/rpcbind
tcp        0      0 *:ssh                   *:*                     LISTEN      1240/sshd
tcp        0      0 *:32938                 *:*                     LISTEN      547/rpc.statd
tcp6       0      0 [::]:sunrpc             [::]:*                  LISTEN      518/rpcbind
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      1240/sshd
tcp6       0      0 [::]:33737              [::]:*                  LISTEN      547/rpc.statd
udp        0      0 *:sunrpc                *:*                                 518/rpcbind
udp        0      0 *:691                   *:*                                 518/rpcbind
udp        0      0 localhost:723           *:*                                 547/rpc.statd
udp        0      0 *:60129                 *:*                                 547/rpc.statd
udp        0      0 *:3845                  *:*                                 562/dhclient
udp        0      0 *:bootpc                *:*                                 562/dhclient
udp6       0      0 [::]:47444              [::]:*                              547/rpc.statd
udp6       0      0 [::]:sunrpc             [::]:*                              518/rpcbind
udp6       0      0 [::]:50038              [::]:*                              562/dhclient
udp6       0      0 [::]:691                [::]:*                              518/rpcbind
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
unix  2      [ ACC ]     STREAM     LISTENING     7724     518/rpcbind         /run/rpcbind.sock
unix  2      [ ACC ]     STREAM     LISTENING     6525     1/init              @/com/ubuntu/upstart
unix  2      [ ACC ]     STREAM     LISTENING     8559     835/dbus-daemon     /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     9190     1087/acpid          /var/run/acpid.socket
unix  2      [ ACC ]     SEQPACKET  LISTENING     7156     378/systemd-udevd   /run/udev/control
sylvain@ubuntu$
```
# task 5


