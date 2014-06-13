#!/bin/sh
nc -d 127.0.0.1 30003 | \
    awk 'BEGIN{FS=",";} $2 ==3 {print $7, $8, $15, $16;}'
