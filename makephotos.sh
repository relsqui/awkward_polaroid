#!/bin/bash

for count in `seq -w 1 1`; do
    CF3/cfdg -s 500 polaroids.cfdg polaroids/$count.png
done
