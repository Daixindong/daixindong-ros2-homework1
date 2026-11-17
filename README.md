# 선박생산공학기초및실습 과제 1

따이신동 (Dai Xindong)

`daixindong_homework1_pkg`는 RCLPY 기반 ROS 2 패키지입니다. `DaixindongPublisher`가 1초마다 `/DaixindongTopic`에 메시지를 발행합니다. `DaixindongSubscriber`는 같은 토픽을 구독하고 받은 값을 터미널에 출력합니다.

`daixindong_homework1_interfaces`는 `StudentData.msg`를 정의합니다. 매번 같은 세 값을 전송합니다.

| 필드 | 형식 | 값 |
| --- | --- | --- |
| `student_name` | `string` | `DXD` |
| `sequence_number` | `int32` | `98` |
| `measurement` | `float64` | `1.17` |

## 빌드

Ubuntu 22.04에서 ROS 2 Humble을 사용합니다. 두 패키지 디렉터리를 같은 워크스페이스의 `src`에 넣고, 워크스페이스 루트에서 실행합니다.

```bash
source /opt/ros/humble/setup.bash
rosdep install --from-paths src --ignore-src -y
colcon build --symlink-install --packages-up-to daixindong_homework1_pkg
source install/setup.bash
ros2 interface show daixindong_homework1_interfaces/msg/StudentData
```

## 실행

새 터미널마다 Humble과 워크스페이스의 설정을 불러온 뒤, 아래 두 노드를 별도 터미널에서 실행합니다.

```bash
ros2 run daixindong_homework1_pkg publisher
ros2 run daixindong_homework1_pkg subscriber
```

두 노드를 실행한 상태에서 세 번째 터미널에 다음 명령을 입력합니다.

```bash
ros2 topic info /DaixindongTopic
ros2 run rqt_graph rqt_graph
```
