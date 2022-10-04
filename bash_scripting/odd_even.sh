#!/bin/bash

if (( ${#1}%2 == 0 ))
then
echo "Odd"
else
echo "Even"
fi
