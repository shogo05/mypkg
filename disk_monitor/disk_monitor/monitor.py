import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import shutil

class DiskMonitor(Node):
    def __init__(self):
        super().__init__('disk_monitor')
        self.pub = self.create_publisher(Float32, 'disk_usage', 10)
        self.create_timer(1.0, self.cb)

    def cb(self):
        total, used, free = shutil.disk_usage("/")
        usage_percent = (used / total) * 100
        msg = Float32()
        msg.data = usage_percent
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = DiskMonitor()
    rclpy.spin(node)
    rclpy.shutdown()
