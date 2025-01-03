import logging

from fastapi import APIRouter, WebSocket

from data_poster.lib.node import NodeDep
from pydantic import BaseModel, ValidationError

from motor_control_interfaces.msg import MotorCommand


logger = logging.getLogger(__name__)
router = APIRouter()


class MotorCommandModel(BaseModel):
    direction: float
    speed: float


@router.websocket("/motor_command")
async def motor_command(ws: WebSocket, node: NodeDep):
    await ws.accept()
    logger.info("Connection to motor command websocket established")

    while True:
        data = await ws.receive_json()
        try:
            command = MotorCommandModel.parse_obj(data)
        except ValidationError as e:
            await ws.send_json({"status": "error", "message": str(e)})
            logger.error("Failed to validate motor command: %s", e)
            continue

        msg = MotorCommand()
        msg.direction = command.direction
        msg.speed = command.speed

        node.motor_command_publisher.publish(msg)

        await ws.send_json({"status": "ok"})
