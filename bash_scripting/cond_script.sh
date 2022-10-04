#!/bin/bash
 
[[ $1 == $2 ]]
echo $?
[[ $1 > $2 ]]
echo $?
[[ $TEST > 0 ]]
echo $?
[[ $3 != $4 ]]
echo $?
[[ $3 -ge $4 ]]
echo $?
