# ROS Robot Movement Simulation

🐢 A basic ROS project to simulate a TurtleBot3 moving autonomously using Python and `geometry_msgs/Twist`.

## 🎯 Project Goal
To publish velocity commands using ROS and move the robot in a Gazebo simulation environment (via The Construct platform).

## 💻 What I Learned
- ROS topics and message types (`/cmd_vel`, `Twist`)
- How to control a robot with Python (`rospy`)
- Writing and executing ROS nodes
- Using The Construct for ROS simulation

## 📁 Files Included
- `move_bot.py` – Publishes Twist messages to move the robot

## 🛠 Tools & Technologies
- ROS Noetic
- TurtleBot3
- Python 2.7 (rospy)
- The Construct Simulator

## 📸 Simulation Screenshot

![robot_moving_simulation](https://github.com/user-attachments/assets/e96c1987-cbbf-403a-b8e5-dea3fbf8aa6d)

## ▶️ How to Run
In your ROS environment:

```bash
# Terminal 1
roscore

# Terminal 2
rosrun robot_movement move_bot.py




