import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from my_service.action import MoveTurtle


class MoveTurtleActionClient(Node):

    def __init__(self):
        super().__init__('move_turtle_action_client')
        self._client = ActionClient(self, MoveTurtle, 'move_turtle')

    def send_goal(self, x, y, theta, duration):
        goal_msg = MoveTurtle.Goal()
        goal_msg.x = x
        goal_msg.y = y
        goal_msg.theta = theta
        goal_msg.duration = duration

        self._client.wait_for_server()
        self._client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(
            f"Distance moved: {feedback_msg.feedback.distance_moved:.2f}"
        )


def main(args=None):
    rclpy.init(args=args)

    client = MoveTurtleActionClient()
    client.send_goal(2.0, 0.0, 0.0, 3.0)

    rclpy.spin(client)
    rclpy.shutdown()


if __name__ == '__main__':
    main()