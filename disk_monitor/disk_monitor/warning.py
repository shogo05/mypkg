import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class DiskWarning(Node):
    def __init__(self):
        super().__init__('disk_warning')
        self.create_subscription(Float32, 'disk_usage', self.cb, 10)

    def cb(self, msg):
        if msg.data > 90.0:
            self.get_logger().warn(f"Danger! Disk usage is {msg.data:.1f}%")
        else:
            self.get_logger().info(f"Disk usage is {msg.data:.1f}% (Safe)")

def main():
    rclpy.init()
    node = DiskWarning()
    rclpy.spin(node)
    rclpy.shutdown()
