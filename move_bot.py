#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    rospy.init_node('move_robot', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    vel_msg = Twist()
    vel_msg.linear.x = 0.2
    vel_msg.angular.z = 0.5

    rospy.loginfo("Moving the robot...")
    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
