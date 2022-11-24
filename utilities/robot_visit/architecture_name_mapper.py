#!/usr/bin/env python
import rospy

# The name of a boolean parameter to active random testing.
# If the value is `False` a keyboard-based interface will be used to produce stimulus 
# (i.e., speech, gesture and battery signals). Instead, random stimulus will be generate 
# if `True`. In the latter case, the architecture also requires all the parameters 
# with a the scope `test/random_sense/*`, which are not used if `False`.
PARAM_RANDOM_ACTIVE = 'test/random_sense/active'
TOPIC_CONTROL = 'state/control'
TOPIC_BATTERY = 'state/battery'

TOPIC_CHARGE = 'state/charge'

NODE_SDM = 'state_decision_maker'
NODE_MOVE = 'move'
NODE_BATTERY = 'battery'
NODE_CONTROL = 'control'
SVR_ARMOR = 'armor_interface_srv'
SVR_MOVE = 'motion/move'
# The delay between changes of battery levels, i.e., high/low.
# It should be a list `[min_time, max_time]`, and the battery level change
# will occur after a random number of seconds within such an interval.
PARAM_BATTERY_TIME = 'test/random_sense/battery_time'
# ---------------------------------------------------------

# The name of the planner node.
NODE_PLANNER = 'planner'

# The name of the action server solving the motion planning problem.
ACTION_PLANNER = 'motion/planner'

PARAM_CONTROLLER_TIME = 'test/random_motion_time'
# -------------------------------------------------

# Function used to label each log with a producer tag.
def tag_log(msg, producer_tag):
    return f'@{producer_tag}>> {msg}'
