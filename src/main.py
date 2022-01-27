'''!@file       main.py
    The main code to run on the microcontroller to complete a step response on
    a motor. Includes functionality to set the setpoint and controller gain.
    The time and motor position are printed to the console as a two column list
    after the step response.
    @author     Tori Bornino
    @author     Jackson McLaughlin
    @author     Zach Stednitz
    @date       January 27, 2022
'''

import time
import pyb

import shares
import encoder
import proportionalcontroller
import motor

##  @brief     Encoder PPR in ticks per revolution.
PPR = 256*4

if __name__ == '__main__':
    
    # Instantiate share for motor position
    encoder_share = shares.Share(0)

    # Instantiate encoder 1 with default pins and timer
    encoder1 = encoder.EncoderDriver(pyb.Pin.cpu.B6, pyb.Pin.cpu.B7, 4)
    
    # Instantiate proportional controller 1
    pController1 = proportionalcontroller.ProportionalController(0, 1, encoder_share)
    
    # Instantiate motor 1 with default pins and timer
    motor1 = motor.MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4,
                               pyb.Pin.board.PB5, pyb.Timer(3, freq=20000))
    
#     # Read desired set point position from serial port
#     # Converts degrees to ticks
#     pController1.set_set_point(float(input())*(PPR/360))
#     
#     # Read desired proportional gain constant from serial port
#     # Converts dutyCycle/degree to dutyCycle/ticks
#     pController1.set_gain(float(input())*(360/PPR))
#     
#     # Read time length of step response from serial port
#     _stepResponseTime = float(input())
    
    pController1.set_set_point(360*(PPR/360))
    pController1.set_gain(0.75*(360/PPR))
    _stepResponseTime = 5
    
    # Run a second step response when serial port reads 's'
    if input() == b's':
        
        try:
            
            while _stepResponseTime > 0:
                encoder_share.write(encoder1.read()) # read encoder position
                motor1.set_duty_cycle(pController1.run()) # set motor duty
                time.sleep_ms(10)
                _stepResponseTime -= 0.010
                
            pController1.print_data() # Print step response data to serial port
            print('Done!')
            
        except KeyboardInterrupt:
            
            print('Ending Step Response...')
