"""
       The following table describes all of the available commands and queries:
       UNITS tt    Specifies the operational units designated by the mnemonic parameter tt.
       UNITS?      Possible parameters are:
                     NM for nanometers, UM for micrometers, WN for wavenumbers (cm-1)
                   The response to UNITS? is always the two character mnemonic for the current units.

       GOWAVE xxx.xxx   Moves the wavelength drive at maximum speed to the step position closest
       WAVE?            to the specified wavelength parameter. This parameter must be in the current
                        units and may be either a floating-point number or an integer.

       CALIBRATE xxx.xxx    Execute this command to define the current position as the wavelength
                            specified in the numeric parameter XXX.XXX. Calculates a new OFFSET for
                            the grating and saves it accordingly.

       ABORT       Stops any wavelength motion immediately, i.e. GOSCAN, GOWAVE, STEP, etc...


       STEP xxxx     Moves the wavelength drive by the integer number of steps indicated in XXXX.
       STEP?         The parameter can be positive or negative, however, one step is the smallest
                     increment the Cornerstone can move, and so this parameter must be an integer.
                     The response to STEP? is the current step position as measured from the
                     physical home sensors.

       GRAT x        Moves the wavelength drive to the grating specified in the integer parameter.
       GRAT?         The parameter should be either "1" or "2". When changing to grating #2, the
                     system stops at the zero order position for that grating.
                     The response to GRAT? contains three parameters separated by commas without
                     spaces. The first parameter is the grating number, then the lines/mm, then
                     the label for that grating

       GRAT1LABEL tttttt    Sets the user defined label for the grating #1 to the < 9 characters
       GRAT1LABEL?          parameter tttttt. The parameter can be letters or numbers. 
       GRAT2LABEL tttttt    same for the grating #2 
       GRAT2LABEL?

       GRAT1LINES xxxx    Sets the lines per millimeter of grating #1 to the integer parameter
       GRAT1LINES?        specified as xxxx Warning: this value is used to calculate wavelength
                          motion. Lines/mm is usually changed only when installing a new grating,
                          and in that case, the parameter should match the value provided by Newport
       GRAT2LINES xxxx    same for the grating #2
       GRAT2LINES? 

       GRAT1FACTOR xxx.xxx Sets the calibration factor of grating #1 to the numeric parameter
       GRAT1FACTOR?        specified as xxx.xxx. Warning: this value is used to calculate wavelength
                           motion. Factor is usually changed only when installing a new grating, and
                           in that case, the parameter should match the value provided by Oriel
       GRAT2FACTOR xxx.xxx same for the grating #2
       GRAT2FACTOR? 

       GRAT1OFFSET xxx.xxx Sets the calibration offset for grating #1 as the floating-point parameter
       GRAT1OFFSET?        specified as xxx.xxx. Warning: this value is used to calculate wavelength
                           motion. Offset is usually changed only when installing a new grating, and
                           in that case, the parameter should match the value provided by Newport
       GRAT2OFFSET xxx.xxx same for the grating #2
       GRAT2OFFSET? 

       GRAT1ZERO xxx.xxx   Sets the zero parameter for grating #1 as thefloating-point parameter
       GRAT1ZERO?          specified in XXX.XXX. Warning: this value is used to calculate wavelength
                           motion. Zero is usually changed onl if the default value becomes corrupted.
                           The correct value for this parameter is 0.0872665
       GRAT2ZERO xxx.xxx   same for the grating #2
       GRAT2ZERO?          The correct value for this parameter is 3.2288589


       SHUTTER t     Closes or opens the shutter depending upon the single letter mnemonic parameter t.
       SHUTTER?      Closing the shutter requires "C", whereas opening it requires "O". The response to
                     SHUTTER? is simply the  one character parameter describing the current state

       FILTER x     Moves the filter wheel to the position specified in the single integer parameter x.
       FILTER?      Acceptable values range from 1 through 6. The response to FILTER? is the integer
                    value describing the current filter position; if there is no filter wheel connected,
                    or if the wheel is out of position, 0 is returned and an error is set in the status
                    byte              

       INFO?   Query for basic instrument information. Generates the same response as the GPIB specific
               *IDN? That response is "Oriel, Model 74000 Cornerstone 130,SNXXX,VYY.YY.YY" where XXX is
               the unit's serial number and YY.YY.YY is the version number for internal firmware. This
               information is displayed for 3 seconds when [LOCAL] is pressed on the Hand Controller.
               Model 74000 is  displayed for RS232/GPIB instruments. Model 74004 is displayed for USB
               instruments

       STB?    Query status byte. The response will be 32 when an error occurred or 00 when no error
               is present. Reading this code clears the status byte.
               
       ERROR?  Use this query to obtain further information about an error state reported in the
               Status byte. The response will be an integer from 0 through 9.
"""