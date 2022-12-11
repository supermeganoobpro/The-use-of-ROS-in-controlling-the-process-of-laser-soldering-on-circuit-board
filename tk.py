#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
       
def talker():
    pub = rospy.Publisher('arduino', String, queue_size=10)
    rospy.init_node('main', anonymous=True)
    rate = rospy.Rate(0.8) # 10hz
    while not rospy.is_shutdown():
        hello_str = "{20, 0}"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        
        hello_str = "{0, 80}"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        
        hello_str = "{-20, 0}"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        
        hello_str = "{0, -80}"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
