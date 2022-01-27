'''!@file proportionalcontroller.py
    A class that performs a closed loop proportional control.
    
    @author     Tori Bornino
    @author     Jackson McLaughlin
    @author     Zach Stednitz
    @date       February 3, 2022
'''

import time

class ProportionalController:
    '''! 
    This class implements a generic proportional controller.
    '''
    def __init__ (self, set_point, gain, sensor_share):
        '''! 
        Creates a proportional controller by initializing setpoints 
        @param setpoint       The initial desired location of the step response  
        @param gain           The proportional gain for the controller.
        @param sensor_share   A share the contains the read position from sensor
        @param data_list      A list that stores the data
        
        '''
        self._set_point = set_point
        self._gain = gain
        self._sensor_share = sensor_share
        self._data_list = []
        
    def run(self):
        '''! 
        Continuously runs the control algorithm. Reads the position data from a sensor
        and then finds the error between the actual position and the desired setpoint value.
        Then we append the stored data list with a tuple of values. 
        @return The actuation value to fix steady state error.
        '''
        error = self._sensor_share.read() - self._set_point
        actuation_value = -self._gain*error
        self.data_store()
        if actuation_value > 100:
            actuation_value = 100
        elif actuation_value < -100:
            actuation_value = -100
        return actuation_value
    
    def set_set_point(self, set_point):
        '''! 
        Sets the desired setpoint for the step response.
        
        @param set_point  The desired steady state response value.  
        '''
        self._set_point = set_point
        
    def set_gain(self, gain):
        '''! 
        Sets the proportional gain controller value. 
        @param gain The proportional gain value that the controller uses
        '''
        self._gain = gain
        
    def data_store(self):
        '''!
        Stores the data in a csv format.
        '''
        start_time = time.ticks_ms()
        self._data_list.append((time.ticks_diff(time.ticks_ms(),start_time),self._sensor_share.read()))
        
    def print_data(self):
        '''!
        Prints each line in the data list in a comma separated format.
        '''
        for data_point in self._data_list:
            print(f"{data_point[0]},{data_point[1]}")
            