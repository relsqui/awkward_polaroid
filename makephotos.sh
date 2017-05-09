#!/bin/bash

for count in `seq -w 1 999`; do
    CF3/cfdg -s 627 polaroids.cfdg polaroids/$count.png
done
