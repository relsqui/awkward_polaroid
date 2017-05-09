#!/bin/bash

# Copyright (c) 2017 Finn Ellis.
# Free to use and modify under the terms of the MIT license.
# See included LICENSE file for details.

for count in `seq -w 1 999`; do
    CF3/cfdg -s 627 polaroids.cfdg polaroids/$count.png
done
