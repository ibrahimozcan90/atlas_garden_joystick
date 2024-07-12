from distutils.core import setup

from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=["atlas_garden_joystick"],
    package_dir={"": "src"},
    # requires=['rospy', 'std_msgs', 'diagnostic_msgs']
)

setup(**setup_args)
