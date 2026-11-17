import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from daixindong_homework1_interfaces.msg import StudentData


TOPIC = '/DaixindongTopic'
QUEUE_DEPTH = 10


class DaixindongPublisher(Node):
    def __init__(self):
        super().__init__('DaixindongPublisher')
        self._publisher = self.create_publisher(StudentData, TOPIC, QUEUE_DEPTH)
        self._timer = self.create_timer(1.0, self._publish_message)

    def _publish_message(self):
        message = StudentData()
        message.student_name = 'DXD'
        message.sequence_number = 98
        message.measurement = 1.17
        self._publisher.publish(message)
        self.get_logger().info(
            f'Published name={message.student_name}, sequence={message.sequence_number}, '
            f'measurement={message.measurement:.2f}'
        )


class DaixindongSubscriber(Node):
    def __init__(self):
        super().__init__('DaixindongSubscriber')
        self._subscription = self.create_subscription(
            StudentData, TOPIC, self._receive_message, QUEUE_DEPTH
        )

    def _receive_message(self, message):
        self.get_logger().info(
            f'Received name={message.student_name}, sequence={message.sequence_number}, '
            f'measurement={message.measurement:.2f}'
        )


def _run_node(node_type, args):
    rclpy.init(args=args)
    node = None
    try:
        node = node_type()
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        if node is not None:
            node.destroy_node()
        rclpy.try_shutdown()


def publisher_main(args=None):
    _run_node(DaixindongPublisher, args)


def subscriber_main(args=None):
    _run_node(DaixindongSubscriber, args)
