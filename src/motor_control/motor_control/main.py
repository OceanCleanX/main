import logging

import rclpy
from rclpy.node import Node

from motor_control_interfaces.msg import MotorCommand
from .control import Control
from .motor import MotorControl

logger = logging.getLogger(__name__)


class MotorControlNode(Node):
    def __init__(self):
        super().__init__("motor_control")
        try:
            self.motor_control = MotorControl()
        except FileNotFoundError as e:
            logger.warning(f"Could not find motor control device: \"{e}\", using dummy control")
            self.motor_control = Control()

        self.subscription = self.create_subscription(
            MotorCommand, "motor_command", self.motor_command_callback, 10
        )

    def motor_command_callback(self, msg: MotorCommand):
        self.motor_control.set(msg.direction, msg.speed)


def main(args=None) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s (%(name)s:%(lineno)s) [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    rclpy.init(args=args)
    motor_control_node = MotorControlNode()
    rclpy.spin(motor_control_node)
    motor_control_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
