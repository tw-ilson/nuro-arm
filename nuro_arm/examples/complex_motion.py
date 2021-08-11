import time
import numpy as np
import matplotlib.pyplot as plt
import pybullet as pb

from nuro_arm.robot.robot_arm import RobotArm
from nuro_arm.robot.xarm_controller import itos
##################################
# generate circular path to follow
##################################
N = 100
R = 0.06
center = np.array((0.19, 0, 0.008))
angles = np.linspace(0, 2*np.pi, num=N, endpoint=True)
waypts = np.zeros((N, 3)) + center
waypts[:,0] += R * np.cos(angles)
waypts[:,1] += R * np.sin(angles)

###########################
# simulator to calculate ik
###########################
robot = RobotArm('sim', headless=False, realtime=False)
client = robot.mp.get_client()
yaw, pitch, _, target = pb.getDebugVisualizerCamera()[-4:]
pb.resetDebugVisualizerCamera(0.75, yaw, pitch, target)

arm_jposs = []
robot.move_hand_to(waypts[0])
for i in range(len(waypts)):
    pb.addUserDebugLine(waypts[i-1], waypts[i],
                        [0.8,0.3,0.2],
                        physicsClientId=client)
    arm_jpos, _ = robot.mp.calculate_ik(waypts[i])
    arm_jposs.append(arm_jpos)
    robot.move_arm_jpos(arm_jpos)

pb.disconnect(client)

##############################
# follow arm_jposs on real arm
##############################
robot = RobotArm('real')

robot.move_arm_jpos(arm_jposs[0])
joint_ids = robot.controller.arm_joint_ids
for arm_jpos in arm_jposs:
    robot.controller.move_servos(joint_ids, arm_jpos, duration=15)
    time.sleep(0.015)

time.sleep(2)
