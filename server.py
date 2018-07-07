import zmq
import json
flag=1

context=zmq.Context()
socket_rep=context.socket(zmq.REP)
socket_rep.bind("tcp://127.0.0.1:5678")
socket_pub=context.socket(zmq.PUB)
socket_pub.bind("tcp://127.0.0.1:5679")

def drones_respond():
	while True:
		global flag
		if flag==1:
			message=socket_rep.recv()
			socket_rep.send_string(json.dumps({
				'name':'drone1',
				'cordinates':'0,0,0'
				}))
			print("<---drone 1 just registered--->")
			flag=flag+1

		if flag==2:
			message=socket_rep.recv()
			socket_rep.send_string(json.dumps({
				'name':'drone2',
				'cordinates':'0,0,10'
				}))
			print("<---drone 2 just registered--->")
			flag=flag+1

		if flag>2:
			newCordinates=input("[cordinates]>")
			x,y,z=newCordinates.split(",")
			socket_pub.send_string(json.dumps({
				'name':'drone1',
				'cordinates':x+","+y+","+z
				}))
			z=str(int(z)+10)
			socket_pub.send_string(json.dumps({
				'name':'drone2',
				'cordinates':x+","+y+","+z
				}))





if __name__ == '__main__':
	print("server started at 5678 and is ready to serve the drones")
	drones_respond()