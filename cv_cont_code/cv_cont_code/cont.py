#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class ContNode(Node):
    def __init__(self):
        super().__init__("ContNode")
        self.counter_ = 0
        self.publisher = self.create_publisher(Twist, "/cmd_vel", 10)
        self.create_timer(0.5, self.callback_func)

    def callback_func(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 2.0
        self.publisher.publish(msg)
        self.get_logger().info(f"msg pub {self.counter_}")
        self.counter_ += 1


def main(args=None):
    rclpy.init(args=args)
    node = ContNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
