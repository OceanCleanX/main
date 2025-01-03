from typing import Annotated

import rclpy
from fastapi import Depends
from rclpy.node import Node

from motor_control_interfaces.msg import MotorCommand
from .executor import get_global_executor


class DataPosterNode(Node):
    def __init__(self):
        super().__init__("data_poster")
        self.motor_command_publisher = self.create_publisher(MotorCommand, "motor_command", 10)


node: DataPosterNode | None = None


async def get_node():
    global node

    if node is None:
        node = DataPosterNode()
        get_global_executor().submit(rclpy.spin, node)

    return node

def cleanup_node():
    global node

    if node is not None:
        node.destroy_node()
        rclpy.shutdown()


NodeDep = Annotated[DataPosterNode, Depends(get_node)]
