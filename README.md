# Mush

### Mushroom game for classroom environment to foster children's attention during the classes.

<p align="center">
  <img align="center" src="resources/blueMush.jpg" width=15%>
  <img align="center" src="resources/purpleMush.jpg" width=15%>
  <img align="center" src="resources/redMush.jpg" width=15%>
</p>

In this first prototype of our collaborative game, environmental volume is analysed: If environment is quiete (if it does not exceed the noise threshold  value) mushrooms are growing during in the session. We can imagine this working in a class environment: if a group of students is quite during the class session mushrooms grow. In future development we want to exploit speech and audio deep learning technique to extract information from the students. Examples are: emotion recognition, sentiment analysis, speech recognition etc.  

Students are awarded with breaktimes: students can take a break as long as the amount of mushrooms they grow.

For volume measurement rcaudio (https://github.com/mhy12345/rcaudio) is used.

For game part pygame library is used.
  
##  Game object's definition 

### Mushrooms
<p align="center">
<img src="resources/redMush.jpg" width=20%>
</p>

Mushrooms are grown since the measured total volume during a session is not exceeded the threshold value. In this case: They keep grow up until the end of the class. If instead the measured total volume during a session is exceeded the treshold value, mushrooms are stop appearing.
  
### Mage
<p align="center">
 <img src="resources/mage.jpg" width=20%>
</p>

Mage comes at the end of the all sessions and she announces the awarded breaktime that change according to the numer of mushrooms grew.
<p align="center">
<img src="resources/2.png" width=50%>
</p>

https://www.youtube.com/watch?v=-tU486wmFCQ
