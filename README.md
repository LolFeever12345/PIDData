# **PID Data Tuning Tool**

## How to Use

To utilize this tool, have your PID controller or drive code print out the data in the format of time, left motor speed, right motor speed, target and paste it into the csv file, but make sure you do not paste over the first line as that is a header line and the script reads to know how to sort the data.
This python script will generate a graph that can be used to compare to ideal PID tuned graphs to allow for easier tuning. As a recommendation, try to ensure that you have at least 200 data points in the csv file to generate a helpful graph.
