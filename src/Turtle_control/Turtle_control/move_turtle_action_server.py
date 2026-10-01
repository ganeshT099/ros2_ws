import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from my_service.action import MoveTurtle
from geometry_msgs.msg import Twist
import time


class MoveTurtleActionServer(Node):

    def __init__(self):
        super().__init__('move_turtle_action_server')

        # Publisher for turtle velocity
        self._publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        # Action server
        self._action_server = ActionServer(
            self,
            MoveTurtle,
            'move_turtle',
            self.execute_callback
        )

        self.get_logger().info(
            'MoveTurtle Action Server is ready.'
        )

    def execute_callback(self, goal_handle):

        self.get_logger().info('Executing goal...')

        goal = goal_handle.request

        duration = goal.duration

        # Check duration
        if duration <= 0.0:

            self.get_logger().error(
                'Duration must be greater than zero.'
            )

            goal_handle.abort()

            result = MoveTurtle.Result()
            result.success = False

            return result

        # Calculate velocity
        x_speed = goal.x / duration
        y_speed = goal.y / duration
        theta_speed = goal.theta / duration

        start_time = (
            self.get_clock().now().nanoseconds / 1e9
        )

        elapsed = 0.0
        distance_moved = 0.0

        # 10 Hz
        rate = 10
        dt = 1.0 / rate

        twist = Twist()

        while elapsed < duration:

            # Set velocity
            twist.linear.x = x_speed
            twist.linear.y = y_speed
            twist.angular.z = theta_speed

            # Publish velocity
            self._publisher.publish(twist)

            # Calculate distance moved
            distance_moved += abs(x_speed) * dt

            # Send continuous feedback
            feedback_msg = MoveTurtle.Feedback()
            feedback_msg.distance_moved = distance_moved

            goal_handle.publish_feedback(feedback_msg)

            # Display feedback
            self.get_logger().info(
                f'Distance moved: {distance_moved:.2f} m'
            )

            # Wait
            time.sleep(dt)

            # Calculate elapsed time
            elapsed = (
                self.get_clock().now().nanoseconds / 1e9
                - start_time
            )

        # Stop turtle
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.angular.z = 0.0

        self._publisher.publish(twist)

        # Final result
        result = MoveTurtle.Result()
        result.success = True

        goal_handle.succeed()

        self.get_logger().info(
            f'Goal completed successfully. '
            f'Total distance: {distance_moved:.2f} m'
        )

        return result


def main(args=None):

    rclpy.init(args=args)

    node = MoveTurtleActionServer()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()