@Filename: C:\vsm-lv\System_Admin\data\Dominique\DD146\dd144_dry\dd144_dry-Hys-00.VHD
@Measurement Controlfilename: c:\vsm-lv\System_Admin\Recipes\VC_HL.VHC
@Calibration filename: c:\vsm-lv\System_Admin\settings\default.cal
@Parameter Filec:\vsm-lv\System_Admin\settings\default.cal
@Operator: System_Admin
@Samplename: dd144_dry
@Date: Friday, September 30, 2016    (2016-09-30)
@Time: 15:12:02
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
Shape = Cylindrical;  Length = 6.60 [mm] Width = 6.60 [mm] Thickness = 1.000E+3 [nm] Diameter = 8.00 [mm] Volume : 3.318E-7 [m^3] Area = 0.000E+0 [mm^2] Mass = 6.740E-3 [g] Nd =  0.00 Sample Angle Offset = 0.000 
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
@Emu/v: 58.907
@Y Coils Correction Factor: 1.385
@Sample Shape Correction Factor: 1.000
@Coil Angle Alpha: 45.000
@Coil Angle Beta: -45.000
[Data Manipulation]
Field Linearity Correction = No
Image Effect Correction = Yes
Image Correction Array Length = 17
14998.000000   1.000000
15247.000000   1.000156
15497.000000   1.000302
15747.000000   1.000527
15997.000000   1.000751
16247.000000   1.001191
16497.000000   1.001494
16746.000000   1.001865
16996.000000   1.002237
17247.000000   1.002688
17496.000000   1.003286
17746.000000   1.003738
17996.000000   1.004259
18245.000000   1.005007
18495.000000   1.005686
18745.000000   1.006367
18995.000000   1.007118
Sample image effect correction factor = 1.000000, Sample holder image effect correction factor = 0.700000
Background Subtraction = Yes   Method = Point by point
Background Signal array length = 32
-18993.000000   2.406274E-3   0.000000E+0   0.000000E+0
-18502.000000   2.348410E-3   0.000000E+0   0.000000E+0
-18001.000000   2.288960E-3   0.000000E+0   0.000000E+0
-17501.000000   2.227346E-3   0.000000E+0   0.000000E+0
-17002.000000   2.166318E-3   0.000000E+0   0.000000E+0
-16501.000000   2.104911E-3   0.000000E+0   0.000000E+0
-16000.000000   2.042623E-3   0.000000E+0   0.000000E+0
-15501.000000   1.978574E-3   0.000000E+0   0.000000E+0
-15001.000000   1.918608E-3   0.000000E+0   0.000000E+0
-13001.000000   1.670876E-3   0.000000E+0   0.000000E+0
-11001.000000   1.415849E-3   0.000000E+0   0.000000E+0
-9001.000000   1.161825E-3   0.000000E+0   0.000000E+0
-7002.000000   9.030077E-4   0.000000E+0   0.000000E+0
-5001.000000   6.471822E-4   0.000000E+0   0.000000E+0
-3002.000000   3.860235E-4   0.000000E+0   0.000000E+0
-1002.000000   1.238858E-4   0.000000E+0   0.000000E+0
995.000000   -1.233702E-4   0.000000E+0   0.000000E+0
2996.000000   -3.852079E-4   0.000000E+0   0.000000E+0
4997.000000   -6.443583E-4   0.000000E+0   0.000000E+0
6997.000000   -9.021850E-4   0.000000E+0   0.000000E+0
8998.000000   -1.158138E-3   0.000000E+0   0.000000E+0
10996.000000   -1.413947E-3   0.000000E+0   0.000000E+0
12997.000000   -1.666259E-3   0.000000E+0   0.000000E+0
14997.000000   -1.916258E-3   0.000000E+0   0.000000E+0
15498.000000   -1.978401E-3   0.000000E+0   0.000000E+0
15998.000000   -2.040843E-3   0.000000E+0   0.000000E+0
16498.000000   -2.100129E-3   0.000000E+0   0.000000E+0
16997.000000   -2.163433E-3   0.000000E+0   0.000000E+0
17498.000000   -2.225328E-3   0.000000E+0   0.000000E+0
17997.000000   -2.283674E-3   0.000000E+0   0.000000E+0
18496.000000   -2.348147E-3   0.000000E+0   0.000000E+0
18992.000000   -2.401551E-3   0.000000E+0   0.000000E+0
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
Date and time of last calibration = Thursday, September 01, 2016  17:19:09
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
@Time at start of measurement: 15:12:03
@@Data
New Section: Section 0: 
1.442600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.000000E+0   -7.000000E+0   -2.178575E-1   -2.185543E-4   
1.879600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   3.290911E-2   3.308551E-5   
2.424900E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+1   1.000000E+1   3.115678E-1   3.129896E-4   
3.047800E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.100000E+1   2.100000E+1   6.089162E-1   6.117077E-4   
3.578000E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.100000E+1   3.100000E+1   8.784098E-1   8.824464E-4   
4.108500E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.100000E+1   4.100000E+1   1.154245E+0   1.159527E-3   
4.730500E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.100000E+1   5.100000E+1   1.425867E+0   1.432394E-3   
5.394900E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.600000E+1   7.600000E+1   2.074210E+0   2.083849E-3   
5.967600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+2   1.000000E+2   2.692503E+0   2.705130E-3   
6.665200E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.260000E+2   1.260000E+2   3.285320E+0   3.301181E-3   
7.242000E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.510000E+2   1.510000E+2   3.842422E+0   3.861393E-3   
7.818600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.750000E+2   1.750000E+2   4.365760E+0   4.387716E-3   
8.393300E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.000000E+2   2.000000E+2   4.863599E+0   4.888664E-3   
8.975300E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.250000E+2   2.250000E+2   5.332383E+0   5.360556E-3   
9.551200E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.500000E+2   2.500000E+2   5.776633E+0   5.807912E-3   
1.022850E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.750000E+2   2.750000E+2   6.194324E+0   6.228709E-3   
1.080290E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.000000E+2   3.000000E+2   6.596262E+0   6.633753E-3   
1.138620E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.260000E+2   3.260000E+2   6.975296E+0   7.016016E-3   
1.196190E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.500000E+2   3.500000E+2   7.333736E+0   7.377437E-3   
1.254350E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.750000E+2   3.750000E+2   7.675188E+0   7.721993E-3   
1.311840E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.000000E+2   4.000000E+2   8.004104E+0   8.054013E-3   
1.370040E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.250000E+2   4.250000E+2   8.317126E+0   8.370139E-3   
1.427760E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.510000E+2   4.510000E+2   8.618108E+0   8.674348E-3   
1.485510E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.750000E+2   4.750000E+2   8.903480E+0   8.962698E-3   
1.543010E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.000000E+2   5.000000E+2   9.178236E+0   9.240557E-3   
1.601350E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.250000E+2   5.250000E+2   9.440163E+0   9.505586E-3   
1.658970E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.500000E+2   5.500000E+2   9.694089E+0   9.762614E-3   
1.717300E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.750000E+2   5.750000E+2   9.937778E+0   1.000940E-2   
1.774770E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.000000E+2   6.000000E+2   1.017364E+1   1.024837E-2   
1.833080E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.250000E+2   6.250000E+2   1.039951E+1   1.047734E-2   
1.891910E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.500000E+2   6.500000E+2   1.061613E+1   1.069706E-2   
1.950720E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.750000E+2   6.750000E+2   1.082672E+1   1.091075E-2   
2.008960E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.000000E+2   7.000000E+2   1.103520E+1   1.112233E-2   
2.068790E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.250000E+2   7.250000E+2   1.123024E+1   1.132048E-2   
2.126530E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.500000E+2   7.500000E+2   1.142309E+1   1.151643E-2   
2.184850E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.750000E+2   7.750000E+2   1.160777E+1   1.170420E-2   
2.251580E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.000000E+2   8.000000E+2   1.177965E+1   1.187918E-2   
2.309660E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.250000E+2   8.250000E+2   1.195941E+1   1.206205E-2   
2.367760E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.500000E+2   8.500000E+2   1.213076E+1   1.223650E-2   
2.425870E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.750000E+2   8.750000E+2   1.229264E+1   1.240147E-2   
2.483270E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.000000E+2   9.000000E+2   1.245764E+1   1.256957E-2   
2.541490E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.250000E+2   9.250000E+2   1.261074E+1   1.272577E-2   
2.599620E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.500000E+2   9.500000E+2   1.276278E+1   1.288091E-2   
2.657830E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.750000E+2   9.750000E+2   1.290988E+1   1.303111E-2   
2.718050E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+3   1.000000E+3   1.305208E+1   1.317644E-2   
2.817780E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.500000E+3   1.500000E+3   1.532632E+1   1.551617E-2   
2.908950E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.000000E+3   2.000000E+3   1.689722E+1   1.715253E-2   
3.000300E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.500000E+3   2.500000E+3   1.807871E+1   1.839949E-2   
3.091500E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.000000E+3   3.000000E+3   1.901515E+1   1.940137E-2   
3.182820E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.500000E+3   3.500000E+3   1.979007E+1   2.024106E-2   
3.274030E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.001000E+3   4.001000E+3   2.044173E+1   2.095762E-2   
3.364930E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.500000E+3   4.500000E+3   2.100283E+1   2.158337E-2   
3.456280E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.000000E+3   5.000000E+3   2.150106E+1   2.214636E-2   
3.547020E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.501000E+3   5.501000E+3   2.194205E+1   2.265196E-2   
3.639470E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.001000E+3   6.001000E+3   2.233531E+1   2.310968E-2   
3.730160E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.500000E+3   6.500000E+3   2.269239E+1   2.353110E-2   
3.821410E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.000000E+3   7.000000E+3   2.301682E+1   2.391999E-2   
3.912100E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.501000E+3   7.501000E+3   2.330859E+1   2.427585E-2   
4.006680E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.002000E+3   8.002000E+3   2.357895E+1   2.461030E-2   
4.096790E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.501000E+3   8.501000E+3   2.383421E+1   2.492940E-2   
4.186730E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.001000E+3   9.001000E+3   2.406806E+1   2.522721E-2   
4.276850E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.501000E+3   9.501000E+3   2.428576E+1   2.550893E-2   
4.367560E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000200E+4   1.000200E+4   2.448729E+1   2.577461E-2   
4.478160E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.100100E+4   1.100100E+4   2.485913E+1   2.627435E-2   
4.580430E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.200100E+4   1.200100E+4   2.518111E+1   2.672243E-2   
4.682990E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.300100E+4   1.300100E+4   2.547217E+1   2.713959E-2   
4.785310E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.400100E+4   1.400100E+4   2.572287E+1   2.751529E-2   
4.892730E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.500100E+4   1.500100E+4   2.594864E+1   2.786611E-2   
5.000100E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.600100E+4   1.600100E+4   2.612419E+1   2.818587E-2   
5.117600E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.700100E+4   1.700100E+4   2.628396E+1   2.850761E-2   
5.240530E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.800100E+4   1.800100E+4   2.639422E+1   2.879191E-2   
5.363420E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.900000E+4   1.900000E+4   2.648759E+1   2.907838E-2   
5.499540E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.800600E+4   1.800600E+4   2.639877E+1   2.879752E-2   
5.622400E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.700500E+4   1.700500E+4   2.628572E+1   2.851005E-2   
5.725640E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.600700E+4   1.600700E+4   2.614351E+1   2.820620E-2   
5.838230E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.500500E+4   1.500500E+4   2.595144E+1   2.786948E-2   
5.946360E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.400500E+4   1.400500E+4   2.573869E+1   2.753162E-2   
6.054680E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.300400E+4   1.300400E+4   2.548869E+1   2.715648E-2   
6.163030E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.200400E+4   1.200400E+4   2.519691E+1   2.673861E-2   
6.271420E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.100300E+4   1.100300E+4   2.487915E+1   2.629462E-2   
6.373980E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000400E+4   1.000400E+4   2.451469E+1   2.580226E-2   
6.479250E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.503000E+3   9.503000E+3   2.430683E+1   2.553025E-2   
6.575880E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.003000E+3   9.003000E+3   2.409615E+1   2.525555E-2   
6.672800E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.502000E+3   8.502000E+3   2.386372E+1   2.495904E-2   
6.774720E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.002000E+3   8.002000E+3   2.361373E+1   2.464508E-2   
6.876490E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.503000E+3   7.503000E+3   2.334512E+1   2.431264E-2   
6.973270E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.002000E+3   7.002000E+3   2.304632E+1   2.394975E-2   
7.070190E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.502000E+3   6.502000E+3   2.273137E+1   2.357033E-2   
7.166950E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.002000E+3   6.002000E+3   2.237710E+1   2.315160E-2   
7.263860E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.502000E+3   5.502000E+3   2.198490E+1   2.269493E-2   
7.360670E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.002000E+3   5.002000E+3   2.155196E+1   2.219752E-2   
7.457660E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.502000E+3   4.502000E+3   2.106252E+1   2.164332E-2   
7.554480E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.002000E+3   4.002000E+3   2.049934E+1   2.101537E-2   
7.651450E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.502000E+3   3.502000E+3   1.984941E+1   2.030067E-2   
7.745640E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.002000E+3   3.002000E+3   1.908187E+1   1.946835E-2   
7.842600E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.502000E+3   2.502000E+3   1.814087E+1   1.846191E-2   
7.939320E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.002000E+3   2.002000E+3   1.695796E+1   1.721354E-2   
8.033220E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.502000E+3   1.502000E+3   1.538953E+1   1.557964E-2   
8.130020E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.001000E+3   1.001000E+3   1.311705E+1   1.324155E-2   
8.197690E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.750000E+2   9.750000E+2   1.296889E+1   1.309012E-2   
8.257830E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.500000E+2   9.500000E+2   1.281965E+1   1.293778E-2   
8.316730E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.260000E+2   9.260000E+2   1.266938E+1   1.278453E-2   
8.375800E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.000000E+2   9.000000E+2   1.251384E+1   1.262577E-2   
8.434500E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.750000E+2   8.750000E+2   1.235267E+1   1.246150E-2   
8.494770E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.500000E+2   8.500000E+2   1.219150E+1   1.229723E-2   
8.553490E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.250000E+2   8.250000E+2   1.202088E+1   1.212351E-2   
8.611550E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.000000E+2   8.000000E+2   1.184776E+1   1.194729E-2   
8.670490E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.750000E+2   7.750000E+2   1.167044E+1   1.176687E-2   
8.730960E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.500000E+2   7.500000E+2   1.148084E+1   1.157417E-2   
8.789800E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.250000E+2   7.250000E+2   1.129194E+1   1.138218E-2   
8.847380E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.000000E+2   7.000000E+2   1.109566E+1   1.118280E-2   
8.906310E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.750000E+2   6.750000E+2   1.088958E+1   1.097361E-2   
8.964550E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.500000E+2   6.500000E+2   1.067784E+1   1.075878E-2   
9.024900E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.250000E+2   6.250000E+2   1.046191E+1   1.053974E-2   
9.083220E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.010000E+2   6.010000E+2   1.023718E+1   1.031203E-2   
9.142780E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.760000E+2   5.760000E+2   1.000267E+1   1.007442E-2   
9.202270E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.510000E+2   5.510000E+2   9.757556E+0   9.826207E-3   
9.261840E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.260000E+2   5.260000E+2   9.506174E+0   9.571723E-3   
9.321150E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.010000E+2   5.010000E+2   9.240384E+0   9.302830E-3   
9.380680E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.760000E+2   4.760000E+2   8.968608E+0   9.027952E-3   
9.440280E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.510000E+2   4.510000E+2   8.684556E+0   8.740797E-3   
9.499820E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.260000E+2   4.260000E+2   8.386472E+0   8.439611E-3   
9.559160E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.010000E+2   4.010000E+2   8.076772E+0   8.126807E-3   
9.618680E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.760000E+2   3.760000E+2   7.748480E+0   7.795411E-3   
9.678260E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.510000E+2   3.510000E+2   7.407206E+0   7.451033E-3   
9.737860E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.260000E+2   3.260000E+2   7.046221E+0   7.086943E-3   
9.797130E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.010000E+2   3.010000E+2   6.668777E+0   6.706394E-3   
9.856620E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.760000E+2   2.760000E+2   6.275887E+0   6.310399E-3   
9.916060E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.510000E+2   2.510000E+2   5.855238E+0   5.886643E-3   
9.975500E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.260000E+2   2.260000E+2   5.407916E+0   5.436214E-3   
1.003490E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.010000E+2   2.010000E+2   4.938124E+0   4.963314E-3   
1.009437E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.760000E+2   1.760000E+2   4.437781E+0   4.459863E-3   
1.015383E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.510000E+2   1.510000E+2   3.910405E+0   3.929378E-3   
1.021331E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.260000E+2   1.260000E+2   3.351067E+0   3.366931E-3   
1.027261E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.010000E+2   1.010000E+2   2.753116E+0   2.765869E-3   
1.033074E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.600000E+1   7.600000E+1   2.122859E+0   2.132500E-3   
1.038879E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.100000E+1   5.100000E+1   1.458891E+0   1.465419E-3   
1.045116E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.100000E+1   4.100000E+1   1.185727E+0   1.191009E-3   
1.050524E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.100000E+1   3.100000E+1   9.058854E-1   9.099228E-4   
1.055923E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.100000E+1   2.100000E+1   6.232355E-1   6.260273E-4   
1.061312E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.100000E+1   1.100000E+1   3.384778E-1   3.400241E-4   
1.066543E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   5.688125E-2   5.705827E-5   
1.071794E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.000000E+0   -7.000000E+0   -2.243646E-1   -2.250616E-4   
1.077544E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.700000E+1   -1.700000E+1   -5.070151E-1   -5.089576E-4   
1.083297E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.700000E+1   -2.700000E+1   -7.868546E-1   -7.900425E-4   
1.088819E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.700000E+1   -3.700000E+1   -1.065291E+0   -1.069725E-3   
1.094579E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.700000E+1   -4.700000E+1   -1.341622E+0   -1.347300E-3   
1.101940E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.200000E+1   -7.200000E+1   -2.010154E+0   -2.018945E-3   
1.108142E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.700000E+1   -9.700000E+1   -2.642512E+0   -2.654415E-3   
1.114515E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.220000E+2   -1.220000E+2   -3.247484E+0   -3.262499E-3   
1.121289E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.470000E+2   -1.470000E+2   -3.813147E+0   -3.831271E-3   
1.127808E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.720000E+2   -1.720000E+2   -4.350003E+0   -4.371237E-3   
1.133824E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.970000E+2   -1.970000E+2   -4.848941E+0   -4.873283E-3   
1.140138E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.220000E+2   -2.220000E+2   -5.322595E+0   -5.350045E-3   
1.146662E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.470000E+2   -2.470000E+2   -5.773780E+0   -5.804336E-3   
1.153442E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.720000E+2   -2.720000E+2   -6.198271E+0   -6.231934E-3   
1.160266E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.970000E+2   -2.970000E+2   -6.598206E+0   -6.634974E-3   
1.166323E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.220000E+2   -3.220000E+2   -6.977758E+0   -7.017632E-3   
1.172792E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.470000E+2   -3.470000E+2   -7.342938E+0   -7.385916E-3   
1.179605E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.720000E+2   -3.720000E+2   -7.687723E+0   -7.733806E-3   
1.185614E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.970000E+2   -3.970000E+2   -8.015331E+0   -8.064518E-3   
1.191623E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.220000E+2   -4.220000E+2   -8.330993E+0   -8.383284E-3   
1.198435E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.470000E+2   -4.470000E+2   -8.634013E+0   -8.689407E-3   
1.204442E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.720000E+2   -4.720000E+2   -8.919833E+0   -8.978329E-3   
1.210501E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.970000E+2   -4.970000E+2   -9.195425E+0   -9.257024E-3   
1.216864E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.220000E+2   -5.220000E+2   -9.462960E+0   -9.527661E-3   
1.222935E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.470000E+2   -5.470000E+2   -9.714730E+0   -9.782534E-3   
1.228949E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.720000E+2   -5.720000E+2   -9.955957E+0   -1.002686E-2   
1.235479E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.970000E+2   -5.970000E+2   -1.019436E+1   -1.026836E-2   
1.241492E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.230000E+2   -6.230000E+2   -1.042189E+1   -1.049912E-2   
1.247511E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.480000E+2   -6.480000E+2   -1.064447E+1   -1.072480E-2   
1.253923E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.730000E+2   -6.730000E+2   -1.085517E+1   -1.093860E-2   
1.259892E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.980000E+2   -6.980000E+2   -1.105812E+1   -1.114465E-2   
1.265854E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.230000E+2   -7.230000E+2   -1.125716E+1   -1.134680E-2   
1.272330E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.480000E+2   -7.480000E+2   -1.144962E+1   -1.154235E-2   
1.278291E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.730000E+2   -7.730000E+2   -1.163570E+1   -1.173154E-2   
1.284308E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.980000E+2   -7.980000E+2   -1.181547E+1   -1.191440E-2   
1.290720E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.230000E+2   -8.230000E+2   -1.199245E+1   -1.209448E-2   
1.296731E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.480000E+2   -8.480000E+2   -1.216063E+1   -1.226576E-2   
1.302734E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.730000E+2   -8.730000E+2   -1.232669E+1   -1.243492E-2   
1.309202E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.980000E+2   -8.980000E+2   -1.248715E+1   -1.259849E-2   
1.315154E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.230000E+2   -9.230000E+2   -1.264479E+1   -1.275922E-2   
1.321164E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.480000E+2   -9.480000E+2   -1.279506E+1   -1.291259E-2   
1.327625E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.730000E+2   -9.730000E+2   -1.294254E+1   -1.306317E-2   
1.333587E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.980000E+2   -9.980000E+2   -1.308789E+1   -1.321162E-2   
1.344180E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.497000E+3   -1.497000E+3   -1.536567E+1   -1.555483E-2   
1.353939E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.996000E+3   -1.996000E+3   -1.694498E+1   -1.719959E-2   
1.363711E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.497000E+3   -2.497000E+3   -1.812578E+1   -1.844608E-2   
1.373474E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.997000E+3   -2.997000E+3   -1.906220E+1   -1.944806E-2   
1.383237E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.497000E+3   -3.497000E+3   -1.982938E+1   -2.028059E-2   
1.392987E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.997000E+3   -3.997000E+3   -2.048176E+1   -2.099831E-2   
1.403239E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.498000E+3   -4.498000E+3   -2.103934E+1   -2.162136E-2   
1.413141E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.998000E+3   -4.998000E+3   -2.153651E+1   -2.218386E-2   
1.422906E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.497000E+3   -5.497000E+3   -2.197120E+1   -2.268237E-2   
1.433159E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.998000E+3   -5.998000E+3   -2.236375E+1   -2.313898E-2   
1.443357E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.498000E+3   -6.498000E+3   -2.272750E+1   -2.356667E-2   
1.452774E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.998000E+3   -6.998000E+3   -2.304737E+1   -2.395047E-2   
1.462501E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.498000E+3   -7.498000E+3   -2.334266E+1   -2.431050E-2   
1.472406E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.997000E+3   -7.997000E+3   -2.361441E+1   -2.464686E-2   
1.482133E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.498000E+3   -8.498000E+3   -2.387074E+1   -2.496807E-2   
1.492333E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.998000E+3   -8.998000E+3   -2.409650E+1   -2.525856E-2   
1.502539E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.498000E+3   -9.498000E+3   -2.430963E+1   -2.553521E-2   
1.512448E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.998000E+3   -9.998000E+3   -2.451573E+1   -2.580483E-2   
1.524099E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.099800E+4   -1.099800E+4   -2.488616E+1   -2.630227E-2   
1.534920E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.199800E+4   -1.199800E+4   -2.520532E+1   -2.674895E-2   
1.545746E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.299900E+4   -1.299900E+4   -2.548903E+1   -2.716031E-2   
1.557075E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.399800E+4   -1.399800E+4   -2.573936E+1   -2.753440E-2   
1.567899E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.499800E+4   -1.499800E+4   -2.596234E+1   -2.788125E-2   
1.579224E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.599700E+4   -1.599700E+4   -2.614351E+1   -2.820607E-2   
1.591576E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.699900E+4   -1.699900E+4   -2.629590E+1   -2.852150E-2   
1.604425E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.799800E+4   -1.799800E+4   -2.641845E+1   -2.882040E-2   
1.617766E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.899800E+4   -1.899800E+4   -2.650482E+1   -2.910045E-2   
1.631896E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.800200E+4   -1.800200E+4   -2.641597E+1   -2.881872E-2   
1.644198E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.700200E+4   -1.700200E+4   -2.629905E+1   -2.852517E-2   
1.656496E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.600100E+4   -1.600100E+4   -2.614807E+1   -2.821132E-2   
1.667787E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.500100E+4   -1.500100E+4   -2.596269E+1   -2.788202E-2   
1.678581E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.400100E+4   -1.400100E+4   -2.575694E+1   -2.755235E-2   
1.689381E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.300100E+4   -1.300100E+4   -2.550308E+1   -2.717462E-2   
1.699891E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.200100E+4   -1.200100E+4   -2.522357E+1   -2.676759E-2   
1.710687E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.100000E+4   -1.100000E+4   -2.489599E+1   -2.631236E-2   
1.720654E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.000000E+4   -1.000000E+4   -2.453506E+1   -2.582440E-2   
1.730580E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.500000E+3   -9.500000E+3   -2.433841E+1   -2.556425E-2   
1.739642E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.000000E+3   -9.000000E+3   -2.411969E+1   -2.528201E-2   
1.748743E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.499000E+3   -8.499000E+3   -2.388513E+1   -2.498258E-2   
1.757814E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.999000E+3   -7.999000E+3   -2.363726E+1   -2.466997E-2   
1.766905E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.499000E+3   -7.499000E+3   -2.336547E+1   -2.433343E-2   
1.775970E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.000000E+3   -7.000000E+3   -2.307298E+1   -2.397634E-2   
1.785064E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.499000E+3   -6.499000E+3   -2.275630E+1   -2.359559E-2   
1.794146E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.999000E+3   -5.999000E+3   -2.240905E+1   -2.318441E-2   
1.803179E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.499000E+3   -5.499000E+3   -2.201896E+1   -2.273039E-2   
1.812260E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.999000E+3   -4.999000E+3   -2.158392E+1   -2.223140E-2   
1.821296E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.499000E+3   -4.499000E+3   -2.109307E+1   -2.167521E-2   
1.830315E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.998000E+3   -3.998000E+3   -2.053479E+1   -2.105147E-2   
1.839338E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.499000E+3   -3.499000E+3   -1.988417E+1   -2.033564E-2   
1.848353E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.999000E+3   -2.999000E+3   -1.911557E+1   -1.950169E-2   
1.857379E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.499000E+3   -2.499000E+3   -1.817494E+1   -1.849551E-2   
1.866399E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.998000E+3   -1.998000E+3   -1.699342E+1   -1.724830E-2   
1.875428E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.499000E+3   -1.499000E+3   -1.541831E+1   -1.560774E-2   
1.884448E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.990000E+2   -9.990000E+2   -1.313814E+1   -1.326200E-2   
1.891085E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.730000E+2   -9.730000E+2   -1.298750E+1   -1.310813E-2   
1.896850E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.480000E+2   -9.480000E+2   -1.283791E+1   -1.295545E-2   
1.902603E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.230000E+2   -9.230000E+2   -1.268693E+1   -1.280137E-2   
1.908363E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.980000E+2   -8.980000E+2   -1.253033E+1   -1.264167E-2   
1.914126E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.730000E+2   -8.730000E+2   -1.236951E+1   -1.247775E-2   
1.919107E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.500000E+2   -8.500000E+2   -1.221783E+1   -1.232321E-2   
1.924915E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.230000E+2   -8.230000E+2   -1.202997E+1   -1.213201E-2   
1.930666E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.980000E+2   -7.980000E+2   -1.185513E+1   -1.195407E-2   
1.936427E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.730000E+2   -7.730000E+2   -1.167712E+1   -1.177295E-2   
1.941405E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.500000E+2   -7.500000E+2   -1.150613E+1   -1.159911E-2   
1.947226E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.230000E+2   -7.230000E+2   -1.129861E+1   -1.138825E-2   
1.952994E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.980000E+2   -6.980000E+2   -1.109705E+1   -1.118359E-2   
1.958754E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.730000E+2   -6.730000E+2   -1.089169E+1   -1.097512E-2   
1.963735E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.500000E+2   -6.500000E+2   -1.069854E+1   -1.077913E-2   
1.968785E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.250000E+2   -6.250000E+2   -1.048123E+1   -1.055872E-2   
1.973810E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.000000E+2   -6.000000E+2   -1.025335E+1   -1.032772E-2   
1.979635E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.730000E+2   -5.730000E+2   -9.998429E+0   -1.006946E-2   
1.984616E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.500000E+2   -5.500000E+2   -9.773709E+0   -9.841885E-3   
1.990440E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.230000E+2   -5.230000E+2   -9.498434E+0   -9.563260E-3   
1.995417E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.990000E+2   -4.990000E+2   -9.253367E+0   -9.315215E-3   
2.000467E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.750000E+2   -4.750000E+2   -8.980213E+0   -9.039082E-3   
2.005493E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.500000E+2   -4.500000E+2   -8.694747E+0   -8.750514E-3   
2.010542E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.250000E+2   -4.250000E+2   -8.393847E+0   -8.446511E-3   
2.015555E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.000000E+2   -4.000000E+2   -8.077467E+0   -8.127027E-3   
2.021671E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.720000E+2   -3.720000E+2   -7.723197E+0   -7.769281E-3   
2.026973E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.490000E+2   -3.490000E+2   -7.405097E+0   -7.448325E-3   
2.032032E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.240000E+2   -3.240000E+2   -7.044100E+0   -7.084223E-3   
2.037075E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.990000E+2   -2.990000E+2   -6.662085E+0   -6.699103E-3   
2.042122E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.750000E+2   -2.750000E+2   -6.262869E+0   -6.296905E-3   
2.047172E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.490000E+2   -2.490000E+2   -5.837333E+0   -5.868139E-3   
2.052226E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.240000E+2   -2.240000E+2   -5.389659E+0   -5.417358E-3   
2.057254E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.990000E+2   -1.990000E+2   -4.918112E+0   -4.942703E-3   
2.062302E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.740000E+2   -1.740000E+2   -4.415312E+0   -4.436794E-3   
2.067336E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.490000E+2   -1.490000E+2   -3.879860E+0   -3.898234E-3   
2.072385E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.240000E+2   -1.240000E+2   -3.312091E+0   -3.327354E-3   
2.077373E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.900000E+1   -9.900000E+1   -2.714842E+0   -2.726994E-3   
2.082618E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.400000E+1   -7.400000E+1   -2.076515E+0   -2.085556E-3   
2.087852E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.900000E+1   -4.900000E+1   -1.405526E+0   -1.411454E-3   
2.094012E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.700000E+1   -3.700000E+1   -1.075824E+0   -1.080258E-3   
2.099558E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.800000E+1   -2.800000E+1   -7.942274E-1   -7.975393E-4   
2.105100E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.700000E+1   -1.700000E+1   -5.126330E-1   -5.145756E-4   
2.110262E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.000000E+0   -7.000000E+0   -2.299825E-1   -2.306797E-4   
2.114628E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   2.668498E-2   2.686122E-5   
2.119151E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+1   1.000000E+1   3.082818E-1   3.097035E-4   
2.124458E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.100000E+1   2.100000E+1   6.263953E-1   6.291872E-4   
2.129029E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.000000E+1   3.000000E+1   8.777924E-1   8.817052E-4   
2.134332E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.100000E+1   4.100000E+1   1.189238E+0   1.194520E-3   
2.139640E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.100000E+1   5.100000E+1   1.458891E+0   1.465419E-3   
2.146180E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.600000E+1   7.600000E+1   2.124263E+0   2.133904E-3   
2.151956E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.010000E+2   1.010000E+2   2.753818E+0   2.766571E-3   
2.157723E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.250000E+2   1.250000E+2   3.353174E+0   3.368913E-3   
2.163491E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.510000E+2   1.510000E+2   3.921997E+0   3.940970E-3   
2.169257E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.750000E+2   1.750000E+2   4.447966E+0   4.469925E-3   
2.175003E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.000000E+2   2.000000E+2   4.950763E+0   4.975830E-3   
2.180830E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.260000E+2   2.260000E+2   5.422310E+0   5.450609E-3   
2.186605E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.510000E+2   2.510000E+2   5.868228E+0   5.899634E-3   
2.192393E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.760000E+2   2.760000E+2   6.292028E+0   6.326540E-3   
2.198162E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.010000E+2   3.010000E+2   6.689123E+0   6.726741E-3   
2.203933E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.250000E+2   3.250000E+2   7.069041E+0   7.109640E-3   
2.209701E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.510000E+2   3.510000E+2   7.431063E+0   7.474891E-3   
2.215483E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.760000E+2   3.760000E+2   7.774824E+0   7.821756E-3   
2.221243E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.000000E+2   4.000000E+2   8.101018E+0   8.150930E-3   
2.227092E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.260000E+2   4.260000E+2   8.412097E+0   8.465236E-3   
2.232863E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.510000E+2   4.510000E+2   8.715459E+0   8.771701E-3   
2.238645E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.760000E+2   4.760000E+2   9.001243E+0   9.060588E-3   
2.244406E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.010000E+2   5.010000E+2   9.274809E+0   9.337257E-3   
2.250181E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.250000E+2   5.250000E+2   9.537772E+0   9.603198E-3   
2.255941E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.500000E+2   5.500000E+2   9.790568E+0   9.859096E-3   
2.261776E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.750000E+2   5.750000E+2   1.003460E+1   1.010623E-2   
2.267524E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.000000E+2   6.000000E+2   1.027023E+1   1.034496E-2   
2.273406E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.250000E+2   6.250000E+2   1.049349E+1   1.057132E-2   
2.279231E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.500000E+2   6.500000E+2   1.071542E+1   1.079635E-2   
2.285111E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.750000E+2   6.750000E+2   1.092151E+1   1.100554E-2   
2.290925E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.000000E+2   7.000000E+2   1.112904E+1   1.121618E-2   
2.296756E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.250000E+2   7.250000E+2   1.132706E+1   1.141730E-2   
2.302517E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.500000E+2   7.500000E+2   1.152019E+1   1.161352E-2   
2.308348E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.750000E+2   7.750000E+2   1.170345E+1   1.179988E-2   
2.314091E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.000000E+2   8.000000E+2   1.188253E+1   1.198206E-2   
2.319912E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.250000E+2   8.250000E+2   1.205666E+1   1.215929E-2   
2.325725E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.500000E+2   8.500000E+2   1.222697E+1   1.233271E-2   
2.331546E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.750000E+2   8.750000E+2   1.239096E+1   1.249979E-2   
2.337286E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.000000E+2   9.000000E+2   1.255035E+1   1.266228E-2   
2.343106E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.250000E+2   9.250000E+2   1.270519E+1   1.282023E-2   
2.348921E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.500000E+2   9.500000E+2   1.285756E+1   1.297570E-2   
2.354743E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.750000E+2   9.750000E+2   1.300680E+1   1.312803E-2   
2.360603E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+3   1.000000E+3   1.315039E+1   1.327476E-2   
2.370574E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.500000E+3   1.500000E+3   1.542182E+1   1.561167E-2   
2.379710E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.001000E+3   2.001000E+3   1.699412E+1   1.724957E-2   
2.388794E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.500000E+3   2.500000E+3   1.817037E+1   1.849115E-2   
2.397914E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.000000E+3   3.000000E+3   1.910435E+1   1.949057E-2   
2.407041E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.501000E+3   3.501000E+3   1.986906E+1   2.032019E-2   
2.416112E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.001000E+3   4.001000E+3   2.051864E+1   2.103454E-2   
2.425197E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.500000E+3   4.500000E+3   2.108040E+1   2.166094E-2   
2.434332E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.000000E+3   5.000000E+3   2.156847E+1   2.221378E-2   
2.443407E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.501000E+3   5.501000E+3   2.200702E+1   2.271692E-2   
2.452406E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.001000E+3   6.001000E+3   2.240835E+1   2.318272E-2   
2.461412E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.501000E+3   6.501000E+3   2.276262E+1   2.360146E-2   
2.470469E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.000000E+3   7.000000E+3   2.308282E+1   2.398599E-2   
2.479538E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.501000E+3   7.501000E+3   2.337531E+1   2.434257E-2   
2.488534E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.002000E+3   8.002000E+3   2.364533E+1   2.467668E-2   
2.497590E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.501000E+3   8.501000E+3   2.389144E+1   2.498663E-2   
2.506585E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.001000E+3   9.001000E+3   2.412705E+1   2.528620E-2   
2.515605E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.502000E+3   9.502000E+3   2.433982E+1   2.556312E-2   
2.524696E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000200E+4   1.000200E+4   2.455050E+1   2.583782E-2   
2.535748E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.100100E+4   1.100100E+4   2.491811E+1   2.633333E-2   
2.545975E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.200100E+4   1.200100E+4   2.523693E+1   2.677825E-2   
2.556226E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.300100E+4   1.300100E+4   2.552343E+1   2.719085E-2   
2.566457E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.400100E+4   1.400100E+4   2.576747E+1   2.755990E-2   
2.576949E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.500100E+4   1.500100E+4   2.599253E+1   2.791001E-2   
2.587696E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.600100E+4   1.600100E+4   2.617370E+1   2.823542E-2   
2.599447E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.700100E+4   1.700100E+4   2.632574E+1   2.854948E-2   
2.611733E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.800100E+4   1.800100E+4   2.644827E+1   2.884619E-2   
2.624541E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.900100E+4   1.900100E+4   2.652412E+1   2.911516E-2   
@@END Data.
@Time at end of measurement: 15:55:51
@Instrument  Changes:
@Emu Range: 500 uV
@END Instrument  Changes:
First Error: 2016-09-30  09:44:05
32KP Set Field V2

Set Field: Field did not reach target field Target = 20000.000000, Reached = 19000.000000
Start Field18999.000 [Oe]   Field to set 20000.000 [Oe]   Limited Field 19000.000 [Oe]   
Timer at start = 2110169, Timer now = 2112308, difference = 2139, total sweep time + 100 = 767
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = 19000.000
 Timer Now = 2112308
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19000.000
19000.000
 Timer Now = 2112308

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19000.000
19000.000
 Timer Now = 2112308
Error History:
Actions History:
2016-09-30  09:44:05
32KP Set Field V2

Set Field: Field did not reach target field Target = 20000.000000, Reached = 19000.000000
Start Field18999.000 [Oe]   Field to set 20000.000 [Oe]   Limited Field 19000.000 [Oe]   
Timer at start = 2110169, Timer now = 2112308, difference = 2139, total sweep time + 100 = 767
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = 19000.000
 Timer Now = 2112308
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19000.000
19000.000
 Timer Now = 2112308

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19000.000
19000.000
 Timer Now = 2112308

2016-09-30  10:02:14
32KP Set Field V2

Set Field: Field did not reach target field Target = -20000.000000, Reached = -18999.000000
Start Field-18999.000 [Oe]   Field to set -20000.000 [Oe]   Limited Field -19000.000 [Oe]   
Timer at start = 3199402, Timer now = 3201554, difference = 2152, total sweep time + 100 = 767
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = -18999.000
 Timer Now = 3201554
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -18999.000
-18999.000
 Timer Now = 3201554

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -18999.000
-18999.000
 Timer Now = 3201554

2016-09-30  10:02:45
32KP Set Field V2

Set Field: Field did not reach target field Target = -20000.000000, Reached = -18999.000000
Start Field-19000.000 [Oe]   Field to set -20000.000 [Oe]   Limited Field -19000.000 [Oe]   
Timer at start = 3230966, Timer now = 3233028, difference = 2062, total sweep time + 100 = 100
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = -18999.000
 Timer Now = 3233028
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -18999.000
-18999.000
 Timer Now = 3233028

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -18999.000
-18999.000
 Timer Now = 3233028

2016-09-30  10:03:10
32KP Set Field V2

Set Field: Field did not reach target field Target = -20000.000000, Reached = -18999.000000
Start Field-18999.000 [Oe]   Field to set -20000.000 [Oe]   Limited Field -19000.000 [Oe]   
Timer at start = 3254949, Timer now = 3257104, difference = 2155, total sweep time + 100 = 767
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = -18999.000
 Timer Now = 3257104
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -18999.000
-18999.000
 Timer Now = 3257104

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -18999.000
-18999.000
 Timer Now = 3257104

2016-09-30  10:31:00
32KP Set Field V2

Set Field: Field did not reach target field Target = 20000.000000, Reached = 19002.000000
Start Field19001.000 [Oe]   Field to set 20000.000 [Oe]   Limited Field 19000.000 [Oe]   
Timer at start = 4925033, Timer now = 4927169, difference = 2136, total sweep time + 100 = 767
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = 19002.000
 Timer Now = 4927169
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19002.000
19002.000
 Timer Now = 4927169

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19002.000
19002.000
 Timer Now = 4927169

2016-09-30  10:49:21
32KP Set Field V2

Set Field: Field did not reach target field Target = -20000.000000, Reached = -19000.000000
Start Field-18999.000 [Oe]   Field to set -20000.000 [Oe]   Limited Field -19000.000 [Oe]   
Timer at start = 6026443, Timer now = 6028583, difference = 2140, total sweep time + 100 = 767
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = -19000.000
 Timer Now = 6028583
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19000.000
-19000.000
 Timer Now = 6028583

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19000.000
-19000.000
 Timer Now = 6028583

2016-09-30  10:49:51
32KP Set Field V2

Set Field: Field did not reach target field Target = -20000.000000, Reached = -19000.000000
Start Field-19000.000 [Oe]   Field to set -20000.000 [Oe]   Limited Field -19000.000 [Oe]   
Timer at start = 6056803, Timer now = 6058863, difference = 2060, total sweep time + 100 = 100
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = -19000.000
 Timer Now = 6058863
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19000.000
-19000.000
 Timer Now = 6058863

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19000.000
-19000.000
 Timer Now = 6058863

2016-09-30  10:50:15
32KP Set Field V2

Set Field: Field did not reach target field Target = -20000.000000, Reached = -19000.000000
Start Field-19000.000 [Oe]   Field to set -20000.000 [Oe]   Limited Field -19000.000 [Oe]   
Timer at start = 6080458, Timer now = 6082534, difference = 2076, total sweep time + 100 = 100
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = -19000.000
 Timer Now = 6082534
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19000.000
-19000.000
 Timer Now = 6082534

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19000.000
-19000.000
 Timer Now = 6082534

2016-09-30  11:07:29
32KP Set Field V2

Set Field: Field did not reach target field Target = 20000.000000, Reached = 19002.000000
Start Field19002.000 [Oe]   Field to set 20000.000 [Oe]   Limited Field 19000.000 [Oe]   
Timer at start = 7114734, Timer now = 7116886, difference = 2152, total sweep time + 100 = 773
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = 19002.000
 Timer Now = 7116886
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19002.000
19002.000
 Timer Now = 7116886

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19002.000
19002.000
 Timer Now = 7116886

2016-09-30  11:25:08
32KP Set Field V2

Set Field: Field did not reach target field Target = 20000.000000, Reached = 19002.000000
Start Field19002.000 [Oe]   Field to set 20000.000 [Oe]   Limited Field 19000.000 [Oe]   
Timer at start = 8173294, Timer now = 8175430, difference = 2136, total sweep time + 100 = 773
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = 19002.000
 Timer Now = 8175430
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19002.000
19002.000
 Timer Now = 8175430

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19002.000
19002.000
 Timer Now = 8175430

2016-09-30  11:43:35
32KP Set Field V2

Set Field: Field did not reach target field Target = -20000.000000, Reached = -19000.000000
Start Field-19000.000 [Oe]   Field to set -20000.000 [Oe]   Limited Field -19000.000 [Oe]   
Timer at start = 9280854, Timer now = 9282914, difference = 2060, total sweep time + 100 = 100
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = -19000.000
 Timer Now = 9282914
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19000.000
-19000.000
 Timer Now = 9282914

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19000.000
-19000.000
 Timer Now = 9282914

2016-09-30  11:44:02
32KP Set Field V2

Set Field: Field did not reach target field Target = -20000.000000, Reached = -19000.000000
Start Field-19001.000 [Oe]   Field to set -20000.000 [Oe]   Limited Field -19000.000 [Oe]   
Timer at start = 9307477, Timer now = 9309619, difference = 2142, total sweep time + 100 = 767
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = -19000.000
 Timer Now = 9309619
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19000.000
-19000.000
 Timer Now = 9309619

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19000.000
-19000.000
 Timer Now = 9309619

2016-09-30  11:44:25
32KP Set Field V2

Set Field: Field did not reach target field Target = -20000.000000, Reached = -19000.000000
Start Field-19000.000 [Oe]   Field to set -20000.000 [Oe]   Limited Field -19000.000 [Oe]   
Timer at start = 9330458, Timer now = 9332519, difference = 2061, total sweep time + 100 = 100
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = -19000.000
 Timer Now = 9332519
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19000.000
-19000.000
 Timer Now = 9332519

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19000.000
-19000.000
 Timer Now = 9332519

2016-09-30  12:01:41
32KP Set Field V2

Set Field: Field did not reach target field Target = 20000.000000, Reached = 19002.000000
Start Field19002.000 [Oe]   Field to set 20000.000 [Oe]   Limited Field 19000.000 [Oe]   
Timer at start = 10366049, Timer now = 10368185, difference = 2136, total sweep time + 100 = 773
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = 19002.000
 Timer Now = 10368185
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19002.000
19002.000
 Timer Now = 10368185

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19002.000
19002.000
 Timer Now = 10368185

2016-09-30  13:10:59
32KP Set Field V2

Set Field: Field did not reach target field Target = 20000.000000, Reached = 19003.000000
Start Field19002.000 [Oe]   Field to set 20000.000 [Oe]   Limited Field 19000.000 [Oe]   
Timer at start = 14524875, Timer now = 14527027, difference = 2152, total sweep time + 100 = 773
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = 19003.000
 Timer Now = 14527027
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19003.000
19003.000
 Timer Now = 14527027

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19003.000
19003.000
 Timer Now = 14527027

2016-09-30  13:29:28
32KP Set Field V2

Set Field: Field did not reach target field Target = -20000.000000, Reached = -19000.000000
Start Field-19000.000 [Oe]   Field to set -20000.000 [Oe]   Limited Field -19000.000 [Oe]   
Timer at start = 15633446, Timer now = 15635516, difference = 2070, total sweep time + 100 = 100
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = -19000.000
 Timer Now = 15635516
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19000.000
-19000.000
 Timer Now = 15635516

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19000.000
-19000.000
 Timer Now = 15635516

2016-09-30  13:29:57
32KP Set Field V2

Set Field: Field did not reach target field Target = -20000.000000, Reached = -19001.000000
Start Field-19000.000 [Oe]   Field to set -20000.000 [Oe]   Limited Field -19000.000 [Oe]   
Timer at start = 15662727, Timer now = 15664789, difference = 2062, total sweep time + 100 = 100
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = -19001.000
 Timer Now = 15664789
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19001.000
-19000.000
 Timer Now = 15664789

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19001.000
-19000.000
 Timer Now = 15664789

2016-09-30  13:30:20
32KP Set Field V2

Set Field: Field did not reach target field Target = -20000.000000, Reached = -19001.000000
Start Field-19001.000 [Oe]   Field to set -20000.000 [Oe]   Limited Field -19000.000 [Oe]   
Timer at start = 15685825, Timer now = 15687974, difference = 2149, total sweep time + 100 = 767
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = -19001.000
 Timer Now = 15687974
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19001.000
-19000.000
 Timer Now = 15687974

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = TRUE; Stable=  TRUE; Stability Array = -19001.000
-19000.000
 Timer Now = 15687974

2016-09-30  13:47:34
32KP Set Field V2

Set Field: Field did not reach target field Target = 20000.000000, Reached = 19003.000000
Start Field19003.000 [Oe]   Field to set 20000.000 [Oe]   Limited Field 19000.000 [Oe]   
Timer at start = 16719735, Timer now = 16721874, difference = 2139, total sweep time + 100 = 780
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  FALSE; Stability Array = 19003.000
 Timer Now = 16721874
Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19003.000
19002.000
 Timer Now = 16721874

Reason wait ended:Stop Global = FALSE; Decreased Precision = FALSE; Slow Approach = FALSE; >=20 seconds =  FALSE; Field reached = FALSE; Stable=  TRUE; Stability Array = 19003.000
19002.000
 Timer Now = 16721874

@@Final Manipulated Data
New Section: Section 0: 
1.442600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.000000E+0   -7.000000E+0   -2.178575E-1   -2.185543E-4   
1.879600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   3.290911E-2   3.308551E-5   
2.424900E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+1   1.000000E+1   3.115678E-1   3.129896E-4   
3.047800E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.100000E+1   2.100000E+1   6.089162E-1   6.117077E-4   
3.578000E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.100000E+1   3.100000E+1   8.784098E-1   8.824464E-4   
4.108500E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.100000E+1   4.100000E+1   1.154245E+0   1.159527E-3   
4.730500E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.100000E+1   5.100000E+1   1.425867E+0   1.432394E-3   
5.394900E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.600000E+1   7.600000E+1   2.074210E+0   2.083849E-3   
5.967600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+2   1.000000E+2   2.692503E+0   2.705130E-3   
6.665200E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.260000E+2   1.260000E+2   3.285320E+0   3.301181E-3   
7.242000E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.510000E+2   1.510000E+2   3.842422E+0   3.861393E-3   
7.818600E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.750000E+2   1.750000E+2   4.365760E+0   4.387716E-3   
8.393300E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.000000E+2   2.000000E+2   4.863599E+0   4.888664E-3   
8.975300E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.250000E+2   2.250000E+2   5.332383E+0   5.360556E-3   
9.551200E+1   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.500000E+2   2.500000E+2   5.776633E+0   5.807912E-3   
1.022850E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.750000E+2   2.750000E+2   6.194324E+0   6.228709E-3   
1.080290E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.000000E+2   3.000000E+2   6.596262E+0   6.633753E-3   
1.138620E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.260000E+2   3.260000E+2   6.975296E+0   7.016016E-3   
1.196190E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.500000E+2   3.500000E+2   7.333736E+0   7.377437E-3   
1.254350E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.750000E+2   3.750000E+2   7.675188E+0   7.721993E-3   
1.311840E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.000000E+2   4.000000E+2   8.004104E+0   8.054013E-3   
1.370040E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.250000E+2   4.250000E+2   8.317126E+0   8.370139E-3   
1.427760E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.510000E+2   4.510000E+2   8.618108E+0   8.674348E-3   
1.485510E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.750000E+2   4.750000E+2   8.903480E+0   8.962698E-3   
1.543010E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.000000E+2   5.000000E+2   9.178236E+0   9.240557E-3   
1.601350E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.250000E+2   5.250000E+2   9.440163E+0   9.505586E-3   
1.658970E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.500000E+2   5.500000E+2   9.694089E+0   9.762614E-3   
1.717300E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.750000E+2   5.750000E+2   9.937778E+0   1.000940E-2   
1.774770E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.000000E+2   6.000000E+2   1.017364E+1   1.024837E-2   
1.833080E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.250000E+2   6.250000E+2   1.039951E+1   1.047734E-2   
1.891910E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.500000E+2   6.500000E+2   1.061613E+1   1.069706E-2   
1.950720E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.750000E+2   6.750000E+2   1.082672E+1   1.091075E-2   
2.008960E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.000000E+2   7.000000E+2   1.103520E+1   1.112233E-2   
2.068790E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.250000E+2   7.250000E+2   1.123024E+1   1.132048E-2   
2.126530E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.500000E+2   7.500000E+2   1.142309E+1   1.151643E-2   
2.184850E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.750000E+2   7.750000E+2   1.160777E+1   1.170420E-2   
2.251580E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.000000E+2   8.000000E+2   1.177965E+1   1.187918E-2   
2.309660E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.250000E+2   8.250000E+2   1.195941E+1   1.206205E-2   
2.367760E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.500000E+2   8.500000E+2   1.213076E+1   1.223650E-2   
2.425870E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.750000E+2   8.750000E+2   1.229264E+1   1.240147E-2   
2.483270E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.000000E+2   9.000000E+2   1.245764E+1   1.256957E-2   
2.541490E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.250000E+2   9.250000E+2   1.261074E+1   1.272577E-2   
2.599620E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.500000E+2   9.500000E+2   1.276278E+1   1.288091E-2   
2.657830E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.750000E+2   9.750000E+2   1.290988E+1   1.303111E-2   
2.718050E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+3   1.000000E+3   1.305208E+1   1.317644E-2   
2.817780E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.500000E+3   1.500000E+3   1.532632E+1   1.551617E-2   
2.908950E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.000000E+3   2.000000E+3   1.689722E+1   1.715253E-2   
3.000300E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.500000E+3   2.500000E+3   1.807871E+1   1.839949E-2   
3.091500E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.000000E+3   3.000000E+3   1.901515E+1   1.940137E-2   
3.182820E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.500000E+3   3.500000E+3   1.979007E+1   2.024106E-2   
3.274030E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.001000E+3   4.001000E+3   2.044173E+1   2.095762E-2   
3.364930E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.500000E+3   4.500000E+3   2.100283E+1   2.158337E-2   
3.456280E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.000000E+3   5.000000E+3   2.150106E+1   2.214636E-2   
3.547020E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.501000E+3   5.501000E+3   2.194205E+1   2.265196E-2   
3.639470E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.001000E+3   6.001000E+3   2.233531E+1   2.310968E-2   
3.730160E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.500000E+3   6.500000E+3   2.269239E+1   2.353110E-2   
3.821410E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.000000E+3   7.000000E+3   2.301682E+1   2.391999E-2   
3.912100E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.501000E+3   7.501000E+3   2.330859E+1   2.427585E-2   
4.006680E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.002000E+3   8.002000E+3   2.357895E+1   2.461030E-2   
4.096790E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.501000E+3   8.501000E+3   2.383421E+1   2.492940E-2   
4.186730E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.001000E+3   9.001000E+3   2.406806E+1   2.522721E-2   
4.276850E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.501000E+3   9.501000E+3   2.428576E+1   2.550893E-2   
4.367560E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000200E+4   1.000200E+4   2.448729E+1   2.577461E-2   
4.478160E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.100100E+4   1.100100E+4   2.485913E+1   2.627435E-2   
4.580430E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.200100E+4   1.200100E+4   2.518111E+1   2.672243E-2   
4.682990E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.300100E+4   1.300100E+4   2.547217E+1   2.713959E-2   
4.785310E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.400100E+4   1.400100E+4   2.572287E+1   2.751529E-2   
4.892730E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.500100E+4   1.500100E+4   2.594864E+1   2.786611E-2   
5.000100E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.600100E+4   1.600100E+4   2.612419E+1   2.818587E-2   
5.117600E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.700100E+4   1.700100E+4   2.628396E+1   2.850761E-2   
5.240530E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.800100E+4   1.800100E+4   2.639422E+1   2.879191E-2   
5.363420E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.900000E+4   1.900000E+4   2.648759E+1   2.907838E-2   
5.499540E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.800600E+4   1.800600E+4   2.639877E+1   2.879752E-2   
5.622400E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.700500E+4   1.700500E+4   2.628572E+1   2.851005E-2   
5.725640E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.600700E+4   1.600700E+4   2.614351E+1   2.820620E-2   
5.838230E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.500500E+4   1.500500E+4   2.595144E+1   2.786948E-2   
5.946360E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.400500E+4   1.400500E+4   2.573869E+1   2.753162E-2   
6.054680E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.300400E+4   1.300400E+4   2.548869E+1   2.715648E-2   
6.163030E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.200400E+4   1.200400E+4   2.519691E+1   2.673861E-2   
6.271420E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.100300E+4   1.100300E+4   2.487915E+1   2.629462E-2   
6.373980E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000400E+4   1.000400E+4   2.451469E+1   2.580226E-2   
6.479250E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.503000E+3   9.503000E+3   2.430683E+1   2.553025E-2   
6.575880E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.003000E+3   9.003000E+3   2.409615E+1   2.525555E-2   
6.672800E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.502000E+3   8.502000E+3   2.386372E+1   2.495904E-2   
6.774720E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.002000E+3   8.002000E+3   2.361373E+1   2.464508E-2   
6.876490E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.503000E+3   7.503000E+3   2.334512E+1   2.431264E-2   
6.973270E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.002000E+3   7.002000E+3   2.304632E+1   2.394975E-2   
7.070190E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.502000E+3   6.502000E+3   2.273137E+1   2.357033E-2   
7.166950E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.002000E+3   6.002000E+3   2.237710E+1   2.315160E-2   
7.263860E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.502000E+3   5.502000E+3   2.198490E+1   2.269493E-2   
7.360670E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.002000E+3   5.002000E+3   2.155196E+1   2.219752E-2   
7.457660E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.502000E+3   4.502000E+3   2.106252E+1   2.164332E-2   
7.554480E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.002000E+3   4.002000E+3   2.049934E+1   2.101537E-2   
7.651450E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.502000E+3   3.502000E+3   1.984941E+1   2.030067E-2   
7.745640E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.002000E+3   3.002000E+3   1.908187E+1   1.946835E-2   
7.842600E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.502000E+3   2.502000E+3   1.814087E+1   1.846191E-2   
7.939320E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.002000E+3   2.002000E+3   1.695796E+1   1.721354E-2   
8.033220E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.502000E+3   1.502000E+3   1.538953E+1   1.557964E-2   
8.130020E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.001000E+3   1.001000E+3   1.311705E+1   1.324155E-2   
8.197690E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.750000E+2   9.750000E+2   1.296889E+1   1.309012E-2   
8.257830E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.500000E+2   9.500000E+2   1.281965E+1   1.293778E-2   
8.316730E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.260000E+2   9.260000E+2   1.266938E+1   1.278453E-2   
8.375800E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.000000E+2   9.000000E+2   1.251384E+1   1.262577E-2   
8.434500E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.750000E+2   8.750000E+2   1.235267E+1   1.246150E-2   
8.494770E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.500000E+2   8.500000E+2   1.219150E+1   1.229723E-2   
8.553490E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.250000E+2   8.250000E+2   1.202088E+1   1.212351E-2   
8.611550E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.000000E+2   8.000000E+2   1.184776E+1   1.194729E-2   
8.670490E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.750000E+2   7.750000E+2   1.167044E+1   1.176687E-2   
8.730960E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.500000E+2   7.500000E+2   1.148084E+1   1.157417E-2   
8.789800E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.250000E+2   7.250000E+2   1.129194E+1   1.138218E-2   
8.847380E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.000000E+2   7.000000E+2   1.109566E+1   1.118280E-2   
8.906310E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.750000E+2   6.750000E+2   1.088958E+1   1.097361E-2   
8.964550E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.500000E+2   6.500000E+2   1.067784E+1   1.075878E-2   
9.024900E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.250000E+2   6.250000E+2   1.046191E+1   1.053974E-2   
9.083220E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.010000E+2   6.010000E+2   1.023718E+1   1.031203E-2   
9.142780E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.760000E+2   5.760000E+2   1.000267E+1   1.007442E-2   
9.202270E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.510000E+2   5.510000E+2   9.757556E+0   9.826207E-3   
9.261840E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.260000E+2   5.260000E+2   9.506174E+0   9.571723E-3   
9.321150E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.010000E+2   5.010000E+2   9.240384E+0   9.302830E-3   
9.380680E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.760000E+2   4.760000E+2   8.968608E+0   9.027952E-3   
9.440280E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.510000E+2   4.510000E+2   8.684556E+0   8.740797E-3   
9.499820E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.260000E+2   4.260000E+2   8.386472E+0   8.439611E-3   
9.559160E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.010000E+2   4.010000E+2   8.076772E+0   8.126807E-3   
9.618680E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.760000E+2   3.760000E+2   7.748480E+0   7.795411E-3   
9.678260E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.510000E+2   3.510000E+2   7.407206E+0   7.451033E-3   
9.737860E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.260000E+2   3.260000E+2   7.046221E+0   7.086943E-3   
9.797130E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.010000E+2   3.010000E+2   6.668777E+0   6.706394E-3   
9.856620E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.760000E+2   2.760000E+2   6.275887E+0   6.310399E-3   
9.916060E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.510000E+2   2.510000E+2   5.855238E+0   5.886643E-3   
9.975500E+2   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.260000E+2   2.260000E+2   5.407916E+0   5.436214E-3   
1.003490E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.010000E+2   2.010000E+2   4.938124E+0   4.963314E-3   
1.009437E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.760000E+2   1.760000E+2   4.437781E+0   4.459863E-3   
1.015383E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.510000E+2   1.510000E+2   3.910405E+0   3.929378E-3   
1.021331E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.260000E+2   1.260000E+2   3.351067E+0   3.366931E-3   
1.027261E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.010000E+2   1.010000E+2   2.753116E+0   2.765869E-3   
1.033074E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.600000E+1   7.600000E+1   2.122859E+0   2.132500E-3   
1.038879E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.100000E+1   5.100000E+1   1.458891E+0   1.465419E-3   
1.045116E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.100000E+1   4.100000E+1   1.185727E+0   1.191009E-3   
1.050524E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.100000E+1   3.100000E+1   9.058854E-1   9.099228E-4   
1.055923E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.100000E+1   2.100000E+1   6.232355E-1   6.260273E-4   
1.061312E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.100000E+1   1.100000E+1   3.384778E-1   3.400241E-4   
1.066543E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   5.688125E-2   5.705827E-5   
1.071794E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.000000E+0   -7.000000E+0   -2.243646E-1   -2.250616E-4   
1.077544E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.700000E+1   -1.700000E+1   -5.070151E-1   -5.089576E-4   
1.083297E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.700000E+1   -2.700000E+1   -7.868546E-1   -7.900425E-4   
1.088819E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.700000E+1   -3.700000E+1   -1.065291E+0   -1.069725E-3   
1.094579E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.700000E+1   -4.700000E+1   -1.341622E+0   -1.347300E-3   
1.101940E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.200000E+1   -7.200000E+1   -2.010154E+0   -2.018945E-3   
1.108142E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.700000E+1   -9.700000E+1   -2.642512E+0   -2.654415E-3   
1.114515E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.220000E+2   -1.220000E+2   -3.247484E+0   -3.262499E-3   
1.121289E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.470000E+2   -1.470000E+2   -3.813147E+0   -3.831271E-3   
1.127808E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.720000E+2   -1.720000E+2   -4.350003E+0   -4.371237E-3   
1.133824E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.970000E+2   -1.970000E+2   -4.848941E+0   -4.873283E-3   
1.140138E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.220000E+2   -2.220000E+2   -5.322595E+0   -5.350045E-3   
1.146662E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.470000E+2   -2.470000E+2   -5.773780E+0   -5.804336E-3   
1.153442E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.720000E+2   -2.720000E+2   -6.198271E+0   -6.231934E-3   
1.160266E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.970000E+2   -2.970000E+2   -6.598206E+0   -6.634974E-3   
1.166323E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.220000E+2   -3.220000E+2   -6.977758E+0   -7.017632E-3   
1.172792E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.470000E+2   -3.470000E+2   -7.342938E+0   -7.385916E-3   
1.179605E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.720000E+2   -3.720000E+2   -7.687723E+0   -7.733806E-3   
1.185614E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.970000E+2   -3.970000E+2   -8.015331E+0   -8.064518E-3   
1.191623E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.220000E+2   -4.220000E+2   -8.330993E+0   -8.383284E-3   
1.198435E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.470000E+2   -4.470000E+2   -8.634013E+0   -8.689407E-3   
1.204442E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.720000E+2   -4.720000E+2   -8.919833E+0   -8.978329E-3   
1.210501E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.970000E+2   -4.970000E+2   -9.195425E+0   -9.257024E-3   
1.216864E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.220000E+2   -5.220000E+2   -9.462960E+0   -9.527661E-3   
1.222935E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.470000E+2   -5.470000E+2   -9.714730E+0   -9.782534E-3   
1.228949E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.720000E+2   -5.720000E+2   -9.955957E+0   -1.002686E-2   
1.235479E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.970000E+2   -5.970000E+2   -1.019436E+1   -1.026836E-2   
1.241492E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.230000E+2   -6.230000E+2   -1.042189E+1   -1.049912E-2   
1.247511E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.480000E+2   -6.480000E+2   -1.064447E+1   -1.072480E-2   
1.253923E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.730000E+2   -6.730000E+2   -1.085517E+1   -1.093860E-2   
1.259892E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.980000E+2   -6.980000E+2   -1.105812E+1   -1.114465E-2   
1.265854E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.230000E+2   -7.230000E+2   -1.125716E+1   -1.134680E-2   
1.272330E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.480000E+2   -7.480000E+2   -1.144962E+1   -1.154235E-2   
1.278291E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.730000E+2   -7.730000E+2   -1.163570E+1   -1.173154E-2   
1.284308E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.980000E+2   -7.980000E+2   -1.181547E+1   -1.191440E-2   
1.290720E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.230000E+2   -8.230000E+2   -1.199245E+1   -1.209448E-2   
1.296731E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.480000E+2   -8.480000E+2   -1.216063E+1   -1.226576E-2   
1.302734E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.730000E+2   -8.730000E+2   -1.232669E+1   -1.243492E-2   
1.309202E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.980000E+2   -8.980000E+2   -1.248715E+1   -1.259849E-2   
1.315154E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.230000E+2   -9.230000E+2   -1.264479E+1   -1.275922E-2   
1.321164E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.480000E+2   -9.480000E+2   -1.279506E+1   -1.291259E-2   
1.327625E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.730000E+2   -9.730000E+2   -1.294254E+1   -1.306317E-2   
1.333587E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.980000E+2   -9.980000E+2   -1.308789E+1   -1.321162E-2   
1.344180E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.497000E+3   -1.497000E+3   -1.536567E+1   -1.555483E-2   
1.353939E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.996000E+3   -1.996000E+3   -1.694498E+1   -1.719959E-2   
1.363711E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.497000E+3   -2.497000E+3   -1.812578E+1   -1.844608E-2   
1.373474E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.997000E+3   -2.997000E+3   -1.906220E+1   -1.944806E-2   
1.383237E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.497000E+3   -3.497000E+3   -1.982938E+1   -2.028059E-2   
1.392987E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.997000E+3   -3.997000E+3   -2.048176E+1   -2.099831E-2   
1.403239E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.498000E+3   -4.498000E+3   -2.103934E+1   -2.162136E-2   
1.413141E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.998000E+3   -4.998000E+3   -2.153651E+1   -2.218386E-2   
1.422906E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.497000E+3   -5.497000E+3   -2.197120E+1   -2.268237E-2   
1.433159E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.998000E+3   -5.998000E+3   -2.236375E+1   -2.313898E-2   
1.443357E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.498000E+3   -6.498000E+3   -2.272750E+1   -2.356667E-2   
1.452774E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.998000E+3   -6.998000E+3   -2.304737E+1   -2.395047E-2   
1.462501E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.498000E+3   -7.498000E+3   -2.334266E+1   -2.431050E-2   
1.472406E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.997000E+3   -7.997000E+3   -2.361441E+1   -2.464686E-2   
1.482133E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.498000E+3   -8.498000E+3   -2.387074E+1   -2.496807E-2   
1.492333E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.998000E+3   -8.998000E+3   -2.409650E+1   -2.525856E-2   
1.502539E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.498000E+3   -9.498000E+3   -2.430963E+1   -2.553521E-2   
1.512448E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.998000E+3   -9.998000E+3   -2.451573E+1   -2.580483E-2   
1.524099E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.099800E+4   -1.099800E+4   -2.488616E+1   -2.630227E-2   
1.534920E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.199800E+4   -1.199800E+4   -2.520532E+1   -2.674895E-2   
1.545746E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.299900E+4   -1.299900E+4   -2.548903E+1   -2.716031E-2   
1.557075E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.399800E+4   -1.399800E+4   -2.573936E+1   -2.753440E-2   
1.567899E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.499800E+4   -1.499800E+4   -2.596234E+1   -2.788125E-2   
1.579224E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.599700E+4   -1.599700E+4   -2.614351E+1   -2.820607E-2   
1.591576E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.699900E+4   -1.699900E+4   -2.629590E+1   -2.852150E-2   
1.604425E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.799800E+4   -1.799800E+4   -2.641845E+1   -2.882040E-2   
1.617766E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.899800E+4   -1.899800E+4   -2.650482E+1   -2.910045E-2   
1.631896E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.800200E+4   -1.800200E+4   -2.641597E+1   -2.881872E-2   
1.644198E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.700200E+4   -1.700200E+4   -2.629905E+1   -2.852517E-2   
1.656496E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.600100E+4   -1.600100E+4   -2.614807E+1   -2.821132E-2   
1.667787E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.500100E+4   -1.500100E+4   -2.596269E+1   -2.788202E-2   
1.678581E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.400100E+4   -1.400100E+4   -2.575694E+1   -2.755235E-2   
1.689381E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.300100E+4   -1.300100E+4   -2.550308E+1   -2.717462E-2   
1.699891E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.200100E+4   -1.200100E+4   -2.522357E+1   -2.676759E-2   
1.710687E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.100000E+4   -1.100000E+4   -2.489599E+1   -2.631236E-2   
1.720654E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.000000E+4   -1.000000E+4   -2.453506E+1   -2.582440E-2   
1.730580E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.500000E+3   -9.500000E+3   -2.433841E+1   -2.556425E-2   
1.739642E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.000000E+3   -9.000000E+3   -2.411969E+1   -2.528201E-2   
1.748743E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.499000E+3   -8.499000E+3   -2.388513E+1   -2.498258E-2   
1.757814E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.999000E+3   -7.999000E+3   -2.363726E+1   -2.466997E-2   
1.766905E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.499000E+3   -7.499000E+3   -2.336547E+1   -2.433343E-2   
1.775970E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.000000E+3   -7.000000E+3   -2.307298E+1   -2.397634E-2   
1.785064E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.499000E+3   -6.499000E+3   -2.275630E+1   -2.359559E-2   
1.794146E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.999000E+3   -5.999000E+3   -2.240905E+1   -2.318441E-2   
1.803179E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.499000E+3   -5.499000E+3   -2.201896E+1   -2.273039E-2   
1.812260E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.999000E+3   -4.999000E+3   -2.158392E+1   -2.223140E-2   
1.821296E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.499000E+3   -4.499000E+3   -2.109307E+1   -2.167521E-2   
1.830315E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.998000E+3   -3.998000E+3   -2.053479E+1   -2.105147E-2   
1.839338E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.499000E+3   -3.499000E+3   -1.988417E+1   -2.033564E-2   
1.848353E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.999000E+3   -2.999000E+3   -1.911557E+1   -1.950169E-2   
1.857379E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.499000E+3   -2.499000E+3   -1.817494E+1   -1.849551E-2   
1.866399E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.998000E+3   -1.998000E+3   -1.699342E+1   -1.724830E-2   
1.875428E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.499000E+3   -1.499000E+3   -1.541831E+1   -1.560774E-2   
1.884448E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.990000E+2   -9.990000E+2   -1.313814E+1   -1.326200E-2   
1.891085E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.730000E+2   -9.730000E+2   -1.298750E+1   -1.310813E-2   
1.896850E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.480000E+2   -9.480000E+2   -1.283791E+1   -1.295545E-2   
1.902603E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.230000E+2   -9.230000E+2   -1.268693E+1   -1.280137E-2   
1.908363E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.980000E+2   -8.980000E+2   -1.253033E+1   -1.264167E-2   
1.914126E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.730000E+2   -8.730000E+2   -1.236951E+1   -1.247775E-2   
1.919107E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.500000E+2   -8.500000E+2   -1.221783E+1   -1.232321E-2   
1.924915E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -8.230000E+2   -8.230000E+2   -1.202997E+1   -1.213201E-2   
1.930666E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.980000E+2   -7.980000E+2   -1.185513E+1   -1.195407E-2   
1.936427E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.730000E+2   -7.730000E+2   -1.167712E+1   -1.177295E-2   
1.941405E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.500000E+2   -7.500000E+2   -1.150613E+1   -1.159911E-2   
1.947226E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.230000E+2   -7.230000E+2   -1.129861E+1   -1.138825E-2   
1.952994E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.980000E+2   -6.980000E+2   -1.109705E+1   -1.118359E-2   
1.958754E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.730000E+2   -6.730000E+2   -1.089169E+1   -1.097512E-2   
1.963735E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.500000E+2   -6.500000E+2   -1.069854E+1   -1.077913E-2   
1.968785E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.250000E+2   -6.250000E+2   -1.048123E+1   -1.055872E-2   
1.973810E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -6.000000E+2   -6.000000E+2   -1.025335E+1   -1.032772E-2   
1.979635E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.730000E+2   -5.730000E+2   -9.998429E+0   -1.006946E-2   
1.984616E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.500000E+2   -5.500000E+2   -9.773709E+0   -9.841885E-3   
1.990440E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -5.230000E+2   -5.230000E+2   -9.498434E+0   -9.563260E-3   
1.995417E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.990000E+2   -4.990000E+2   -9.253367E+0   -9.315215E-3   
2.000467E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.750000E+2   -4.750000E+2   -8.980213E+0   -9.039082E-3   
2.005493E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.500000E+2   -4.500000E+2   -8.694747E+0   -8.750514E-3   
2.010542E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.250000E+2   -4.250000E+2   -8.393847E+0   -8.446511E-3   
2.015555E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.000000E+2   -4.000000E+2   -8.077467E+0   -8.127027E-3   
2.021671E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.720000E+2   -3.720000E+2   -7.723197E+0   -7.769281E-3   
2.026973E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.490000E+2   -3.490000E+2   -7.405097E+0   -7.448325E-3   
2.032032E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.240000E+2   -3.240000E+2   -7.044100E+0   -7.084223E-3   
2.037075E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.990000E+2   -2.990000E+2   -6.662085E+0   -6.699103E-3   
2.042122E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.750000E+2   -2.750000E+2   -6.262869E+0   -6.296905E-3   
2.047172E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.490000E+2   -2.490000E+2   -5.837333E+0   -5.868139E-3   
2.052226E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.240000E+2   -2.240000E+2   -5.389659E+0   -5.417358E-3   
2.057254E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.990000E+2   -1.990000E+2   -4.918112E+0   -4.942703E-3   
2.062302E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.740000E+2   -1.740000E+2   -4.415312E+0   -4.436794E-3   
2.067336E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.490000E+2   -1.490000E+2   -3.879860E+0   -3.898234E-3   
2.072385E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.240000E+2   -1.240000E+2   -3.312091E+0   -3.327354E-3   
2.077373E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -9.900000E+1   -9.900000E+1   -2.714842E+0   -2.726994E-3   
2.082618E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.400000E+1   -7.400000E+1   -2.076515E+0   -2.085556E-3   
2.087852E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -4.900000E+1   -4.900000E+1   -1.405526E+0   -1.411454E-3   
2.094012E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -3.700000E+1   -3.700000E+1   -1.075824E+0   -1.080258E-3   
2.099558E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -2.800000E+1   -2.800000E+1   -7.942274E-1   -7.975393E-4   
2.105100E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -1.700000E+1   -1.700000E+1   -5.126330E-1   -5.145756E-4   
2.110262E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   -7.000000E+0   -7.000000E+0   -2.299825E-1   -2.306797E-4   
2.114628E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   0.000000E+0   2.668498E-2   2.686122E-5   
2.119151E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+1   1.000000E+1   3.082818E-1   3.097035E-4   
2.124458E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.100000E+1   2.100000E+1   6.263953E-1   6.291872E-4   
2.129029E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.000000E+1   3.000000E+1   8.777924E-1   8.817052E-4   
2.134332E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.100000E+1   4.100000E+1   1.189238E+0   1.194520E-3   
2.139640E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.100000E+1   5.100000E+1   1.458891E+0   1.465419E-3   
2.146180E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.600000E+1   7.600000E+1   2.124263E+0   2.133904E-3   
2.151956E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.010000E+2   1.010000E+2   2.753818E+0   2.766571E-3   
2.157723E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.250000E+2   1.250000E+2   3.353174E+0   3.368913E-3   
2.163491E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.510000E+2   1.510000E+2   3.921997E+0   3.940970E-3   
2.169257E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.750000E+2   1.750000E+2   4.447966E+0   4.469925E-3   
2.175003E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.000000E+2   2.000000E+2   4.950763E+0   4.975830E-3   
2.180830E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.260000E+2   2.260000E+2   5.422310E+0   5.450609E-3   
2.186605E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.510000E+2   2.510000E+2   5.868228E+0   5.899634E-3   
2.192393E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.760000E+2   2.760000E+2   6.292028E+0   6.326540E-3   
2.198162E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.010000E+2   3.010000E+2   6.689123E+0   6.726741E-3   
2.203933E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.250000E+2   3.250000E+2   7.069041E+0   7.109640E-3   
2.209701E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.510000E+2   3.510000E+2   7.431063E+0   7.474891E-3   
2.215483E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.760000E+2   3.760000E+2   7.774824E+0   7.821756E-3   
2.221243E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.000000E+2   4.000000E+2   8.101018E+0   8.150930E-3   
2.227092E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.260000E+2   4.260000E+2   8.412097E+0   8.465236E-3   
2.232863E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.510000E+2   4.510000E+2   8.715459E+0   8.771701E-3   
2.238645E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.760000E+2   4.760000E+2   9.001243E+0   9.060588E-3   
2.244406E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.010000E+2   5.010000E+2   9.274809E+0   9.337257E-3   
2.250181E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.250000E+2   5.250000E+2   9.537772E+0   9.603198E-3   
2.255941E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.500000E+2   5.500000E+2   9.790568E+0   9.859096E-3   
2.261776E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.750000E+2   5.750000E+2   1.003460E+1   1.010623E-2   
2.267524E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.000000E+2   6.000000E+2   1.027023E+1   1.034496E-2   
2.273406E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.250000E+2   6.250000E+2   1.049349E+1   1.057132E-2   
2.279231E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.500000E+2   6.500000E+2   1.071542E+1   1.079635E-2   
2.285111E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.750000E+2   6.750000E+2   1.092151E+1   1.100554E-2   
2.290925E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.000000E+2   7.000000E+2   1.112904E+1   1.121618E-2   
2.296756E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.250000E+2   7.250000E+2   1.132706E+1   1.141730E-2   
2.302517E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.500000E+2   7.500000E+2   1.152019E+1   1.161352E-2   
2.308348E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.750000E+2   7.750000E+2   1.170345E+1   1.179988E-2   
2.314091E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.000000E+2   8.000000E+2   1.188253E+1   1.198206E-2   
2.319912E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.250000E+2   8.250000E+2   1.205666E+1   1.215929E-2   
2.325725E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.500000E+2   8.500000E+2   1.222697E+1   1.233271E-2   
2.331546E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.750000E+2   8.750000E+2   1.239096E+1   1.249979E-2   
2.337286E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.000000E+2   9.000000E+2   1.255035E+1   1.266228E-2   
2.343106E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.250000E+2   9.250000E+2   1.270519E+1   1.282023E-2   
2.348921E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.500000E+2   9.500000E+2   1.285756E+1   1.297570E-2   
2.354743E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.750000E+2   9.750000E+2   1.300680E+1   1.312803E-2   
2.360603E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000000E+3   1.000000E+3   1.315039E+1   1.327476E-2   
2.370574E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.500000E+3   1.500000E+3   1.542182E+1   1.561167E-2   
2.379710E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.001000E+3   2.001000E+3   1.699412E+1   1.724957E-2   
2.388794E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   2.500000E+3   2.500000E+3   1.817037E+1   1.849115E-2   
2.397914E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.000000E+3   3.000000E+3   1.910435E+1   1.949057E-2   
2.407041E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   3.501000E+3   3.501000E+3   1.986906E+1   2.032019E-2   
2.416112E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.001000E+3   4.001000E+3   2.051864E+1   2.103454E-2   
2.425197E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   4.500000E+3   4.500000E+3   2.108040E+1   2.166094E-2   
2.434332E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.000000E+3   5.000000E+3   2.156847E+1   2.221378E-2   
2.443407E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   5.501000E+3   5.501000E+3   2.200702E+1   2.271692E-2   
2.452406E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.001000E+3   6.001000E+3   2.240835E+1   2.318272E-2   
2.461412E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   6.501000E+3   6.501000E+3   2.276262E+1   2.360146E-2   
2.470469E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.000000E+3   7.000000E+3   2.308282E+1   2.398599E-2   
2.479538E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   7.501000E+3   7.501000E+3   2.337531E+1   2.434257E-2   
2.488534E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.002000E+3   8.002000E+3   2.364533E+1   2.467668E-2   
2.497590E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   8.501000E+3   8.501000E+3   2.389144E+1   2.498663E-2   
2.506585E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.001000E+3   9.001000E+3   2.412705E+1   2.528620E-2   
2.515605E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   9.502000E+3   9.502000E+3   2.433982E+1   2.556312E-2   
2.524696E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.000200E+4   1.000200E+4   2.455050E+1   2.583782E-2   
2.535748E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.100100E+4   1.100100E+4   2.491811E+1   2.633333E-2   
2.545975E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.200100E+4   1.200100E+4   2.523693E+1   2.677825E-2   
2.556226E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.300100E+4   1.300100E+4   2.552343E+1   2.719085E-2   
2.566457E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.400100E+4   1.400100E+4   2.576747E+1   2.755990E-2   
2.576949E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.500100E+4   1.500100E+4   2.599253E+1   2.791001E-2   
2.587696E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.600100E+4   1.600100E+4   2.617370E+1   2.823542E-2   
2.599447E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.700100E+4   1.700100E+4   2.632574E+1   2.854948E-2   
2.611733E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.800100E+4   1.800100E+4   2.644827E+1   2.884619E-2   
2.624541E+3   -2.731500E+2   -2.731500E+2   -2.731500E+2   0.000000E+0   0.000000E+0   0.000000E+0   1.900100E+4   1.900100E+4   2.652412E+1   2.911516E-2   
@@END Data.
@Measurement parameters
                                        Upward Part    Downward part  Average        Parameter 'definition'                  
Hysteresis Loop                                                                      Hysteresis Parameters                   
                                                                                                                             
Hc Oe                                   -0.920         0.730          -0.825         Coercive Field: Field at which M//H changes sign
Mr emu                                  33.086E-6      -26.861E-6     -29.973E-6     Remanent Magnetization: M at H=0        
S                                       0.001          0.001          0.001          Squareness: Mr/Ms                       
S*                                      0.130          0.332          0.231          1-(Mr/Hc)(1/slope at Hc)                
M at H max emu                          29.115E-3      -29.100E-3     29.108E-3      M at the maximum field                  
                                                                                                                             

@END Measurement parameters
