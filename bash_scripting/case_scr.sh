#!/bin/bash
echo "Enter your command"
read command
case $command in
 start)
    echo "Service started"
    sleep 9999 ;;
 stop)
    x = getpid
    kill $x
    echo "Service stoped" ;;
 restart)
    echo "Service restarted";;
 *) echo "Service running";;
esac
 
