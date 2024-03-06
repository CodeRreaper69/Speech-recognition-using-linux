#!/bin/bash


#for red fonts

echo -e "\e[31m
"

figlet "WELCOME"
sleep 0.2   #for 0.25 seconds delay
figlet "TO"
sleep 0.25
figlet "TEXT"
sleep 0.25
figlet "TO"
sleep 0.25
figlet "SPEECH"
sleep 0.25
figlet "GENERATOR"
sleep 0.25




#for getting green fonts, green fonts code
echo -e "\e[32m
"
echo Input Text to be converted to speech

echo -e "\n"

#for purple bold fonts
echo  -e "\033[0;95m
"


echo  Author : Sourabh Dey


# for blue fonts

echo -e "\e[34m
"
echo -e "\n"

python3 spd.py

echo -e "\n"

#****END*****#




