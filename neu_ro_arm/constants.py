import numpy as np
import cv2

# all positional units are in meters, since this is the unit in the urdf

tvec_world2rightfoot = np.array((0.0635, 0.091, 0.0))

calibration_gridsize = 0.020
calibration_gridshape = (7,9)

aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
aruco_params = cv2.aruco.DetectorParameters_create()

# this is the measure of the black square that contains the pattern
tag_size = 0.0188976

cube_size = 0.0254
cube_vertices = 0.5 * cube_size * np.array((( 1, 1, 1),
                                            ( 1,-1, 1),
                                            ( 1, 1,-1),
                                            ( 1,-1,-1),
                                            (-1, 1, 1),
                                            (-1,-1, 1),
                                            (-1, 1,-1),
                                            (-1,-1,-1)),
                                           dtype=np.float32)
cube_edges = ((0,1),(0,2),(0,4),(1,3),(1,5),(2,3),
              (2,6),(3,7),(4,5),(4,6),(5,7),(6,7))


# used to place camera in simulator if not using real camera
default_cam_pose_mtx = np.array([
    [ 8.71709181e-01, -3.97821192e-01,  2.86114320e-01, -9.75743393e-02],
    [-4.90013665e-01, -7.03961344e-01,  5.14125504e-01, -3.05716144e-02],
    [-3.1169991e-03, -5.88367848e-01, -8.08587387e-01, 2.56509223e-01],
    [0., 0., 0., 1.0]
])

frame_rate = 20

##############################################
# common gripper states
##############################################
GRIPPER_CLOSED = 0
GRIPPER_OPENED = 1

##############################################
# useful pitch-roll tuples for RobotArm.move_hand_to
##############################################
TOP_DOWN_GRASP = np.array((-np.pi, 0.,))
STANDARD_GRASP = np.array((-2.6, 0.))
HORIZONTAL_GRASP = np.array((-np.pi/2, 0.))
