import motor
from settings import settings

connection = motor.MotorClient(settings['mongo.host'], settings['mongo.port'])
