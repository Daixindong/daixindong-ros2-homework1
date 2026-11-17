from setuptools import setup


package_name = 'daixindong_homework1_pkg'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', [f'resource/{package_name}']),
        (f'share/{package_name}', ['package.xml']),
    ],
    install_requires=['setuptools'],
    maintainer='Dai Xindong',
    maintainer_email='student@example.com',
    description="ROS 2 Python publisher and subscriber for Dai Xindong's homework.",
    license='UNLICENSED',
    entry_points={
        'console_scripts': [
            'publisher = daixindong_homework1_pkg.nodes:publisher_main',
            'subscriber = daixindong_homework1_pkg.nodes:subscriber_main',
        ],
    },
)
