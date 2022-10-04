#! bin/bash

while true
do
echo "Enter your command:"
read input
 case $input in
    ls) echo "Enter path to dir:"
        read uspath
        ls -l $uspath ;;
    pwd) pwd ;;
    hi) echo "Hi $USER" ;;
    exit) break ;;
    *) echo "Enter another command"
 esac
done

 
 
