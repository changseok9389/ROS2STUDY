import rclpy as rp
from rclpy.action import ActionServer
from rclpy.node import Node

from my_first_package_msgs.action import DistTurtle
import time


class DistTurtleServer(Node):

	def __init__(self):
		super().__init__('dist_turtle_action_server')
		self._action_server = ActionServer(
			self, 
			DistTurtle, 
			'dist_turtle', 
			self.execute_callback)

	def execute_callback(self, goal_handle):
		

		feedback_message = DistTurtle.Feedback()
		for n in range(10):
			feedback_message.remained_dist = float(n)
			goal_handle.publish_feedback(feedback_message)
			time.sleep(0.5)

		goal_handle.succeed()
		result = DistTurtle.Result()
		return result


def main(args=None):
	rp.init(args = args)
	dist_turtle_action_server = DistTurtleServer()
	rp.spin(dist_turtle_action_server)


if __name__ == '__main__':
	main()