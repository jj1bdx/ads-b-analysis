# ads-b-analysis

dump1090 data analysis scripts in Python and Geographiclib.

This repository contains a set of script to analyze the BaseStation format data
obtained from [dump1090](https://github.com/MalcolmRobb/dump1090) ADS-B
receiver.

## Files

* `ads-b-log.sh`: analysis script running on the receiver (Raspberry Pi, etc.)
* `ads-b-log-example.txt`: output example from ads-b-log.sh
* `convdist.py`: analyze the data in the output format from stdin, output to stdout, converted to distance (in nautical miles) and azimuth (in degrees)
* `convdxdy.py`: analyze the data in the output format from stdin, output to stdout, converted to dx (distance of X axis, West-to-East) and dy (distance of Y axis, South-to-North) (distance in nautical miles)

## Requirement

* Python [geographiclib](https://pypi.python.org/pypi/geographiclib)
* See also [Geographiclib source page](http://geographiclib.sourceforge.net/)

## Caveats

* Conversion is slow (in Python, after all)
* Do not transfer the raw BaseStation format data to the host analyzing the data via TCP. The rate of packets is high (>20 lines/sec) and may consume the considerable amount of bandwidth and CPU power of the recipient side.

## License

[Public domain aka CC0](http://creativecommons.org/publicdomain/zero/1.0/)

## Author

Kenji Rikitake
