#!/bin/bash

init() {
gpio mode $DS out
gpio mode $STCP out
gpio mode $SHCP out
gpio write $DS 0
gpio write $STCP 0
gpio write $SHCP 0
}

writeByte() {
  
  for((i=0;i<8;i++)) 
  do
    bit=$(($1>>$i&0x01))
#    echo -n $bit
    gpio write $DS $bit
    gpio write $SHCP 0
    gpio write $SHCP 1
   done
#   echo 
  gpio write $STCP 0
  gpio write $STCP 1

}

init
writeByte $1
