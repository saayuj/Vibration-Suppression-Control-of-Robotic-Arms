import sys
import zmq

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
    
if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect ("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)


topicfilter = "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

# process 100 updates
total_value = 0
for update_nbr in range (100):
    string = socket.recv()
    topic, messagedata = string.split()
    total_value += int(messagedata)
    print (topic, messagedata)
