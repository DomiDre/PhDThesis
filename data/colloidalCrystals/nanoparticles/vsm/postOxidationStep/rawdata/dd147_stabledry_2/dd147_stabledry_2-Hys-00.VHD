@Filename: C:\vsm-lv\System_Admin\data\Dominique\DD150\dd147_stabledry_2\dd147_stabledry_2-Hys-00.VHD
@Measurement Controlfilename: c:\vsm-lv\System_Admin\Recipes\VC_HL.VHC
@Calibration filename: c:\vsm-lv\System_Admin\settings\default.cal
@Parameter Filec:\vsm-lv\System_Admin\settings\default.cal
@Operator: System_Admin
@Samplename: dd147_stabledry_2
@Date: Friday, October 14, 2016    (2016-10-14)
@Time: 10:40:45
@Test ID: test
@Apparatus: EZ7; LabVSM; Customer: Grubenhagen; first started on: Wednesday February 03, , 2015
[Installed Options]
VSM Model="EV X"
VSM=TRUE    
Torque=FALSE    
Signal Processor="SRS SR 830"
Torque Signal Processor="NI-6210"
Unipolar=FALSE    
Automation=FALSE    
MR=FALSE    
Torque Signal Inversion=TRUE    
VSM DAQ Card=TRUE    
Time Constant="0.1 s"
DAQ Output=FALSE    

[Signal and Coils]
Signal Connection="A-B"
Vector Coils=FALSE    
Stationary Coils=FALSE    
Z Coils=FALSE    
Sensor Angle="0 deg"
Time Between Averages=0.150000    
Y Averages Multiplier=1    
Reference Source="External"
SR830 Frequency=75.000000    

[Rotation]
Automatic Rotation=TRUE    
Rotate Option="Mdrive"
Rotation Display=FALSE    
Max Angle=400.000000    
Min Angle=-400.000000    
Rotation Serial Port=1    
Rotation Display Serial Port=1    
Torque Rotation Serial Port=4    

[Field]
Gaussmeter="32 KP DRC"
Gauss Probe="1 x"
Maximum Field=19000.000000    
Wait Time=4.000000    
Sweeprate Array="1500.000, 500.000, 100.000, 10.000, "
Averaging Array="1, 1, 1, 10, "
Precision Array="3.000, 0.500, 0.200, 0.200, "
Stability Array="1.000, 1.000, 0.500, 0.100, "
FCM-10 Address="GPIB0::16::INSTR"
Minimum Sweep Time=2.000000    
Minimum Sweep Rate Divider=40.000000    
Stability Time Between Readings=0.300000    
Number of Readings for Stability Check=2.000000    
Slow Approach=TRUE    
Slow Start %=90.000000    
Slow Approach Max Sweep Rate Divider=10.000000    
Max Slow Sweep Time=4.000000    

[MR]
MR Signal Processor=Manual VSM
Punch Through="Variable 0-10V"
Automation Comm Port=0
Max Current=20.000000    
Min AD Voltage=4.600000    
Max AD Voltage=7.000000    
MR Option=FALSE    
MS MR Signal Processor=FALSE    
AC&DC Current Source=FALSE    

[Temperature Control]
Temperature Control=TRUE    
Boil Off Nitrogen=FALSE    
Liquid Helium=FALSE    
Leave Temperature On=TRUE    
Temperature Control Type="SI 9700"
Sensor A="E-type"
Sensor B="E-type"
Control Sensor="A"
Sensor A Table=""
Sensor B Table=""
ITC Serial Port=2    
TC GPIB Address=15    
Temperature Log File="/c/vsm-lv/temperature.log"
Default Temperature=298.150000    
Gas Switching Temperature=333.150000    
Default Soak Time=120.000000    
Set Temperature Sample Time=10.000000    
Temperature Accuracy=1.000000    
Temperature Accuracy %=1.000000    
Automatic Gas Switching=FALSE    
1000 C Option=FALSE    
Number of points for accuracy wait=90    
Time between points for accuracy wait=1.000000    
Wait for Heat Exchanger Removal=FALSE    
Removal Temperature=0.000000    
Wait Time for Heat Exchanger Removal=0.000000    

[SI 9700]
P=1    
I=20    
D=0    
HE-P=1    
HE-I=20    
HE-D=0    
Max T Sweep Seed=1.000000
Min T Sweep Seed=0.200000
Max Heater Power=80    
Max T Sweep Speed=60.000000    
Min T Sweep Speed=12.000000    

[Other]
Transverse Direction="Absolute"
Default Transverse Direction=90.000000    
Time Dependence Start Field Distance=10.000000    
Minimum Remanence Wait Time=2.000000    
Default AC Demag Max Field=10000.000000    
AC Demag Minimum Field=1.000000    
Max Lockin Phase Error=90    
Mains Frequency=50.000000    
Samples Per Cycle=100    

[Interlock]
Door Lock=FALSE    
Interlock=FALSE    
Light Tower=FALSE    
Interlock Interface Name="Dev3"

[Torque Interface]
Torque Interface Name="Dev2"

[Exit Gas Heater Settings]
EGH PC Control=FALSE    
EGH Serial Port=0    
EGH Voltages=""

[VSM Interface]
VSM Interface Name="Dev1"

[MR Interface]
MR Interface Name="Dev1"

[DAQ Communication]
Protocol="Mx"
Remove Spikes=TRUE    

[Sensor Table]
1st Column=0    
Temperature Unit=0    

[Communication]
LIA 1 Address="GPIB0::8::INSTR"
LIA 2 Address=""
VSM Rotation Address="COM1"
Torque Rotation Address=""
Rotation Display Address=""
SI9700 Address="COM12"
EGH Address=""
Communication Mode="Original"
LIA Baud Rate="19200"
LIA Serial Read Delay=50    

[LIA]
Local=0    
Minimum Sensitivity="5 uV"

[MR External Current Source]
Ext I Src Adddress=""
AC MR Channel=""
DC MR Channel=""
Read Termination Character="CR"
CS Baud Rate="300"
Flow Control="Off"
Which LIA="1"
Input="A"
Ref Slope="Sine"
@System Status = Online
@Sample Orientation and Shape: line parallel with field
@@Sample Dimensions
Shape = Circular;  Length = 6.60 [mm] Width = 6.60 [mm] Thickness = 1.000E+3 [nm] Diameter = 8.00 [mm] Volume : 5.027E-11 [m^3] Area = 5.027E+1 [mm^2] Mass = 2.686E-2 [g] Nd =  0.00 Sample Angle Offset = 0.000 
Ms (for Hys loss calculation) = 1.000 [memu]
@@End Sample Dimensions
@Measurement type: Hysteresis Loop
@Product of: MicroSense EasyVSM Software version EasyVSM 20150305-01
@@Comments: 
@@END Comments
@@Parameters
@@Measurement Preparation Actions
Action 0:      Set VSM DAQ AO0 Voltage to 10.0000 [ ] and wait 0.0000 s ; Set Mode = Set and wait till there
Action 1:      Set VSM DAQ AO1 Voltage to 0.0000 [ ] and wait 0.0000 s ; Set Mode = Set and wait till there
Action 2:      Set Field Angle to -0.0000 [deg] and wait 0.0000 s ; Set Mode = Set and wait till there
Action 3:      Set Nothing to 0.9000 [Unitless] and wait 0.0000 s ; Set Mode = Set and wait till there
Action 4:      Set Nothing to 1000.0000 [Unitless] and wait 0.0000 s ; Set Mode = Set and wait till there
@@END Measurement Preparation Actions
@@Measurement Parameters
@Repeat all sections = No
@Number of sections= 18
@Section 0: Hysteresis; New Plot
@Preparation Actions:
Action 0:      Set Gauss Range to 0.0000 [ ] and wait 0.0000 s ; Set Mode = Set and wait till there
@Repeated Actions:
Action 0:      Set Applied Field to 0.0000 [Oe] and wait 1.0000 s ; Set Mode = Set and wait till there; Measure 
@Main Parameter = 0 : Applied Field [Oe].
@Main Parameter Setup:
     From: -10.0000 [Oe] To: 50.0000 [Oe] Min Stepsize/Sweeprate = 10.0000 [Oe] Max Stepsize/Sweeprate = 10.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Measured Signal(s) = X
@Section 0 END
@Section 1: Hysteresis
@Preparation Actions: None
@Main Parameter Setup:
     From: 50.0000 [Oe] To: 1000.0000 [Oe] Min Stepsize/Sweeprate = 25.0000 [Oe] Max Stepsize/Sweeprate = 25.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 1 END
@Section 2: Hysteresis
@Main Parameter Setup:
     From: 1000.0000 [Oe] To: 10000.0000 [Oe] Min Stepsize/Sweeprate = 500.0000 [Oe] Max Stepsize/Sweeprate = 500.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 2 END
@Section 3: Hysteresis
@Main Parameter Setup:
     From: 10000.0000 [Oe] To: 19000.0000 [Oe] Min Stepsize/Sweeprate = 1000.0000 [Oe] Max Stepsize/Sweeprate = 1000.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 3 END
@Section 4: Hysteresis
@Main Parameter Setup:
     From: 19000.0000 [Oe] To: 10000.0000 [Oe] Min Stepsize/Sweeprate = 1000.0000 [Oe] Max Stepsize/Sweeprate = 1000.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 4 END
@Section 5: Hysteresis
@Main Parameter Setup:
     From: 10000.0000 [Oe] To: 1000.0000 [Oe] Min Stepsize/Sweeprate = 500.0000 [Oe] Max Stepsize/Sweeprate = 500.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 5 END
@Section 6: Hysteresis
@Main Parameter Setup:
     From: 1000.0000 [Oe] To: 50.0000 [Oe] Min Stepsize/Sweeprate = 25.0000 [Oe] Max Stepsize/Sweeprate = 25.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 6 END
@Section 7: Hysteresis
@Main Parameter Setup:
     From: 50.0000 [Oe] To: -50.0000 [Oe] Min Stepsize/Sweeprate = 10.0000 [Oe] Max Stepsize/Sweeprate = 10.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 7 END
@Section 8: Hysteresis
@Main Parameter Setup:
     From: -50.0000 [Oe] To: -1000.0000 [Oe] Min Stepsize/Sweeprate = 25.0000 [Oe] Max Stepsize/Sweeprate = 25.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 8 END
@Section 9: Hysteresis
@Main Parameter Setup:
     From: -1000.0000 [Oe] To: -10000.0000 [Oe] Min Stepsize/Sweeprate = 500.0000 [Oe] Max Stepsize/Sweeprate = 500.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 9 END
@Section 10: Hysteresis
@Main Parameter Setup:
     From: -10000.0000 [Oe] To: -19000.0000 [Oe] Min Stepsize/Sweeprate = 1000.0000 [Oe] Max Stepsize/Sweeprate = 1000.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 10 END
@Section 11: Hysteresis
@Main Parameter Setup:
     From: -19000.0000 [Oe] To: -10000.0000 [Oe] Min Stepsize/Sweeprate = 1000.0000 [Oe] Max Stepsize/Sweeprate = 1000.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 11 END
@Section 12: Hysteresis
@Main Parameter Setup:
     From: -10000.0000 [Oe] To: -1000.0000 [Oe] Min Stepsize/Sweeprate = 500.0000 [Oe] Max Stepsize/Sweeprate = 500.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 12 END
@Section 13: Hysteresis
@Main Parameter Setup:
     From: -1000.0000 [Oe] To: -50.0000 [Oe] Min Stepsize/Sweeprate = 25.0000 [Oe] Max Stepsize/Sweeprate = 25.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 13 END
@Section 14: Hysteresis
@Main Parameter Setup:
     From: -50.0000 [Oe] To: 50.0000 [Oe] Min Stepsize/Sweeprate = 10.0000 [Oe] Max Stepsize/Sweeprate = 10.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 14 END
@Section 15: Hysteresis
@Main Parameter Setup:
     From: 50.0000 [Oe] To: 1000.0000 [Oe] Min Stepsize/Sweeprate = 25.0000 [Oe] Max Stepsize/Sweeprate = 25.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 15 END
@Section 16: Hysteresis
@Main Parameter Setup:
     From: 1000.0000 [Oe] To: 10000.0000 [Oe] Min Stepsize/Sweeprate = 500.0000 [Oe] Max Stepsize/Sweeprate = 500.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 16 END
@Section 17: Hysteresis
@Main Parameter Setup:
     From: 10000.0000 [Oe] To: 19000.0000 [Oe] Min Stepsize/Sweeprate = 1000.0000 [Oe] Max Stepsize/Sweeprate = 1000.0000 [Oe]
     Signal change min step =  0.00 [%] Signal change max step =  0.00 [%] ;  Wait time =    1.00 [sec] Up & Down = No
@Section 17 END
@@Plot Settings
Number of plots: 1
Plot 0: Hysteresis = On; Section: 0; Signal: X; Label: Hys X; Point style: 2; Interpolation: On; Color: 14417948; Mirror: Off
@@ENDPlot Settings
@@END Measurement Parameters
@@Instrument Parameters
Stationary Coils = FALSE
Sensor Angle = 0 deg
@Gauss Range: 30 kOe
@Emu Range: 10 nV
@Torque Range: 4000 dyne cm
@Auto-range emu: No
@Number of averages: 5
@Rot 0 deg cal: -21170
@Rot 360 deg cal: 20810
@Dec Pt. constant: 1000
@Emu dec cal: 100
@Emdac: 10530
@Emu/v: 58.557
@Y Coils Correction Factor: 1.385
@Sample Shape Correction Factor: 1.000
@Coil Angle Alpha: 45.000
@Coil Angle Beta: -45.000
[Data Manipulation]
Field Linearity Correction = No
Image Effect Correction = Yes
Image Correction Array Length = 17
14997.000000   1.000000
15246.000000   1.000145
15496.000000   1.000446
15746.000000   1.000592
15995.000000   1.000892
16246.000000   1.001261
16495.000000   1.001631
16745.000000   1.002000
16995.000000   1.002448
17245.000000   1.002965
17495.000000   1.003491
17745.000000   1.004009
17994.000000   1.004605
18244.000000   1.005202
18494.000000   1.006025
18744.000000   1.006702
18994.000000   1.007597
Sample image effect correction factor = 1.000000, Sample holder image effect correction factor = 0.700000
Background Subtraction = Yes   Method = Straight Line
Background slope x, y, z [emu/Oe] = -1.237658E-7   -0.000000E+0   -0.000000E+0
Background Offset x, y, z [emu] = 9.062174E-7   -0.000000E+0   -0.000000E+0
Angular Sensitivity Correction = Yes
Angular Sensitivity array length = 361
0.000000   1.000026E+0   0.000000E+0   0.000000
1.000000   9.998824E-1   0.000000E+0   0.000000
2.000000   9.997501E-1   0.000000E+0   0.000000
3.000000   9.996408E-1   0.000000E+0   0.000000
4.000000   9.995661E-1   0.000000E+0   0.000000
5.000000   9.995373E-1   0.000000E+0   0.000000
6.000000   9.995662E-1   0.000000E+0   0.000000
7.000000   9.996640E-1   0.000000E+0   0.000000
8.000000   9.998424E-1   0.000000E+0   0.000000
9.000000   1.000113E+0   0.000000E+0   0.000000
10.000000   1.000487E+0   0.000000E+0   0.000000
11.000000   1.000976E+0   0.000000E+0   0.000000
12.000000   1.001591E+0   0.000000E+0   0.000000
13.000000   1.002345E+0   0.000000E+0   0.000000
14.000000   1.003248E+0   0.000000E+0   0.000000
15.000000   1.004313E+0   0.000000E+0   0.000000
16.000000   1.005547E+0   0.000000E+0   0.000000
17.000000   1.006952E+0   0.000000E+0   0.000000
18.000000   1.008524E+0   0.000000E+0   0.000000
19.000000   1.010260E+0   0.000000E+0   0.000000
20.000000   1.012158E+0   0.000000E+0   0.000000
21.000000   1.014215E+0   0.000000E+0   0.000000
22.000000   1.016429E+0   0.000000E+0   0.000000
23.000000   1.018797E+0   0.000000E+0   0.000000
24.000000   1.021316E+0   0.000000E+0   0.000000
25.000000   1.023983E+0   0.000000E+0   0.000000
26.000000   1.026796E+0   0.000000E+0   0.000000
27.000000   1.029751E+0   0.000000E+0   0.000000
28.000000   1.032848E+0   0.000000E+0   0.000000
29.000000   1.036082E+0   0.000000E+0   0.000000
30.000000   1.039451E+0   0.000000E+0   0.000000
31.000000   1.042951E+0   0.000000E+0   0.000000
32.000000   1.046574E+0   0.000000E+0   0.000000
33.000000   1.050309E+0   0.000000E+0   0.000000
34.000000   1.054148E+0   0.000000E+0   0.000000
35.000000   1.058079E+0   0.000000E+0   0.000000
36.000000   1.062094E+0   0.000000E+0   0.000000
37.000000   1.066183E+0   0.000000E+0   0.000000
38.000000   1.070335E+0   0.000000E+0   0.000000
39.000000   1.074542E+0   0.000000E+0   0.000000
40.000000   1.078793E+0   0.000000E+0   0.000000
41.000000   1.083078E+0   0.000000E+0   0.000000
42.000000   1.087388E+0   0.000000E+0   0.000000
43.000000   1.091713E+0   0.000000E+0   0.000000
44.000000   1.096043E+0   0.000000E+0   0.000000
45.000000   1.100369E+0   0.000000E+0   0.000000
46.000000   1.104681E+0   0.000000E+0   0.000000
47.000000   1.108977E+0   0.000000E+0   0.000000
48.000000   1.113255E+0   0.000000E+0   0.000000
49.000000   1.117512E+0   0.000000E+0   0.000000
50.000000   1.121748E+0   0.000000E+0   0.000000
51.000000   1.125960E+0   0.000000E+0   0.000000
52.000000   1.130146E+0   0.000000E+0   0.000000
53.000000   1.134304E+0   0.000000E+0   0.000000
54.000000   1.138432E+0   0.000000E+0   0.000000
55.000000   1.142529E+0   0.000000E+0   0.000000
56.000000   1.146593E+0   0.000000E+0   0.000000
57.000000   1.150621E+0   0.000000E+0   0.000000
58.000000   1.154612E+0   0.000000E+0   0.000000
59.000000   1.158564E+0   0.000000E+0   0.000000
60.000000   1.162475E+0   0.000000E+0   0.000000
61.000000   1.166339E+0   0.000000E+0   0.000000
62.000000   1.170133E+0   0.000000E+0   0.000000
63.000000   1.173831E+0   0.000000E+0   0.000000
64.000000   1.177406E+0   0.000000E+0   0.000000
65.000000   1.180831E+0   0.000000E+0   0.000000
66.000000   1.184079E+0   0.000000E+0   0.000000
67.000000   1.187125E+0   0.000000E+0   0.000000
68.000000   1.189940E+0   0.000000E+0   0.000000
69.000000   1.192499E+0   0.000000E+0   0.000000
70.000000   1.194775E+0   0.000000E+0   0.000000
71.000000   1.196740E+0   0.000000E+0   0.000000
72.000000   1.198369E+0   0.000000E+0   0.000000
73.000000   1.199634E+0   0.000000E+0   0.000000
74.000000   1.200509E+0   0.000000E+0   0.000000
75.000000   1.200967E+0   0.000000E+0   0.000000
76.000000   1.200994E+0   0.000000E+0   0.000000
77.000000   1.200624E+0   0.000000E+0   0.000000
78.000000   1.199905E+0   0.000000E+0   0.000000
79.000000   1.198883E+0   0.000000E+0   0.000000
80.000000   1.197605E+0   0.000000E+0   0.000000
81.000000   1.196119E+0   0.000000E+0   0.000000
82.000000   1.194472E+0   0.000000E+0   0.000000
83.000000   1.192710E+0   0.000000E+0   0.000000
84.000000   1.190880E+0   0.000000E+0   0.000000
85.000000   1.189031E+0   0.000000E+0   0.000000
86.000000   1.187207E+0   0.000000E+0   0.000000
87.000000   1.185457E+0   0.000000E+0   0.000000
88.000000   1.183828E+0   0.000000E+0   0.000000
89.000000   1.182367E+0   0.000000E+0   0.000000
90.000000   1.181120E+0   0.000000E+0   0.000000
91.000000   1.180125E+0   0.000000E+0   0.000000
92.000000   1.179386E+0   0.000000E+0   0.000000
93.000000   1.178896E+0   0.000000E+0   0.000000
94.000000   1.178648E+0   0.000000E+0   0.000000
95.000000   1.178636E+0   0.000000E+0   0.000000
96.000000   1.178854E+0   0.000000E+0   0.000000
97.000000   1.179294E+0   0.000000E+0   0.000000
98.000000   1.179952E+0   0.000000E+0   0.000000
99.000000   1.180819E+0   0.000000E+0   0.000000
100.000000   1.181891E+0   0.000000E+0   0.000000
101.000000   1.183160E+0   0.000000E+0   0.000000
102.000000   1.184620E+0   0.000000E+0   0.000000
103.000000   1.186264E+0   0.000000E+0   0.000000
104.000000   1.188087E+0   0.000000E+0   0.000000
105.000000   1.190081E+0   0.000000E+0   0.000000
106.000000   1.192236E+0   0.000000E+0   0.000000
107.000000   1.194518E+0   0.000000E+0   0.000000
108.000000   1.196891E+0   0.000000E+0   0.000000
109.000000   1.199318E+0   0.000000E+0   0.000000
110.000000   1.201761E+0   0.000000E+0   0.000000
111.000000   1.204182E+0   0.000000E+0   0.000000
112.000000   1.206545E+0   0.000000E+0   0.000000
113.000000   1.208812E+0   0.000000E+0   0.000000
114.000000   1.210946E+0   0.000000E+0   0.000000
115.000000   1.212909E+0   0.000000E+0   0.000000
116.000000   1.214664E+0   0.000000E+0   0.000000
117.000000   1.216174E+0   0.000000E+0   0.000000
118.000000   1.217402E+0   0.000000E+0   0.000000
119.000000   1.218310E+0   0.000000E+0   0.000000
120.000000   1.218860E+0   0.000000E+0   0.000000
121.000000   1.219027E+0   0.000000E+0   0.000000
122.000000   1.218821E+0   0.000000E+0   0.000000
123.000000   1.218265E+0   0.000000E+0   0.000000
124.000000   1.217382E+0   0.000000E+0   0.000000
125.000000   1.216194E+0   0.000000E+0   0.000000
126.000000   1.214723E+0   0.000000E+0   0.000000
127.000000   1.212992E+0   0.000000E+0   0.000000
128.000000   1.211022E+0   0.000000E+0   0.000000
129.000000   1.208837E+0   0.000000E+0   0.000000
130.000000   1.206459E+0   0.000000E+0   0.000000
131.000000   1.203910E+0   0.000000E+0   0.000000
132.000000   1.201212E+0   0.000000E+0   0.000000
133.000000   1.198388E+0   0.000000E+0   0.000000
134.000000   1.195459E+0   0.000000E+0   0.000000
135.000000   1.192449E+0   0.000000E+0   0.000000
136.000000   1.189376E+0   0.000000E+0   0.000000
137.000000   1.186243E+0   0.000000E+0   0.000000
138.000000   1.183050E+0   0.000000E+0   0.000000
139.000000   1.179797E+0   0.000000E+0   0.000000
140.000000   1.176482E+0   0.000000E+0   0.000000
141.000000   1.173105E+0   0.000000E+0   0.000000
142.000000   1.169667E+0   0.000000E+0   0.000000
143.000000   1.166166E+0   0.000000E+0   0.000000
144.000000   1.162602E+0   0.000000E+0   0.000000
145.000000   1.158975E+0   0.000000E+0   0.000000
146.000000   1.155283E+0   0.000000E+0   0.000000
147.000000   1.151528E+0   0.000000E+0   0.000000
148.000000   1.147707E+0   0.000000E+0   0.000000
149.000000   1.143822E+0   0.000000E+0   0.000000
150.000000   1.139870E+0   0.000000E+0   0.000000
151.000000   1.135854E+0   0.000000E+0   0.000000
152.000000   1.131784E+0   0.000000E+0   0.000000
153.000000   1.127671E+0   0.000000E+0   0.000000
154.000000   1.123527E+0   0.000000E+0   0.000000
155.000000   1.119362E+0   0.000000E+0   0.000000
156.000000   1.115190E+0   0.000000E+0   0.000000
157.000000   1.111022E+0   0.000000E+0   0.000000
158.000000   1.106868E+0   0.000000E+0   0.000000
159.000000   1.102742E+0   0.000000E+0   0.000000
160.000000   1.098653E+0   0.000000E+0   0.000000
161.000000   1.094615E+0   0.000000E+0   0.000000
162.000000   1.090639E+0   0.000000E+0   0.000000
163.000000   1.086736E+0   0.000000E+0   0.000000
164.000000   1.082918E+0   0.000000E+0   0.000000
165.000000   1.079196E+0   0.000000E+0   0.000000
166.000000   1.075581E+0   0.000000E+0   0.000000
167.000000   1.072078E+0   0.000000E+0   0.000000
168.000000   1.068691E+0   0.000000E+0   0.000000
169.000000   1.065422E+0   0.000000E+0   0.000000
170.000000   1.062276E+0   0.000000E+0   0.000000
171.000000   1.059256E+0   0.000000E+0   0.000000
172.000000   1.056366E+0   0.000000E+0   0.000000
173.000000   1.053609E+0   0.000000E+0   0.000000
174.000000   1.050989E+0   0.000000E+0   0.000000
175.000000   1.048510E+0   0.000000E+0   0.000000
176.000000   1.046174E+0   0.000000E+0   0.000000
177.000000   1.043987E+0   0.000000E+0   0.000000
178.000000   1.041950E+0   0.000000E+0   0.000000
179.000000   1.040068E+0   0.000000E+0   0.000000
180.000000   1.038345E+0   0.000000E+0   0.000000
181.000000   1.036783E+0   0.000000E+0   0.000000
182.000000   1.035385E+0   0.000000E+0   0.000000
183.000000   1.034152E+0   0.000000E+0   0.000000
184.000000   1.033086E+0   0.000000E+0   0.000000
185.000000   1.032187E+0   0.000000E+0   0.000000
186.000000   1.031459E+0   0.000000E+0   0.000000
187.000000   1.030901E+0   0.000000E+0   0.000000
188.000000   1.030516E+0   0.000000E+0   0.000000
189.000000   1.030306E+0   0.000000E+0   0.000000
190.000000   1.030271E+0   0.000000E+0   0.000000
191.000000   1.030414E+0   0.000000E+0   0.000000
192.000000   1.030736E+0   0.000000E+0   0.000000
193.000000   1.031238E+0   0.000000E+0   0.000000
194.000000   1.031922E+0   0.000000E+0   0.000000
195.000000   1.032790E+0   0.000000E+0   0.000000
196.000000   1.033841E+0   0.000000E+0   0.000000
197.000000   1.035069E+0   0.000000E+0   0.000000
198.000000   1.036465E+0   0.000000E+0   0.000000
199.000000   1.038023E+0   0.000000E+0   0.000000
200.000000   1.039733E+0   0.000000E+0   0.000000
201.000000   1.041588E+0   0.000000E+0   0.000000
202.000000   1.043579E+0   0.000000E+0   0.000000
203.000000   1.045699E+0   0.000000E+0   0.000000
204.000000   1.047938E+0   0.000000E+0   0.000000
205.000000   1.050290E+0   0.000000E+0   0.000000
206.000000   1.052746E+0   0.000000E+0   0.000000
207.000000   1.055298E+0   0.000000E+0   0.000000
208.000000   1.057938E+0   0.000000E+0   0.000000
209.000000   1.060657E+0   0.000000E+0   0.000000
210.000000   1.063448E+0   0.000000E+0   0.000000
211.000000   1.066303E+0   0.000000E+0   0.000000
212.000000   1.069213E+0   0.000000E+0   0.000000
213.000000   1.072170E+0   0.000000E+0   0.000000
214.000000   1.075167E+0   0.000000E+0   0.000000
215.000000   1.078196E+0   0.000000E+0   0.000000
216.000000   1.081247E+0   0.000000E+0   0.000000
217.000000   1.084314E+0   0.000000E+0   0.000000
218.000000   1.087389E+0   0.000000E+0   0.000000
219.000000   1.090463E+0   0.000000E+0   0.000000
220.000000   1.093528E+0   0.000000E+0   0.000000
221.000000   1.096576E+0   0.000000E+0   0.000000
222.000000   1.099599E+0   0.000000E+0   0.000000
223.000000   1.102590E+0   0.000000E+0   0.000000
224.000000   1.105540E+0   0.000000E+0   0.000000
225.000000   1.108441E+0   0.000000E+0   0.000000
226.000000   1.111288E+0   0.000000E+0   0.000000
227.000000   1.114083E+0   0.000000E+0   0.000000
228.000000   1.116834E+0   0.000000E+0   0.000000
229.000000   1.119546E+0   0.000000E+0   0.000000
230.000000   1.122224E+0   0.000000E+0   0.000000
231.000000   1.124876E+0   0.000000E+0   0.000000
232.000000   1.127507E+0   0.000000E+0   0.000000
233.000000   1.130123E+0   0.000000E+0   0.000000
234.000000   1.132730E+0   0.000000E+0   0.000000
235.000000   1.135334E+0   0.000000E+0   0.000000
236.000000   1.137940E+0   0.000000E+0   0.000000
237.000000   1.140556E+0   0.000000E+0   0.000000
238.000000   1.143186E+0   0.000000E+0   0.000000
239.000000   1.145838E+0   0.000000E+0   0.000000
240.000000   1.148516E+0   0.000000E+0   0.000000
241.000000   1.151221E+0   0.000000E+0   0.000000
242.000000   1.153928E+0   0.000000E+0   0.000000
243.000000   1.156608E+0   0.000000E+0   0.000000
244.000000   1.159229E+0   0.000000E+0   0.000000
245.000000   1.161761E+0   0.000000E+0   0.000000
246.000000   1.164173E+0   0.000000E+0   0.000000
247.000000   1.166436E+0   0.000000E+0   0.000000
248.000000   1.168519E+0   0.000000E+0   0.000000
249.000000   1.170391E+0   0.000000E+0   0.000000
250.000000   1.172022E+0   0.000000E+0   0.000000
251.000000   1.173381E+0   0.000000E+0   0.000000
252.000000   1.174439E+0   0.000000E+0   0.000000
253.000000   1.175164E+0   0.000000E+0   0.000000
254.000000   1.175526E+0   0.000000E+0   0.000000
255.000000   1.175494E+0   0.000000E+0   0.000000
256.000000   1.175054E+0   0.000000E+0   0.000000
257.000000   1.174243E+0   0.000000E+0   0.000000
258.000000   1.173118E+0   0.000000E+0   0.000000
259.000000   1.171731E+0   0.000000E+0   0.000000
260.000000   1.170138E+0   0.000000E+0   0.000000
261.000000   1.168393E+0   0.000000E+0   0.000000
262.000000   1.166549E+0   0.000000E+0   0.000000
263.000000   1.164661E+0   0.000000E+0   0.000000
264.000000   1.162784E+0   0.000000E+0   0.000000
265.000000   1.160972E+0   0.000000E+0   0.000000
266.000000   1.159278E+0   0.000000E+0   0.000000
267.000000   1.157758E+0   0.000000E+0   0.000000
268.000000   1.156464E+0   0.000000E+0   0.000000
269.000000   1.155453E+0   0.000000E+0   0.000000
270.000000   1.154778E+0   0.000000E+0   0.000000
271.000000   1.154479E+0   0.000000E+0   0.000000
272.000000   1.154546E+0   0.000000E+0   0.000000
273.000000   1.154954E+0   0.000000E+0   0.000000
274.000000   1.155676E+0   0.000000E+0   0.000000
275.000000   1.156690E+0   0.000000E+0   0.000000
276.000000   1.157968E+0   0.000000E+0   0.000000
277.000000   1.159488E+0   0.000000E+0   0.000000
278.000000   1.161223E+0   0.000000E+0   0.000000
279.000000   1.163148E+0   0.000000E+0   0.000000
280.000000   1.165240E+0   0.000000E+0   0.000000
281.000000   1.167472E+0   0.000000E+0   0.000000
282.000000   1.169820E+0   0.000000E+0   0.000000
283.000000   1.172260E+0   0.000000E+0   0.000000
284.000000   1.174765E+0   0.000000E+0   0.000000
285.000000   1.177311E+0   0.000000E+0   0.000000
286.000000   1.179873E+0   0.000000E+0   0.000000
287.000000   1.182423E+0   0.000000E+0   0.000000
288.000000   1.184933E+0   0.000000E+0   0.000000
289.000000   1.187376E+0   0.000000E+0   0.000000
290.000000   1.189723E+0   0.000000E+0   0.000000
291.000000   1.191947E+0   0.000000E+0   0.000000
292.000000   1.194019E+0   0.000000E+0   0.000000
293.000000   1.195912E+0   0.000000E+0   0.000000
294.000000   1.197597E+0   0.000000E+0   0.000000
295.000000   1.199047E+0   0.000000E+0   0.000000
296.000000   1.200234E+0   0.000000E+0   0.000000
297.000000   1.201130E+0   0.000000E+0   0.000000
298.000000   1.201706E+0   0.000000E+0   0.000000
299.000000   1.201936E+0   0.000000E+0   0.000000
300.000000   1.201791E+0   0.000000E+0   0.000000
301.000000   1.201251E+0   0.000000E+0   0.000000
302.000000   1.200329E+0   0.000000E+0   0.000000
303.000000   1.199047E+0   0.000000E+0   0.000000
304.000000   1.197426E+0   0.000000E+0   0.000000
305.000000   1.195488E+0   0.000000E+0   0.000000
306.000000   1.193253E+0   0.000000E+0   0.000000
307.000000   1.190744E+0   0.000000E+0   0.000000
308.000000   1.187980E+0   0.000000E+0   0.000000
309.000000   1.184985E+0   0.000000E+0   0.000000
310.000000   1.181778E+0   0.000000E+0   0.000000
311.000000   1.178381E+0   0.000000E+0   0.000000
312.000000   1.174816E+0   0.000000E+0   0.000000
313.000000   1.171104E+0   0.000000E+0   0.000000
314.000000   1.167266E+0   0.000000E+0   0.000000
315.000000   1.163324E+0   0.000000E+0   0.000000
316.000000   1.159296E+0   0.000000E+0   0.000000
317.000000   1.155191E+0   0.000000E+0   0.000000
318.000000   1.151016E+0   0.000000E+0   0.000000
319.000000   1.146778E+0   0.000000E+0   0.000000
320.000000   1.142484E+0   0.000000E+0   0.000000
321.000000   1.138139E+0   0.000000E+0   0.000000
322.000000   1.133751E+0   0.000000E+0   0.000000
323.000000   1.129325E+0   0.000000E+0   0.000000
324.000000   1.124870E+0   0.000000E+0   0.000000
325.000000   1.120390E+0   0.000000E+0   0.000000
326.000000   1.115894E+0   0.000000E+0   0.000000
327.000000   1.111387E+0   0.000000E+0   0.000000
328.000000   1.106877E+0   0.000000E+0   0.000000
329.000000   1.102369E+0   0.000000E+0   0.000000
330.000000   1.097870E+0   0.000000E+0   0.000000
331.000000   1.093388E+0   0.000000E+0   0.000000
332.000000   1.088932E+0   0.000000E+0   0.000000
333.000000   1.084513E+0   0.000000E+0   0.000000
334.000000   1.080140E+0   0.000000E+0   0.000000
335.000000   1.075824E+0   0.000000E+0   0.000000
336.000000   1.071575E+0   0.000000E+0   0.000000
337.000000   1.067403E+0   0.000000E+0   0.000000
338.000000   1.063319E+0   0.000000E+0   0.000000
339.000000   1.059332E+0   0.000000E+0   0.000000
340.000000   1.055454E+0   0.000000E+0   0.000000
341.000000   1.051693E+0   0.000000E+0   0.000000
342.000000   1.048060E+0   0.000000E+0   0.000000
343.000000   1.044566E+0   0.000000E+0   0.000000
344.000000   1.041221E+0   0.000000E+0   0.000000
345.000000   1.038035E+0   0.000000E+0   0.000000
346.000000   1.035014E+0   0.000000E+0   0.000000
347.000000   1.032151E+0   0.000000E+0   0.000000
348.000000   1.029434E+0   0.000000E+0   0.000000
349.000000   1.026853E+0   0.000000E+0   0.000000
350.000000   1.024396E+0   0.000000E+0   0.000000
351.000000   1.022052E+0   0.000000E+0   0.000000
352.000000   1.019809E+0   0.000000E+0   0.000000
353.000000   1.017656E+0   0.000000E+0   0.000000
354.000000   1.015583E+0   0.000000E+0   0.000000
355.000000   1.013576E+0   0.000000E+0   0.000000
356.000000   1.011627E+0   0.000000E+0   0.000000
357.000000   1.009722E+0   0.000000E+0   0.000000
358.000000   1.007851E+0   0.000000E+0   0.000000
359.000000   1.006003E+0   0.000000E+0   0.000000
360.000000   1.004166E+0   0.000000E+0   0.000000
Remove Slope = No

Remove Signal Offset = No
Remove Signal Drift = FALSE; Drift # Points = 0
Remove Field Offset = No
Field Offset Method = Automatic
Field Offset = 0.0000
Remove Field Lag = No
Field Lag Method = Automatic
Field Lag = 0.0000
Cubic Spline Interpolation = No   # Points = 0
Noise Filter = No   Filter Order = 0   Filter Type = Median
Subtract Files = No
[Demagnetizing Field Correction]
Demagnetizing Field Correction = No; Nd = 0.000   (x 4 Pi); Sample Mounted Perpendicular to Field = No
Date and time of last calibration = Tuesday, October 11, 2016  10:51:58
@@END Instrument Parameters
@@END Parameters
@@Columns
@Column Separator:    
@Column Contents: 
@Number of sections: 18
@Section 0
Column 0: Time since start, Time [s]
Column 1: Raw Temperature, Sample Temperature [degC]
Column 2: Temperature, Sample Temperature [degC]
Column 3: Temperature 2, Sample Temperature [degC]
Column 4: Raw Applied Field, Applied Field [Oe]
Column 5: Applied Field, Applied Field [Oe]
Column 6: Field Angle, Field Angle [deg]
Column 7: Raw Applied Field For Plot , Applied Field [Oe]
Column 8: Applied Field For Plot , Applied Field [Oe]
Column 9: Raw Signal Mx, Moment as measured [memu]
Column 10: Signal X direction, Moment [emu]
@@END Columns
@@End of Header.
Time_since_start   Raw_Temperature   Temperature   Temperature_2   Raw_Applied_Field   Applied_Field   Field_Angle   Raw_Applied_Field_For_Plot_   Applied_Field_For_Plot_   Raw_Signal_Mx   Signal_X_direction      
@Time at start of measurement: 10:40:46
@@Data
New Section: Section 0: 
1.537100E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.000000E+0   -9.000000E+0   -3.374266E-1   -3.394554E-4   
1.979100E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   2.297575E-2   2.207013E-5   
2.500000E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.000000E+0   9.000000E+0   4.688580E-1   4.690779E-4   
3.131700E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.900000E+1   1.900000E+1   8.550587E-1   8.565263E-4   
3.765700E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.900000E+1   2.900000E+1   1.215615E+0   1.218330E-3   
4.306600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.900000E+1   3.900000E+1   1.538419E+0   1.542380E-3   
4.846600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.900000E+1   4.900000E+1   1.834247E+0   1.839453E-3   
5.511000E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.400000E+1   7.400000E+1   2.469601E+0   2.477918E-3   
6.183100E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.900000E+1   9.900000E+1   2.995517E+0   3.006941E-3   
6.778600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.240000E+2   1.240000E+2   3.421459E+0   3.435988E-3   
7.372800E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.490000E+2   1.490000E+2   3.794141E+0   3.811774E-3   
7.967600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.740000E+2   1.740000E+2   4.111753E+0   4.132489E-3   
8.563500E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.990000E+2   1.990000E+2   4.390319E+0   4.414156E-3   
9.160000E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.240000E+2   2.240000E+2   4.638737E+0   4.665675E-3   
9.754000E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.490000E+2   2.490000E+2   4.860500E+0   4.890538E-3   
1.035000E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.740000E+2   2.740000E+2   5.061451E+0   5.094588E-3   
1.094460E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.990000E+2   2.990000E+2   5.243815E+0   5.280051E-3   
1.153980E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.240000E+2   3.240000E+2   5.409777E+0   5.449112E-3   
1.213620E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.490000E+2   3.490000E+2   5.562517E+0   5.604950E-3   
1.273250E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.740000E+2   3.740000E+2   5.703699E+0   5.749229E-3   
1.332860E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.990000E+2   3.990000E+2   5.830658E+0   5.879285E-3   
1.401740E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.240000E+2   4.240000E+2   5.947933E+0   5.999659E-3   
1.461110E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.490000E+2   4.490000E+2   6.062505E+0   6.117328E-3   
1.520680E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.740000E+2   4.740000E+2   6.165998E+0   6.223917E-3   
1.580250E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.990000E+2   4.990000E+2   6.267044E+0   6.328059E-3   
1.641730E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.240000E+2   5.240000E+2   6.360734E+0   6.424847E-3   
1.703210E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.490000E+2   5.490000E+2   6.446520E+0   6.513728E-3   
1.764610E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.740000E+2   5.740000E+2   6.526520E+0   6.596825E-3   
1.824080E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.990000E+2   5.990000E+2   6.605852E+0   6.679253E-3   
1.883480E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.240000E+2   6.240000E+2   6.678263E+0   6.754760E-3   
1.943050E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.490000E+2   6.490000E+2   6.745018E+0   6.824611E-3   
2.002480E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.730000E+2   6.730000E+2   6.812721E+0   6.895286E-3   
2.062110E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.980000E+2   6.980000E+2   6.872331E+0   6.957992E-3   
2.121620E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.240000E+2   7.240000E+2   6.929213E+0   7.018094E-3   
2.181130E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.490000E+2   7.490000E+2   6.986821E+0   7.078797E-3   
2.240550E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.740000E+2   7.740000E+2   7.037754E+0   7.132825E-3   
2.300070E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.990000E+2   7.990000E+2   7.086719E+0   7.184886E-3   
2.359400E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.240000E+2   8.240000E+2   7.135051E+0   7.236314E-3   
2.418860E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.490000E+2   8.490000E+2   7.181499E+0   7.285856E-3   
2.478230E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.740000E+2   8.740000E+2   7.224175E+0   7.331628E-3   
2.539630E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.990000E+2   8.990000E+2   7.270587E+0   7.381135E-3   
2.598970E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.240000E+2   9.240000E+2   7.310991E+0   7.424634E-3   
2.658390E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.490000E+2   9.490000E+2   7.343103E+0   7.459841E-3   
2.717830E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.740000E+2   9.740000E+2   7.381493E+0   7.501326E-3   
2.779420E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.990000E+2   9.990000E+2   7.417610E+0   7.540539E-3   
2.884780E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.499000E+3   1.499000E+3   7.890174E+0   8.074998E-3   
2.980630E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.999000E+3   1.999000E+3   8.121156E+0   8.367869E-3   
3.075180E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.499000E+3   2.499000E+3   8.241830E+0   8.550429E-3   
3.172120E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.999000E+3   2.999000E+3   8.309627E+0   8.680110E-3   
3.263640E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.499000E+3   3.499000E+3   8.344538E+0   8.776905E-3   
3.354640E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.999000E+3   3.999000E+3   8.365208E+0   8.859459E-3   
3.451780E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.499000E+3   4.499000E+3   8.367832E+0   8.923966E-3   
3.545900E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.999000E+3   4.999000E+3   8.365829E+0   8.983846E-3   
3.642370E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.499000E+3   5.499000E+3   8.352221E+0   9.032120E-3   
3.736520E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.999000E+3   5.999000E+3   8.338507E+0   9.080288E-3   
3.827710E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.499000E+3   6.499000E+3   8.322814E+0   9.126478E-3   
3.921760E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.999000E+3   6.999000E+3   8.296533E+0   9.162080E-3   
4.012740E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.500000E+3   7.500000E+3   8.266529E+0   9.194081E-3   
4.104070E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.000000E+3   8.000000E+3   8.240342E+0   9.229777E-3   
4.198600E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.499000E+3   8.499000E+3   8.212259E+0   9.263451E-3   
4.294710E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.000000E+3   9.000000E+3   8.180041E+0   9.293239E-3   
4.388580E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.500000E+3   9.500000E+3   8.143935E+0   9.319015E-3   
4.480100E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+4   1.000000E+4   8.105182E+0   9.342145E-3   
4.593280E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.099900E+4   1.099900E+4   8.030581E+0   9.391184E-3   
4.701110E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.200000E+4   1.200000E+4   7.953017E+0   9.437507E-3   
4.809210E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.299900E+4   1.299900E+4   7.874656E+0   9.482787E-3   
4.916550E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.400000E+4   1.400000E+4   7.790194E+0   9.522212E-3   
5.024520E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.499900E+4   1.499900E+4   7.693857E+0   9.549522E-3   
5.137460E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.600000E+4   1.600000E+4   7.605378E+0   9.591229E-3   
5.255480E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.699900E+4   1.699900E+4   7.501545E+0   9.621609E-3   
5.383310E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.800000E+4   1.800000E+4   7.395816E+0   9.653978E-3   
5.521550E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.899900E+4   1.899900E+4   7.280178E+0   9.680878E-3   
5.657680E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.800400E+4   1.800400E+4   7.384631E+0   9.643300E-3   
5.775910E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.700300E+4   1.700300E+4   7.490303E+0   9.610890E-3   
5.893510E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.600300E+4   1.600300E+4   7.593514E+0   9.579756E-3   
6.011050E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.500200E+4   1.500200E+4   7.680424E+0   9.536473E-3   
6.118800E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.400300E+4   1.400300E+4   7.769266E+0   9.501655E-3   
6.226460E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.300200E+4   1.300200E+4   7.856773E+0   9.465274E-3   
6.334260E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.200200E+4   1.200200E+4   7.931644E+0   9.416381E-3   
6.442160E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.100100E+4   1.100100E+4   8.006514E+0   9.367364E-3   
6.544750E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000200E+4   1.000200E+4   8.080588E+0   9.317798E-3   
6.644480E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.501000E+3   9.501000E+3   8.114340E+0   9.289544E-3   
6.738220E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.001000E+3   9.001000E+3   8.147952E+0   9.261273E-3   
6.834440E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.501000E+3   8.501000E+3   8.174818E+0   9.226257E-3   
6.931110E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.002000E+3   8.002000E+3   8.201871E+0   9.191552E-3   
7.027520E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.501000E+3   7.501000E+3   8.228139E+0   9.155814E-3   
7.121060E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.000000E+3   7.000000E+3   8.259022E+0   9.124691E-3   
7.214960E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.501000E+3   6.501000E+3   8.284693E+0   9.088604E-3   
7.305720E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.001000E+3   6.001000E+3   8.293231E+0   9.035259E-3   
7.399120E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.501000E+3   5.501000E+3   8.311278E+0   8.991423E-3   
7.489830E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.000000E+3   5.000000E+3   8.318972E+0   8.937111E-3   
7.581220E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.501000E+3   4.501000E+3   8.324371E+0   8.880751E-3   
7.677510E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.001000E+3   4.001000E+3   8.315740E+0   8.810237E-3   
7.770910E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.501000E+3   3.501000E+3   8.296369E+0   8.728983E-3   
7.861620E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.001000E+3   3.001000E+3   8.257628E+0   8.628358E-3   
7.954890E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.500000E+3   2.500000E+3   8.191483E+0   8.500204E-3   
8.048630E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.001000E+3   2.001000E+3   8.066722E+0   8.313681E-3   
8.139390E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.500000E+3   1.500000E+3   7.840354E+0   8.025300E-3   
8.230480E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+3   1.000000E+3   7.366994E+0   7.490045E-3   
8.296830E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.740000E+2   9.740000E+2   7.326684E+0   7.446516E-3   
8.354800E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.490000E+2   9.490000E+2   7.290566E+0   7.407303E-3   
8.412800E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.240000E+2   9.240000E+2   7.250431E+0   7.364073E-3   
8.470770E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.990000E+2   8.990000E+2   7.212299E+0   7.322846E-3   
8.528780E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.740000E+2   8.740000E+2   7.167445E+0   7.274896E-3   
8.586760E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.490000E+2   8.490000E+2   7.123621E+0   7.227977E-3   
8.644740E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.240000E+2   8.240000E+2   7.077537E+0   7.178798E-3   
8.702720E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.990000E+2   7.990000E+2   7.027460E+0   7.125625E-3   
8.760800E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.740000E+2   7.740000E+2   6.974829E+0   7.069899E-3   
8.818880E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.490000E+2   7.490000E+2   6.925981E+0   7.017955E-3   
8.876980E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.240000E+2   7.240000E+2   6.870399E+0   6.959278E-3   
8.935000E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.990000E+2   6.990000E+2   6.809243E+0   6.895026E-3   
8.993080E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.740000E+2   6.740000E+2   6.746938E+0   6.829626E-3   
9.051150E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.490000E+2   6.490000E+2   6.679657E+0   6.759248E-3   
9.109250E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.240000E+2   6.240000E+2   6.611591E+0   6.688086E-3   
9.167280E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.990000E+2   5.990000E+2   6.538828E+0   6.612228E-3   
9.225370E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.740000E+2   5.740000E+2   6.462904E+0   6.533207E-3   
9.283420E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.490000E+2   5.490000E+2   6.379941E+0   6.447148E-3   
9.341520E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.240000E+2   5.240000E+2   6.295725E+0   6.359835E-3   
9.399310E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.990000E+2   4.990000E+2   6.200629E+0   6.261643E-3   
9.457210E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.740000E+2   4.740000E+2   6.103073E+0   6.160991E-3   
9.515080E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.490000E+2   4.490000E+2   5.999498E+0   6.054319E-3   
9.573050E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.240000E+2   4.240000E+2   5.888054E+0   5.939777E-3   
9.631060E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.990000E+2   3.990000E+2   5.765999E+0   5.814626E-3   
9.689210E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.740000E+2   3.740000E+2   5.637037E+0   5.682565E-3   
9.747230E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.490000E+2   3.490000E+2   5.499258E+0   5.541689E-3   
9.805290E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.240000E+2   3.240000E+2   5.347345E+0   5.386678E-3   
9.863180E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.990000E+2   2.990000E+2   5.181036E+0   5.217271E-3   
9.921110E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.740000E+2   2.740000E+2   5.001811E+0   5.034947E-3   
9.979120E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.490000E+2   2.490000E+2   4.803129E+0   4.833165E-3   
1.003728E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.240000E+2   2.240000E+2   4.583157E+0   4.610094E-3   
1.009519E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.990000E+2   1.990000E+2   4.340408E+0   4.364244E-3   
1.015319E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.740000E+2   1.740000E+2   4.061277E+0   4.082012E-3   
1.021116E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.490000E+2   1.490000E+2   3.747068E+0   3.764701E-3   
1.026916E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.240000E+2   1.240000E+2   3.382061E+0   3.396589E-3   
1.032631E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.900000E+1   9.900000E+1   2.951105E+0   2.962528E-3   
1.038336E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.400000E+1   7.400000E+1   2.444056E+0   2.452372E-3   
1.044026E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.900000E+1   4.900000E+1   1.810841E+0   1.816046E-3   
1.049417E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.000000E+1   4.000000E+1   1.548366E+0   1.552451E-3   
1.053981E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.000000E+1   3.000000E+1   1.228923E+0   1.231761E-3   
1.059277E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.900000E+1   1.900000E+1   8.499654E-1   8.514329E-4   
1.063807E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+1   1.000000E+1   5.046929E-1   5.050375E-4   
1.068224E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   1.009557E-1   1.000521E-4   
1.073426E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.000000E+0   -9.000000E+0   -3.392535E-1   -3.412824E-4   
1.078826E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.900000E+1   -1.900000E+1   -7.285050E-1   -7.317817E-4   
1.084190E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.800000E+1   -2.800000E+1   -1.090972E+0   -1.095372E-3   
1.089560E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.900000E+1   -3.900000E+1   -1.418270E+0   -1.424040E-3   
1.094966E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.900000E+1   -4.900000E+1   -1.719216E+0   -1.726231E-3   
1.101614E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.300000E+1   -7.300000E+1   -2.361253E+0   -2.371255E-3   
1.107663E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.900000E+1   -9.900000E+1   -2.882171E+0   -2.895405E-3   
1.113619E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.240000E+2   -1.240000E+2   -3.318277E+0   -3.334617E-3   
1.119568E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.490000E+2   -1.490000E+2   -3.687035E+0   -3.706478E-3   
1.125524E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.740000E+2   -1.740000E+2   -4.006479E+0   -4.029025E-3   
1.131476E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.990000E+2   -1.990000E+2   -4.289452E+0   -4.315100E-3   
1.137432E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.240000E+2   -2.240000E+2   -4.536475E+0   -4.565222E-3   
1.143395E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.490000E+2   -2.490000E+2   -4.753566E+0   -4.785414E-3   
1.149347E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.730000E+2   -2.730000E+2   -4.956963E+0   -4.991786E-3   
1.155312E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.980000E+2   -2.980000E+2   -5.136360E+0   -5.174282E-3   
1.161267E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.240000E+2   -3.240000E+2   -5.302757E+0   -5.343901E-3   
1.167239E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.490000E+2   -3.490000E+2   -5.454670E+0   -5.498913E-3   
1.173206E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.740000E+2   -3.740000E+2   -5.594281E+0   -5.641621E-3   
1.179175E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.990000E+2   -3.990000E+2   -5.724029E+0   -5.774467E-3   
1.185139E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.240000E+2   -4.240000E+2   -5.845750E+0   -5.899285E-3   
1.191106E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.490000E+2   -4.490000E+2   -5.957092E+0   -6.013724E-3   
1.197060E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.740000E+2   -4.740000E+2   -6.063196E+0   -6.122925E-3   
1.203027E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.990000E+2   -4.990000E+2   -6.159522E+0   -6.222347E-3   
1.208982E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.230000E+2   -5.230000E+2   -6.250624E+0   -6.316423E-3   
1.214939E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.490000E+2   -5.490000E+2   -6.339185E+0   -6.408204E-3   
1.220893E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.740000E+2   -5.740000E+2   -6.418764E+0   -6.490878E-3   
1.226846E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.990000E+2   -5.990000E+2   -6.497557E+0   -6.572768E-3   
1.232804E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.240000E+2   -6.240000E+2   -6.569980E+0   -6.648287E-3   
1.238728E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.490000E+2   -6.490000E+2   -6.638995E+0   -6.720398E-3   
1.244896E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.740000E+2   -6.740000E+2   -6.701475E+0   -6.785974E-3   
1.250807E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.990000E+2   -6.990000E+2   -6.763955E+0   -6.851549E-3   
1.256723E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.240000E+2   -7.240000E+2   -6.820298E+0   -6.910988E-3   
1.262896E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.490000E+2   -7.490000E+2   -6.878515E+0   -6.972301E-3   
1.268807E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.740000E+2   -7.740000E+2   -6.930326E+0   -7.027207E-3   
1.274721E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.990000E+2   -7.990000E+2   -6.980942E+0   -7.080919E-3   
1.280885E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.240000E+2   -8.240000E+2   -7.028514E+0   -7.131586E-3   
1.286790E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.490000E+2   -8.490000E+2   -7.074691E+0   -7.180859E-3   
1.292696E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.740000E+2   -8.740000E+2   -7.116466E+0   -7.225728E-3   
1.298863E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.990000E+2   -8.990000E+2   -7.160289E+0   -7.272647E-3   
1.304767E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.240000E+2   -9.240000E+2   -7.198691E+0   -7.314144E-3   
1.310672E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.490000E+2   -9.490000E+2   -7.239165E+0   -7.357713E-3   
1.316838E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.740000E+2   -9.740000E+2   -7.273550E+0   -7.395193E-3   
1.323012E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.990000E+2   -9.990000E+2   -7.308531E+0   -7.433269E-3   
1.333562E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.498000E+3   -1.498000E+3   -7.782863E+0   -7.969373E-3   
1.343030E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.998000E+3   -1.998000E+3   -8.008505E+0   -8.256904E-3   
1.352490E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.498000E+3   -2.498000E+3   -8.128406E+0   -8.438690E-3   
1.362187E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.998000E+3   -2.998000E+3   -8.195593E+0   -8.567763E-3   
1.371651E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.498000E+3   -3.498000E+3   -8.230399E+0   -8.664452E-3   
1.381357E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.998000E+3   -3.998000E+3   -8.250309E+0   -8.746245E-3   
1.391560E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.499000E+3   -4.499000E+3   -8.250297E+0   -8.808240E-3   
1.400981E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.999000E+3   -4.999000E+3   -8.247510E+0   -8.867336E-3   
1.410410E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.498000E+3   -5.498000E+3   -8.238422E+0   -8.920007E-3   
1.420137E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.999000E+3   -5.999000E+3   -8.219321E+0   -8.962912E-3   
1.429564E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.499000E+3   -6.499000E+3   -8.204412E+0   -9.009886E-3   
1.438987E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.999000E+3   -6.999000E+3   -8.182770E+0   -9.050125E-3   
1.448413E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.499000E+3   -7.499000E+3   -8.154756E+0   -9.083994E-3   
1.457833E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.998000E+3   -7.998000E+3   -8.124998E+0   -9.115994E-3   
1.467255E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.499000E+3   -8.499000E+3   -8.093576E+0   -9.146578E-3   
1.476921E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.999000E+3   -8.999000E+3   -8.058243E+0   -9.173127E-3   
1.486594E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.499000E+3   -9.499000E+3   -8.024831E+0   -9.201597E-3   
1.496014E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.999000E+3   -9.999000E+3   -7.989919E+0   -9.228567E-3   
1.506858E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.099900E+4   -1.099900E+4   -7.919429E+0   -9.281841E-3   
1.517692E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.199900E+4   -1.199900E+4   -7.841666E+0   -9.327842E-3   
1.528226E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.299900E+4   -1.299900E+4   -7.758164E+0   -9.368103E-3   
1.539044E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.399800E+4   -1.399800E+4   -7.671008E+0   -9.404588E-3   
1.550374E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.499900E+4   -1.499900E+4   -7.581136E+0   -9.438610E-3   
1.562206E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.599900E+4   -1.599900E+4   -7.480875E+0   -9.468289E-3   
1.574521E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.700000E+4   -1.700000E+4   -7.386985E+0   -9.508715E-3   
1.587365E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.799900E+4   -1.799900E+4   -7.282544E+0   -9.541853E-3   
1.600707E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.899900E+4   -1.899900E+4   -7.169096E+0   -9.570762E-3   
1.614848E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.800300E+4   -1.800300E+4   -7.273116E+0   -9.532939E-3   
1.627148E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.700300E+4   -1.700300E+4   -7.378003E+0   -9.500123E-3   
1.639446E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.600100E+4   -1.600100E+4   -7.473637E+0   -9.461312E-3   
1.650228E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.500300E+4   -1.500300E+4   -7.568663E+0   -9.426649E-3   
1.661531E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.400100E+4   -1.400100E+4   -7.662096E+0   -9.396046E-3   
1.672825E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.300200E+4   -1.300200E+4   -7.737564E+0   -9.347874E-3   
1.683618E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.200100E+4   -1.200100E+4   -7.823958E+0   -9.310381E-3   
1.694425E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.100200E+4   -1.100200E+4   -7.900480E+0   -9.263263E-3   
1.705208E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.000100E+4   -1.000100E+4   -7.970631E+0   -9.209526E-3   
1.715158E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.501000E+3   -9.501000E+3   -8.007381E+0   -9.184394E-3   
1.724547E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.001000E+3   -9.001000E+3   -8.034692E+0   -9.149823E-3   
1.733952E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.501000E+3   -8.501000E+3   -8.072297E+0   -9.125546E-3   
1.743264E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.000000E+3   -8.000000E+3   -8.098389E+0   -9.089633E-3   
1.752648E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.500000E+3   -7.500000E+3   -8.125595E+0   -9.054956E-3   
1.762285E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.001000E+3   -7.001000E+3   -8.154662E+0   -9.022265E-3   
1.771673E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.500000E+3   -6.500000E+3   -8.174806E+0   -8.980402E-3   
1.780749E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.000000E+3   -6.000000E+3   -8.195839E+0   -8.939553E-3   
1.789834E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.500000E+3   -5.500000E+3   -8.209635E+0   -8.891467E-3   
1.799166E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.000000E+3   -5.000000E+3   -8.222822E+0   -8.842771E-3   
1.808260E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.500000E+3   -4.500000E+3   -8.220726E+0   -8.778792E-3   
1.817337E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.000000E+3   -4.000000E+3   -8.220796E+0   -8.716979E-3   
1.826407E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.500000E+3   -3.500000E+3   -8.199692E+0   -8.633992E-3   
1.835482E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.000000E+3   -3.000000E+3   -8.161455E+0   -8.533871E-3   
1.844818E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.500000E+3   -2.500000E+3   -8.094970E+0   -8.405501E-3   
1.853886E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.000000E+3   -2.000000E+3   -7.971333E+0   -8.219978E-3   
1.862974E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.500000E+3   -1.500000E+3   -7.744028E+0   -7.930785E-3   
1.872307E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.000000E+3   -1.000000E+3   -7.278094E+0   -7.402955E-3   
1.878992E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.750000E+2   -9.750000E+2   -7.240828E+0   -7.362594E-3   
1.884777E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.490000E+2   -9.490000E+2   -7.203399E+0   -7.321946E-3   
1.890552E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.250000E+2   -9.250000E+2   -7.163615E+0   -7.279191E-3   
1.896392E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.000000E+2   -9.000000E+2   -7.124664E+0   -7.237144E-3   
1.902229E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.750000E+2   -8.750000E+2   -7.082959E+0   -7.192345E-3   
1.908013E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.490000E+2   -8.490000E+2   -7.039171E+0   -7.145337E-3   
1.913798E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.240000E+2   -8.240000E+2   -6.991939E+0   -7.095010E-3   
1.919556E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.990000E+2   -7.990000E+2   -6.942927E+0   -7.042903E-3   
1.925352E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.740000E+2   -7.740000E+2   -6.891070E+0   -6.987950E-3   
1.931160E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.490000E+2   -7.490000E+2   -6.840477E+0   -6.934261E-3   
1.936957E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.240000E+2   -7.240000E+2   -6.783665E+0   -6.874354E-3   
1.942712E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.000000E+2   -7.000000E+2   -6.726338E+0   -6.814055E-3   
1.948569E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.750000E+2   -6.750000E+2   -6.663694E+0   -6.748316E-3   
1.954377E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.490000E+2   -6.490000E+2   -6.598767E+0   -6.680168E-3   
1.960191E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.240000E+2   -6.240000E+2   -6.531146E+0   -6.609451E-3   
1.965988E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.990000E+2   -5.990000E+2   -6.457329E+0   -6.532539E-3   
1.971805E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.740000E+2   -5.740000E+2   -6.379507E+0   -6.451621E-3   
1.977624E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.490000E+2   -5.490000E+2   -6.297926E+0   -6.366944E-3   
1.983439E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.240000E+2   -5.240000E+2   -6.212141E+0   -6.278062E-3   
1.989231E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.990000E+2   -4.990000E+2   -6.120886E+0   -6.183711E-3   
1.995051E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.740000E+2   -4.740000E+2   -6.025580E+0   -6.085307E-3   
2.000871E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.490000E+2   -4.490000E+2   -5.919662E+0   -5.976293E-3   
2.006694E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.240000E+2   -4.240000E+2   -5.810673E+0   -5.864207E-3   
2.012513E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.990000E+2   -3.990000E+2   -5.687730E+0   -5.738167E-3   
2.018331E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.740000E+2   -3.740000E+2   -5.560162E+0   -5.607502E-3   
2.024158E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.490000E+2   -3.490000E+2   -5.420291E+0   -5.464532E-3   
2.029975E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.240000E+2   -3.240000E+2   -5.269686E+0   -5.310830E-3   
2.035791E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.990000E+2   -2.990000E+2   -5.107043E+0   -5.145088E-3   
2.041607E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.740000E+2   -2.740000E+2   -4.923804E+0   -4.958750E-3   
2.047432E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.490000E+2   -2.490000E+2   -4.727653E+0   -4.759499E-3   
2.053256E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.240000E+2   -2.240000E+2   -4.507680E+0   -4.536427E-3   
2.059072E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.990000E+2   -1.990000E+2   -4.263100E+0   -4.288746E-3   
2.064894E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.740000E+2   -1.740000E+2   -3.984142E+0   -4.006687E-3   
2.070720E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.490000E+2   -1.490000E+2   -3.669061E+0   -3.688503E-3   
2.076546E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.240000E+2   -1.240000E+2   -3.300738E+0   -3.317077E-3   
2.082265E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.900000E+1   -9.900000E+1   -2.870830E+0   -2.884064E-3   
2.087939E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.400000E+1   -7.400000E+1   -2.352614E+0   -2.362741E-3   
2.093597E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.900000E+1   -4.900000E+1   -1.713017E+0   -1.720032E-3   
2.099002E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.000000E+1   -4.000000E+1   -1.449853E+0   -1.455748E-3   
2.103573E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.000000E+1   -3.000000E+1   -1.121859E+0   -1.126507E-3   
2.108136E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.000000E+1   -2.000000E+1   -7.699514E-1   -7.733529E-4   
2.112673E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.000000E+1   -1.000000E+1   -3.875061E-1   -3.896601E-4   
2.117093E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   1.483365E-2   1.392782E-5   
2.122285E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.000000E+0   9.000000E+0   4.452701E-1   4.454894E-4   
2.127672E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.900000E+1   1.900000E+1   8.256223E-1   8.270891E-4   
2.133073E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.900000E+1   2.900000E+1   1.173863E+0   1.176577E-3   
2.138482E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.900000E+1   3.900000E+1   1.490431E+0   1.494390E-3   
2.143883E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.900000E+1   4.900000E+1   1.780555E+0   1.785760E-3   
2.150527E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.400000E+1   7.400000E+1   2.403221E+0   2.411536E-3   
2.156322E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.900000E+1   9.900000E+1   2.908960E+0   2.920382E-3   
2.162272E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.240000E+2   1.240000E+2   3.330058E+0   3.344585E-3   
2.168227E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.490000E+2   1.490000E+2   3.692182E+0   3.709813E-3   
2.174185E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.740000E+2   1.740000E+2   4.001245E+0   4.021978E-3   
2.180148E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.990000E+2   1.990000E+2   4.277499E+0   4.301333E-3   
2.186100E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.240000E+2   2.240000E+2   4.517713E+0   4.544648E-3   
2.192255E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.490000E+2   2.490000E+2   4.733149E+0   4.763183E-3   
2.198217E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.740000E+2   2.740000E+2   4.928778E+0   4.961912E-3   
2.204178E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.990000E+2   2.990000E+2   5.105646E+0   5.141878E-3   
2.210130E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.240000E+2   3.240000E+2   5.269948E+0   5.309279E-3   
2.216094E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.490000E+2   3.490000E+2   5.417588E+0   5.460016E-3   
2.222057E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.740000E+2   3.740000E+2   5.556325E+0   5.601851E-3   
2.228020E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.990000E+2   3.990000E+2   5.684415E+0   5.733039E-3   
2.233976E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.240000E+2   4.240000E+2   5.800903E+0   5.852624E-3   
2.239928E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.490000E+2   4.490000E+2   5.910855E+0   5.965674E-3   
2.245885E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.740000E+2   4.740000E+2   6.015824E+0   6.073739E-3   
2.251843E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.990000E+2   4.990000E+2   6.109608E+0   6.170620E-3   
2.257806E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.240000E+2   5.240000E+2   6.200465E+0   6.264573E-3   
2.263954E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.490000E+2   5.490000E+2   6.284833E+0   6.352038E-3   
2.269903E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.740000E+2   5.740000E+2   6.366320E+0   6.436621E-3   
2.276049E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.990000E+2   5.990000E+2   6.439013E+0   6.512409E-3   
2.281987E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.240000E+2   6.240000E+2   6.513953E+0   6.590446E-3   
2.287941E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.480000E+2   6.480000E+2   6.580368E+0   6.659833E-3   
2.293882E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.730000E+2   6.730000E+2   6.642918E+0   6.725479E-3   
2.299835E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.980000E+2   6.980000E+2   6.708115E+0   6.793772E-3   
2.305786E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.240000E+2   7.240000E+2   6.761425E+0   6.850301E-3   
2.311739E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.490000E+2   7.490000E+2   6.818647E+0   6.910618E-3   
2.317682E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.740000E+2   7.740000E+2   6.873713E+0   6.968781E-3   
2.323634E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.990000E+2   7.990000E+2   6.922315E+0   7.020478E-3   
2.329568E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.240000E+2   8.240000E+2   6.969172E+0   7.070430E-3   
2.335513E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.490000E+2   8.490000E+2   7.012282E+0   7.116635E-3   
2.341447E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.740000E+2   8.740000E+2   7.057148E+0   7.164596E-3   
2.347583E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.990000E+2   8.990000E+2   7.100491E+0   7.211035E-3   
2.353516E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.240000E+2   9.240000E+2   7.137148E+0   7.250787E-3   
2.359462E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.490000E+2   9.490000E+2   7.173102E+0   7.289836E-3   
2.365400E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.740000E+2   9.740000E+2   7.213166E+0   7.332995E-3   
2.371558E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.990000E+2   9.990000E+2   7.247550E+0   7.370475E-3   
2.382095E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.499000E+3   1.499000E+3   7.713755E+0   7.898574E-3   
2.391197E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.999000E+3   1.999000E+3   7.935907E+0   8.182615E-3   
2.400651E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.499000E+3   2.499000E+3   8.055538E+0   8.364132E-3   
2.410335E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.999000E+3   2.999000E+3   8.117842E+0   8.488320E-3   
2.419921E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.499000E+3   3.499000E+3   8.157707E+0   8.590070E-3   
2.429016E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.999000E+3   3.999000E+3   8.170625E+0   8.664871E-3   
2.438678E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.499000E+3   4.499000E+3   8.172475E+0   8.728604E-3   
2.448085E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.999000E+3   4.999000E+3   8.169231E+0   8.787243E-3   
2.457202E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.499000E+3   5.499000E+3   8.153620E+0   8.833514E-3   
2.466615E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.999000E+3   5.999000E+3   8.140094E+0   8.881870E-3   
2.475726E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.499000E+3   6.499000E+3   8.129624E+0   8.933283E-3   
2.484840E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.999000E+3   6.999000E+3   8.101259E+0   8.966800E-3   
2.493937E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.500000E+3   7.500000E+3   8.073421E+0   9.000968E-3   
2.503071E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.000000E+3   8.000000E+3   8.042890E+0   9.032319E-3   
2.512480E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.499000E+3   8.499000E+3   8.014958E+0   9.066146E-3   
2.521842E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.999000E+3   8.999000E+3   7.980855E+0   9.093924E-3   
2.531181E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.500000E+3   9.500000E+3   7.945065E+0   9.120140E-3   
2.540334E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+4   1.000000E+4   7.913058E+0   9.150015E-3   
2.551653E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.099900E+4   1.099900E+4   7.838258E+0   9.198855E-3   
2.562430E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.200000E+4   1.200000E+4   7.759300E+0   9.243785E-3   
2.573245E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.299900E+4   1.299900E+4   7.675974E+0   9.284099E-3   
2.583982E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.400000E+4   1.400000E+4   7.591079E+0   9.323091E-3   
2.594788E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.499900E+4   1.499900E+4   7.499121E+0   9.354781E-3   
2.606059E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.600000E+4   1.600000E+4   7.402948E+0   9.388611E-3   
2.618358E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.700000E+4   1.700000E+4   7.307220E+0   9.426938E-3   
2.631349E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.800000E+4   1.800000E+4   7.201993E+0   9.459255E-3   
2.645173E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.899900E+4   1.899900E+4   7.089061E+0   9.488304E-3   
@@END Data.
@Time at end of measurement: 11:24:54
@Instrument  Changes:
@Emu Range: 200 uV
@END Instrument  Changes:
@@Final Manipulated Data
New Section: Section 0: 
1.537100E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.000000E+0   -9.000000E+0   -3.374266E-1   -3.394554E-4   
1.979100E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   2.297575E-2   2.207013E-5   
2.500000E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.000000E+0   9.000000E+0   4.688580E-1   4.690779E-4   
3.131700E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.900000E+1   1.900000E+1   8.550587E-1   8.565263E-4   
3.765700E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.900000E+1   2.900000E+1   1.215615E+0   1.218330E-3   
4.306600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.900000E+1   3.900000E+1   1.538419E+0   1.542380E-3   
4.846600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.900000E+1   4.900000E+1   1.834247E+0   1.839453E-3   
5.511000E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.400000E+1   7.400000E+1   2.469601E+0   2.477918E-3   
6.183100E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.900000E+1   9.900000E+1   2.995517E+0   3.006941E-3   
6.778600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.240000E+2   1.240000E+2   3.421459E+0   3.435988E-3   
7.372800E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.490000E+2   1.490000E+2   3.794141E+0   3.811774E-3   
7.967600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.740000E+2   1.740000E+2   4.111753E+0   4.132489E-3   
8.563500E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.990000E+2   1.990000E+2   4.390319E+0   4.414156E-3   
9.160000E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.240000E+2   2.240000E+2   4.638737E+0   4.665675E-3   
9.754000E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.490000E+2   2.490000E+2   4.860500E+0   4.890538E-3   
1.035000E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.740000E+2   2.740000E+2   5.061451E+0   5.094588E-3   
1.094460E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.990000E+2   2.990000E+2   5.243815E+0   5.280051E-3   
1.153980E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.240000E+2   3.240000E+2   5.409777E+0   5.449112E-3   
1.213620E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.490000E+2   3.490000E+2   5.562517E+0   5.604950E-3   
1.273250E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.740000E+2   3.740000E+2   5.703699E+0   5.749229E-3   
1.332860E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.990000E+2   3.990000E+2   5.830658E+0   5.879285E-3   
1.401740E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.240000E+2   4.240000E+2   5.947933E+0   5.999659E-3   
1.461110E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.490000E+2   4.490000E+2   6.062505E+0   6.117328E-3   
1.520680E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.740000E+2   4.740000E+2   6.165998E+0   6.223917E-3   
1.580250E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.990000E+2   4.990000E+2   6.267044E+0   6.328059E-3   
1.641730E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.240000E+2   5.240000E+2   6.360734E+0   6.424847E-3   
1.703210E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.490000E+2   5.490000E+2   6.446520E+0   6.513728E-3   
1.764610E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.740000E+2   5.740000E+2   6.526520E+0   6.596825E-3   
1.824080E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.990000E+2   5.990000E+2   6.605852E+0   6.679253E-3   
1.883480E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.240000E+2   6.240000E+2   6.678263E+0   6.754760E-3   
1.943050E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.490000E+2   6.490000E+2   6.745018E+0   6.824611E-3   
2.002480E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.730000E+2   6.730000E+2   6.812721E+0   6.895286E-3   
2.062110E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.980000E+2   6.980000E+2   6.872331E+0   6.957992E-3   
2.121620E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.240000E+2   7.240000E+2   6.929213E+0   7.018094E-3   
2.181130E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.490000E+2   7.490000E+2   6.986821E+0   7.078797E-3   
2.240550E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.740000E+2   7.740000E+2   7.037754E+0   7.132825E-3   
2.300070E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.990000E+2   7.990000E+2   7.086719E+0   7.184886E-3   
2.359400E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.240000E+2   8.240000E+2   7.135051E+0   7.236314E-3   
2.418860E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.490000E+2   8.490000E+2   7.181499E+0   7.285856E-3   
2.478230E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.740000E+2   8.740000E+2   7.224175E+0   7.331628E-3   
2.539630E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.990000E+2   8.990000E+2   7.270587E+0   7.381135E-3   
2.598970E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.240000E+2   9.240000E+2   7.310991E+0   7.424634E-3   
2.658390E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.490000E+2   9.490000E+2   7.343103E+0   7.459841E-3   
2.717830E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.740000E+2   9.740000E+2   7.381493E+0   7.501326E-3   
2.779420E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.990000E+2   9.990000E+2   7.417610E+0   7.540539E-3   
2.884780E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.499000E+3   1.499000E+3   7.890174E+0   8.074998E-3   
2.980630E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.999000E+3   1.999000E+3   8.121156E+0   8.367869E-3   
3.075180E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.499000E+3   2.499000E+3   8.241830E+0   8.550429E-3   
3.172120E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.999000E+3   2.999000E+3   8.309627E+0   8.680110E-3   
3.263640E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.499000E+3   3.499000E+3   8.344538E+0   8.776905E-3   
3.354640E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.999000E+3   3.999000E+3   8.365208E+0   8.859459E-3   
3.451780E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.499000E+3   4.499000E+3   8.367832E+0   8.923966E-3   
3.545900E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.999000E+3   4.999000E+3   8.365829E+0   8.983846E-3   
3.642370E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.499000E+3   5.499000E+3   8.352221E+0   9.032120E-3   
3.736520E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.999000E+3   5.999000E+3   8.338507E+0   9.080288E-3   
3.827710E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.499000E+3   6.499000E+3   8.322814E+0   9.126478E-3   
3.921760E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.999000E+3   6.999000E+3   8.296533E+0   9.162080E-3   
4.012740E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.500000E+3   7.500000E+3   8.266529E+0   9.194081E-3   
4.104070E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.000000E+3   8.000000E+3   8.240342E+0   9.229777E-3   
4.198600E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.499000E+3   8.499000E+3   8.212259E+0   9.263451E-3   
4.294710E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.000000E+3   9.000000E+3   8.180041E+0   9.293239E-3   
4.388580E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.500000E+3   9.500000E+3   8.143935E+0   9.319015E-3   
4.480100E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+4   1.000000E+4   8.105182E+0   9.342145E-3   
4.593280E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.099900E+4   1.099900E+4   8.030581E+0   9.391184E-3   
4.701110E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.200000E+4   1.200000E+4   7.953017E+0   9.437507E-3   
4.809210E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.299900E+4   1.299900E+4   7.874656E+0   9.482787E-3   
4.916550E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.400000E+4   1.400000E+4   7.790194E+0   9.522212E-3   
5.024520E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.499900E+4   1.499900E+4   7.693857E+0   9.549522E-3   
5.137460E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.600000E+4   1.600000E+4   7.605378E+0   9.591229E-3   
5.255480E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.699900E+4   1.699900E+4   7.501545E+0   9.621609E-3   
5.383310E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.800000E+4   1.800000E+4   7.395816E+0   9.653978E-3   
5.521550E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.899900E+4   1.899900E+4   7.280178E+0   9.680878E-3   
5.657680E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.800400E+4   1.800400E+4   7.384631E+0   9.643300E-3   
5.775910E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.700300E+4   1.700300E+4   7.490303E+0   9.610890E-3   
5.893510E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.600300E+4   1.600300E+4   7.593514E+0   9.579756E-3   
6.011050E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.500200E+4   1.500200E+4   7.680424E+0   9.536473E-3   
6.118800E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.400300E+4   1.400300E+4   7.769266E+0   9.501655E-3   
6.226460E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.300200E+4   1.300200E+4   7.856773E+0   9.465274E-3   
6.334260E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.200200E+4   1.200200E+4   7.931644E+0   9.416381E-3   
6.442160E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.100100E+4   1.100100E+4   8.006514E+0   9.367364E-3   
6.544750E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000200E+4   1.000200E+4   8.080588E+0   9.317798E-3   
6.644480E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.501000E+3   9.501000E+3   8.114340E+0   9.289544E-3   
6.738220E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.001000E+3   9.001000E+3   8.147952E+0   9.261273E-3   
6.834440E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.501000E+3   8.501000E+3   8.174818E+0   9.226257E-3   
6.931110E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.002000E+3   8.002000E+3   8.201871E+0   9.191552E-3   
7.027520E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.501000E+3   7.501000E+3   8.228139E+0   9.155814E-3   
7.121060E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.000000E+3   7.000000E+3   8.259022E+0   9.124691E-3   
7.214960E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.501000E+3   6.501000E+3   8.284693E+0   9.088604E-3   
7.305720E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.001000E+3   6.001000E+3   8.293231E+0   9.035259E-3   
7.399120E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.501000E+3   5.501000E+3   8.311278E+0   8.991423E-3   
7.489830E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.000000E+3   5.000000E+3   8.318972E+0   8.937111E-3   
7.581220E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.501000E+3   4.501000E+3   8.324371E+0   8.880751E-3   
7.677510E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.001000E+3   4.001000E+3   8.315740E+0   8.810237E-3   
7.770910E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.501000E+3   3.501000E+3   8.296369E+0   8.728983E-3   
7.861620E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.001000E+3   3.001000E+3   8.257628E+0   8.628358E-3   
7.954890E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.500000E+3   2.500000E+3   8.191483E+0   8.500204E-3   
8.048630E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.001000E+3   2.001000E+3   8.066722E+0   8.313681E-3   
8.139390E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.500000E+3   1.500000E+3   7.840354E+0   8.025300E-3   
8.230480E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+3   1.000000E+3   7.366994E+0   7.490045E-3   
8.296830E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.740000E+2   9.740000E+2   7.326684E+0   7.446516E-3   
8.354800E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.490000E+2   9.490000E+2   7.290566E+0   7.407303E-3   
8.412800E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.240000E+2   9.240000E+2   7.250431E+0   7.364073E-3   
8.470770E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.990000E+2   8.990000E+2   7.212299E+0   7.322846E-3   
8.528780E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.740000E+2   8.740000E+2   7.167445E+0   7.274896E-3   
8.586760E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.490000E+2   8.490000E+2   7.123621E+0   7.227977E-3   
8.644740E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.240000E+2   8.240000E+2   7.077537E+0   7.178798E-3   
8.702720E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.990000E+2   7.990000E+2   7.027460E+0   7.125625E-3   
8.760800E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.740000E+2   7.740000E+2   6.974829E+0   7.069899E-3   
8.818880E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.490000E+2   7.490000E+2   6.925981E+0   7.017955E-3   
8.876980E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.240000E+2   7.240000E+2   6.870399E+0   6.959278E-3   
8.935000E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.990000E+2   6.990000E+2   6.809243E+0   6.895026E-3   
8.993080E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.740000E+2   6.740000E+2   6.746938E+0   6.829626E-3   
9.051150E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.490000E+2   6.490000E+2   6.679657E+0   6.759248E-3   
9.109250E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.240000E+2   6.240000E+2   6.611591E+0   6.688086E-3   
9.167280E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.990000E+2   5.990000E+2   6.538828E+0   6.612228E-3   
9.225370E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.740000E+2   5.740000E+2   6.462904E+0   6.533207E-3   
9.283420E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.490000E+2   5.490000E+2   6.379941E+0   6.447148E-3   
9.341520E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.240000E+2   5.240000E+2   6.295725E+0   6.359835E-3   
9.399310E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.990000E+2   4.990000E+2   6.200629E+0   6.261643E-3   
9.457210E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.740000E+2   4.740000E+2   6.103073E+0   6.160991E-3   
9.515080E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.490000E+2   4.490000E+2   5.999498E+0   6.054319E-3   
9.573050E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.240000E+2   4.240000E+2   5.888054E+0   5.939777E-3   
9.631060E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.990000E+2   3.990000E+2   5.765999E+0   5.814626E-3   
9.689210E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.740000E+2   3.740000E+2   5.637037E+0   5.682565E-3   
9.747230E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.490000E+2   3.490000E+2   5.499258E+0   5.541689E-3   
9.805290E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.240000E+2   3.240000E+2   5.347345E+0   5.386678E-3   
9.863180E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.990000E+2   2.990000E+2   5.181036E+0   5.217271E-3   
9.921110E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.740000E+2   2.740000E+2   5.001811E+0   5.034947E-3   
9.979120E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.490000E+2   2.490000E+2   4.803129E+0   4.833165E-3   
1.003728E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.240000E+2   2.240000E+2   4.583157E+0   4.610094E-3   
1.009519E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.990000E+2   1.990000E+2   4.340408E+0   4.364244E-3   
1.015319E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.740000E+2   1.740000E+2   4.061277E+0   4.082012E-3   
1.021116E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.490000E+2   1.490000E+2   3.747068E+0   3.764701E-3   
1.026916E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.240000E+2   1.240000E+2   3.382061E+0   3.396589E-3   
1.032631E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.900000E+1   9.900000E+1   2.951105E+0   2.962528E-3   
1.038336E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.400000E+1   7.400000E+1   2.444056E+0   2.452372E-3   
1.044026E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.900000E+1   4.900000E+1   1.810841E+0   1.816046E-3   
1.049417E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.000000E+1   4.000000E+1   1.548366E+0   1.552451E-3   
1.053981E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.000000E+1   3.000000E+1   1.228923E+0   1.231761E-3   
1.059277E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.900000E+1   1.900000E+1   8.499654E-1   8.514329E-4   
1.063807E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+1   1.000000E+1   5.046929E-1   5.050375E-4   
1.068224E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   1.009557E-1   1.000521E-4   
1.073426E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.000000E+0   -9.000000E+0   -3.392535E-1   -3.412824E-4   
1.078826E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.900000E+1   -1.900000E+1   -7.285050E-1   -7.317817E-4   
1.084190E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.800000E+1   -2.800000E+1   -1.090972E+0   -1.095372E-3   
1.089560E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.900000E+1   -3.900000E+1   -1.418270E+0   -1.424040E-3   
1.094966E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.900000E+1   -4.900000E+1   -1.719216E+0   -1.726231E-3   
1.101614E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.300000E+1   -7.300000E+1   -2.361253E+0   -2.371255E-3   
1.107663E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.900000E+1   -9.900000E+1   -2.882171E+0   -2.895405E-3   
1.113619E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.240000E+2   -1.240000E+2   -3.318277E+0   -3.334617E-3   
1.119568E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.490000E+2   -1.490000E+2   -3.687035E+0   -3.706478E-3   
1.125524E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.740000E+2   -1.740000E+2   -4.006479E+0   -4.029025E-3   
1.131476E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.990000E+2   -1.990000E+2   -4.289452E+0   -4.315100E-3   
1.137432E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.240000E+2   -2.240000E+2   -4.536475E+0   -4.565222E-3   
1.143395E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.490000E+2   -2.490000E+2   -4.753566E+0   -4.785414E-3   
1.149347E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.730000E+2   -2.730000E+2   -4.956963E+0   -4.991786E-3   
1.155312E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.980000E+2   -2.980000E+2   -5.136360E+0   -5.174282E-3   
1.161267E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.240000E+2   -3.240000E+2   -5.302757E+0   -5.343901E-3   
1.167239E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.490000E+2   -3.490000E+2   -5.454670E+0   -5.498913E-3   
1.173206E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.740000E+2   -3.740000E+2   -5.594281E+0   -5.641621E-3   
1.179175E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.990000E+2   -3.990000E+2   -5.724029E+0   -5.774467E-3   
1.185139E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.240000E+2   -4.240000E+2   -5.845750E+0   -5.899285E-3   
1.191106E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.490000E+2   -4.490000E+2   -5.957092E+0   -6.013724E-3   
1.197060E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.740000E+2   -4.740000E+2   -6.063196E+0   -6.122925E-3   
1.203027E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.990000E+2   -4.990000E+2   -6.159522E+0   -6.222347E-3   
1.208982E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.230000E+2   -5.230000E+2   -6.250624E+0   -6.316423E-3   
1.214939E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.490000E+2   -5.490000E+2   -6.339185E+0   -6.408204E-3   
1.220893E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.740000E+2   -5.740000E+2   -6.418764E+0   -6.490878E-3   
1.226846E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.990000E+2   -5.990000E+2   -6.497557E+0   -6.572768E-3   
1.232804E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.240000E+2   -6.240000E+2   -6.569980E+0   -6.648287E-3   
1.238728E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.490000E+2   -6.490000E+2   -6.638995E+0   -6.720398E-3   
1.244896E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.740000E+2   -6.740000E+2   -6.701475E+0   -6.785974E-3   
1.250807E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.990000E+2   -6.990000E+2   -6.763955E+0   -6.851549E-3   
1.256723E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.240000E+2   -7.240000E+2   -6.820298E+0   -6.910988E-3   
1.262896E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.490000E+2   -7.490000E+2   -6.878515E+0   -6.972301E-3   
1.268807E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.740000E+2   -7.740000E+2   -6.930326E+0   -7.027207E-3   
1.274721E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.990000E+2   -7.990000E+2   -6.980942E+0   -7.080919E-3   
1.280885E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.240000E+2   -8.240000E+2   -7.028514E+0   -7.131586E-3   
1.286790E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.490000E+2   -8.490000E+2   -7.074691E+0   -7.180859E-3   
1.292696E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.740000E+2   -8.740000E+2   -7.116466E+0   -7.225728E-3   
1.298863E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.990000E+2   -8.990000E+2   -7.160289E+0   -7.272647E-3   
1.304767E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.240000E+2   -9.240000E+2   -7.198691E+0   -7.314144E-3   
1.310672E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.490000E+2   -9.490000E+2   -7.239165E+0   -7.357713E-3   
1.316838E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.740000E+2   -9.740000E+2   -7.273550E+0   -7.395193E-3   
1.323012E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.990000E+2   -9.990000E+2   -7.308531E+0   -7.433269E-3   
1.333562E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.498000E+3   -1.498000E+3   -7.782863E+0   -7.969373E-3   
1.343030E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.998000E+3   -1.998000E+3   -8.008505E+0   -8.256904E-3   
1.352490E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.498000E+3   -2.498000E+3   -8.128406E+0   -8.438690E-3   
1.362187E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.998000E+3   -2.998000E+3   -8.195593E+0   -8.567763E-3   
1.371651E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.498000E+3   -3.498000E+3   -8.230399E+0   -8.664452E-3   
1.381357E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.998000E+3   -3.998000E+3   -8.250309E+0   -8.746245E-3   
1.391560E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.499000E+3   -4.499000E+3   -8.250297E+0   -8.808240E-3   
1.400981E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.999000E+3   -4.999000E+3   -8.247510E+0   -8.867336E-3   
1.410410E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.498000E+3   -5.498000E+3   -8.238422E+0   -8.920007E-3   
1.420137E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.999000E+3   -5.999000E+3   -8.219321E+0   -8.962912E-3   
1.429564E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.499000E+3   -6.499000E+3   -8.204412E+0   -9.009886E-3   
1.438987E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.999000E+3   -6.999000E+3   -8.182770E+0   -9.050125E-3   
1.448413E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.499000E+3   -7.499000E+3   -8.154756E+0   -9.083994E-3   
1.457833E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.998000E+3   -7.998000E+3   -8.124998E+0   -9.115994E-3   
1.467255E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.499000E+3   -8.499000E+3   -8.093576E+0   -9.146578E-3   
1.476921E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.999000E+3   -8.999000E+3   -8.058243E+0   -9.173127E-3   
1.486594E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.499000E+3   -9.499000E+3   -8.024831E+0   -9.201597E-3   
1.496014E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.999000E+3   -9.999000E+3   -7.989919E+0   -9.228567E-3   
1.506858E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.099900E+4   -1.099900E+4   -7.919429E+0   -9.281841E-3   
1.517692E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.199900E+4   -1.199900E+4   -7.841666E+0   -9.327842E-3   
1.528226E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.299900E+4   -1.299900E+4   -7.758164E+0   -9.368103E-3   
1.539044E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.399800E+4   -1.399800E+4   -7.671008E+0   -9.404588E-3   
1.550374E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.499900E+4   -1.499900E+4   -7.581136E+0   -9.438610E-3   
1.562206E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.599900E+4   -1.599900E+4   -7.480875E+0   -9.468289E-3   
1.574521E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.700000E+4   -1.700000E+4   -7.386985E+0   -9.508715E-3   
1.587365E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.799900E+4   -1.799900E+4   -7.282544E+0   -9.541853E-3   
1.600707E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.899900E+4   -1.899900E+4   -7.169096E+0   -9.570762E-3   
1.614848E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.800300E+4   -1.800300E+4   -7.273116E+0   -9.532939E-3   
1.627148E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.700300E+4   -1.700300E+4   -7.378003E+0   -9.500123E-3   
1.639446E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.600100E+4   -1.600100E+4   -7.473637E+0   -9.461312E-3   
1.650228E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.500300E+4   -1.500300E+4   -7.568663E+0   -9.426649E-3   
1.661531E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.400100E+4   -1.400100E+4   -7.662096E+0   -9.396046E-3   
1.672825E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.300200E+4   -1.300200E+4   -7.737564E+0   -9.347874E-3   
1.683618E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.200100E+4   -1.200100E+4   -7.823958E+0   -9.310381E-3   
1.694425E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.100200E+4   -1.100200E+4   -7.900480E+0   -9.263263E-3   
1.705208E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.000100E+4   -1.000100E+4   -7.970631E+0   -9.209526E-3   
1.715158E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.501000E+3   -9.501000E+3   -8.007381E+0   -9.184394E-3   
1.724547E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.001000E+3   -9.001000E+3   -8.034692E+0   -9.149823E-3   
1.733952E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.501000E+3   -8.501000E+3   -8.072297E+0   -9.125546E-3   
1.743264E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.000000E+3   -8.000000E+3   -8.098389E+0   -9.089633E-3   
1.752648E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.500000E+3   -7.500000E+3   -8.125595E+0   -9.054956E-3   
1.762285E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.001000E+3   -7.001000E+3   -8.154662E+0   -9.022265E-3   
1.771673E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.500000E+3   -6.500000E+3   -8.174806E+0   -8.980402E-3   
1.780749E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.000000E+3   -6.000000E+3   -8.195839E+0   -8.939553E-3   
1.789834E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.500000E+3   -5.500000E+3   -8.209635E+0   -8.891467E-3   
1.799166E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.000000E+3   -5.000000E+3   -8.222822E+0   -8.842771E-3   
1.808260E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.500000E+3   -4.500000E+3   -8.220726E+0   -8.778792E-3   
1.817337E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.000000E+3   -4.000000E+3   -8.220796E+0   -8.716979E-3   
1.826407E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.500000E+3   -3.500000E+3   -8.199692E+0   -8.633992E-3   
1.835482E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.000000E+3   -3.000000E+3   -8.161455E+0   -8.533871E-3   
1.844818E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.500000E+3   -2.500000E+3   -8.094970E+0   -8.405501E-3   
1.853886E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.000000E+3   -2.000000E+3   -7.971333E+0   -8.219978E-3   
1.862974E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.500000E+3   -1.500000E+3   -7.744028E+0   -7.930785E-3   
1.872307E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.000000E+3   -1.000000E+3   -7.278094E+0   -7.402955E-3   
1.878992E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.750000E+2   -9.750000E+2   -7.240828E+0   -7.362594E-3   
1.884777E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.490000E+2   -9.490000E+2   -7.203399E+0   -7.321946E-3   
1.890552E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.250000E+2   -9.250000E+2   -7.163615E+0   -7.279191E-3   
1.896392E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.000000E+2   -9.000000E+2   -7.124664E+0   -7.237144E-3   
1.902229E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.750000E+2   -8.750000E+2   -7.082959E+0   -7.192345E-3   
1.908013E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.490000E+2   -8.490000E+2   -7.039171E+0   -7.145337E-3   
1.913798E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.240000E+2   -8.240000E+2   -6.991939E+0   -7.095010E-3   
1.919556E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.990000E+2   -7.990000E+2   -6.942927E+0   -7.042903E-3   
1.925352E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.740000E+2   -7.740000E+2   -6.891070E+0   -6.987950E-3   
1.931160E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.490000E+2   -7.490000E+2   -6.840477E+0   -6.934261E-3   
1.936957E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.240000E+2   -7.240000E+2   -6.783665E+0   -6.874354E-3   
1.942712E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.000000E+2   -7.000000E+2   -6.726338E+0   -6.814055E-3   
1.948569E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.750000E+2   -6.750000E+2   -6.663694E+0   -6.748316E-3   
1.954377E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.490000E+2   -6.490000E+2   -6.598767E+0   -6.680168E-3   
1.960191E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.240000E+2   -6.240000E+2   -6.531146E+0   -6.609451E-3   
1.965988E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.990000E+2   -5.990000E+2   -6.457329E+0   -6.532539E-3   
1.971805E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.740000E+2   -5.740000E+2   -6.379507E+0   -6.451621E-3   
1.977624E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.490000E+2   -5.490000E+2   -6.297926E+0   -6.366944E-3   
1.983439E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.240000E+2   -5.240000E+2   -6.212141E+0   -6.278062E-3   
1.989231E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.990000E+2   -4.990000E+2   -6.120886E+0   -6.183711E-3   
1.995051E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.740000E+2   -4.740000E+2   -6.025580E+0   -6.085307E-3   
2.000871E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.490000E+2   -4.490000E+2   -5.919662E+0   -5.976293E-3   
2.006694E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.240000E+2   -4.240000E+2   -5.810673E+0   -5.864207E-3   
2.012513E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.990000E+2   -3.990000E+2   -5.687730E+0   -5.738167E-3   
2.018331E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.740000E+2   -3.740000E+2   -5.560162E+0   -5.607502E-3   
2.024158E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.490000E+2   -3.490000E+2   -5.420291E+0   -5.464532E-3   
2.029975E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.240000E+2   -3.240000E+2   -5.269686E+0   -5.310830E-3   
2.035791E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.990000E+2   -2.990000E+2   -5.107043E+0   -5.145088E-3   
2.041607E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.740000E+2   -2.740000E+2   -4.923804E+0   -4.958750E-3   
2.047432E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.490000E+2   -2.490000E+2   -4.727653E+0   -4.759499E-3   
2.053256E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.240000E+2   -2.240000E+2   -4.507680E+0   -4.536427E-3   
2.059072E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.990000E+2   -1.990000E+2   -4.263100E+0   -4.288746E-3   
2.064894E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.740000E+2   -1.740000E+2   -3.984142E+0   -4.006687E-3   
2.070720E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.490000E+2   -1.490000E+2   -3.669061E+0   -3.688503E-3   
2.076546E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.240000E+2   -1.240000E+2   -3.300738E+0   -3.317077E-3   
2.082265E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.900000E+1   -9.900000E+1   -2.870830E+0   -2.884064E-3   
2.087939E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.400000E+1   -7.400000E+1   -2.352614E+0   -2.362741E-3   
2.093597E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.900000E+1   -4.900000E+1   -1.713017E+0   -1.720032E-3   
2.099002E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.000000E+1   -4.000000E+1   -1.449853E+0   -1.455748E-3   
2.103573E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.000000E+1   -3.000000E+1   -1.121859E+0   -1.126507E-3   
2.108136E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.000000E+1   -2.000000E+1   -7.699514E-1   -7.733529E-4   
2.112673E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.000000E+1   -1.000000E+1   -3.875061E-1   -3.896601E-4   
2.117093E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   1.483365E-2   1.392782E-5   
2.122285E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.000000E+0   9.000000E+0   4.452701E-1   4.454894E-4   
2.127672E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.900000E+1   1.900000E+1   8.256223E-1   8.270891E-4   
2.133073E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.900000E+1   2.900000E+1   1.173863E+0   1.176577E-3   
2.138482E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.900000E+1   3.900000E+1   1.490431E+0   1.494390E-3   
2.143883E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.900000E+1   4.900000E+1   1.780555E+0   1.785760E-3   
2.150527E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.400000E+1   7.400000E+1   2.403221E+0   2.411536E-3   
2.156322E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.900000E+1   9.900000E+1   2.908960E+0   2.920382E-3   
2.162272E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.240000E+2   1.240000E+2   3.330058E+0   3.344585E-3   
2.168227E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.490000E+2   1.490000E+2   3.692182E+0   3.709813E-3   
2.174185E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.740000E+2   1.740000E+2   4.001245E+0   4.021978E-3   
2.180148E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.990000E+2   1.990000E+2   4.277499E+0   4.301333E-3   
2.186100E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.240000E+2   2.240000E+2   4.517713E+0   4.544648E-3   
2.192255E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.490000E+2   2.490000E+2   4.733149E+0   4.763183E-3   
2.198217E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.740000E+2   2.740000E+2   4.928778E+0   4.961912E-3   
2.204178E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.990000E+2   2.990000E+2   5.105646E+0   5.141878E-3   
2.210130E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.240000E+2   3.240000E+2   5.269948E+0   5.309279E-3   
2.216094E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.490000E+2   3.490000E+2   5.417588E+0   5.460016E-3   
2.222057E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.740000E+2   3.740000E+2   5.556325E+0   5.601851E-3   
2.228020E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.990000E+2   3.990000E+2   5.684415E+0   5.733039E-3   
2.233976E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.240000E+2   4.240000E+2   5.800903E+0   5.852624E-3   
2.239928E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.490000E+2   4.490000E+2   5.910855E+0   5.965674E-3   
2.245885E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.740000E+2   4.740000E+2   6.015824E+0   6.073739E-3   
2.251843E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.990000E+2   4.990000E+2   6.109608E+0   6.170620E-3   
2.257806E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.240000E+2   5.240000E+2   6.200465E+0   6.264573E-3   
2.263954E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.490000E+2   5.490000E+2   6.284833E+0   6.352038E-3   
2.269903E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.740000E+2   5.740000E+2   6.366320E+0   6.436621E-3   
2.276049E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.990000E+2   5.990000E+2   6.439013E+0   6.512409E-3   
2.281987E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.240000E+2   6.240000E+2   6.513953E+0   6.590446E-3   
2.287941E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.480000E+2   6.480000E+2   6.580368E+0   6.659833E-3   
2.293882E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.730000E+2   6.730000E+2   6.642918E+0   6.725479E-3   
2.299835E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.980000E+2   6.980000E+2   6.708115E+0   6.793772E-3   
2.305786E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.240000E+2   7.240000E+2   6.761425E+0   6.850301E-3   
2.311739E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.490000E+2   7.490000E+2   6.818647E+0   6.910618E-3   
2.317682E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.740000E+2   7.740000E+2   6.873713E+0   6.968781E-3   
2.323634E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.990000E+2   7.990000E+2   6.922315E+0   7.020478E-3   
2.329568E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.240000E+2   8.240000E+2   6.969172E+0   7.070430E-3   
2.335513E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.490000E+2   8.490000E+2   7.012282E+0   7.116635E-3   
2.341447E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.740000E+2   8.740000E+2   7.057148E+0   7.164596E-3   
2.347583E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.990000E+2   8.990000E+2   7.100491E+0   7.211035E-3   
2.353516E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.240000E+2   9.240000E+2   7.137148E+0   7.250787E-3   
2.359462E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.490000E+2   9.490000E+2   7.173102E+0   7.289836E-3   
2.365400E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.740000E+2   9.740000E+2   7.213166E+0   7.332995E-3   
2.371558E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.990000E+2   9.990000E+2   7.247550E+0   7.370475E-3   
2.382095E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.499000E+3   1.499000E+3   7.713755E+0   7.898574E-3   
2.391197E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.999000E+3   1.999000E+3   7.935907E+0   8.182615E-3   
2.400651E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.499000E+3   2.499000E+3   8.055538E+0   8.364132E-3   
2.410335E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.999000E+3   2.999000E+3   8.117842E+0   8.488320E-3   
2.419921E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.499000E+3   3.499000E+3   8.157707E+0   8.590070E-3   
2.429016E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.999000E+3   3.999000E+3   8.170625E+0   8.664871E-3   
2.438678E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.499000E+3   4.499000E+3   8.172475E+0   8.728604E-3   
2.448085E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.999000E+3   4.999000E+3   8.169231E+0   8.787243E-3   
2.457202E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.499000E+3   5.499000E+3   8.153620E+0   8.833514E-3   
2.466615E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.999000E+3   5.999000E+3   8.140094E+0   8.881870E-3   
2.475726E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.499000E+3   6.499000E+3   8.129624E+0   8.933283E-3   
2.484840E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.999000E+3   6.999000E+3   8.101259E+0   8.966800E-3   
2.493937E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.500000E+3   7.500000E+3   8.073421E+0   9.000968E-3   
2.503071E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.000000E+3   8.000000E+3   8.042890E+0   9.032319E-3   
2.512480E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.499000E+3   8.499000E+3   8.014958E+0   9.066146E-3   
2.521842E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.999000E+3   8.999000E+3   7.980855E+0   9.093924E-3   
2.531181E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.500000E+3   9.500000E+3   7.945065E+0   9.120140E-3   
2.540334E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+4   1.000000E+4   7.913058E+0   9.150015E-3   
2.551653E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.099900E+4   1.099900E+4   7.838258E+0   9.198855E-3   
2.562430E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.200000E+4   1.200000E+4   7.759300E+0   9.243785E-3   
2.573245E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.299900E+4   1.299900E+4   7.675974E+0   9.284099E-3   
2.583982E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.400000E+4   1.400000E+4   7.591079E+0   9.323091E-3   
2.594788E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.499900E+4   1.499900E+4   7.499121E+0   9.354781E-3   
2.606059E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.600000E+4   1.600000E+4   7.402948E+0   9.388611E-3   
2.618358E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.700000E+4   1.700000E+4   7.307220E+0   9.426938E-3   
2.631349E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.800000E+4   1.800000E+4   7.201993E+0   9.459255E-3   
2.645173E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.899900E+4   1.899900E+4   7.089061E+0   9.488304E-3   
@@END Data.
@Measurement parameters
                                        Upward Part    Downward part  Average        Parameter 'definition'                  
Hysteresis Loop                                                                      Hysteresis Parameters                   
                                                                                                                             
Hc Oe                                   9.000          18999.000      -9495.000      Coercive Field: Field at which M//H changes sign
Mr emu                                  339.455E-6     9.488E-3       4.574E-3       Remanent Magnetization: M at H=0        
S                                       0.035          0.991          0.513          Squareness: Mr/Ms                       
S*                                      22.795         1.000          11.897         1-(Mr/Hc)(1/slope at Hc)                
M at H max emu                          9.681E-3       -9.571E-3      9.626E-3       M at the maximum field                  
                                                                                                                             

@END Measurement parameters
