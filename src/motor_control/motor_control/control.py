import abc
import logging

logger = logging.getLogger(__name__)


class Control(abc.ABC):
    @staticmethod
    def set(direction: float, speed: float):
        """
        control the motor speed by converting direction and speed to PWM wave of two motor
        :param direction: [-1, 1], negative is left
        :param speed: [-1, 1], negative is reverse
        """
        if abs(direction) > 1 or abs(speed) > 1:
            logger.warning(f"Invalid speed or direction: {speed}, {direction}")
            return

        logger.info(f"speed: {speed}, direction: {direction}")
