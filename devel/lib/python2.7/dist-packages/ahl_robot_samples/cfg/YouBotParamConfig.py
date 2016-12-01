## *********************************************************
## 
## File autogenerated for the ahl_robot_samples package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 235, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/jade/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [{'upper': 'YOUBOT_PARAM', 'lower': 'youbot_param', 'srcline': 109, 'name': 'youbot_param', 'parent': 0, 'srcfile': '/opt/ros/jade/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::YOUBOT_PARAM', 'field': 'DEFAULT::youbot_param', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 9, 'description': 'Show reference position', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'show_target', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 10, 'description': 'desired x sin wave', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'sin_x', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 11, 'description': 'desired y sin wave', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'sin_y', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 12, 'description': 'desired z sin wave', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'sin_z', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 14, 'description': 'desired x for gripper', 'max': 3.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'x_arm', 'edit_method': '', 'default': 0.5, 'level': 0, 'min': -3.0, 'type': 'double'}, {'srcline': 15, 'description': 'desired y for gripper', 'max': 3.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'y_arm', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -3.0, 'type': 'double'}, {'srcline': 16, 'description': 'desired z for gripper', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'z_arm', 'edit_method': '', 'default': 0.07, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 18, 'description': 'desired roll  for gripper', 'max': 3.14, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'roll_arm', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -3.14, 'type': 'double'}, {'srcline': 19, 'description': 'desired pitch for gripper', 'max': 3.14, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'pitch_arm', 'edit_method': '', 'default': 3.14, 'level': 0, 'min': -3.14, 'type': 'double'}, {'srcline': 20, 'description': 'desired yaw   for gripper', 'max': 3.14, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'yaw_arm', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -3.14, 'type': 'double'}, {'srcline': 22, 'description': 'desired x for base', 'max': 3.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'x_base', 'edit_method': '', 'default': 0.4, 'level': 0, 'min': -3.0, 'type': 'double'}, {'srcline': 23, 'description': 'desired y for base', 'max': 3.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'y_base', 'edit_method': '', 'default': 0.2, 'level': 0, 'min': -3.0, 'type': 'double'}, {'srcline': 24, 'description': 'desired z for base', 'max': 3.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'z_base', 'edit_method': '', 'default': 0.4, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 26, 'description': 'desired roll  for base', 'max': 3.14, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'roll_base', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -3.14, 'type': 'double'}, {'srcline': 27, 'description': 'desired pitch for base', 'max': 3.14, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'pitch_base', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -3.14, 'type': 'double'}, {'srcline': 28, 'description': 'desired yaw   for base', 'max': 3.14, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'yaw_base', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -3.14, 'type': 'double'}, {'srcline': 30, 'description': 'displacement of base along x axis', 'max': 3.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'q_base1', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -3.0, 'type': 'double'}, {'srcline': 31, 'description': 'displacement of base along y axis', 'max': 3.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'q_base2', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -3.0, 'type': 'double'}, {'srcline': 32, 'description': 'orientation of base', 'max': 3.14, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'q_base3', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -3.14, 'type': 'double'}, {'srcline': 33, 'description': 'angle of arm joint1', 'max': 3.14, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'q1', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -3.14, 'type': 'double'}, {'srcline': 34, 'description': 'angle of arm joint2', 'max': 3.14, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'q2', 'edit_method': '', 'default': 0.5, 'level': 0, 'min': -3.14, 'type': 'double'}, {'srcline': 35, 'description': 'angle of arm joint3', 'max': 3.14, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'q3', 'edit_method': '', 'default': 0.5, 'level': 0, 'min': -3.14, 'type': 'double'}, {'srcline': 36, 'description': 'angle of arm joint4', 'max': 3.14, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'q4', 'edit_method': '', 'default': 0.5, 'level': 0, 'min': -3.14, 'type': 'double'}, {'srcline': 37, 'description': 'angle of arm joint5', 'max': 3.14, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/bilynbk/catkin_ws_ahl/src/ahl_ros_packages/ahl_wbc/samples/ahl_robot_samples/cfg/YouBotParam.cfg', 'name': 'q5', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -3.14, 'type': 'double'}], 'type': '', 'id': 1}], 'parameters': [], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

