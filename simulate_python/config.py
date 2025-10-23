ROBOT = "go2" # Robot name, "go2", "b2", "b2w", "h1", "go2w", "g1" 
import os
ROBOT_SCENE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "unitree_robots", ROBOT, "scene.xml") # Robot scene
DOMAIN_ID = 0 # Domain id
INTERFACE = "lo" # Interface 

USE_JOYSTICK = 1 # Simulate Unitree WirelessController using a gamepad
JOYSTICK_TYPE = "xbox" # support "xbox" and "switch" gamepad layout
JOYSTICK_DEVICE = 0 # Joystick number

PRINT_SCENE_INFORMATION = True # Print link, joint and sensors information of robot
ENABLE_ELASTIC_BAND = False # Virtual spring band, used for lifting h1

SIMULATE_DT = 0.005  # Need to be larger than the runtime of viewer.sync()
VIEWER_DT = 0.02  # 50 fps for viewer
