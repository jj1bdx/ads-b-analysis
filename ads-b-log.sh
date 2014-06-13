#!/bin/sh
nc -d raspi-sdr 30003 | \
    awk 'BEGIN{FS=",";} $2 ==3 {print $7, $8, $15, $16;}'
