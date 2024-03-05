#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class Publisher(Node):
    def __init__(self):
        super().__init__("Publisher")
        self.cmd_vel_pub = self.create_publisher(Twist, "/cmd_vel", 10)
        """
        the creates a publisher with a Twist msg to the turle1/cmd_vel topic with a buffer of 10 msgs
        """
        self.timer = self.create_timer(0.5, self.send_vel_cmd)
        """
        the create_timer calls the callback function, send_vel_cmd after 0.5 seconds
        """

    def send_vel_cmd(self):
        msg = Twist()
        #creates a msg instance
        msg.linear.x = 4.0
        msg.angular.z = 2.0
        #sets the value of a message instance
        
        self.cmd_vel_pub.publish(msg)
        #publishes the msg instance
        
        self.get_logger().info("Publisher")
        #logs the msg to the console

         


def main(args = None):

    rclpy.init(args = args)

    node = Publisher()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()