## Odometry (first exercise)
To run odometry:


1. Open RViz launch on development machine (PC)
2. On machine (development PC) run: 

```bash
rosrun amsagv set_odom_frame.py 
``` 
3. Set 2D Pose Estimation (green arrow)
4. Connect to AGV with:
```bash
ssh pic@192.168.222.72
```
4. Go to working directory
```bash
cd ros/work/src/amsagv/scripts/
 ```
 5. Run the script:
 ```bash
rosrun amsagv agv.py
 ```

6. Run tag reader
```bash
rosrun amsagv tag_reader.py
```
6. Run control line
```bash
rosrun amsagv control_line.py
```

6. Run control point odom
```bash
rosrun amsagv agv.py
rosrun amsagv control_point_odom.py
```

7. Run display on PC:
~~~bash
rosrun amsagv display.py
~~~