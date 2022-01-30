'''!@file pidcontroller.py
    A class that performs closed loop pid control.
    
    @author     Tori Bornino
    @author     Jackson McLaughlin
    @author     Zach Stednitz
    @date       February 3, 2022
'''

import time

class PIDController:
    '''! 
    This class implements a generic proportional controller.
    '''
    def __init__ (self, set_point, Kp, Ki, Kd, sensor_share):
        '''! 
        Creates a proportional controller by initializing setpoints and gains
        
        @param setpoint      The initial desired location of the step response  
        @param Kp            The proportional gain for the controller.
                             Units of (dutyCycle/ticks)
        @param Ki            The integral gain for the controller.
                             Units of (dutyCycle/(ticks*seconds))
        @param Kd            The derivative gain for the controller.
                             Units of (dutyCycle/(ticks/seconds))
        @param sensor_share  A share the contains the read position from sensor        
        '''
        self._set_point = set_point
        self._Kp = Kp
        self._Ki = Ki
        self._Kd = Kd
        self._sensor_share = sensor_share
        
        ##  @brief      Stored Step Response Data.
        #   @details    Recorded as (time(ms), position(ticks))
        self.data_list = []
        
        ##  @brief      Step response start time
        self.start time = None
        self._last_error = 0
        self._Iduty = 0
        
    def run(self):
        '''! 
        Continuously runs the control algorithm. Reads the position data from a
        sensor and then finds the error between the actual position and the 
        desired setpoint value. Then we append the stored data list with a
        tuple of values.
        
        @return The actuation value to fix steady state error.
        '''
        # Calculate the current error in position
        error = self._sensor_share.read() - self._set_point
        
        # Calculate the PID actuation value
        Pduty = self._Kp*error
        self._Iduty += self._Ki*error*
                       (self.data_list[-1, 0] - self.data_list[-2, 0])
        Dduty = self._Kd*(error-self._last_error)/
                         (self.data_list[-1, 0] - self.data_list[-2, 0])
        
        actuation_value = Pduty + self_Iduty + Dduty
        
        # Store the time and position data
        self.data_store()
        
        # Filter saturated values
        if actuation_value > 100:
            actuation_value = 100
        elif actuation_value < -100:
            actuation_value = -100
        
        # Store error for next iteration
        self._last_error = error
        
        return actuation_value
    
    def set_set_point(self, set_point):
        '''! 
        Sets the desired setpoint for the step response.
        
        @param set_point  The desired steady state response value.  
        '''
        self._set_point = set_point
        
    def set_gains(self, Kp, Ki, Kd):
        '''! 
        Sets the proportional gain controller value.
        
        @param Kp           The proportional gain for the controller.
                            Units of (dutyCycle/ticks)
        @param Ki           The integral gain for the controller.
                            Units of (dutyCycle/(ticks*seconds))
        @param Kd           The derivative gain for the controller.
                            Units of (dutyCycle/(ticks/seconds))
        '''
        self._Kp = Kp
        self._Ki = Ki
        self._Kd = Kd
        
    def data_store(self):
        '''!
        Stores the data in a csv format.
        '''
        if self.start_time == None:
            self.start_time = time.ticks_ms()
            
        self.data_list.append((time.ticks_diff(time.ticks_ms(),self.start_time),
                                self._sensor_share.read()))
        
    def print_data(self):
        '''!
        Prints each line in the data list in a comma separated format.
        '''
        for data_point in self.data_list:
            print(f"{data_point[0]},{data_point[1]}")
        
        # Reset variables for next step response
        self.start_time = None
        self._last_error = 0
        self._Iduty = 0
            
