#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import re

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10
        )
        
    def listener_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')
        
        # Extract the integers using regex
        matches = re.findall(r'\d+', msg.data)
        if len(matches) >= 2:
            int_val1 = int(matches[0])
            int_val2 = int(matches[1])
            sum_result = int_val1 + int_val2
            self.get_logger().info(f'Extracted values: {int_val1}, {int_val2}')
            self.get_logger().info(f'Sum: {sum_result}')
        
def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()