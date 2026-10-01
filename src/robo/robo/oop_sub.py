#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MySubscriberNode(Node):

    def __init__(self):
        super().__init__("python_subscriber_oop")

        self.subscriber_ = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10
        )

        self.get_logger().info("Subscriber OOP has been started.")

    def listener_callback(self, msg):
        self.get_logger().info(f"Received: '{msg.data}'")


def main(args=None):
    rclpy.init(args=args)

    node = MySubscriberNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()