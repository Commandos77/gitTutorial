#!/bin/bash

if (( $# < 2 ))
then
echo $1
else
if (( $# > 2 )) && (( $# < 4 ))
then 
echo "${@: -1}"
else
echo "Invalid number of arguments"
fi
fi
