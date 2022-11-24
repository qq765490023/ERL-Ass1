import rospy
import time
import random
from robot_visit import architecture_name_mapper as anm
from robot_visit.srv import Move

#
#
## @package robot_visit 
# \file move.py
# \brief This is the /move module, which is used for control the phscical movement of the robot.
# \author Zhouyang Hong 
# \version 0.1 
# \date 22/11/2022 
# 
# \details 

# Node: /move
# Service: /motion/move
# [None] 
# Description: 
# This node provide a service to state-decision-maker, when robot want to go somewhere, this service will be called to move 
# the robot to the destination.



class Move_manager(object):
    """
    A class used to physicially move the robot
    ...
    Attributes ---------- 
    
    Methods -------
    execute_callback():
    This function will be called when required to move to target location.
    Here is just simply simulating this process by simply randomly wait an amount of time.
    """
    def __init__(self):

        self.s = rospy.Service(anm.SVR_MOVE, Move,self.execute_callback)

    def execute_callback(self,msg):
        rospy.loginfo('moving')
        time.sleep(random.uniform(0.5,1.5))
        return True

if __name__ == '__main__':
    # Initialise the node 
    rospy.init_node(anm.NODE_MOVE, log_level=rospy.INFO)
    server = Move_manager()
    rospy.spin()
