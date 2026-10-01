#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyPublisherNode(Node):
    def __init__(self):
        super().__init__("python_publisher_oop")
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.i = 0
        self.msg = String()
        self.get_logger().info("Publisher OOP has been started.")

    def timer_callback(self):
        self.msg.data = f"Hello, world: {self.i}"
        self.i += 1
        self.get_logger().info(f"Publishing: '{self.msg.data}'")
        self.publisher_.publish(self.msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyPublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()