#!/bin/bash
product=1
for i in `seq 1 $@`
do
product=`expr $product \* $i`
done
echo $product
