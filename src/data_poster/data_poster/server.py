import logging

import rclpy
import uvicorn
from fastapi import FastAPI

from .lifespan import lifespan
from .router import motor_command


app = FastAPI(lifespan=lifespan)
app.include_router(motor_command.router)


def main(args=None):
    rclpy.init(args=args)
    uvicorn.run(app)  # TODO: custom logger


if __name__ == "__main__":
    main()
