# Fuzzing_detector

# About this project:
In this project I implemented a Fuzzing detector in Python. This tool
listen to packets in the network, and detects "Fuzzing" attacks. 
This tool detect only Fuzzing attacks on SSH protocol
You can read more about Fuzzing here: https://en.wikipedia.org/wiki/Fuzzing
You can read more about SSH protocol here: https://en.wikipedia.org/wiki/Secure_Shell

# More about the project:
The tool support Windows and Linux – Ubuntu.
The Fuzzing detector run in the background of your computer (after you play the tool of course..)
In this project I used scapy python library in order to listen the network communication,
and then I analyzed only SSH packets.
Here you can see how SSH packets looks like (from wireshark):
![image](https://user-images.githubusercontent.com/92723105/167287906-a3e595a4-49d3-4de1-a0f5-94d6c7e65384.png)
for each relevant packet I got, I analyzed the content and noticed if an attack was detected.
I also used spellchecker python library for this mission.

# Project structure:
The project has 2 main classes: "Fuzzing" , "Fuzz".
The first is the Fuzzing detector tool.
The  other one is a tool that produces SSH packets in order to test the Fuzzing detector.

# How to run the project:
Enter the project directory, open cmd (Windows) or terminal (Linux) 
through project's path and run the following command:
python Fuzzing.py
You can also play the Fuzz (tester) with:
python Fuzz.py
![image](https://user-images.githubusercontent.com/92723105/167288127-c48b8db7-9b9a-41d1-a606-bf092840f988.png)
![image](https://user-images.githubusercontent.com/92723105/167288138-233cb575-66ad-496b-add2-e8a7d390b354.png)

Here you can see the output of the tool when Fuzzing attack was detected:
![image](https://user-images.githubusercontent.com/92723105/167288204-a8a0db6f-8c30-4d80-bfd6-da7231b86910.png)

