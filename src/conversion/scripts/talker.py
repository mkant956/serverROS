#!/usr/bin/env python

# license removed for brevity
import rospy
#roslib.load_manifest('beginner_tutorials')
import roslib; roslib.load_manifest('beginner_tutorials')
from std_msgs.msg import String
from geometry_msgs.msg import TransformStamped
import math

def angle(w,x,y,z):
    sin=2.0*(w*z+x*y)
    cos=1.0-2.0*(y*y+z*z)
    return (180.0*math.atan2(sin,cos)/3.141592653589 + 180.0 - 10.25)%360 - 180.0

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
def callback(transform):
    # print(transform.transform.rotation)
    rospy.loginfo(rospy.get_caller_id() + 'I heard %f', angle(transform.transform.rotation.w, transform.transform.rotation.x, transform.transform.rotation.y, transform.transform.rotation.z))

def listenVicon():
    rospy.init_node('angleConvert', anonymous=True)
    rospy.Subscriber('vicon/Wayne/Wayne', TransformStamped, callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        listenVicon()
    except rospy.ROSInterruptException:
        pass


