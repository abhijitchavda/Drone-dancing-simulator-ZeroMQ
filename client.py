import zmq
import json

context=zmq.Context()
socket_req=context.socket(zmq.REQ)
socket_req.connect("tcp://127.0.0.1:5678")
socket_sub=context.socket(zmq.SUB)
socket_sub.setsockopt_string(zmq.SUBSCRIBE,"")
socket_sub.connect("tcp://127.0.0.1:5679")

nam=""

def get_cordinates():
	global nam
	while(True):
		message=json.loads(socket_sub.recv())
		if message['name']==nam:
			print("[cordinates]:"+message['cordinates'])			

if __name__=='__main__':
	socket_req.send_string("I want to connect")
	message=json.loads(socket_req.recv())
	if message['name']=='drone1':
		nam="drone1"
		print("You are registered with server as drone1\n")
		print("[cordinates]:"+message['cordinates'])
	elif message['name']=='drone2':
		nam="drone2"
		print("You are registered with server as drone2\n")
		print("[cordinates]:"+message['cordinates'])
	get_cordinates()