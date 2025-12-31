import launch
import launch.actions
import launch_ros.actions

def generate_launch_description():
    monitor = launch_ros.actions.Node(
        package='disk_monitor',
        executable='monitor',
        )
    warning = launch_ros.actions.Node(
        package='disk_monitor',
        executable='warning',
        output='screen'
        )

    return launch.LaunchDescription([monitor, warning])
