from my_first_package_msgs.srv import MultiSpawn
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import Spawn

import rclpy as rp
from rclpy.node import Node

import math
import time

class MultiSpawning(Node):
	def __init__(self):
		super().__init__('multi_spawn')
		self.server = self.create_service(MultiSpawn, 'multi_spawn', self.callback_service)
		self.teleport = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
		self.req_teleport = TeleportAbsolute.Request()

		self.spawn = self.create_client(Spawn, '/spawn')
		self.req_spawn = Spawn.Request()

	def callback_service(self, request, response):
		print('Request : {}'.format(request))

		num = request.num

		response.x = [1., 2., 3.]
		response.y = [10., 20.]
		response.theta = [100., 200., 300.]
		# self.req_teleport.x = 1.
		# self.req_teleport.y = 1.
		# self.teleport.call_async(self.req_teleport)

		# assume r = 10 and center =(5, 5)
		r = 3
		c_x = 5.54
		c_y = 5.54
		theta = [2*math.pi/num * x for x in range(num)]
		x = [r * math.cos(i) for i in theta]
		y = [r * math.sin(i) for i in theta]

		for i in range(num):
			self.req_spawn.x = c_x+x[i]
			self.req_spawn.y = c_y+y[i]
			self.req_spawn.theta = -theta[i]
			self.spawn.call_async(self.req_spawn)
			time.sleep(0.05)

		return response

def main(args=None):
	rp.init(args=args)
	multi_spawn=MultiSpawning()
	rp.spin(multi_spawn)
	rp.shutdown()

if __name__=='__main__':
	main()