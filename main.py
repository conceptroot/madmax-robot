from gpiozero import Robot
from time import sleep
robot= Robot(left=(19,26,13), right=(21,20,16))
def scriptik(speed=0.3):
    robot.forward(speed=speed)
    sleep(0.5)
    robot.stop()
    sleep(1)
    robot.backward(speed=speed)
    sleep(0.5)
    robot.stop()
    sleep(3)
    robot.right(speed=speed)
    sleep(0.5)
    robot.stop()
    sleep(1)
    robot.left(speed=speed)
    sleep(0.5)
    robot.stop()
    print("finishing job")

if __name__ == "__main__":
    scriptik()
