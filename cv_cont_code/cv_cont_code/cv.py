#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
import cv_bridge


class Subscriber(Node):
    def __init__(self):
        super().__init__("Subscriber")
        self.subscriber = self.create_subscription(Image, "/camera/image_raw", self.pose_callback, 10)  
git 
    def pose_callback(self, msg: Image):
        
        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)

    sub = Subscriber()

    rclpy.spin(sub)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
