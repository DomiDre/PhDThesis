<?xml version="1.0" encoding="UTF-8"?>
<BornAgain Version="1.14.0">
    <DocumentInfo ProjectName="SimulateGISANS"/>
    <DocumentModel Name="DefaultName">
        <Item ModelType="SimulationOptions" Tag="rootTag" DisplayName="SimulationOptions">
            <Item ModelType="Property" Tag="Run Policy" DisplayName="Run Policy">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Immediately;In background"/>
            </Item>
            <Item ModelType="Property" Tag="Number of Threads" DisplayName="Number of Threads">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Max (4 threads);3 threads;2 threads;1 thread"/>
            </Item>
            <Item ModelType="Property" Tag="Computation method" DisplayName="Computation method">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Analytical;Monte-Carlo Integration"/>
            </Item>
            <Item ModelType="Property" Tag="Number of MC points" DisplayName="Number of MC points">
                <Parameter ParType="int" ParRole="0" ParValue="100"/>
            </Item>
            <Item ModelType="Property" Tag="Material for Fresnel calculations" DisplayName="Material for Fresnel calculations">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Ambient Layer Material;Average Layer Material"/>
            </Item>
            <Item ModelType="Property" Tag="Include specular peak" DisplayName="Include specular peak">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="No;Yes"/>
            </Item>
        </Item>
    </DocumentModel>
    <MaterialModel Name="DefaultName">
        <Item ModelType="Material" Tag="rootTag" DisplayName="Material">
            <Item ModelType="Property" Tag="Name" DisplayName="Name">
                <Parameter ParType="QString" ParRole="0" ParValue="Default"/>
            </Item>
            <Item ModelType="Property" Tag="Color" DisplayName="Color">
                <Parameter ParType="ExternalProperty" ParRole="0" Text="[0, 255, 0] (255)" Color="#ff00ff00" Identifier=""/>
            </Item>
            <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Refractive index based;SLD based"/>
                <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                    <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e-3"/>
                    </Item>
                    <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e-5"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                <Item ModelType="Property" Tag="X" DisplayName="X">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Y" DisplayName="Y">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Z" DisplayName="Z">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
            </Item>
            <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                <Parameter ParType="QString" ParRole="0" ParValue="{a380d398-7c39-4370-a0d4-40504ee5db1d}"/>
            </Item>
        </Item>
        <Item ModelType="Material" Tag="rootTag" DisplayName="Material">
            <Item ModelType="Property" Tag="Name" DisplayName="Name">
                <Parameter ParType="QString" ParRole="0" ParValue="Air"/>
            </Item>
            <Item ModelType="Property" Tag="Color" DisplayName="Color">
                <Parameter ParType="ExternalProperty" ParRole="0" Text="[179, 242, 255] (255)" Color="#ffb3f2ff" Identifier=""/>
            </Item>
            <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Refractive index based;SLD based"/>
                <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                    <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                <Item ModelType="Property" Tag="X" DisplayName="X">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Y" DisplayName="Y">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Z" DisplayName="Z">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
            </Item>
            <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                <Parameter ParType="QString" ParRole="0" ParValue="{af03a6f6-c8a4-47a5-8278-80606f5c5a03}"/>
            </Item>
        </Item>
        <Item ModelType="Material" Tag="rootTag" DisplayName="Material">
            <Item ModelType="Property" Tag="Name" DisplayName="Name">
                <Parameter ParType="QString" ParRole="0" ParValue="Particle"/>
            </Item>
            <Item ModelType="Property" Tag="Color" DisplayName="Color">
                <Parameter ParType="ExternalProperty" ParRole="0" Text="[146, 198, 255] (255)" Color="#ff92c6ff" Identifier=""/>
            </Item>
            <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Refractive index based;SLD based"/>
                <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                    <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                        <Parameter ParType="double" ParRole="0" ParValue="6.000000000000e-4"/>
                    </Item>
                    <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                        <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e-8"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                <Item ModelType="Property" Tag="X" DisplayName="X">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Y" DisplayName="Y">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Z" DisplayName="Z">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
            </Item>
            <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                <Parameter ParType="QString" ParRole="0" ParValue="{1fd8d69c-1c34-4b52-8eb6-7856e058cd56}"/>
            </Item>
        </Item>
        <Item ModelType="Material" Tag="rootTag" DisplayName="Material">
            <Item ModelType="Property" Tag="Name" DisplayName="Name">
                <Parameter ParType="QString" ParRole="0" ParValue="Substrate"/>
            </Item>
            <Item ModelType="Property" Tag="Color" DisplayName="Color">
                <Parameter ParType="ExternalProperty" ParRole="0" Text="[205, 102, 0] (255)" Color="#ffcd6600" Identifier=""/>
            </Item>
            <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Refractive index based;SLD based"/>
                <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                    <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                        <Parameter ParType="double" ParRole="0" ParValue="6.000000000000e-6"/>
                    </Item>
                    <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                        <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e-8"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                <Item ModelType="Property" Tag="X" DisplayName="X">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Y" DisplayName="Y">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Z" DisplayName="Z">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
            </Item>
            <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                <Parameter ParType="QString" ParRole="0" ParValue="{a2927dd7-139d-4e14-b135-5aa14bfc1841}"/>
            </Item>
        </Item>
        <Item ModelType="Material" Tag="rootTag" DisplayName="Material">
            <Item ModelType="Property" Tag="Name" DisplayName="Name">
                <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_Air"/>
            </Item>
            <Item ModelType="Property" Tag="Color" DisplayName="Color">
                <Parameter ParType="ExternalProperty" ParRole="0" Text="[179, 242, 255] (255)" Color="#ffb3f2ff" Identifier=""/>
            </Item>
            <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                    <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                </Item>
                <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                    <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                <Item ModelType="Property" Tag="X" DisplayName="X">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Y" DisplayName="Y">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Z" DisplayName="Z">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
            </Item>
            <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                <Parameter ParType="QString" ParRole="0" ParValue="{7bf9f01b-6724-4970-9d8d-caa85d70eff5}"/>
            </Item>
        </Item>
        <Item ModelType="Material" Tag="rootTag" DisplayName="Material">
            <Item ModelType="Property" Tag="Name" DisplayName="Name">
                <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_OleicAcid"/>
            </Item>
            <Item ModelType="Property" Tag="Color" DisplayName="Color">
                <Parameter ParType="ExternalProperty" ParRole="0" Text="[234, 136, 135] (255)" Color="#ffea8887" Identifier=""/>
            </Item>
            <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                    <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                </Item>
                <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                    <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                        <Parameter ParType="double" ParRole="0" ParValue="7.800000000000e-8"/>
                    </Item>
                    <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                <Item ModelType="Property" Tag="X" DisplayName="X">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Y" DisplayName="Y">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Z" DisplayName="Z">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
            </Item>
            <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                <Parameter ParType="QString" ParRole="0" ParValue="{7121c7fd-470b-47fe-a792-300589f6c95b}"/>
            </Item>
        </Item>
        <Item ModelType="Material" Tag="rootTag" DisplayName="Material">
            <Item ModelType="Property" Tag="Name" DisplayName="Name">
                <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_Particle"/>
            </Item>
            <Item ModelType="Property" Tag="Color" DisplayName="Color">
                <Parameter ParType="ExternalProperty" ParRole="0" Text="[146, 198, 255] (255)" Color="#ff92c6ff" Identifier=""/>
            </Item>
            <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                    <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                </Item>
                <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                    <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                        <Parameter ParType="double" ParRole="0" ParValue="6.132000000000e-6"/>
                    </Item>
                    <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                <Item ModelType="Property" Tag="X" DisplayName="X">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Y" DisplayName="Y">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Z" DisplayName="Z">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
            </Item>
            <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                <Parameter ParType="QString" ParRole="0" ParValue="{66f2fb62-4673-41fb-97ea-4acbd6467401}"/>
            </Item>
        </Item>
        <Item ModelType="Material" Tag="rootTag" DisplayName="Material">
            <Item ModelType="Property" Tag="Name" DisplayName="Name">
                <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_SiO2"/>
            </Item>
            <Item ModelType="Property" Tag="Color" DisplayName="Color">
                <Parameter ParType="ExternalProperty" ParRole="0" Text="[121, 91, 55] (255)" Color="#ff795b37" Identifier=""/>
            </Item>
            <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                    <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                </Item>
                <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                    <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                        <Parameter ParType="double" ParRole="0" ParValue="4.186000000000e-6"/>
                    </Item>
                    <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                <Item ModelType="Property" Tag="X" DisplayName="X">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Y" DisplayName="Y">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Z" DisplayName="Z">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
            </Item>
            <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                <Parameter ParType="QString" ParRole="0" ParValue="{653071f1-3be9-46e7-ac08-ee7e81e99ce3}"/>
            </Item>
        </Item>
        <Item ModelType="Material" Tag="rootTag" DisplayName="Material">
            <Item ModelType="Property" Tag="Name" DisplayName="Name">
                <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_Si"/>
            </Item>
            <Item ModelType="Property" Tag="Color" DisplayName="Color">
                <Parameter ParType="ExternalProperty" ParRole="0" Text="[13, 67, 63] (255)" Color="#ff0d433f" Identifier=""/>
            </Item>
            <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                    <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                </Item>
                <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                    <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                        <Parameter ParType="double" ParRole="0" ParValue="2.079000000000e-6"/>
                    </Item>
                    <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                <Item ModelType="Property" Tag="X" DisplayName="X">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Y" DisplayName="Y">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Z" DisplayName="Z">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
            </Item>
            <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                <Parameter ParType="QString" ParRole="0" ParValue="{df6bc971-6827-425c-82cb-a183d12b9e72}"/>
            </Item>
        </Item>
    </MaterialModel>
    <InstrumentModel Name="DefaultName">
        <Item ModelType="GISASInstrument" Tag="rootTag" DisplayName="GISASInstrument">
            <Item ModelType="Property" Tag="Name" DisplayName="Name">
                <Parameter ParType="QString" ParRole="0" ParValue="GISAS"/>
            </Item>
            <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                <Parameter ParType="QString" ParRole="0" ParValue="{58ad1123-1955-4e10-af30-cde425383c34}"/>
            </Item>
            <Item ModelType="GISASBeam" Tag="Beam" DisplayName="Beam">
                <Item ModelType="Property" Tag="Intensity" DisplayName="Intensity">
                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+8"/>
                </Item>
                <Item ModelType="BeamAzimuthalAngle" Tag="AzimuthalAngle" DisplayName="AzimuthalAngle">
                    <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="5" ParExt="Cosine;Gate;Gaussian;Log Normal;Lorentz;None;Trapezoid"/>
                        <Item ModelType="DistributionNone" Tag="Item tag" DisplayName="DistributionNone">
                            <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Mean" DisplayName="Value">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                </Item>
                <Item ModelType="Vector" Tag="Polarization" DisplayName="Polarization">
                    <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                    <Item ModelType="Property" Tag="X" DisplayName="X">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Y" DisplayName="Y">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Z" DisplayName="Z">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                </Item>
                <Item ModelType="BeamInclinationAngle" Tag="InclinationAngle" DisplayName="InclinationAngle">
                    <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="5" ParExt="Cosine;Gate;Gaussian;Log Normal;Lorentz;None;Trapezoid"/>
                        <Item ModelType="DistributionNone" Tag="Item tag" DisplayName="DistributionNone">
                            <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Mean" DisplayName="Value">
                                <Parameter ParType="double" ParRole="0" ParValue="4.000000000000e-1"/>
                            </Item>
                        </Item>
                    </Item>
                </Item>
                <Item ModelType="BeamWavelength" Tag="Wavelength" DisplayName="Wavelength">
                    <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="5" ParExt="Cosine;Gate;Gaussian;Log Normal;Lorentz;None;Trapezoid"/>
                        <Item ModelType="DistributionNone" Tag="Item tag" DisplayName="DistributionNone">
                            <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Mean" DisplayName="Value">
                                <Parameter ParType="double" ParRole="0" ParValue="6.000000000000e-1"/>
                            </Item>
                        </Item>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="GroupProperty" Tag="Detector" DisplayName="Detector">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Rectangular detector;Spherical detector"/>
                <Item ModelType="SphericalDetector" Tag="Item tag" DisplayName="SphericalDetector">
                    <Item ModelType="Vector" Tag="Analyzer direction" DisplayName="Analyzer direction">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Efficiency" DisplayName="Efficiency">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Transmission" DisplayName="Transmission">
                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                    </Item>
                    <Item ModelType="BasicAxis" Tag="Phi axis" DisplayName="Phi axis">
                        <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                            <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                        </Item>
                        <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                            <Parameter ParType="int" ParRole="0" ParValue="100"/>
                        </Item>
                        <Item ModelType="Property" Tag="Min" DisplayName="Min">
                            <Parameter ParType="double" ParRole="0" ParValue="-1.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Max" DisplayName="Max">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="title" DisplayName="title">
                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                        </Item>
                        <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                            <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                        </Item>
                    </Item>
                    <Item ModelType="BasicAxis" Tag="Alpha axis" DisplayName="Alpha axis">
                        <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                            <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                        </Item>
                        <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                            <Parameter ParType="int" ParRole="0" ParValue="100"/>
                        </Item>
                        <Item ModelType="Property" Tag="Min" DisplayName="Min">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Max" DisplayName="Max">
                            <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="title" DisplayName="title">
                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                        </Item>
                        <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                            <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                        </Item>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Resolution function" DisplayName="Type">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="2D Gaussian;None"/>
                        <Item ModelType="ResolutionFunctionNone" Tag="Item tag" DisplayName="ResolutionFunctionNone"/>
                    </Item>
                </Item>
                <Item ModelType="RectangularDetector" Tag="Item tag" DisplayName="RectangularDetector">
                    <Item ModelType="Vector" Tag="Analyzer direction" DisplayName="Analyzer direction">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Efficiency" DisplayName="Efficiency">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Transmission" DisplayName="Transmission">
                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                    </Item>
                    <Item ModelType="BasicAxis" Tag="X axis" DisplayName="X axis">
                        <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                            <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                        </Item>
                        <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                            <Parameter ParType="int" ParRole="0" ParValue="128"/>
                        </Item>
                        <Item ModelType="Property" Tag="Min" DisplayName="Min">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Max" DisplayName="Width">
                            <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="title" DisplayName="title">
                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                        </Item>
                        <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                            <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                        </Item>
                    </Item>
                    <Item ModelType="BasicAxis" Tag="Y axis" DisplayName="Y axis">
                        <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                            <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                        </Item>
                        <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                            <Parameter ParType="int" ParRole="0" ParValue="256"/>
                        </Item>
                        <Item ModelType="Property" Tag="Min" DisplayName="Min">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Max" DisplayName="Height">
                            <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="title" DisplayName="title">
                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                        </Item>
                        <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                            <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Alignment" DisplayName="Alignment">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Generic;Perpendicular to direct beam;Perpendicular to sample x-axis;Perpendicular to reflected beam;Perpendicular to reflected beam (dpos)"/>
                    </Item>
                    <Item ModelType="Vector" Tag="Normal vector" DisplayName="Normal vector">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+3"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Direction vector" DisplayName="Direction vector">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="-1.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="u0" DisplayName="u0">
                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="v0" DisplayName="v0">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="u0 (dbeam)" DisplayName="u0 (dbeam)">
                        <Parameter ParType="double" ParRole="0" ParValue="3.192250000000e+2"/>
                    </Item>
                    <Item ModelType="Property" Tag="v0 (dbeam)" DisplayName="v0 (dbeam)">
                        <Parameter ParType="double" ParRole="0" ParValue="3.261500000000e+2"/>
                    </Item>
                    <Item ModelType="Property" Tag="Distance" DisplayName="Distance">
                        <Parameter ParType="double" ParRole="0" ParValue="5.000000000000e+3"/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Resolution function" DisplayName="Type">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="2D Gaussian;None"/>
                        <Item ModelType="ResolutionFunctionNone" Tag="Item tag" DisplayName="ResolutionFunctionNone"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="GroupProperty" Tag="Background" DisplayName="Type">
                <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Constant background;None;Poisson noise"/>
                <Item ModelType="NoBackground" Tag="Item tag" DisplayName="NoBackground"/>
            </Item>
        </Item>
    </InstrumentModel>
    <SampleModel Name="DefaultName">
        <Item ModelType="MultiLayer" Tag="rootTag" DisplayName="MultiLayer">
            <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                <Parameter ParType="double" ParRole="0" ParValue="5.000000000000e+1"/>
            </Item>
            <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                <Parameter ParType="double" ParRole="0" ParValue="8.000000000000e+2"/>
            </Item>
            <Item ModelType="Property" Tag="Name" DisplayName="Name">
                <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer"/>
            </Item>
            <Item ModelType="Property" Tag="CrossCorrelationLength" DisplayName="CrossCorrelationLength">
                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
            </Item>
            <Item ModelType="Vector" Tag="ExternalField" DisplayName="ExternalField">
                <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                <Item ModelType="Property" Tag="X" DisplayName="X">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Y" DisplayName="Y">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Z" DisplayName="Z">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
            </Item>
            <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                    <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                </Item>
                <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Material" DisplayName="Material">
                    <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_Air" Color="#ffb3f2ff" Identifier="{7bf9f01b-6724-4970-9d8d-caa85d70eff5}"/>
                </Item>
                <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                    <Parameter ParType="int" ParRole="0" ParValue="1"/>
                </Item>
                <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                    <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                </Item>
            </Item>
            <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                    <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                </Item>
                <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                    <Parameter ParType="double" ParRole="0" ParValue="3.000000000000e+1"/>
                </Item>
                <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                    <Parameter ParType="double" ParRole="0" ParValue="1.018000000000e+1"/>
                </Item>
                <Item ModelType="Property" Tag="Material" DisplayName="Material">
                    <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_OleicAcid" Color="#ffea8887" Identifier="{7121c7fd-470b-47fe-a792-300589f6c95b}"/>
                </Item>
                <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                    <Parameter ParType="int" ParRole="0" ParValue="10"/>
                </Item>
                <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                    <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                </Item>
                <Item ModelType="ParticleLayout" Tag="Layout tag" DisplayName="ParticleLayout">
                    <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                        <Parameter ParType="double" ParRole="0" ParValue="-7.300000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                        <Parameter ParType="double" ParRole="0" ParValue="8.600000000000e+2"/>
                    </Item>
                    <Item ModelType="Property" Tag="Approximation" DisplayName="Approximation">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Decoupling Approximation;Size Space Coupling Approximation"/>
                    </Item>
                    <Item ModelType="Property" Tag="TotalParticleDensity" DisplayName="TotalParticleDensity">
                        <Parameter ParType="double" ParRole="0" ParValue="5.670271447235e-3"/>
                    </Item>
                    <Item ModelType="Property" Tag="Weight" DisplayName="Weight">
                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                    </Item>
                    <Item ModelType="ParticleDistribution" Tag="Particle Tag" DisplayName="ParticleDistribution">
                        <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                            <Parameter ParType="double" ParRole="0" ParValue="-2.220000000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                            <Parameter ParType="double" ParRole="0" ParValue="8.600000000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="Abundance" DisplayName="Abundance">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                        </Item>
                        <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="3" ParExt="Cosine distribution;Gate distribution;Gaussian distribution;Log Normal distribution;Lorentz distribution;Trapezoid distribution"/>
                            <Item ModelType="DistributionGaussian" Tag="Item tag" DisplayName="DistributionGaussian">
                                <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Mean" DisplayName="Mean">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="StdDev" DisplayName="StdDev">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Number of samples" DisplayName="Number of samples">
                                    <Parameter ParType="int" ParRole="0" ParValue="5"/>
                                </Item>
                                <Item ModelType="Property" Tag="Sigma factor" DisplayName="Sigma factor">
                                    <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e+0"/>
                                </Item>
                                <Item ModelType="GroupProperty" Tag="Limits" DisplayName="Limits">
                                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Limited;Unlimited;LowerLimited;Nonnegative;Positive;UpperLimited"/>
                                    <Item ModelType="RealLimitsLimitless" Tag="Item tag" DisplayName="RealLimitsLimitless"/>
                                </Item>
                            </Item>
                            <Item ModelType="DistributionLogNormal" Tag="Item tag" DisplayName="DistributionLogNormal">
                                <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Median" DisplayName="Median">
                                    <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="ScaleParameter" DisplayName="ScaleParameter">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Number of samples" DisplayName="Number of samples">
                                    <Parameter ParType="int" ParRole="0" ParValue="5"/>
                                </Item>
                                <Item ModelType="Property" Tag="Sigma factor" DisplayName="Sigma factor">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.500000000000e-1"/>
                                </Item>
                                <Item ModelType="GroupProperty" Tag="Limits" DisplayName="Limits">
                                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Limited;Unlimited;LowerLimited;Nonnegative;Positive;UpperLimited"/>
                                    <Item ModelType="RealLimitsLimitless" Tag="Item tag" DisplayName="RealLimitsLimitless"/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Particle" Tag="Particle Tag" DisplayName="Particle">
                            <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                                <Parameter ParType="double" ParRole="0" ParValue="-3.720000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                                <Parameter ParType="double" ParRole="0" ParValue="8.600000000000e+2"/>
                            </Item>
                            <Item ModelType="GroupProperty" Tag="Form Factor" DisplayName="Form Factor">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Aniso Pyramid;Box;Cone;Cone6;Cuboctahedron;Cylinder;Dodecahedron;Dot;Ellipsoidal Cylinder;Full Sphere;Full Spheroid;Hemi Ellipsoid;Icosahedron;Prism3;Prism6;Pyramid;Ripple1;Ripple2;Tetrahedron;Truncated Cube;Truncated Sphere;Truncated Spheroid"/>
                                <Item ModelType="Cylinder" Tag="Item tag" DisplayName="Cylinder">
                                    <Item ModelType="Property" Tag="Radius" DisplayName="Radius">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Height" DisplayName="Height">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.600000000000e+1"/>
                                    </Item>
                                </Item>
                                <Item ModelType="Box" Tag="Item tag" DisplayName="Box">
                                    <Item ModelType="Property" Tag="Length" DisplayName="Length">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Width" DisplayName="Width">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Height" DisplayName="Height">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="Property" Tag="Material" DisplayName="Material">
                                <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_Particle" Color="#ff92c6ff" Identifier="{66f2fb62-4673-41fb-97ea-4acbd6467401}"/>
                            </Item>
                            <Item ModelType="Property" Tag="Abundance" DisplayName="Abundance">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Vector" Tag="Position Offset" DisplayName="Position Offset">
                                <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, -10.18)"/>
                                <Item ModelType="Property" Tag="X" DisplayName="X">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                    <Parameter ParType="double" ParRole="0" ParValue="-1.018000000000e+1"/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Property" Tag="Distributed parameter" DisplayName="Distributed parameter">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="None;Particle/Box/Length;Particle/Box/Width;Particle/Box/Height;Particle/Position Offset/X;Particle/Position Offset/Y;Particle/Position Offset/Z"/>
                        </Item>
                        <Item ModelType="Property" Tag="Linked parameter" DisplayName="Linked parameter">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="0,1" ParExt="Particle/Box/Width;Particle/Box/Height;Particle/Position Offset/X;Particle/Position Offset/Y;Particle/Position Offset/Z"/>
                        </Item>
                    </Item>
                    <Item ModelType="Interference2DParaCrystal" Tag="Interference Tag" DisplayName="Interference2DParaCrystal">
                        <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                            <Parameter ParType="double" ParRole="0" ParValue="-2.220000000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                            <Parameter ParType="double" ParRole="0" ParValue="1.010000000000e+3"/>
                        </Item>
                        <Item ModelType="GroupProperty" Tag="LatticeType" DisplayName="LatticeType">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Basic;Hexagonal;Square"/>
                            <Item ModelType="HexagonalLattice" Tag="Item tag" DisplayName="HexagonalLattice">
                                <Item ModelType="Property" Tag="LatticeLength" DisplayName="LatticeLength">
                                    <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e+1"/>
                                </Item>
                                <Item ModelType="Property" Tag="Xi" DisplayName="Xi">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                            </Item>
                            <Item ModelType="BasicLattice" Tag="Item tag" DisplayName="BasicLattice">
                                <Item ModelType="Property" Tag="LatticeLength1" DisplayName="LatticeLength1">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                </Item>
                                <Item ModelType="Property" Tag="LatticeLength2" DisplayName="LatticeLength2">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                </Item>
                                <Item ModelType="Property" Tag="Alpha" DisplayName="Alpha">
                                    <Parameter ParType="double" ParRole="0" ParValue="9.000000000000e+1"/>
                                </Item>
                                <Item ModelType="Property" Tag="Xi" DisplayName="Xi">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Property" Tag="Integration_over_xi" DisplayName="Integration_over_xi">
                            <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                        </Item>
                        <Item ModelType="Property" Tag="DampingLength" DisplayName="DampingLength">
                            <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="DomainSize1" DisplayName="DomainSize1">
                            <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="DomainSize2" DisplayName="DomainSize2">
                            <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                        </Item>
                        <Item ModelType="GroupProperty" Tag="PDF #1" DisplayName="PDF #1">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="3" ParExt="Cauchy 2D;Cone 2D;Gate 2D;Gauss 2D;Voigt 2D"/>
                            <Item ModelType="FTDistribution2DCauchy" Tag="Item tag" DisplayName="FTDistribution2DCauchy0">
                                <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                            </Item>
                            <Item ModelType="FTDistribution2DGauss" Tag="Item tag" DisplayName="FTDistribution2DGauss0">
                                <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="GroupProperty" Tag="PDF #2" DisplayName="PDF #2">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="3" ParExt="Cauchy 2D;Cone 2D;Gate 2D;Gauss 2D;Voigt 2D"/>
                            <Item ModelType="FTDistribution2DCauchy" Tag="Item tag" DisplayName="FTDistribution2DCauchy">
                                <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                            </Item>
                            <Item ModelType="FTDistribution2DGauss" Tag="Item tag" DisplayName="FTDistribution2DGauss1">
                                <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                    <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                </Item>
                <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                    <Parameter ParType="double" ParRole="0" ParValue="6.800000000000e+1"/>
                </Item>
                <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                    <Parameter ParType="double" ParRole="0" ParValue="7.400000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Material" DisplayName="Material">
                    <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_SiO2" Color="#ff795b37" Identifier="{653071f1-3be9-46e7-ac08-ee7e81e99ce3}"/>
                </Item>
                <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                    <Parameter ParType="int" ParRole="0" ParValue="1"/>
                </Item>
                <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                    <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                </Item>
            </Item>
            <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                    <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                </Item>
                <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                    <Parameter ParType="double" ParRole="0" ParValue="1.040000000000e+2"/>
                </Item>
                <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Property" Tag="Material" DisplayName="Material">
                    <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_Si" Color="#ff0d433f" Identifier="{df6bc971-6827-425c-82cb-a183d12b9e72}"/>
                </Item>
                <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                    <Parameter ParType="int" ParRole="0" ParValue="1"/>
                </Item>
                <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                    <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                </Item>
            </Item>
        </Item>
    </SampleModel>
    <RealDataModel Name="DefaultName"/>
    <JobModel Name="DefaultName">
        <Item ModelType="JobItem" Tag="rootTag" DisplayName="JobItem">
            <Item ModelType="Property" Tag="Name" DisplayName="Name">
                <Parameter ParType="QString" ParRole="0" ParValue="job1"/>
            </Item>
            <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                <Parameter ParType="QString" ParRole="0" ParValue="{c46102bf-e10e-4885-8fa2-b1c8e76cf9f5}"/>
            </Item>
            <Item ModelType="Property" Tag="Sample" DisplayName="Sample">
                <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer"/>
            </Item>
            <Item ModelType="Property" Tag="Instrument" DisplayName="Instrument">
                <Parameter ParType="QString" ParRole="0" ParValue="GISAS"/>
            </Item>
            <Item ModelType="Property" Tag="With Fitting" DisplayName="With Fitting">
                <Parameter ParType="bool" ParRole="0" ParValue="0"/>
            </Item>
            <Item ModelType="Property" Tag="Status" DisplayName="Status">
                <Parameter ParType="QString" ParRole="0" ParValue="Completed"/>
            </Item>
            <Item ModelType="Property" Tag="Begin Time" DisplayName="Begin Time">
                <Parameter ParType="QString" ParRole="0" ParValue="2019.01.03 00:10:57"/>
            </Item>
            <Item ModelType="Property" Tag="End Time" DisplayName="End Time">
                <Parameter ParType="QString" ParRole="0" ParValue="2019.01.03 00:11:03"/>
            </Item>
            <Item ModelType="Property" Tag="Duration" DisplayName="Duration">
                <Parameter ParType="QString" ParRole="0" ParValue="6.072"/>
            </Item>
            <Item ModelType="Property" Tag="Comments" DisplayName="Comments">
                <Parameter ParType="QString" ParRole="0" ParValue=""/>
            </Item>
            <Item ModelType="Property" Tag="Progress" DisplayName="Progress">
                <Parameter ParType="int" ParRole="0" ParValue="100"/>
            </Item>
            <Item ModelType="Property" Tag="Presentation Type" DisplayName="Presentation Type">
                <Parameter ParType="QString" ParRole="0" ParValue="Color Map"/>
            </Item>
            <Item ModelType="MultiLayer" Tag="Sample Tag" DisplayName="MultiLayer">
                <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                    <Parameter ParType="double" ParRole="0" ParValue="5.000000000000e+1"/>
                </Item>
                <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                    <Parameter ParType="double" ParRole="0" ParValue="8.000000000000e+2"/>
                </Item>
                <Item ModelType="Property" Tag="Name" DisplayName="Name">
                    <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer"/>
                </Item>
                <Item ModelType="Property" Tag="CrossCorrelationLength" DisplayName="CrossCorrelationLength">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Vector" Tag="ExternalField" DisplayName="ExternalField">
                    <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                    <Item ModelType="Property" Tag="X" DisplayName="X">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Y" DisplayName="Y">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Z" DisplayName="Z">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                </Item>
                <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                    <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                        <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Material" DisplayName="Material">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_Air" Color="#ffb3f2ff" Identifier="{60187b2f-de17-4aa6-a9fa-0a25ea4a7782}"/>
                    </Item>
                    <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                        <Parameter ParType="int" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                        <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                    </Item>
                </Item>
                <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                    <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                        <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                        <Parameter ParType="double" ParRole="0" ParValue="3.000000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                        <Parameter ParType="double" ParRole="0" ParValue="1.018000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Material" DisplayName="Material">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_OleicAcid" Color="#ffea8887" Identifier="{8c0c2365-d864-4b4f-b4eb-1aae6c8c8a6b}"/>
                    </Item>
                    <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                        <Parameter ParType="int" ParRole="0" ParValue="10"/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                        <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                    </Item>
                    <Item ModelType="ParticleLayout" Tag="Layout tag" DisplayName="ParticleLayout">
                        <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                            <Parameter ParType="double" ParRole="0" ParValue="-7.300000000000e+1"/>
                        </Item>
                        <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                            <Parameter ParType="double" ParRole="0" ParValue="8.600000000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="Approximation" DisplayName="Approximation">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Decoupling Approximation;Size Space Coupling Approximation"/>
                        </Item>
                        <Item ModelType="Property" Tag="TotalParticleDensity" DisplayName="TotalParticleDensity">
                            <Parameter ParType="double" ParRole="0" ParValue="5.670271447235e-3"/>
                        </Item>
                        <Item ModelType="Property" Tag="Weight" DisplayName="Weight">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                        </Item>
                        <Item ModelType="ParticleDistribution" Tag="Particle Tag" DisplayName="ParticleDistribution">
                            <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                                <Parameter ParType="double" ParRole="0" ParValue="-2.220000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                                <Parameter ParType="double" ParRole="0" ParValue="8.600000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="Abundance" DisplayName="Abundance">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="3" ParExt="Cosine distribution;Gate distribution;Gaussian distribution;Log Normal distribution;Lorentz distribution;Trapezoid distribution"/>
                                <Item ModelType="DistributionGaussian" Tag="Item tag" DisplayName="DistributionGaussian">
                                    <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                        <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Mean" DisplayName="Mean">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="StdDev" DisplayName="StdDev">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Number of samples" DisplayName="Number of samples">
                                        <Parameter ParType="int" ParRole="0" ParValue="5"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Sigma factor" DisplayName="Sigma factor">
                                        <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="GroupProperty" Tag="Limits" DisplayName="Limits">
                                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Limited;Unlimited;LowerLimited;Nonnegative;Positive;UpperLimited"/>
                                        <Item ModelType="RealLimitsLimitless" Tag="Item tag" DisplayName="RealLimitsLimitless"/>
                                    </Item>
                                </Item>
                                <Item ModelType="DistributionLogNormal" Tag="Item tag" DisplayName="DistributionLogNormal">
                                    <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                        <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Median" DisplayName="Median">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="ScaleParameter" DisplayName="ScaleParameter">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Number of samples" DisplayName="Number of samples">
                                        <Parameter ParType="int" ParRole="0" ParValue="5"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Sigma factor" DisplayName="Sigma factor">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.500000000000e-1"/>
                                    </Item>
                                    <Item ModelType="GroupProperty" Tag="Limits" DisplayName="Limits">
                                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Limited;Unlimited;LowerLimited;Nonnegative;Positive;UpperLimited"/>
                                        <Item ModelType="RealLimitsLimitless" Tag="Item tag" DisplayName="RealLimitsLimitless"/>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="Particle" Tag="Particle Tag" DisplayName="Particle">
                                <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                                    <Parameter ParType="double" ParRole="0" ParValue="-3.720000000000e+2"/>
                                </Item>
                                <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                                    <Parameter ParType="double" ParRole="0" ParValue="8.600000000000e+2"/>
                                </Item>
                                <Item ModelType="GroupProperty" Tag="Form Factor" DisplayName="Form Factor">
                                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Aniso Pyramid;Box;Cone;Cone6;Cuboctahedron;Cylinder;Dodecahedron;Dot;Ellipsoidal Cylinder;Full Sphere;Full Spheroid;Hemi Ellipsoid;Icosahedron;Prism3;Prism6;Pyramid;Ripple1;Ripple2;Tetrahedron;Truncated Cube;Truncated Sphere;Truncated Spheroid"/>
                                    <Item ModelType="Cylinder" Tag="Item tag" DisplayName="Cylinder">
                                        <Item ModelType="Property" Tag="Radius" DisplayName="Radius">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.000000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Height" DisplayName="Height">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.600000000000e+1"/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Box" Tag="Item tag" DisplayName="Box">
                                        <Item ModelType="Property" Tag="Length" DisplayName="Length">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Width" DisplayName="Width">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Height" DisplayName="Height">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                        </Item>
                                    </Item>
                                </Item>
                                <Item ModelType="Property" Tag="Material" DisplayName="Material">
                                    <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_Particle" Color="#ff92c6ff" Identifier="{47d6aebc-7653-4ee5-830b-34af40f02911}"/>
                                </Item>
                                <Item ModelType="Property" Tag="Abundance" DisplayName="Abundance">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Vector" Tag="Position Offset" DisplayName="Position Offset">
                                    <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, -10.18)"/>
                                    <Item ModelType="Property" Tag="X" DisplayName="X">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                        <Parameter ParType="double" ParRole="0" ParValue="-1.018000000000e+1"/>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="Property" Tag="Distributed parameter" DisplayName="Distributed parameter">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="None;Particle/Box/Length;Particle/Box/Width;Particle/Box/Height;Particle/Position Offset/X;Particle/Position Offset/Y;Particle/Position Offset/Z"/>
                            </Item>
                            <Item ModelType="Property" Tag="Linked parameter" DisplayName="Linked parameter">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0,1" ParExt="Particle/Box/Width;Particle/Box/Height;Particle/Position Offset/X;Particle/Position Offset/Y;Particle/Position Offset/Z"/>
                            </Item>
                        </Item>
                        <Item ModelType="Interference2DParaCrystal" Tag="Interference Tag" DisplayName="Interference2DParaCrystal">
                            <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                                <Parameter ParType="double" ParRole="0" ParValue="-2.220000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                                <Parameter ParType="double" ParRole="0" ParValue="1.010000000000e+3"/>
                            </Item>
                            <Item ModelType="GroupProperty" Tag="LatticeType" DisplayName="LatticeType">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Basic;Hexagonal;Square"/>
                                <Item ModelType="HexagonalLattice" Tag="Item tag" DisplayName="HexagonalLattice">
                                    <Item ModelType="Property" Tag="LatticeLength" DisplayName="LatticeLength">
                                        <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e+1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Xi" DisplayName="Xi">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                                <Item ModelType="BasicLattice" Tag="Item tag" DisplayName="BasicLattice">
                                    <Item ModelType="Property" Tag="LatticeLength1" DisplayName="LatticeLength1">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="LatticeLength2" DisplayName="LatticeLength2">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Alpha" DisplayName="Alpha">
                                        <Parameter ParType="double" ParRole="0" ParValue="9.000000000000e+1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Xi" DisplayName="Xi">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="Property" Tag="Integration_over_xi" DisplayName="Integration_over_xi">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                            <Item ModelType="Property" Tag="DampingLength" DisplayName="DampingLength">
                                <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="DomainSize1" DisplayName="DomainSize1">
                                <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="DomainSize2" DisplayName="DomainSize2">
                                <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                            </Item>
                            <Item ModelType="GroupProperty" Tag="PDF #1" DisplayName="PDF #1">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="3" ParExt="Cauchy 2D;Cone 2D;Gate 2D;Gauss 2D;Voigt 2D"/>
                                <Item ModelType="FTDistribution2DCauchy" Tag="Item tag" DisplayName="FTDistribution2DCauchy0">
                                    <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                                <Item ModelType="FTDistribution2DGauss" Tag="Item tag" DisplayName="FTDistribution2DGauss0">
                                    <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="GroupProperty" Tag="PDF #2" DisplayName="PDF #2">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="3" ParExt="Cauchy 2D;Cone 2D;Gate 2D;Gauss 2D;Voigt 2D"/>
                                <Item ModelType="FTDistribution2DCauchy" Tag="Item tag" DisplayName="FTDistribution2DCauchy">
                                    <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                                <Item ModelType="FTDistribution2DGauss" Tag="Item tag" DisplayName="FTDistribution2DGauss1">
                                    <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                </Item>
                <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                    <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                        <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                        <Parameter ParType="double" ParRole="0" ParValue="6.800000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                        <Parameter ParType="double" ParRole="0" ParValue="7.400000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Material" DisplayName="Material">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_SiO2" Color="#ff795b37" Identifier="{5c9a6bda-ac3c-40a9-8f8e-a3dfe2136513}"/>
                    </Item>
                    <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                        <Parameter ParType="int" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                        <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                    </Item>
                </Item>
                <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                    <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                        <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                        <Parameter ParType="double" ParRole="0" ParValue="1.040000000000e+2"/>
                    </Item>
                    <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Material" DisplayName="Material">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_Si" Color="#ff0d433f" Identifier="{ded678ae-e43e-4a0a-8888-e55710666804}"/>
                    </Item>
                    <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                        <Parameter ParType="int" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                        <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="MaterialContainer" Tag="Material Container" DisplayName="MaterialContainer">
                <Item ModelType="Property" Tag="Name" DisplayName="Name">
                    <Parameter ParType="QString" ParRole="0" ParValue="Materials"/>
                </Item>
                <Item ModelType="Material" Tag="MaterialVector" DisplayName="Material">
                    <Item ModelType="Property" Tag="Name" DisplayName="Name">
                        <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_Air"/>
                    </Item>
                    <Item ModelType="Property" Tag="Color" DisplayName="Color">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="[179, 242, 255] (255)" Color="#ffb3f2ff" Identifier=""/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                        <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                            <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                        <Parameter ParType="QString" ParRole="0" ParValue="{60187b2f-de17-4aa6-a9fa-0a25ea4a7782}"/>
                    </Item>
                </Item>
                <Item ModelType="Material" Tag="MaterialVector" DisplayName="Material">
                    <Item ModelType="Property" Tag="Name" DisplayName="Name">
                        <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_OleicAcid"/>
                    </Item>
                    <Item ModelType="Property" Tag="Color" DisplayName="Color">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="[234, 136, 135] (255)" Color="#ffea8887" Identifier=""/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                        <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                            <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="7.800000000000e-8"/>
                            </Item>
                            <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                        <Parameter ParType="QString" ParRole="0" ParValue="{8c0c2365-d864-4b4f-b4eb-1aae6c8c8a6b}"/>
                    </Item>
                </Item>
                <Item ModelType="Material" Tag="MaterialVector" DisplayName="Material">
                    <Item ModelType="Property" Tag="Name" DisplayName="Name">
                        <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_Particle"/>
                    </Item>
                    <Item ModelType="Property" Tag="Color" DisplayName="Color">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="[146, 198, 255] (255)" Color="#ff92c6ff" Identifier=""/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                        <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                            <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="6.132000000000e-6"/>
                            </Item>
                            <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                        <Parameter ParType="QString" ParRole="0" ParValue="{47d6aebc-7653-4ee5-830b-34af40f02911}"/>
                    </Item>
                </Item>
                <Item ModelType="Material" Tag="MaterialVector" DisplayName="Material">
                    <Item ModelType="Property" Tag="Name" DisplayName="Name">
                        <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_SiO2"/>
                    </Item>
                    <Item ModelType="Property" Tag="Color" DisplayName="Color">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="[121, 91, 55] (255)" Color="#ff795b37" Identifier=""/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                        <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                            <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="4.186000000000e-6"/>
                            </Item>
                            <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                        <Parameter ParType="QString" ParRole="0" ParValue="{5c9a6bda-ac3c-40a9-8f8e-a3dfe2136513}"/>
                    </Item>
                </Item>
                <Item ModelType="Material" Tag="MaterialVector" DisplayName="Material">
                    <Item ModelType="Property" Tag="Name" DisplayName="Name">
                        <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_Si"/>
                    </Item>
                    <Item ModelType="Property" Tag="Color" DisplayName="Color">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="[13, 67, 63] (255)" Color="#ff0d433f" Identifier=""/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                        <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                            <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="2.079000000000e-6"/>
                            </Item>
                            <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                        <Parameter ParType="QString" ParRole="0" ParValue="{ded678ae-e43e-4a0a-8888-e55710666804}"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="GISASInstrument" Tag="Instrument Tag" DisplayName="GISASInstrument">
                <Item ModelType="Property" Tag="Name" DisplayName="Name">
                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument"/>
                </Item>
                <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                    <Parameter ParType="QString" ParRole="0" ParValue="{d2642e57-f945-4d9a-b74b-460eb97fd4d7}"/>
                </Item>
                <Item ModelType="GISASBeam" Tag="Beam" DisplayName="Beam">
                    <Item ModelType="Property" Tag="Intensity" DisplayName="Intensity">
                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+8"/>
                    </Item>
                    <Item ModelType="BeamAzimuthalAngle" Tag="AzimuthalAngle" DisplayName="AzimuthalAngle">
                        <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="5" ParExt="Cosine;Gate;Gaussian;Log Normal;Lorentz;None;Trapezoid"/>
                            <Item ModelType="DistributionNone" Tag="Item tag" DisplayName="DistributionNone">
                                <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Mean" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Polarization" DisplayName="Polarization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="BeamInclinationAngle" Tag="InclinationAngle" DisplayName="InclinationAngle">
                        <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="5" ParExt="Cosine;Gate;Gaussian;Log Normal;Lorentz;None;Trapezoid"/>
                            <Item ModelType="DistributionNone" Tag="Item tag" DisplayName="DistributionNone">
                                <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Mean" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e-1"/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="BeamWavelength" Tag="Wavelength" DisplayName="Wavelength">
                        <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="5" ParExt="Cosine;Gate;Gaussian;Log Normal;Lorentz;None;Trapezoid"/>
                            <Item ModelType="DistributionNone" Tag="Item tag" DisplayName="DistributionNone">
                                <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Mean" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e-1"/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                </Item>
                <Item ModelType="GroupProperty" Tag="Detector" DisplayName="Detector">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Rectangular detector;Spherical detector"/>
                    <Item ModelType="SphericalDetector" Tag="Item tag" DisplayName="SphericalDetector">
                        <Item ModelType="Vector" Tag="Analyzer direction" DisplayName="Analyzer direction">
                            <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                            <Item ModelType="Property" Tag="X" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="Property" Tag="Efficiency" DisplayName="Efficiency">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Transmission" DisplayName="Transmission">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                        </Item>
                        <Item ModelType="BasicAxis" Tag="Phi axis" DisplayName="Phi axis">
                            <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                            <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                                <Parameter ParType="int" ParRole="0" ParValue="100"/>
                            </Item>
                            <Item ModelType="Property" Tag="Min" DisplayName="Min">
                                <Parameter ParType="double" ParRole="0" ParValue="-1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Max" DisplayName="Max">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="title" DisplayName="title">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                            <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                        </Item>
                        <Item ModelType="BasicAxis" Tag="Alpha axis" DisplayName="Alpha axis">
                            <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                            <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                                <Parameter ParType="int" ParRole="0" ParValue="100"/>
                            </Item>
                            <Item ModelType="Property" Tag="Min" DisplayName="Min">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Max" DisplayName="Max">
                                <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="title" DisplayName="title">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                            <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                        </Item>
                        <Item ModelType="GroupProperty" Tag="Resolution function" DisplayName="Type">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="2D Gaussian;None"/>
                            <Item ModelType="ResolutionFunctionNone" Tag="Item tag" DisplayName="ResolutionFunctionNone"/>
                        </Item>
                    </Item>
                    <Item ModelType="RectangularDetector" Tag="Item tag" DisplayName="RectangularDetector">
                        <Item ModelType="Vector" Tag="Analyzer direction" DisplayName="Analyzer direction">
                            <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                            <Item ModelType="Property" Tag="X" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="Property" Tag="Efficiency" DisplayName="Efficiency">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Transmission" DisplayName="Transmission">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                        </Item>
                        <Item ModelType="BasicAxis" Tag="X axis" DisplayName="X axis">
                            <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                            <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                                <Parameter ParType="int" ParRole="0" ParValue="128"/>
                            </Item>
                            <Item ModelType="Property" Tag="Min" DisplayName="Min">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Max" DisplayName="Width">
                                <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="title" DisplayName="title">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                            <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                        </Item>
                        <Item ModelType="BasicAxis" Tag="Y axis" DisplayName="Y axis">
                            <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                            <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                                <Parameter ParType="int" ParRole="0" ParValue="256"/>
                            </Item>
                            <Item ModelType="Property" Tag="Min" DisplayName="Min">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Max" DisplayName="Height">
                                <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="title" DisplayName="title">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                            <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                        </Item>
                        <Item ModelType="Property" Tag="Alignment" DisplayName="Alignment">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Generic;Perpendicular to direct beam;Perpendicular to sample x-axis;Perpendicular to reflected beam;Perpendicular to reflected beam (dpos)"/>
                        </Item>
                        <Item ModelType="Vector" Tag="Normal vector" DisplayName="Normal vector">
                            <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                            <Item ModelType="Property" Tag="X" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+3"/>
                            </Item>
                            <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="Vector" Tag="Direction vector" DisplayName="Direction vector">
                            <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                            <Item ModelType="Property" Tag="X" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="-1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="Property" Tag="u0" DisplayName="u0">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+1"/>
                        </Item>
                        <Item ModelType="Property" Tag="v0" DisplayName="v0">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="u0 (dbeam)" DisplayName="u0 (dbeam)">
                            <Parameter ParType="double" ParRole="0" ParValue="3.192250000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="v0 (dbeam)" DisplayName="v0 (dbeam)">
                            <Parameter ParType="double" ParRole="0" ParValue="3.261500000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="Distance" DisplayName="Distance">
                            <Parameter ParType="double" ParRole="0" ParValue="5.000000000000e+3"/>
                        </Item>
                        <Item ModelType="GroupProperty" Tag="Resolution function" DisplayName="Type">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="2D Gaussian;None"/>
                            <Item ModelType="ResolutionFunctionNone" Tag="Item tag" DisplayName="ResolutionFunctionNone"/>
                        </Item>
                    </Item>
                </Item>
                <Item ModelType="GroupProperty" Tag="Background" DisplayName="Type">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Constant background;None;Poisson noise"/>
                    <Item ModelType="NoBackground" Tag="Item tag" DisplayName="NoBackground"/>
                </Item>
            </Item>
            <Item ModelType="IntensityData" Tag="Output Tag" DisplayName="IntensityData">
                <Item ModelType="Property" Tag="FileName" DisplayName="FileName">
                    <Parameter ParType="QString" ParRole="0" ParValue="jobdata_job1_0.int.gz"/>
                </Item>
                <Item ModelType="Property" Tag="Axes Units" DisplayName="Axes Units">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="4" ParExt="nbins;Radians;Degrees;q-space;mm"/>
                </Item>
                <Item ModelType="Property" Tag="Title" DisplayName="Title">
                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                </Item>
                <Item ModelType="Property" Tag="Projections" DisplayName="Projections">
                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                </Item>
                <Item ModelType="Property" Tag="Interpolation" DisplayName="Interpolation">
                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                </Item>
                <Item ModelType="Property" Tag="Gradient" DisplayName="Gradient">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="9" ParExt="Grayscale;Hot;Cold;Night;Candy;Geography;Ion;Thermal;Polar;Spectrum;Jet;Hues"/>
                </Item>
                <Item ModelType="BasicAxis" Tag="x-axis" DisplayName="x-axis">
                    <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                        <Parameter ParType="int" ParRole="0" ParValue="128"/>
                    </Item>
                    <Item ModelType="Property" Tag="Min" DisplayName="Min">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Max" DisplayName="Max">
                        <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                    </Item>
                    <Item ModelType="Property" Tag="title" DisplayName="title">
                        <Parameter ParType="QString" ParRole="0" ParValue="X [mm]"/>
                    </Item>
                    <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                </Item>
                <Item ModelType="BasicAxis" Tag="y-axis" DisplayName="y-axis">
                    <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                        <Parameter ParType="int" ParRole="0" ParValue="256"/>
                    </Item>
                    <Item ModelType="Property" Tag="Min" DisplayName="Min">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Max" DisplayName="Max">
                        <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                    </Item>
                    <Item ModelType="Property" Tag="title" DisplayName="title">
                        <Parameter ParType="QString" ParRole="0" ParValue="Y [mm]"/>
                    </Item>
                    <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                </Item>
                <Item ModelType="AmplitudeAxis" Tag="color-axis" DisplayName="color-axis">
                    <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                        <Parameter ParType="int" ParRole="0" ParValue="100"/>
                    </Item>
                    <Item ModelType="Property" Tag="Min" DisplayName="Min">
                        <Parameter ParType="double" ParRole="0" ParValue="1.274111183639e-2"/>
                    </Item>
                    <Item ModelType="Property" Tag="Max" DisplayName="Max">
                        <Parameter ParType="double" ParRole="0" ParValue="1.401522302003e+2"/>
                    </Item>
                    <Item ModelType="Property" Tag="title" DisplayName="title">
                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                    </Item>
                    <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Lock (min, max)" DisplayName="Lock (min, max)">
                        <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                    </Item>
                    <Item ModelType="Property" Tag="log10" DisplayName="log10">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="Parameter Container" Tag="Parameter Tree" DisplayName="Parameter Container">
                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Materials">
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="simulateMonolayer_Air">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Air/Material data/MaterialSLDData/SLD, real"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Air/Material data/MaterialSLDData/SLD, imaginary"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Magnetization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Air/Magnetization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Air/Magnetization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Air/Magnetization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="simulateMonolayer_OleicAcid">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="7.800000000000e-8"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_OleicAcid/Material data/MaterialSLDData/SLD, real"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="7.800000000000e-8"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_OleicAcid/Material data/MaterialSLDData/SLD, imaginary"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Magnetization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_OleicAcid/Magnetization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_OleicAcid/Magnetization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_OleicAcid/Magnetization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="simulateMonolayer_Particle">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="6.132000000000e-6"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Particle/Material data/MaterialSLDData/SLD, real"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="6.132000000000e-6"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Particle/Material data/MaterialSLDData/SLD, imaginary"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Magnetization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Particle/Magnetization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Particle/Magnetization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Particle/Magnetization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="simulateMonolayer_SiO2">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="4.186000000000e-6"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_SiO2/Material data/MaterialSLDData/SLD, real"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="4.186000000000e-6"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_SiO2/Material data/MaterialSLDData/SLD, imaginary"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Magnetization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_SiO2/Magnetization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_SiO2/Magnetization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_SiO2/Magnetization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="simulateMonolayer_Si">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="2.079000000000e-6"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Si/Material data/MaterialSLDData/SLD, real"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="2.079000000000e-6"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Si/Material data/MaterialSLDData/SLD, imaginary"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Magnetization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Si/Magnetization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Si/Magnetization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Si/Magnetization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                </Item>
                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MultiLayer">
                    <Item ModelType="Parameter" Tag="children tag" DisplayName="CrossCorrelationLength">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/CrossCorrelationLength"/>
                        </Item>
                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="ExternalField">
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/ExternalField/X"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/ExternalField/Y"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/ExternalField/Z"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Layer0"/>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Layer1">
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Thickness">
                            <Parameter ParType="double" ParRole="0" ParValue="1.018000000000e+1"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/Thickness"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="1.018000000000e+1"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="ParticleLayout">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Weight">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Weight"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter Label" Tag="children tag" DisplayName="ParticleDistribution">
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="Abundance">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Abundance"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="DistributionLogNormal">
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="Median">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Distribution/DistributionLogNormal/Median"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="ScaleParameter">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Distribution/DistributionLogNormal/ScaleParameter"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="Sigma factor">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.500000000000e-1"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Distribution/DistributionLogNormal/Sigma factor"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.500000000000e-1"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Particle">
                                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Box">
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Length">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Form Factor/Box/Length"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Width">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Form Factor/Box/Width"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Height">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Form Factor/Box/Height"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Position Offset">
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Position Offset/X"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Position Offset/Y"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                            <Parameter ParType="double" ParRole="0" ParValue="-1.018000000000e+1"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Position Offset/Z"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="-1.018000000000e+1"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Interference2DParaCrystal">
                                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="BasicLattice">
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="LatticeLength1">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/LatticeType/BasicLattice/LatticeLength1"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="LatticeLength2">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/LatticeType/BasicLattice/LatticeLength2"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="Alpha">
                                        <Parameter ParType="double" ParRole="0" ParValue="9.000000000000e+1"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/LatticeType/BasicLattice/Alpha"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="9.000000000000e+1"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="DampingLength">
                                    <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/DampingLength"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="DomainSize1">
                                    <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/DomainSize1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="DomainSize2">
                                    <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/DomainSize2"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="FTDistribution2DGauss0">
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #1/FTDistribution2DGauss0/OmegaX"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #1/FTDistribution2DGauss0/OmegaY"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #1/FTDistribution2DGauss0/Gamma"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="FTDistribution2DGauss1">
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #2/FTDistribution2DGauss1/OmegaX"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #2/FTDistribution2DGauss1/OmegaY"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #2/FTDistribution2DGauss1/Gamma"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Layer2">
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Thickness">
                            <Parameter ParType="double" ParRole="0" ParValue="7.400000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer2/Thickness"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="7.400000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Layer3"/>
                </Item>
                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="GISASInstrument">
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Beam">
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Intensity">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+8"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/Intensity"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+8"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="AzimuthalAngle">
                            <Item ModelType="Parameter Label" Tag="children tag" DisplayName="DistributionNone">
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/AzimuthalAngle/Distribution/DistributionNone/Value"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Polarization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/Polarization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/Polarization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/Polarization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="InclinationAngle">
                            <Item ModelType="Parameter Label" Tag="children tag" DisplayName="DistributionNone">
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e-1"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/InclinationAngle/Distribution/DistributionNone/Value"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e-1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Wavelength">
                            <Item ModelType="Parameter Label" Tag="children tag" DisplayName="DistributionNone">
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e-1"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/Wavelength/Distribution/DistributionNone/Value"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e-1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="RectangularDetector">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Analyzer direction">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Analyzer direction/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Analyzer direction/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Analyzer direction/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Efficiency">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Efficiency"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Transmission">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Transmission"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="X axis">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Width">
                                <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/X axis/Width"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Y axis">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Height">
                                <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Y axis/Height"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="u0 (dbeam)">
                            <Parameter ParType="double" ParRole="0" ParValue="3.192250000000e+2"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/u0 (dbeam)"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="3.192250000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="v0 (dbeam)">
                            <Parameter ParType="double" ParRole="0" ParValue="3.261500000000e+2"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/v0 (dbeam)"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="3.261500000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Distance">
                            <Parameter ParType="double" ParRole="0" ParValue="5.000000000000e+3"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Distance"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="5.000000000000e+3"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="SimulationOptions" Tag="Simulation Options" DisplayName="SimulationOptions">
                <Item ModelType="Property" Tag="Run Policy" DisplayName="Run Policy">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Immediately;In background"/>
                </Item>
                <Item ModelType="Property" Tag="Number of Threads" DisplayName="Number of Threads">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Max (4 threads);3 threads;2 threads;1 thread"/>
                </Item>
                <Item ModelType="Property" Tag="Computation method" DisplayName="Computation method">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Analytical;Monte-Carlo Integration"/>
                </Item>
                <Item ModelType="Property" Tag="Number of MC points" DisplayName="Number of MC points">
                    <Parameter ParType="int" ParRole="0" ParValue="100"/>
                </Item>
                <Item ModelType="Property" Tag="Material for Fresnel calculations" DisplayName="Material for Fresnel calculations">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Ambient Layer Material;Average Layer Material"/>
                </Item>
                <Item ModelType="Property" Tag="Include specular peak" DisplayName="Include specular peak">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="No;Yes"/>
                </Item>
            </Item>
        </Item>
        <Item ModelType="JobItem" Tag="rootTag" DisplayName="JobItem">
            <Item ModelType="Property" Tag="Name" DisplayName="Name">
                <Parameter ParType="QString" ParRole="0" ParValue="job2"/>
            </Item>
            <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                <Parameter ParType="QString" ParRole="0" ParValue="{be5934dd-0a54-4124-aa58-e1a599e7d1d0}"/>
            </Item>
            <Item ModelType="Property" Tag="Sample" DisplayName="Sample">
                <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer"/>
            </Item>
            <Item ModelType="Property" Tag="Instrument" DisplayName="Instrument">
                <Parameter ParType="QString" ParRole="0" ParValue="GISAS"/>
            </Item>
            <Item ModelType="Property" Tag="With Fitting" DisplayName="With Fitting">
                <Parameter ParType="bool" ParRole="0" ParValue="0"/>
            </Item>
            <Item ModelType="Property" Tag="Status" DisplayName="Status">
                <Parameter ParType="QString" ParRole="0" ParValue="Completed"/>
            </Item>
            <Item ModelType="Property" Tag="Begin Time" DisplayName="Begin Time">
                <Parameter ParType="QString" ParRole="0" ParValue="2019.01.03 00:11:16"/>
            </Item>
            <Item ModelType="Property" Tag="End Time" DisplayName="End Time">
                <Parameter ParType="QString" ParRole="0" ParValue="2019.01.03 00:11:22"/>
            </Item>
            <Item ModelType="Property" Tag="Duration" DisplayName="Duration">
                <Parameter ParType="QString" ParRole="0" ParValue="5.704"/>
            </Item>
            <Item ModelType="Property" Tag="Comments" DisplayName="Comments">
                <Parameter ParType="QString" ParRole="0" ParValue=""/>
            </Item>
            <Item ModelType="Property" Tag="Progress" DisplayName="Progress">
                <Parameter ParType="int" ParRole="0" ParValue="100"/>
            </Item>
            <Item ModelType="Property" Tag="Presentation Type" DisplayName="Presentation Type">
                <Parameter ParType="QString" ParRole="0" ParValue="Color Map"/>
            </Item>
            <Item ModelType="MultiLayer" Tag="Sample Tag" DisplayName="MultiLayer">
                <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                    <Parameter ParType="double" ParRole="0" ParValue="5.000000000000e+1"/>
                </Item>
                <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                    <Parameter ParType="double" ParRole="0" ParValue="8.000000000000e+2"/>
                </Item>
                <Item ModelType="Property" Tag="Name" DisplayName="Name">
                    <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer"/>
                </Item>
                <Item ModelType="Property" Tag="CrossCorrelationLength" DisplayName="CrossCorrelationLength">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Vector" Tag="ExternalField" DisplayName="ExternalField">
                    <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                    <Item ModelType="Property" Tag="X" DisplayName="X">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Y" DisplayName="Y">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Z" DisplayName="Z">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                </Item>
                <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                    <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                        <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Material" DisplayName="Material">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_Air" Color="#ffb3f2ff" Identifier="{3b07684e-5198-4c77-9f2e-e444aa5e2dae}"/>
                    </Item>
                    <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                        <Parameter ParType="int" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                        <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                    </Item>
                </Item>
                <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                    <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                        <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                        <Parameter ParType="double" ParRole="0" ParValue="3.000000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                        <Parameter ParType="double" ParRole="0" ParValue="1.018000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Material" DisplayName="Material">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_OleicAcid" Color="#ffea8887" Identifier="{7e43747e-37e7-4479-9fcc-46f0270eb62f}"/>
                    </Item>
                    <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                        <Parameter ParType="int" ParRole="0" ParValue="10"/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                        <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                    </Item>
                    <Item ModelType="ParticleLayout" Tag="Layout tag" DisplayName="ParticleLayout">
                        <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                            <Parameter ParType="double" ParRole="0" ParValue="-7.300000000000e+1"/>
                        </Item>
                        <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                            <Parameter ParType="double" ParRole="0" ParValue="8.600000000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="Approximation" DisplayName="Approximation">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Decoupling Approximation;Size Space Coupling Approximation"/>
                        </Item>
                        <Item ModelType="Property" Tag="TotalParticleDensity" DisplayName="TotalParticleDensity">
                            <Parameter ParType="double" ParRole="0" ParValue="5.670271447235e-3"/>
                        </Item>
                        <Item ModelType="Property" Tag="Weight" DisplayName="Weight">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                        </Item>
                        <Item ModelType="ParticleDistribution" Tag="Particle Tag" DisplayName="ParticleDistribution">
                            <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                                <Parameter ParType="double" ParRole="0" ParValue="-2.220000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                                <Parameter ParType="double" ParRole="0" ParValue="8.600000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="Abundance" DisplayName="Abundance">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="3" ParExt="Cosine distribution;Gate distribution;Gaussian distribution;Log Normal distribution;Lorentz distribution;Trapezoid distribution"/>
                                <Item ModelType="DistributionGaussian" Tag="Item tag" DisplayName="DistributionGaussian">
                                    <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                        <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Mean" DisplayName="Mean">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="StdDev" DisplayName="StdDev">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Number of samples" DisplayName="Number of samples">
                                        <Parameter ParType="int" ParRole="0" ParValue="5"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Sigma factor" DisplayName="Sigma factor">
                                        <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="GroupProperty" Tag="Limits" DisplayName="Limits">
                                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Limited;Unlimited;LowerLimited;Nonnegative;Positive;UpperLimited"/>
                                        <Item ModelType="RealLimitsLimitless" Tag="Item tag" DisplayName="RealLimitsLimitless"/>
                                    </Item>
                                </Item>
                                <Item ModelType="DistributionLogNormal" Tag="Item tag" DisplayName="DistributionLogNormal">
                                    <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                        <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Median" DisplayName="Median">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="ScaleParameter" DisplayName="ScaleParameter">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Number of samples" DisplayName="Number of samples">
                                        <Parameter ParType="int" ParRole="0" ParValue="5"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Sigma factor" DisplayName="Sigma factor">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.500000000000e-1"/>
                                    </Item>
                                    <Item ModelType="GroupProperty" Tag="Limits" DisplayName="Limits">
                                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Limited;Unlimited;LowerLimited;Nonnegative;Positive;UpperLimited"/>
                                        <Item ModelType="RealLimitsLimitless" Tag="Item tag" DisplayName="RealLimitsLimitless"/>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="Particle" Tag="Particle Tag" DisplayName="Particle">
                                <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                                    <Parameter ParType="double" ParRole="0" ParValue="-3.720000000000e+2"/>
                                </Item>
                                <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                                    <Parameter ParType="double" ParRole="0" ParValue="8.600000000000e+2"/>
                                </Item>
                                <Item ModelType="GroupProperty" Tag="Form Factor" DisplayName="Form Factor">
                                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Aniso Pyramid;Box;Cone;Cone6;Cuboctahedron;Cylinder;Dodecahedron;Dot;Ellipsoidal Cylinder;Full Sphere;Full Spheroid;Hemi Ellipsoid;Icosahedron;Prism3;Prism6;Pyramid;Ripple1;Ripple2;Tetrahedron;Truncated Cube;Truncated Sphere;Truncated Spheroid"/>
                                    <Item ModelType="Cylinder" Tag="Item tag" DisplayName="Cylinder">
                                        <Item ModelType="Property" Tag="Radius" DisplayName="Radius">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.000000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Height" DisplayName="Height">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.600000000000e+1"/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Box" Tag="Item tag" DisplayName="Box">
                                        <Item ModelType="Property" Tag="Length" DisplayName="Length">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Width" DisplayName="Width">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Height" DisplayName="Height">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                        </Item>
                                    </Item>
                                </Item>
                                <Item ModelType="Property" Tag="Material" DisplayName="Material">
                                    <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_Particle" Color="#ff92c6ff" Identifier="{09343fa8-5476-44db-9083-032e1915f7a7}"/>
                                </Item>
                                <Item ModelType="Property" Tag="Abundance" DisplayName="Abundance">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Vector" Tag="Position Offset" DisplayName="Position Offset">
                                    <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, -10.18)"/>
                                    <Item ModelType="Property" Tag="X" DisplayName="X">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                        <Parameter ParType="double" ParRole="0" ParValue="-1.018000000000e+1"/>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="Property" Tag="Distributed parameter" DisplayName="Distributed parameter">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="None;Particle/Box/Length;Particle/Box/Width;Particle/Box/Height;Particle/Position Offset/X;Particle/Position Offset/Y;Particle/Position Offset/Z"/>
                            </Item>
                            <Item ModelType="Property" Tag="Linked parameter" DisplayName="Linked parameter">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0,1" ParExt="Particle/Box/Width;Particle/Box/Height;Particle/Position Offset/X;Particle/Position Offset/Y;Particle/Position Offset/Z"/>
                            </Item>
                        </Item>
                        <Item ModelType="Interference2DParaCrystal" Tag="Interference Tag" DisplayName="Interference2DParaCrystal">
                            <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                                <Parameter ParType="double" ParRole="0" ParValue="-2.220000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                                <Parameter ParType="double" ParRole="0" ParValue="1.010000000000e+3"/>
                            </Item>
                            <Item ModelType="GroupProperty" Tag="LatticeType" DisplayName="LatticeType">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Basic;Hexagonal;Square"/>
                                <Item ModelType="HexagonalLattice" Tag="Item tag" DisplayName="HexagonalLattice">
                                    <Item ModelType="Property" Tag="LatticeLength" DisplayName="LatticeLength">
                                        <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e+1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Xi" DisplayName="Xi">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                                <Item ModelType="BasicLattice" Tag="Item tag" DisplayName="BasicLattice">
                                    <Item ModelType="Property" Tag="LatticeLength1" DisplayName="LatticeLength1">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="LatticeLength2" DisplayName="LatticeLength2">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Alpha" DisplayName="Alpha">
                                        <Parameter ParType="double" ParRole="0" ParValue="9.000000000000e+1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Xi" DisplayName="Xi">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="Property" Tag="Integration_over_xi" DisplayName="Integration_over_xi">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                            <Item ModelType="Property" Tag="DampingLength" DisplayName="DampingLength">
                                <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="DomainSize1" DisplayName="DomainSize1">
                                <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="DomainSize2" DisplayName="DomainSize2">
                                <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                            </Item>
                            <Item ModelType="GroupProperty" Tag="PDF #1" DisplayName="PDF #1">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="3" ParExt="Cauchy 2D;Cone 2D;Gate 2D;Gauss 2D;Voigt 2D"/>
                                <Item ModelType="FTDistribution2DCauchy" Tag="Item tag" DisplayName="FTDistribution2DCauchy0">
                                    <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                                <Item ModelType="FTDistribution2DGauss" Tag="Item tag" DisplayName="FTDistribution2DGauss0">
                                    <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="GroupProperty" Tag="PDF #2" DisplayName="PDF #2">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="3" ParExt="Cauchy 2D;Cone 2D;Gate 2D;Gauss 2D;Voigt 2D"/>
                                <Item ModelType="FTDistribution2DCauchy" Tag="Item tag" DisplayName="FTDistribution2DCauchy">
                                    <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                                <Item ModelType="FTDistribution2DGauss" Tag="Item tag" DisplayName="FTDistribution2DGauss1">
                                    <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                </Item>
                <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                    <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                        <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                        <Parameter ParType="double" ParRole="0" ParValue="6.800000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                        <Parameter ParType="double" ParRole="0" ParValue="7.400000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Material" DisplayName="Material">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_SiO2" Color="#ff795b37" Identifier="{360cb493-2e64-40af-8b45-d85d93a78760}"/>
                    </Item>
                    <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                        <Parameter ParType="int" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                        <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                    </Item>
                </Item>
                <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                    <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                        <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                        <Parameter ParType="double" ParRole="0" ParValue="1.040000000000e+2"/>
                    </Item>
                    <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Material" DisplayName="Material">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_Si" Color="#ff0d433f" Identifier="{a1259aa1-1d61-4d76-9c6d-c86c33e41517}"/>
                    </Item>
                    <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                        <Parameter ParType="int" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                        <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="MaterialContainer" Tag="Material Container" DisplayName="MaterialContainer">
                <Item ModelType="Property" Tag="Name" DisplayName="Name">
                    <Parameter ParType="QString" ParRole="0" ParValue="Materials"/>
                </Item>
                <Item ModelType="Material" Tag="MaterialVector" DisplayName="Material">
                    <Item ModelType="Property" Tag="Name" DisplayName="Name">
                        <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_Air"/>
                    </Item>
                    <Item ModelType="Property" Tag="Color" DisplayName="Color">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="[179, 242, 255] (255)" Color="#ffb3f2ff" Identifier=""/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                        <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                            <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                        <Parameter ParType="QString" ParRole="0" ParValue="{3b07684e-5198-4c77-9f2e-e444aa5e2dae}"/>
                    </Item>
                </Item>
                <Item ModelType="Material" Tag="MaterialVector" DisplayName="Material">
                    <Item ModelType="Property" Tag="Name" DisplayName="Name">
                        <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_OleicAcid"/>
                    </Item>
                    <Item ModelType="Property" Tag="Color" DisplayName="Color">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="[234, 136, 135] (255)" Color="#ffea8887" Identifier=""/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                        <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                            <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="7.800000000000e-8"/>
                            </Item>
                            <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                        <Parameter ParType="QString" ParRole="0" ParValue="{7e43747e-37e7-4479-9fcc-46f0270eb62f}"/>
                    </Item>
                </Item>
                <Item ModelType="Material" Tag="MaterialVector" DisplayName="Material">
                    <Item ModelType="Property" Tag="Name" DisplayName="Name">
                        <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_Particle"/>
                    </Item>
                    <Item ModelType="Property" Tag="Color" DisplayName="Color">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="[146, 198, 255] (255)" Color="#ff92c6ff" Identifier=""/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                        <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                            <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="6.132000000000e-6"/>
                            </Item>
                            <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                        <Parameter ParType="QString" ParRole="0" ParValue="{09343fa8-5476-44db-9083-032e1915f7a7}"/>
                    </Item>
                </Item>
                <Item ModelType="Material" Tag="MaterialVector" DisplayName="Material">
                    <Item ModelType="Property" Tag="Name" DisplayName="Name">
                        <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_SiO2"/>
                    </Item>
                    <Item ModelType="Property" Tag="Color" DisplayName="Color">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="[121, 91, 55] (255)" Color="#ff795b37" Identifier=""/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                        <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                            <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="4.186000000000e-6"/>
                            </Item>
                            <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                        <Parameter ParType="QString" ParRole="0" ParValue="{360cb493-2e64-40af-8b45-d85d93a78760}"/>
                    </Item>
                </Item>
                <Item ModelType="Material" Tag="MaterialVector" DisplayName="Material">
                    <Item ModelType="Property" Tag="Name" DisplayName="Name">
                        <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_Si"/>
                    </Item>
                    <Item ModelType="Property" Tag="Color" DisplayName="Color">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="[13, 67, 63] (255)" Color="#ff0d433f" Identifier=""/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                        <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                            <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="2.079000000000e-6"/>
                            </Item>
                            <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                        <Parameter ParType="QString" ParRole="0" ParValue="{a1259aa1-1d61-4d76-9c6d-c86c33e41517}"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="GISASInstrument" Tag="Instrument Tag" DisplayName="GISASInstrument">
                <Item ModelType="Property" Tag="Name" DisplayName="Name">
                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument"/>
                </Item>
                <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                    <Parameter ParType="QString" ParRole="0" ParValue="{44642e97-e1c5-45b2-94bf-0e3ec2f79b6c}"/>
                </Item>
                <Item ModelType="GISASBeam" Tag="Beam" DisplayName="Beam">
                    <Item ModelType="Property" Tag="Intensity" DisplayName="Intensity">
                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+8"/>
                    </Item>
                    <Item ModelType="BeamAzimuthalAngle" Tag="AzimuthalAngle" DisplayName="AzimuthalAngle">
                        <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="5" ParExt="Cosine;Gate;Gaussian;Log Normal;Lorentz;None;Trapezoid"/>
                            <Item ModelType="DistributionNone" Tag="Item tag" DisplayName="DistributionNone">
                                <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Mean" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Polarization" DisplayName="Polarization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="BeamInclinationAngle" Tag="InclinationAngle" DisplayName="InclinationAngle">
                        <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="5" ParExt="Cosine;Gate;Gaussian;Log Normal;Lorentz;None;Trapezoid"/>
                            <Item ModelType="DistributionNone" Tag="Item tag" DisplayName="DistributionNone">
                                <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Mean" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e-1"/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="BeamWavelength" Tag="Wavelength" DisplayName="Wavelength">
                        <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="5" ParExt="Cosine;Gate;Gaussian;Log Normal;Lorentz;None;Trapezoid"/>
                            <Item ModelType="DistributionNone" Tag="Item tag" DisplayName="DistributionNone">
                                <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Mean" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e-1"/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                </Item>
                <Item ModelType="GroupProperty" Tag="Detector" DisplayName="Detector">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Rectangular detector;Spherical detector"/>
                    <Item ModelType="SphericalDetector" Tag="Item tag" DisplayName="SphericalDetector">
                        <Item ModelType="Vector" Tag="Analyzer direction" DisplayName="Analyzer direction">
                            <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                            <Item ModelType="Property" Tag="X" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="Property" Tag="Efficiency" DisplayName="Efficiency">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Transmission" DisplayName="Transmission">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                        </Item>
                        <Item ModelType="BasicAxis" Tag="Phi axis" DisplayName="Phi axis">
                            <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                            <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                                <Parameter ParType="int" ParRole="0" ParValue="100"/>
                            </Item>
                            <Item ModelType="Property" Tag="Min" DisplayName="Min">
                                <Parameter ParType="double" ParRole="0" ParValue="-1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Max" DisplayName="Max">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="title" DisplayName="title">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                            <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                        </Item>
                        <Item ModelType="BasicAxis" Tag="Alpha axis" DisplayName="Alpha axis">
                            <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                            <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                                <Parameter ParType="int" ParRole="0" ParValue="100"/>
                            </Item>
                            <Item ModelType="Property" Tag="Min" DisplayName="Min">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Max" DisplayName="Max">
                                <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="title" DisplayName="title">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                            <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                        </Item>
                        <Item ModelType="GroupProperty" Tag="Resolution function" DisplayName="Type">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="2D Gaussian;None"/>
                            <Item ModelType="ResolutionFunctionNone" Tag="Item tag" DisplayName="ResolutionFunctionNone"/>
                        </Item>
                    </Item>
                    <Item ModelType="RectangularDetector" Tag="Item tag" DisplayName="RectangularDetector">
                        <Item ModelType="Vector" Tag="Analyzer direction" DisplayName="Analyzer direction">
                            <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                            <Item ModelType="Property" Tag="X" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="Property" Tag="Efficiency" DisplayName="Efficiency">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Transmission" DisplayName="Transmission">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                        </Item>
                        <Item ModelType="BasicAxis" Tag="X axis" DisplayName="X axis">
                            <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                            <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                                <Parameter ParType="int" ParRole="0" ParValue="128"/>
                            </Item>
                            <Item ModelType="Property" Tag="Min" DisplayName="Min">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Max" DisplayName="Width">
                                <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="title" DisplayName="title">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                            <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                        </Item>
                        <Item ModelType="BasicAxis" Tag="Y axis" DisplayName="Y axis">
                            <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                            <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                                <Parameter ParType="int" ParRole="0" ParValue="256"/>
                            </Item>
                            <Item ModelType="Property" Tag="Min" DisplayName="Min">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Max" DisplayName="Height">
                                <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="title" DisplayName="title">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                            <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                        </Item>
                        <Item ModelType="Property" Tag="Alignment" DisplayName="Alignment">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Generic;Perpendicular to direct beam;Perpendicular to sample x-axis;Perpendicular to reflected beam;Perpendicular to reflected beam (dpos)"/>
                        </Item>
                        <Item ModelType="Vector" Tag="Normal vector" DisplayName="Normal vector">
                            <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                            <Item ModelType="Property" Tag="X" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+3"/>
                            </Item>
                            <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="Vector" Tag="Direction vector" DisplayName="Direction vector">
                            <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                            <Item ModelType="Property" Tag="X" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="-1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="Property" Tag="u0" DisplayName="u0">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+1"/>
                        </Item>
                        <Item ModelType="Property" Tag="v0" DisplayName="v0">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="u0 (dbeam)" DisplayName="u0 (dbeam)">
                            <Parameter ParType="double" ParRole="0" ParValue="3.192250000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="v0 (dbeam)" DisplayName="v0 (dbeam)">
                            <Parameter ParType="double" ParRole="0" ParValue="3.261500000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="Distance" DisplayName="Distance">
                            <Parameter ParType="double" ParRole="0" ParValue="5.000000000000e+3"/>
                        </Item>
                        <Item ModelType="GroupProperty" Tag="Resolution function" DisplayName="Type">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="2D Gaussian;None"/>
                            <Item ModelType="ResolutionFunctionNone" Tag="Item tag" DisplayName="ResolutionFunctionNone"/>
                        </Item>
                    </Item>
                </Item>
                <Item ModelType="GroupProperty" Tag="Background" DisplayName="Type">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Constant background;None;Poisson noise"/>
                    <Item ModelType="NoBackground" Tag="Item tag" DisplayName="NoBackground"/>
                </Item>
            </Item>
            <Item ModelType="IntensityData" Tag="Output Tag" DisplayName="IntensityData">
                <Item ModelType="Property" Tag="FileName" DisplayName="FileName">
                    <Parameter ParType="QString" ParRole="0" ParValue="jobdata_job2_0.int.gz"/>
                </Item>
                <Item ModelType="Property" Tag="Axes Units" DisplayName="Axes Units">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="4" ParExt="nbins;Radians;Degrees;q-space;mm"/>
                </Item>
                <Item ModelType="Property" Tag="Title" DisplayName="Title">
                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                </Item>
                <Item ModelType="Property" Tag="Projections" DisplayName="Projections">
                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                </Item>
                <Item ModelType="Property" Tag="Interpolation" DisplayName="Interpolation">
                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                </Item>
                <Item ModelType="Property" Tag="Gradient" DisplayName="Gradient">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="9" ParExt="Grayscale;Hot;Cold;Night;Candy;Geography;Ion;Thermal;Polar;Spectrum;Jet;Hues"/>
                </Item>
                <Item ModelType="BasicAxis" Tag="x-axis" DisplayName="x-axis">
                    <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                        <Parameter ParType="int" ParRole="0" ParValue="128"/>
                    </Item>
                    <Item ModelType="Property" Tag="Min" DisplayName="Min">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Max" DisplayName="Max">
                        <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                    </Item>
                    <Item ModelType="Property" Tag="title" DisplayName="title">
                        <Parameter ParType="QString" ParRole="0" ParValue="X [mm]"/>
                    </Item>
                    <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                </Item>
                <Item ModelType="BasicAxis" Tag="y-axis" DisplayName="y-axis">
                    <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                        <Parameter ParType="int" ParRole="0" ParValue="256"/>
                    </Item>
                    <Item ModelType="Property" Tag="Min" DisplayName="Min">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Max" DisplayName="Max">
                        <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                    </Item>
                    <Item ModelType="Property" Tag="title" DisplayName="title">
                        <Parameter ParType="QString" ParRole="0" ParValue="Y [mm]"/>
                    </Item>
                    <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                </Item>
                <Item ModelType="AmplitudeAxis" Tag="color-axis" DisplayName="color-axis">
                    <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                        <Parameter ParType="int" ParRole="0" ParValue="100"/>
                    </Item>
                    <Item ModelType="Property" Tag="Min" DisplayName="Min">
                        <Parameter ParType="double" ParRole="0" ParValue="1.274111183639e-2"/>
                    </Item>
                    <Item ModelType="Property" Tag="Max" DisplayName="Max">
                        <Parameter ParType="double" ParRole="0" ParValue="1.401522302003e+2"/>
                    </Item>
                    <Item ModelType="Property" Tag="title" DisplayName="title">
                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                    </Item>
                    <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Lock (min, max)" DisplayName="Lock (min, max)">
                        <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                    </Item>
                    <Item ModelType="Property" Tag="log10" DisplayName="log10">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="Parameter Container" Tag="Parameter Tree" DisplayName="Parameter Container">
                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Materials">
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="simulateMonolayer_Air">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Air/Material data/MaterialSLDData/SLD, real"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Air/Material data/MaterialSLDData/SLD, imaginary"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Magnetization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Air/Magnetization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Air/Magnetization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Air/Magnetization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="simulateMonolayer_OleicAcid">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="7.800000000000e-8"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_OleicAcid/Material data/MaterialSLDData/SLD, real"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="7.800000000000e-8"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_OleicAcid/Material data/MaterialSLDData/SLD, imaginary"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Magnetization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_OleicAcid/Magnetization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_OleicAcid/Magnetization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_OleicAcid/Magnetization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="simulateMonolayer_Particle">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="6.132000000000e-6"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Particle/Material data/MaterialSLDData/SLD, real"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="6.132000000000e-6"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Particle/Material data/MaterialSLDData/SLD, imaginary"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Magnetization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Particle/Magnetization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Particle/Magnetization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Particle/Magnetization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="simulateMonolayer_SiO2">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="4.186000000000e-6"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_SiO2/Material data/MaterialSLDData/SLD, real"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="4.186000000000e-6"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_SiO2/Material data/MaterialSLDData/SLD, imaginary"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Magnetization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_SiO2/Magnetization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_SiO2/Magnetization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_SiO2/Magnetization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="simulateMonolayer_Si">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="2.079000000000e-6"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Si/Material data/MaterialSLDData/SLD, real"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="2.079000000000e-6"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Si/Material data/MaterialSLDData/SLD, imaginary"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Magnetization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Si/Magnetization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Si/Magnetization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Si/Magnetization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                </Item>
                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MultiLayer">
                    <Item ModelType="Parameter" Tag="children tag" DisplayName="CrossCorrelationLength">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/CrossCorrelationLength"/>
                        </Item>
                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="ExternalField">
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/ExternalField/X"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/ExternalField/Y"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/ExternalField/Z"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Layer0"/>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Layer1">
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Thickness">
                            <Parameter ParType="double" ParRole="0" ParValue="1.018000000000e+1"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/Thickness"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="1.018000000000e+1"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="ParticleLayout">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Weight">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Weight"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter Label" Tag="children tag" DisplayName="ParticleDistribution">
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="Abundance">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Abundance"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="DistributionLogNormal">
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="Median">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Distribution/DistributionLogNormal/Median"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="ScaleParameter">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Distribution/DistributionLogNormal/ScaleParameter"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="Sigma factor">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.500000000000e-1"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Distribution/DistributionLogNormal/Sigma factor"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.500000000000e-1"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Particle">
                                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Box">
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Length">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Form Factor/Box/Length"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Width">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Form Factor/Box/Width"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Height">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Form Factor/Box/Height"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Position Offset">
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Position Offset/X"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Position Offset/Y"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                            <Parameter ParType="double" ParRole="0" ParValue="-1.018000000000e+1"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Position Offset/Z"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="-1.018000000000e+1"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Interference2DParaCrystal">
                                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="BasicLattice">
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="LatticeLength1">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/LatticeType/BasicLattice/LatticeLength1"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="LatticeLength2">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/LatticeType/BasicLattice/LatticeLength2"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="Alpha">
                                        <Parameter ParType="double" ParRole="0" ParValue="9.000000000000e+1"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/LatticeType/BasicLattice/Alpha"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="9.000000000000e+1"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="DampingLength">
                                    <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/DampingLength"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="DomainSize1">
                                    <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/DomainSize1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="DomainSize2">
                                    <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/DomainSize2"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="FTDistribution2DGauss0">
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #1/FTDistribution2DGauss0/OmegaX"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #1/FTDistribution2DGauss0/OmegaY"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #1/FTDistribution2DGauss0/Gamma"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="FTDistribution2DGauss1">
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #2/FTDistribution2DGauss1/OmegaX"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #2/FTDistribution2DGauss1/OmegaY"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #2/FTDistribution2DGauss1/Gamma"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Layer2">
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Thickness">
                            <Parameter ParType="double" ParRole="0" ParValue="7.400000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer2/Thickness"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="7.400000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Layer3"/>
                </Item>
                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="GISASInstrument">
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Beam">
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Intensity">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+8"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/Intensity"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+8"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="AzimuthalAngle">
                            <Item ModelType="Parameter Label" Tag="children tag" DisplayName="DistributionNone">
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/AzimuthalAngle/Distribution/DistributionNone/Value"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Polarization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/Polarization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/Polarization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/Polarization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="InclinationAngle">
                            <Item ModelType="Parameter Label" Tag="children tag" DisplayName="DistributionNone">
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e-1"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/InclinationAngle/Distribution/DistributionNone/Value"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e-1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Wavelength">
                            <Item ModelType="Parameter Label" Tag="children tag" DisplayName="DistributionNone">
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e-1"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/Wavelength/Distribution/DistributionNone/Value"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e-1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="RectangularDetector">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Analyzer direction">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Analyzer direction/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Analyzer direction/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Analyzer direction/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Efficiency">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Efficiency"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Transmission">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Transmission"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="X axis">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Width">
                                <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/X axis/Width"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Y axis">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Height">
                                <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Y axis/Height"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="u0 (dbeam)">
                            <Parameter ParType="double" ParRole="0" ParValue="3.192250000000e+2"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/u0 (dbeam)"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="3.192250000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="v0 (dbeam)">
                            <Parameter ParType="double" ParRole="0" ParValue="3.261500000000e+2"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/v0 (dbeam)"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="3.261500000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Distance">
                            <Parameter ParType="double" ParRole="0" ParValue="5.000000000000e+3"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Distance"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="5.000000000000e+3"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="SimulationOptions" Tag="Simulation Options" DisplayName="SimulationOptions">
                <Item ModelType="Property" Tag="Run Policy" DisplayName="Run Policy">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Immediately;In background"/>
                </Item>
                <Item ModelType="Property" Tag="Number of Threads" DisplayName="Number of Threads">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Max (4 threads);3 threads;2 threads;1 thread"/>
                </Item>
                <Item ModelType="Property" Tag="Computation method" DisplayName="Computation method">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Analytical;Monte-Carlo Integration"/>
                </Item>
                <Item ModelType="Property" Tag="Number of MC points" DisplayName="Number of MC points">
                    <Parameter ParType="int" ParRole="0" ParValue="100"/>
                </Item>
                <Item ModelType="Property" Tag="Material for Fresnel calculations" DisplayName="Material for Fresnel calculations">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Ambient Layer Material;Average Layer Material"/>
                </Item>
                <Item ModelType="Property" Tag="Include specular peak" DisplayName="Include specular peak">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="No;Yes"/>
                </Item>
            </Item>
        </Item>
        <Item ModelType="JobItem" Tag="rootTag" DisplayName="JobItem">
            <Item ModelType="Property" Tag="Name" DisplayName="Name">
                <Parameter ParType="QString" ParRole="0" ParValue="job3"/>
            </Item>
            <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                <Parameter ParType="QString" ParRole="0" ParValue="{7e8d5c6a-0a90-4319-ad9f-c01f496d46b4}"/>
            </Item>
            <Item ModelType="Property" Tag="Sample" DisplayName="Sample">
                <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer"/>
            </Item>
            <Item ModelType="Property" Tag="Instrument" DisplayName="Instrument">
                <Parameter ParType="QString" ParRole="0" ParValue="GISAS"/>
            </Item>
            <Item ModelType="Property" Tag="With Fitting" DisplayName="With Fitting">
                <Parameter ParType="bool" ParRole="0" ParValue="0"/>
            </Item>
            <Item ModelType="Property" Tag="Status" DisplayName="Status">
                <Parameter ParType="QString" ParRole="0" ParValue="Completed"/>
            </Item>
            <Item ModelType="Property" Tag="Begin Time" DisplayName="Begin Time">
                <Parameter ParType="QString" ParRole="0" ParValue="2019.01.03 00:11:37"/>
            </Item>
            <Item ModelType="Property" Tag="End Time" DisplayName="End Time">
                <Parameter ParType="QString" ParRole="0" ParValue="2019.01.03 00:11:43"/>
            </Item>
            <Item ModelType="Property" Tag="Duration" DisplayName="Duration">
                <Parameter ParType="QString" ParRole="0" ParValue="6.168"/>
            </Item>
            <Item ModelType="Property" Tag="Comments" DisplayName="Comments">
                <Parameter ParType="QString" ParRole="0" ParValue=""/>
            </Item>
            <Item ModelType="Property" Tag="Progress" DisplayName="Progress">
                <Parameter ParType="int" ParRole="0" ParValue="100"/>
            </Item>
            <Item ModelType="Property" Tag="Presentation Type" DisplayName="Presentation Type">
                <Parameter ParType="QString" ParRole="0" ParValue="Color Map"/>
            </Item>
            <Item ModelType="MultiLayer" Tag="Sample Tag" DisplayName="MultiLayer">
                <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                    <Parameter ParType="double" ParRole="0" ParValue="5.000000000000e+1"/>
                </Item>
                <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                    <Parameter ParType="double" ParRole="0" ParValue="8.000000000000e+2"/>
                </Item>
                <Item ModelType="Property" Tag="Name" DisplayName="Name">
                    <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer"/>
                </Item>
                <Item ModelType="Property" Tag="CrossCorrelationLength" DisplayName="CrossCorrelationLength">
                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                </Item>
                <Item ModelType="Vector" Tag="ExternalField" DisplayName="ExternalField">
                    <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                    <Item ModelType="Property" Tag="X" DisplayName="X">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Y" DisplayName="Y">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Z" DisplayName="Z">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                </Item>
                <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                    <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                        <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Material" DisplayName="Material">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_Air" Color="#ffb3f2ff" Identifier="{2d32f8dc-8653-4f3e-9f33-5a0d917c5a3d}"/>
                    </Item>
                    <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                        <Parameter ParType="int" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                        <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                    </Item>
                </Item>
                <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                    <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                        <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                        <Parameter ParType="double" ParRole="0" ParValue="3.000000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                        <Parameter ParType="double" ParRole="0" ParValue="1.018000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Material" DisplayName="Material">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_OleicAcid" Color="#ffea8887" Identifier="{f544cb6c-e7b8-438f-982b-ddb1940f0862}"/>
                    </Item>
                    <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                        <Parameter ParType="int" ParRole="0" ParValue="10"/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                        <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                    </Item>
                    <Item ModelType="ParticleLayout" Tag="Layout tag" DisplayName="ParticleLayout">
                        <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                            <Parameter ParType="double" ParRole="0" ParValue="-7.300000000000e+1"/>
                        </Item>
                        <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                            <Parameter ParType="double" ParRole="0" ParValue="8.600000000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="Approximation" DisplayName="Approximation">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Decoupling Approximation;Size Space Coupling Approximation"/>
                        </Item>
                        <Item ModelType="Property" Tag="TotalParticleDensity" DisplayName="TotalParticleDensity">
                            <Parameter ParType="double" ParRole="0" ParValue="5.670271447235e-3"/>
                        </Item>
                        <Item ModelType="Property" Tag="Weight" DisplayName="Weight">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                        </Item>
                        <Item ModelType="ParticleDistribution" Tag="Particle Tag" DisplayName="ParticleDistribution">
                            <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                                <Parameter ParType="double" ParRole="0" ParValue="-2.220000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                                <Parameter ParType="double" ParRole="0" ParValue="8.600000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="Abundance" DisplayName="Abundance">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="3" ParExt="Cosine distribution;Gate distribution;Gaussian distribution;Log Normal distribution;Lorentz distribution;Trapezoid distribution"/>
                                <Item ModelType="DistributionGaussian" Tag="Item tag" DisplayName="DistributionGaussian">
                                    <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                        <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Mean" DisplayName="Mean">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="StdDev" DisplayName="StdDev">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Number of samples" DisplayName="Number of samples">
                                        <Parameter ParType="int" ParRole="0" ParValue="5"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Sigma factor" DisplayName="Sigma factor">
                                        <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="GroupProperty" Tag="Limits" DisplayName="Limits">
                                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Limited;Unlimited;LowerLimited;Nonnegative;Positive;UpperLimited"/>
                                        <Item ModelType="RealLimitsLimitless" Tag="Item tag" DisplayName="RealLimitsLimitless"/>
                                    </Item>
                                </Item>
                                <Item ModelType="DistributionLogNormal" Tag="Item tag" DisplayName="DistributionLogNormal">
                                    <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                        <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Median" DisplayName="Median">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="ScaleParameter" DisplayName="ScaleParameter">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Number of samples" DisplayName="Number of samples">
                                        <Parameter ParType="int" ParRole="0" ParValue="5"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Sigma factor" DisplayName="Sigma factor">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.500000000000e-1"/>
                                    </Item>
                                    <Item ModelType="GroupProperty" Tag="Limits" DisplayName="Limits">
                                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Limited;Unlimited;LowerLimited;Nonnegative;Positive;UpperLimited"/>
                                        <Item ModelType="RealLimitsLimitless" Tag="Item tag" DisplayName="RealLimitsLimitless"/>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="Particle" Tag="Particle Tag" DisplayName="Particle">
                                <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                                    <Parameter ParType="double" ParRole="0" ParValue="-3.720000000000e+2"/>
                                </Item>
                                <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                                    <Parameter ParType="double" ParRole="0" ParValue="8.600000000000e+2"/>
                                </Item>
                                <Item ModelType="GroupProperty" Tag="Form Factor" DisplayName="Form Factor">
                                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Aniso Pyramid;Box;Cone;Cone6;Cuboctahedron;Cylinder;Dodecahedron;Dot;Ellipsoidal Cylinder;Full Sphere;Full Spheroid;Hemi Ellipsoid;Icosahedron;Prism3;Prism6;Pyramid;Ripple1;Ripple2;Tetrahedron;Truncated Cube;Truncated Sphere;Truncated Spheroid"/>
                                    <Item ModelType="Cylinder" Tag="Item tag" DisplayName="Cylinder">
                                        <Item ModelType="Property" Tag="Radius" DisplayName="Radius">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.000000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Height" DisplayName="Height">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.600000000000e+1"/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Box" Tag="Item tag" DisplayName="Box">
                                        <Item ModelType="Property" Tag="Length" DisplayName="Length">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Width" DisplayName="Width">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Height" DisplayName="Height">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                        </Item>
                                    </Item>
                                </Item>
                                <Item ModelType="Property" Tag="Material" DisplayName="Material">
                                    <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_Particle" Color="#ff92c6ff" Identifier="{d2198e19-e9a9-4e89-b13c-e13de9bfc567}"/>
                                </Item>
                                <Item ModelType="Property" Tag="Abundance" DisplayName="Abundance">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Vector" Tag="Position Offset" DisplayName="Position Offset">
                                    <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, -10.18)"/>
                                    <Item ModelType="Property" Tag="X" DisplayName="X">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                        <Parameter ParType="double" ParRole="0" ParValue="-1.018000000000e+1"/>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="Property" Tag="Distributed parameter" DisplayName="Distributed parameter">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="None;Particle/Box/Length;Particle/Box/Width;Particle/Box/Height;Particle/Position Offset/X;Particle/Position Offset/Y;Particle/Position Offset/Z"/>
                            </Item>
                            <Item ModelType="Property" Tag="Linked parameter" DisplayName="Linked parameter">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0,1" ParExt="Particle/Box/Width;Particle/Box/Height;Particle/Position Offset/X;Particle/Position Offset/Y;Particle/Position Offset/Z"/>
                            </Item>
                        </Item>
                        <Item ModelType="Interference2DParaCrystal" Tag="Interference Tag" DisplayName="Interference2DParaCrystal">
                            <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                                <Parameter ParType="double" ParRole="0" ParValue="-2.220000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                                <Parameter ParType="double" ParRole="0" ParValue="1.010000000000e+3"/>
                            </Item>
                            <Item ModelType="GroupProperty" Tag="LatticeType" DisplayName="LatticeType">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Basic;Hexagonal;Square"/>
                                <Item ModelType="HexagonalLattice" Tag="Item tag" DisplayName="HexagonalLattice">
                                    <Item ModelType="Property" Tag="LatticeLength" DisplayName="LatticeLength">
                                        <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e+1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Xi" DisplayName="Xi">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                                <Item ModelType="BasicLattice" Tag="Item tag" DisplayName="BasicLattice">
                                    <Item ModelType="Property" Tag="LatticeLength1" DisplayName="LatticeLength1">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="LatticeLength2" DisplayName="LatticeLength2">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Alpha" DisplayName="Alpha">
                                        <Parameter ParType="double" ParRole="0" ParValue="9.000000000000e+1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Xi" DisplayName="Xi">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="Property" Tag="Integration_over_xi" DisplayName="Integration_over_xi">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                            <Item ModelType="Property" Tag="DampingLength" DisplayName="DampingLength">
                                <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="DomainSize1" DisplayName="DomainSize1">
                                <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="DomainSize2" DisplayName="DomainSize2">
                                <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                            </Item>
                            <Item ModelType="GroupProperty" Tag="PDF #1" DisplayName="PDF #1">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="3" ParExt="Cauchy 2D;Cone 2D;Gate 2D;Gauss 2D;Voigt 2D"/>
                                <Item ModelType="FTDistribution2DCauchy" Tag="Item tag" DisplayName="FTDistribution2DCauchy0">
                                    <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                                <Item ModelType="FTDistribution2DGauss" Tag="Item tag" DisplayName="FTDistribution2DGauss0">
                                    <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="GroupProperty" Tag="PDF #2" DisplayName="PDF #2">
                                <Parameter ParType="ComboProperty" ParRole="0" ParValue="3" ParExt="Cauchy 2D;Cone 2D;Gate 2D;Gauss 2D;Voigt 2D"/>
                                <Item ModelType="FTDistribution2DCauchy" Tag="Item tag" DisplayName="FTDistribution2DCauchy">
                                    <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                                <Item ModelType="FTDistribution2DGauss" Tag="Item tag" DisplayName="FTDistribution2DGauss1">
                                    <Item ModelType="Property" Tag="OmegaX" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="OmegaY" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Gamma" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                </Item>
                <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                    <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                        <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                        <Parameter ParType="double" ParRole="0" ParValue="6.800000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                        <Parameter ParType="double" ParRole="0" ParValue="7.400000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Material" DisplayName="Material">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_SiO2" Color="#ff795b37" Identifier="{872b5dde-7794-427a-b00e-e7ab2adbd585}"/>
                    </Item>
                    <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                        <Parameter ParType="int" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                        <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                    </Item>
                </Item>
                <Item ModelType="Layer" Tag="Layer tag" DisplayName="Layer">
                    <Item ModelType="Property" Tag="xpos" DisplayName="xpos">
                        <Parameter ParType="double" ParRole="0" ParValue="1.400000000000e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="ypos" DisplayName="ypos">
                        <Parameter ParType="double" ParRole="0" ParValue="1.040000000000e+2"/>
                    </Item>
                    <Item ModelType="Property" Tag="Thickness" DisplayName="Thickness">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Material" DisplayName="Material">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="simulateMonolayer_Si" Color="#ff0d433f" Identifier="{dbe9a105-f94c-4487-a19a-c15b2dc2b99c}"/>
                    </Item>
                    <Item ModelType="Property" Tag="Number of slices" DisplayName="Number of slices">
                        <Parameter ParType="int" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Top roughness" DisplayName="Top roughness">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Basic;No"/>
                        <Item ModelType="LayerZeroRoughness" Tag="Item tag" DisplayName="LayerZeroRoughness"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="MaterialContainer" Tag="Material Container" DisplayName="MaterialContainer">
                <Item ModelType="Property" Tag="Name" DisplayName="Name">
                    <Parameter ParType="QString" ParRole="0" ParValue="Materials"/>
                </Item>
                <Item ModelType="Material" Tag="MaterialVector" DisplayName="Material">
                    <Item ModelType="Property" Tag="Name" DisplayName="Name">
                        <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_Air"/>
                    </Item>
                    <Item ModelType="Property" Tag="Color" DisplayName="Color">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="[179, 242, 255] (255)" Color="#ffb3f2ff" Identifier=""/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                        <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                            <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                        <Parameter ParType="QString" ParRole="0" ParValue="{2d32f8dc-8653-4f3e-9f33-5a0d917c5a3d}"/>
                    </Item>
                </Item>
                <Item ModelType="Material" Tag="MaterialVector" DisplayName="Material">
                    <Item ModelType="Property" Tag="Name" DisplayName="Name">
                        <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_OleicAcid"/>
                    </Item>
                    <Item ModelType="Property" Tag="Color" DisplayName="Color">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="[234, 136, 135] (255)" Color="#ffea8887" Identifier=""/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                        <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                            <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="7.800000000000e-8"/>
                            </Item>
                            <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                        <Parameter ParType="QString" ParRole="0" ParValue="{f544cb6c-e7b8-438f-982b-ddb1940f0862}"/>
                    </Item>
                </Item>
                <Item ModelType="Material" Tag="MaterialVector" DisplayName="Material">
                    <Item ModelType="Property" Tag="Name" DisplayName="Name">
                        <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_Particle"/>
                    </Item>
                    <Item ModelType="Property" Tag="Color" DisplayName="Color">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="[146, 198, 255] (255)" Color="#ff92c6ff" Identifier=""/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                        <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                            <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="6.132000000000e-6"/>
                            </Item>
                            <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                        <Parameter ParType="QString" ParRole="0" ParValue="{d2198e19-e9a9-4e89-b13c-e13de9bfc567}"/>
                    </Item>
                </Item>
                <Item ModelType="Material" Tag="MaterialVector" DisplayName="Material">
                    <Item ModelType="Property" Tag="Name" DisplayName="Name">
                        <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_SiO2"/>
                    </Item>
                    <Item ModelType="Property" Tag="Color" DisplayName="Color">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="[121, 91, 55] (255)" Color="#ff795b37" Identifier=""/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                        <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                            <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="4.186000000000e-6"/>
                            </Item>
                            <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                        <Parameter ParType="QString" ParRole="0" ParValue="{872b5dde-7794-427a-b00e-e7ab2adbd585}"/>
                    </Item>
                </Item>
                <Item ModelType="Material" Tag="MaterialVector" DisplayName="Material">
                    <Item ModelType="Property" Tag="Name" DisplayName="Name">
                        <Parameter ParType="QString" ParRole="0" ParValue="simulateMonolayer_Si"/>
                    </Item>
                    <Item ModelType="Property" Tag="Color" DisplayName="Color">
                        <Parameter ParType="ExternalProperty" ParRole="0" Text="[13, 67, 63] (255)" Color="#ff0d433f" Identifier=""/>
                    </Item>
                    <Item ModelType="GroupProperty" Tag="Material data" DisplayName="Material data">
                        <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Refractive index based;SLD based"/>
                        <Item ModelType="MaterialRefractiveData" Tag="Item tag" DisplayName="MaterialRefractiveData">
                            <Item ModelType="Property" Tag="Delta" DisplayName="Delta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Beta" DisplayName="Beta">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="MaterialSLDData" Tag="Item tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Property" Tag="SLD, real" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="2.079000000000e-6"/>
                            </Item>
                            <Item ModelType="Property" Tag="SLD, imaginary" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Magnetization" DisplayName="Magnetization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                        <Parameter ParType="QString" ParRole="0" ParValue="{dbe9a105-f94c-4487-a19a-c15b2dc2b99c}"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="GISASInstrument" Tag="Instrument Tag" DisplayName="GISASInstrument">
                <Item ModelType="Property" Tag="Name" DisplayName="Name">
                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument"/>
                </Item>
                <Item ModelType="Property" Tag="Identifier" DisplayName="Identifier">
                    <Parameter ParType="QString" ParRole="0" ParValue="{937e51c8-b501-4cb1-b7da-cf2e384a646b}"/>
                </Item>
                <Item ModelType="GISASBeam" Tag="Beam" DisplayName="Beam">
                    <Item ModelType="Property" Tag="Intensity" DisplayName="Intensity">
                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+8"/>
                    </Item>
                    <Item ModelType="BeamAzimuthalAngle" Tag="AzimuthalAngle" DisplayName="AzimuthalAngle">
                        <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="5" ParExt="Cosine;Gate;Gaussian;Log Normal;Lorentz;None;Trapezoid"/>
                            <Item ModelType="DistributionNone" Tag="Item tag" DisplayName="DistributionNone">
                                <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Mean" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Vector" Tag="Polarization" DisplayName="Polarization">
                        <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                        <Item ModelType="Property" Tag="X" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Y" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Z" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                    </Item>
                    <Item ModelType="BeamInclinationAngle" Tag="InclinationAngle" DisplayName="InclinationAngle">
                        <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="5" ParExt="Cosine;Gate;Gaussian;Log Normal;Lorentz;None;Trapezoid"/>
                            <Item ModelType="DistributionNone" Tag="Item tag" DisplayName="DistributionNone">
                                <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Mean" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="4.000000000000e-1"/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="BeamWavelength" Tag="Wavelength" DisplayName="Wavelength">
                        <Item ModelType="GroupProperty" Tag="Distribution" DisplayName="Distribution">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="5" ParExt="Cosine;Gate;Gaussian;Log Normal;Lorentz;None;Trapezoid"/>
                            <Item ModelType="DistributionNone" Tag="Item tag" DisplayName="DistributionNone">
                                <Item ModelType="Property" Tag="is initialized" DisplayName="is initialized">
                                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Mean" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e-1"/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                </Item>
                <Item ModelType="GroupProperty" Tag="Detector" DisplayName="Detector">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Rectangular detector;Spherical detector"/>
                    <Item ModelType="SphericalDetector" Tag="Item tag" DisplayName="SphericalDetector">
                        <Item ModelType="Vector" Tag="Analyzer direction" DisplayName="Analyzer direction">
                            <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                            <Item ModelType="Property" Tag="X" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="Property" Tag="Efficiency" DisplayName="Efficiency">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Transmission" DisplayName="Transmission">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                        </Item>
                        <Item ModelType="BasicAxis" Tag="Phi axis" DisplayName="Phi axis">
                            <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                            <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                                <Parameter ParType="int" ParRole="0" ParValue="100"/>
                            </Item>
                            <Item ModelType="Property" Tag="Min" DisplayName="Min">
                                <Parameter ParType="double" ParRole="0" ParValue="-1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Max" DisplayName="Max">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="title" DisplayName="title">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                            <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                        </Item>
                        <Item ModelType="BasicAxis" Tag="Alpha axis" DisplayName="Alpha axis">
                            <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                            <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                                <Parameter ParType="int" ParRole="0" ParValue="100"/>
                            </Item>
                            <Item ModelType="Property" Tag="Min" DisplayName="Min">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Max" DisplayName="Max">
                                <Parameter ParType="double" ParRole="0" ParValue="2.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="title" DisplayName="title">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                            <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                        </Item>
                        <Item ModelType="GroupProperty" Tag="Resolution function" DisplayName="Type">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="2D Gaussian;None"/>
                            <Item ModelType="ResolutionFunctionNone" Tag="Item tag" DisplayName="ResolutionFunctionNone"/>
                        </Item>
                    </Item>
                    <Item ModelType="RectangularDetector" Tag="Item tag" DisplayName="RectangularDetector">
                        <Item ModelType="Vector" Tag="Analyzer direction" DisplayName="Analyzer direction">
                            <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                            <Item ModelType="Property" Tag="X" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="Property" Tag="Efficiency" DisplayName="Efficiency">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Transmission" DisplayName="Transmission">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                        </Item>
                        <Item ModelType="BasicAxis" Tag="X axis" DisplayName="X axis">
                            <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                            <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                                <Parameter ParType="int" ParRole="0" ParValue="128"/>
                            </Item>
                            <Item ModelType="Property" Tag="Min" DisplayName="Min">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Max" DisplayName="Width">
                                <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="title" DisplayName="title">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                            <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                        </Item>
                        <Item ModelType="BasicAxis" Tag="Y axis" DisplayName="Y axis">
                            <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                            <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                                <Parameter ParType="int" ParRole="0" ParValue="256"/>
                            </Item>
                            <Item ModelType="Property" Tag="Min" DisplayName="Min">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Max" DisplayName="Height">
                                <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="title" DisplayName="title">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                            <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                                <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                            </Item>
                        </Item>
                        <Item ModelType="Property" Tag="Alignment" DisplayName="Alignment">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Generic;Perpendicular to direct beam;Perpendicular to sample x-axis;Perpendicular to reflected beam;Perpendicular to reflected beam (dpos)"/>
                        </Item>
                        <Item ModelType="Vector" Tag="Normal vector" DisplayName="Normal vector">
                            <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                            <Item ModelType="Property" Tag="X" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+3"/>
                            </Item>
                            <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="Vector" Tag="Direction vector" DisplayName="Direction vector">
                            <Parameter ParType="QString" ParRole="0" ParValue="(0, 0, 0)"/>
                            <Item ModelType="Property" Tag="X" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Y" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="-1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Z" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                        </Item>
                        <Item ModelType="Property" Tag="u0" DisplayName="u0">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+1"/>
                        </Item>
                        <Item ModelType="Property" Tag="v0" DisplayName="v0">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="u0 (dbeam)" DisplayName="u0 (dbeam)">
                            <Parameter ParType="double" ParRole="0" ParValue="3.192250000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="v0 (dbeam)" DisplayName="v0 (dbeam)">
                            <Parameter ParType="double" ParRole="0" ParValue="3.261500000000e+2"/>
                        </Item>
                        <Item ModelType="Property" Tag="Distance" DisplayName="Distance">
                            <Parameter ParType="double" ParRole="0" ParValue="5.000000000000e+3"/>
                        </Item>
                        <Item ModelType="GroupProperty" Tag="Resolution function" DisplayName="Type">
                            <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="2D Gaussian;None"/>
                            <Item ModelType="ResolutionFunctionNone" Tag="Item tag" DisplayName="ResolutionFunctionNone"/>
                        </Item>
                    </Item>
                </Item>
                <Item ModelType="GroupProperty" Tag="Background" DisplayName="Type">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="1" ParExt="Constant background;None;Poisson noise"/>
                    <Item ModelType="NoBackground" Tag="Item tag" DisplayName="NoBackground"/>
                </Item>
            </Item>
            <Item ModelType="IntensityData" Tag="Output Tag" DisplayName="IntensityData">
                <Item ModelType="Property" Tag="FileName" DisplayName="FileName">
                    <Parameter ParType="QString" ParRole="0" ParValue="jobdata_job3_0.int.gz"/>
                </Item>
                <Item ModelType="Property" Tag="Axes Units" DisplayName="Axes Units">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="4" ParExt="nbins;Radians;Degrees;q-space;mm"/>
                </Item>
                <Item ModelType="Property" Tag="Title" DisplayName="Title">
                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                </Item>
                <Item ModelType="Property" Tag="Projections" DisplayName="Projections">
                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                </Item>
                <Item ModelType="Property" Tag="Interpolation" DisplayName="Interpolation">
                    <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                </Item>
                <Item ModelType="Property" Tag="Gradient" DisplayName="Gradient">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="9" ParExt="Grayscale;Hot;Cold;Night;Candy;Geography;Ion;Thermal;Polar;Spectrum;Jet;Hues"/>
                </Item>
                <Item ModelType="BasicAxis" Tag="x-axis" DisplayName="x-axis">
                    <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                        <Parameter ParType="int" ParRole="0" ParValue="128"/>
                    </Item>
                    <Item ModelType="Property" Tag="Min" DisplayName="Min">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Max" DisplayName="Max">
                        <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                    </Item>
                    <Item ModelType="Property" Tag="title" DisplayName="title">
                        <Parameter ParType="QString" ParRole="0" ParValue="X [mm]"/>
                    </Item>
                    <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                </Item>
                <Item ModelType="BasicAxis" Tag="y-axis" DisplayName="y-axis">
                    <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                        <Parameter ParType="int" ParRole="0" ParValue="256"/>
                    </Item>
                    <Item ModelType="Property" Tag="Min" DisplayName="Min">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                    </Item>
                    <Item ModelType="Property" Tag="Max" DisplayName="Max">
                        <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                    </Item>
                    <Item ModelType="Property" Tag="title" DisplayName="title">
                        <Parameter ParType="QString" ParRole="0" ParValue="Y [mm]"/>
                    </Item>
                    <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                </Item>
                <Item ModelType="AmplitudeAxis" Tag="color-axis" DisplayName="color-axis">
                    <Item ModelType="Property" Tag="Visibility" DisplayName="Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Nbins" DisplayName="Nbins">
                        <Parameter ParType="int" ParRole="0" ParValue="100"/>
                    </Item>
                    <Item ModelType="Property" Tag="Min" DisplayName="Min">
                        <Parameter ParType="double" ParRole="0" ParValue="2.090899193997e-3"/>
                    </Item>
                    <Item ModelType="Property" Tag="Max" DisplayName="Max">
                        <Parameter ParType="double" ParRole="0" ParValue="2.299989113397e+1"/>
                    </Item>
                    <Item ModelType="Property" Tag="title" DisplayName="title">
                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                    </Item>
                    <Item ModelType="Property" Tag="Title Visibility" DisplayName="Title Visibility">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                    <Item ModelType="Property" Tag="Lock (min, max)" DisplayName="Lock (min, max)">
                        <Parameter ParType="bool" ParRole="0" ParValue="0"/>
                    </Item>
                    <Item ModelType="Property" Tag="log10" DisplayName="log10">
                        <Parameter ParType="bool" ParRole="0" ParValue="1"/>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="Parameter Container" Tag="Parameter Tree" DisplayName="Parameter Container">
                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Materials">
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="simulateMonolayer_Air">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Air/Material data/MaterialSLDData/SLD, real"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Air/Material data/MaterialSLDData/SLD, imaginary"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Magnetization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Air/Magnetization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Air/Magnetization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Air/Magnetization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="simulateMonolayer_OleicAcid">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="7.800000000000e-8"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_OleicAcid/Material data/MaterialSLDData/SLD, real"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="7.800000000000e-8"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_OleicAcid/Material data/MaterialSLDData/SLD, imaginary"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Magnetization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_OleicAcid/Magnetization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_OleicAcid/Magnetization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_OleicAcid/Magnetization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="simulateMonolayer_Particle">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="6.132000000000e-6"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Particle/Material data/MaterialSLDData/SLD, real"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="6.132000000000e-6"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Particle/Material data/MaterialSLDData/SLD, imaginary"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Magnetization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Particle/Magnetization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Particle/Magnetization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Particle/Magnetization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="simulateMonolayer_SiO2">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="4.186000000000e-6"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_SiO2/Material data/MaterialSLDData/SLD, real"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="4.186000000000e-6"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_SiO2/Material data/MaterialSLDData/SLD, imaginary"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Magnetization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_SiO2/Magnetization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_SiO2/Magnetization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_SiO2/Magnetization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="simulateMonolayer_Si">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MaterialSLDData">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, real">
                                <Parameter ParType="double" ParRole="0" ParValue="2.079000000000e-6"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Si/Material data/MaterialSLDData/SLD, real"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="2.079000000000e-6"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="SLD, imaginary">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Si/Material data/MaterialSLDData/SLD, imaginary"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Magnetization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Si/Magnetization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Si/Magnetization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="Materials/simulateMonolayer_Si/Magnetization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                </Item>
                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="MultiLayer">
                    <Item ModelType="Parameter" Tag="children tag" DisplayName="CrossCorrelationLength">
                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/CrossCorrelationLength"/>
                        </Item>
                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                        </Item>
                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="ExternalField">
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/ExternalField/X"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/ExternalField/Y"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/ExternalField/Z"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Layer0"/>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Layer1">
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Thickness">
                            <Parameter ParType="double" ParRole="0" ParValue="1.018000000000e+1"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/Thickness"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="1.018000000000e+1"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="ParticleLayout">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Weight">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Weight"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter Label" Tag="children tag" DisplayName="ParticleDistribution">
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="Abundance">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Abundance"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="DistributionLogNormal">
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="Median">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Distribution/DistributionLogNormal/Median"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="ScaleParameter">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Distribution/DistributionLogNormal/ScaleParameter"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="Sigma factor">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.500000000000e-1"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Distribution/DistributionLogNormal/Sigma factor"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.500000000000e-1"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Particle">
                                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Box">
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Length">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Form Factor/Box/Length"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Width">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Form Factor/Box/Width"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Height">
                                            <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Form Factor/Box/Height"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="8.580000000000e+0"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Position Offset">
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Position Offset/X"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Position Offset/Y"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                            <Parameter ParType="double" ParRole="0" ParValue="-1.018000000000e+1"/>
                                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/ParticleDistribution/Particle/Position Offset/Z"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                                <Parameter ParType="double" ParRole="0" ParValue="-1.018000000000e+1"/>
                                            </Item>
                                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                            </Item>
                                        </Item>
                                    </Item>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Interference2DParaCrystal">
                                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="BasicLattice">
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="LatticeLength1">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/LatticeType/BasicLattice/LatticeLength1"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="LatticeLength2">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/LatticeType/BasicLattice/LatticeLength2"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.328000000000e+1"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="Alpha">
                                        <Parameter ParType="double" ParRole="0" ParValue="9.000000000000e+1"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/LatticeType/BasicLattice/Alpha"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="9.000000000000e+1"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="DampingLength">
                                    <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/DampingLength"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="DomainSize1">
                                    <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/DomainSize1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="DomainSize2">
                                    <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/DomainSize2"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="8.770000000000e+2"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="FTDistribution2DGauss0">
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #1/FTDistribution2DGauss0/OmegaX"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #1/FTDistribution2DGauss0/OmegaY"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #1/FTDistribution2DGauss0/Gamma"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                </Item>
                                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="FTDistribution2DGauss1">
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="OmegaX">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #2/FTDistribution2DGauss1/OmegaX"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="OmegaY">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #2/FTDistribution2DGauss1/OmegaY"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="1.630000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                    <Item ModelType="Parameter" Tag="children tag" DisplayName="Gamma">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                        <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                            <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer1/ParticleLayout/Interference2DParaCrystal/PDF #2/FTDistribution2DGauss1/Gamma"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                        </Item>
                                        <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                            <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                        </Item>
                                    </Item>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Layer2">
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Thickness">
                            <Parameter ParType="double" ParRole="0" ParValue="7.400000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="MultiLayer/Layer2/Thickness"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="7.400000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Layer3"/>
                </Item>
                <Item ModelType="Parameter Label" Tag="children tag" DisplayName="GISASInstrument">
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Beam">
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Intensity">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+8"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/Intensity"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+8"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="AzimuthalAngle">
                            <Item ModelType="Parameter Label" Tag="children tag" DisplayName="DistributionNone">
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/AzimuthalAngle/Distribution/DistributionNone/Value"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Polarization">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/Polarization/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/Polarization/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/Polarization/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="InclinationAngle">
                            <Item ModelType="Parameter Label" Tag="children tag" DisplayName="DistributionNone">
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="4.000000000000e-1"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/InclinationAngle/Distribution/DistributionNone/Value"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="4.000000000000e-1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Wavelength">
                            <Item ModelType="Parameter Label" Tag="children tag" DisplayName="DistributionNone">
                                <Item ModelType="Parameter" Tag="children tag" DisplayName="Value">
                                    <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e-1"/>
                                    <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                        <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Beam/Wavelength/Distribution/DistributionNone/Value"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                        <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e-1"/>
                                    </Item>
                                    <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                        <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                    </Item>
                                </Item>
                            </Item>
                        </Item>
                    </Item>
                    <Item ModelType="Parameter Label" Tag="children tag" DisplayName="RectangularDetector">
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Analyzer direction">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="X">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Analyzer direction/X"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Y">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Analyzer direction/Y"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Z">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Analyzer direction/Z"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Efficiency">
                            <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Efficiency"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="0.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Transmission">
                            <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Transmission"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="1.000000000000e+0"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="X axis">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Width">
                                <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/X axis/Width"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter Label" Tag="children tag" DisplayName="Y axis">
                            <Item ModelType="Parameter" Tag="children tag" DisplayName="Height">
                                <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                                <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                    <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Y axis/Height"/>
                                </Item>
                                <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                    <Parameter ParType="double" ParRole="0" ParValue="6.400000000000e+2"/>
                                </Item>
                                <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                    <Parameter ParType="QString" ParRole="0" ParValue=""/>
                                </Item>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="u0 (dbeam)">
                            <Parameter ParType="double" ParRole="0" ParValue="3.192250000000e+2"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/u0 (dbeam)"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="3.192250000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="v0 (dbeam)">
                            <Parameter ParType="double" ParRole="0" ParValue="3.261500000000e+2"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/v0 (dbeam)"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="3.261500000000e+2"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                        <Item ModelType="Parameter" Tag="children tag" DisplayName="Distance">
                            <Parameter ParType="double" ParRole="0" ParValue="5.000000000000e+3"/>
                            <Item ModelType="Property" Tag="Link" DisplayName="Link">
                                <Parameter ParType="QString" ParRole="0" ParValue="GISASInstrument/Detector/RectangularDetector/Distance"/>
                            </Item>
                            <Item ModelType="Property" Tag="Backup" DisplayName="Backup">
                                <Parameter ParType="double" ParRole="0" ParValue="5.000000000000e+3"/>
                            </Item>
                            <Item ModelType="Property" Tag="Domain" DisplayName="Domain">
                                <Parameter ParType="QString" ParRole="0" ParValue=""/>
                            </Item>
                        </Item>
                    </Item>
                </Item>
            </Item>
            <Item ModelType="SimulationOptions" Tag="Simulation Options" DisplayName="SimulationOptions">
                <Item ModelType="Property" Tag="Run Policy" DisplayName="Run Policy">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Immediately;In background"/>
                </Item>
                <Item ModelType="Property" Tag="Number of Threads" DisplayName="Number of Threads">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Max (4 threads);3 threads;2 threads;1 thread"/>
                </Item>
                <Item ModelType="Property" Tag="Computation method" DisplayName="Computation method">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Analytical;Monte-Carlo Integration"/>
                </Item>
                <Item ModelType="Property" Tag="Number of MC points" DisplayName="Number of MC points">
                    <Parameter ParType="int" ParRole="0" ParValue="100"/>
                </Item>
                <Item ModelType="Property" Tag="Material for Fresnel calculations" DisplayName="Material for Fresnel calculations">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="Ambient Layer Material;Average Layer Material"/>
                </Item>
                <Item ModelType="Property" Tag="Include specular peak" DisplayName="Include specular peak">
                    <Parameter ParType="ComboProperty" ParRole="0" ParValue="0" ParExt="No;Yes"/>
                </Item>
            </Item>
        </Item>
    </JobModel>
</BornAgain>
