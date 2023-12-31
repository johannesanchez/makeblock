# Case 1 - Basic Obstale Avoidance
import mbuild, mbot2, event, time, cyberpi

@event.start
def on_start():
    while True:
        if mbuild.ultrasonic2.get(1) < 25:
            mbot2.turn(-90)
        else:
            mbot2.forward(30)
        time.sleep(0.1)