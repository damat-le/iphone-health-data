# iPhone Health Data Processing

This repo contains the code to read the health data exported from the iPhone Health app and processe it. 

## Description

To export the data from the iPhone Health app, follow these steps:

<p align="center">
<img src="assets/png/export-guide.png" alt="drawing" width="600" align="" />
</p>

Health data are provided in a `.xml` file. This file contains a list of *records* with the following structure:

<div style="height: 300px;overflow: scroll;">

```xml
 <Record type="HKQuantityTypeIdentifierStepCount" sourceName="iPhone" sourceVersion="11.4.1" device="&lt;&lt;HKDevice: 0x282374b90&gt;, name:iPhone, manufacturer:Apple, model:iPhone, hardware:iPhone8,1, software:11.4.1&gt;" unit="count" creationDate="2018-08-23 15:25:45 +0100" startDate="2018-08-23 14:27:55 +0100" endDate="2018-08-23 14:34:13 +0100" value="17"/>
 <Record type="HKQuantityTypeIdentifierStepCount" sourceName="iPhone" sourceVersion="11.4.1" device="&lt;&lt;HKDevice: 0x282374b90&gt;, name:iPhone, manufacturer:Apple, model:iPhone, hardware:iPhone8,1, software:11.4.1&gt;" unit="count" creationDate="2018-08-23 15:25:45 +0100" startDate="2018-08-23 14:41:17 +0100" endDate="2018-08-23 14:47:37 +0100" value="13"/>
 <Record type="HKQuantityTypeIdentifierStepCount" sourceName="iPhone" sourceVersion="11.4.1" device="&lt;&lt;HKDevice: 0x282374b90&gt;, name:iPhone, manufacturer:Apple, model:iPhone, hardware:iPhone8,1, software:11.4.1&gt;" unit="count" creationDate="2018-08-23 15:25:45 +0100" startDate="2018-08-23 14:47:37 +0100" endDate="2018-08-23 14:53:08 +0100" value="27"/>
 <Record type="HKQuantityTypeIdentifierStepCount" sourceName="iPhone" sourceVersion="11.4.1" device="&lt;&lt;HKDevice: 0x282374b90&gt;, name:iPhone, manufacturer:Apple, model:iPhone, hardware:iPhone8,1, software:11.4.1&gt;" unit="count" creationDate="2018-08-23 15:25:45 +0100" startDate="2018-08-23 14:57:37 +0100" endDate="2018-08-23 15:03:45 +0100" value="10"/>
 <Record type="HKQuantityTypeIdentifierStepCount" sourceName="iPhone" sourceVersion="11.4.1" device="&lt;&lt;HKDevice: 0x282374b90&gt;, name:iPhone, manufacturer:Apple, model:iPhone, hardware:iPhone8,1, software:11.4.1&gt;" unit="count" creationDate="2018-08-23 15:25:45 +0100" startDate="2018-08-23 15:12:11 +0100" endDate="2018-08-23 15:22:10 +0100" value="80"/>
 <Record type="HKQuantityTypeIdentifierStepCount" sourceName="iPhone" sourceVersion="11.4.1" device="&lt;&lt;HKDevice: 0x282374b90&gt;, name:iPhone, manufacturer:Apple, model:iPhone, hardware:iPhone8,1, software:11.4.1&gt;" unit="count" creationDate="2018-08-23 17:34:46 +0100" startDate="2018-08-23 15:22:10 +0100" endDate="2018-08-23 15:29:54 +0100" value="387"/>
 <Record type="HKQuantityTypeIdentifierStepCount" sourceName="iPhone" sourceVersion="11.4.1" device="&lt;&lt;HKDevice: 0x282374b90&gt;, name:iPhone, manufacturer:Apple, model:iPhone, hardware:iPhone8,1, software:11.4.1&gt;" unit="count" creationDate="2018-08-23 17:34:46 +0100" startDate="2018-08-23 15:36:52 +0100" endDate="2018-08-23 15:42:57 +0100" value="10"/>
 <Record type="HKQuantityTypeIdentifierStepCount" sourceName="iPhone" sourceVersion="11.4.1" device="&lt;&lt;HKDevice: 0x282374b90&gt;, name:iPhone, manufacturer:Apple, model:iPhone, hardware:iPhone8,1, software:11.4.1&gt;" unit="count" creationDate="2018-08-23 17:34:46 +0100" startDate="2018-08-23 15:46:17 +0100" endDate="2018-08-23 15:55:12 +0100" value="148"/>
 <Record type="HKQuantityTypeIdentifierStepCount" sourceName="iPhone" sourceVersion="11.4.1" device="&lt;&lt;HKDevice: 0x282374b90&gt;, name:iPhone, manufacturer:Apple, model:iPhone, hardware:iPhone8,1, software:11.4.1&gt;" unit="count" creationDate="2018-08-23 17:34:46 +0100" startDate="2018-08-23 15:59:13 +0100" endDate="2018-08-23 16:07:33 +0100" value="94"/>
 <Record type="HKQuantityTypeIdentifierStepCount" sourceName="iPhone" sourceVersion="11.4.1" device="&lt;&lt;HKDevice: 0x282374b90&gt;, name:iPhone, manufacturer:Apple, model:iPhone, hardware:iPhone8,1, software:11.4.1&gt;" unit="count" creationDate="2018-08-23 17:34:46 +0100" startDate="2018-08-23 16:07:33 +0100" endDate="2018-08-23 16:14:43 +0100" value="380"/>
 <Record type="HKQuantityTypeIdentifierStepCount" sourceName="iPhone" sourceVersion="11.4.1" device="&lt;&lt;HKDevice: 0x282374b90&gt;, name:iPhone, manufacturer:Apple, model:iPhone, hardware:iPhone8,1, software:11.4.1&gt;" unit="count" creationDate="2018-08-23 17:34:46 +0100" startDate="2018-08-23 16:14:43 +0100" endDate="2018-08-23 16:23:30 +0100" value="337"/>
 <Record type="HKQuantityTypeIdentifierStepCount" sourceName="iPhone" sourceVersion="11.4.1" device="&lt;&lt;HKDevice: 0x282374b90&gt;, name:iPhone, manufacturer:Apple, model:iPhone, hardware:iPhone8,1, software:11.4.1&gt;" unit="count" creationDate="2018-08-23 17:34:46 +0100" startDate="2018-08-23 16:23:30 +0100" endDate="2018-08-23 16:33:28 +0100" value="728"/>
 <Record type="HKQuantityTypeIdentifierStepCount" sourceName="iPhone" sourceVersion="11.4.1" device="&lt;&lt;HKDevice: 0x282374b90&gt;, name:iPhone, manufacturer:Apple, model:iPhone, hardware:iPhone8,1, software:11.4.1&gt;" unit="count" creationDate="2018-08-23 17:34:46 +0100" startDate="2018-08-23 16:33:28 +0100" endDate="2018-08-23 16:43:22 +0100" value="137"/>
 <Record type="HKQuantityTypeIdentifierStepCount" sourceName="iPhone" sourceVersion="11.4.1" device="&lt;&lt;HKDevice: 0x282374b90&gt;, name:iPhone, manufacturer:Apple, model:iPhone, hardware:iPhone8,1, software:11.4.1&gt;" unit="count" creationDate="2018-08-23 17:34:46 +0100" startDate="2018-08-23 16:43:22 +0100" endDate="2018-08-23 16:52:16 +0100" value="599"/>
 <Record type="HKQuantityTypeIdentifierStepCount" sourceName="iPhone" sourceVersion="11.4.1" device="&lt;&lt;HKDevice: 0x282374b90&gt;, name:iPhone, manufacturer:Apple, model:iPhone, hardware:iPhone8,1, software:11.4.1&gt;" unit="count" creationDate="2018-08-23 17:34:46 +0100" startDate="2018-08-23 16:52:16 +0100" endDate="2018-08-23 17:00:58 +0100" value="189"/>
```
</div>

Each record represents a measurement and each measurement is characterised by the following main features:
- `type`: the quantity being measured. Possible values are:
  - `HKQuantityTypeIdentifierStepCount`: a quantity sample type that measures the number of steps the user has taken.
  - `HKQuantityTypeIdentifierDistanceWalkingRunning`: a quantity sample type that measures the distance the user has moved by walking or running.
  - `HKQuantityTypeIdentifierFlightsClimbed`: a quantity sample type that measures the number flights of stairs that the user has climbed.
  - other values: for details read [Apple's Documentation](https://developer.apple.com/documentation/healthkit/data_types)
- `value`: the result of the measurement.
- `startDate`: the time at which the device started to record the measurement.
- `endDate`: the time at which the device ended to record the measurement.
- If you look carefully at the data, you may note an other feature: `CreationDate`. I wasn't able to find it into the documentation, so I don't know exactly what it stands for.

## Processing

The data processing is done in the `src/pipeline.py` file. The script:
- Reads the input `.xml` file.
- Properly parses the datetime fields.
- Creates a new column `middleDate` that represents the middle of the interval `[startDate, endDate]`.
- Set `middleDate` as index of the data.
- Extracts the relevant columns: `middleDate`, `step`, `distance`, `floor`.
- Stores the data in a `.csv` file.


Below is reported an example of the output data, with daily frequency:

```csv
middleDate,step,distance,floor
2018-08-23 00:00:00+01:00,4588,3.45344,0
2018-08-24 00:00:00+01:00,6196,4.0035,2
2018-08-25 00:00:00+01:00,12788,7.91076,10
2018-08-26 00:00:00+01:00,792,0.51739,0
2018-08-27 00:00:00+01:00,4077,2.79072,1
2018-08-28 00:00:00+01:00,3607,2.43844,4
2018-08-29 00:00:00+01:00,3258,2.06088,1
2018-08-30 00:00:00+01:00,8112,5.424664,9
2018-08-31 00:00:00+01:00,6109,4.02908,29
```

## Usage:

```bash
python -m src.pipeline -i <in_data> -o <out_data> -f <freq>

options:
  -h, --help           show this help message and exit
  -i, --in_fn IN_FN    Path to the input data file
  -o, --out_fn OUT_FN  Path to the output data file
  -f, --freq FREQ      Resampling frequency. Valid values are those compatible with pandas.DataFrame.resample method. See https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases
```
