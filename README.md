# ads-b-analysis

dump1090 data analysis scripts in Python and Geographiclib.

This repository contains a set of script to analyze the BaseStation format data
obtained from [dump1090](https://github.com/MalcolmRobb/dump1090) ADS-B
receiver.

## Files

* `ads-b-log.sh`: analysis script running on the receiver (Raspberry Pi, etc.)
* `ads-b-log-example.txt`: output example from ads-b-log.sh
* `antenna-design-20140615.jpg`: antenna design memorandum
* `convdist.py`: analyze the data in the output format from stdin, output to stdout, converted to distance (in nautical miles) and azimuth (in degrees)
* `convdxdy.py`: analyze the data in the output format from stdin, output to stdout, converted to dx (distance of X axis, West-to-East) and dy (distance of Y axis, South-to-North) (distance in nautical miles)
* `plotdxdy.R`: plot the data into a PNG file with R ggplot2 library

## ADS-B message format reference

* Dump1090 source itself is a good reference
* [SBS BaseStation format data reference](http://www.homepages.mcb.net/bones/SBS/Article/Barebones42_Socket_Data.htm)
* [The use of a commercial ADS-B receiver to derive upper air wind and temperature observations from Mode-S EHS information in The Netherlands (pdf)](http://www.knmi.nl/bibliotheek/knmipubTR/TR336.pdf)

## Requirement

* Python [geographiclib](https://pypi.python.org/pypi/geographiclib)
* See also [Geographiclib source page](http://geographiclib.sourceforge.net/)
* [ggplot2 library for R](http://ggplot2.org/)

## Caveats

* Conversion is slow (it's in Python, after all); run the conversion program on a fast machine.
* Do not transfer the raw BaseStation format data to the host analyzing the data via TCP in real-time. The rate of packets is high (>20 lines/sec), and the packets may consume a considerable amount of bandwidth and CPU power (~ full 1 core of Core i7) of the recipient side.
* Computationally lightweight load filtering (e.g., format conversion, choosing items, etc.) should be performed on the Ras Pi.

## Signal receiving tips

* Use the receiver protection and filterting on R820T SDR with:
    * 1/4-wavelength short stub filter for 1090MHz (which may effectively reduce cell phone airwaves around 2.18GHz)
    * Ferrite cores to the power and signal cables from Ras Pi to the R820T
    * Do not expose the receiving antenna close to the transmission antenna; if you have to do so, measure how the transmission affects the overall performance. In my case, 18.1MHz and 21MHz fed with 50W of power to the inverted vee antenna 1m above didn't affect the performance much. You need to experiment to determine the reception performance impact by the transmission.
* Always try to use a better antenna system, with a simple antenna erected highest as possible (a sleeve dipole or a ground plane will work very well)
* The ground height matters; the propagation of line-of-sight path works best.
* Use [daemontools](http://cr.yp.to/daemontools.html) for stable continuous operation
* Update Raspbian distribution as necessary (security fix, etc.)

## License

[Public domain aka CC0](http://creativecommons.org/publicdomain/zero/1.0/)

## Author

Kenji Rikitake
