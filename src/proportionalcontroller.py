'''!@file proportionalcontroller.py
    A class that performs a closed loop proportional control.
    
    @author     Tori Bornino
    @author     Jackson McLaughlin
    @author     Zach Stednitz
    @date       February 3, 2022
'''

import utime

class ProportionalController:
    '''! 
    
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
        Continuously runs the control algorithm.
        
        '''
        error = self._sensor_share.read() - self.set_point
        actuation_value = -self.gain*error
        data_store()
        return actuation_value
    
    def set_set_point(self, set_point):
        '''! 
        Sets the desired setpoint for the step response.
    
        '''
        self._set_point = set_point
        
    def set_gain(self, gain):
        '''! 
        Sets the proportional gain controller value. 
        
        '''
        self._gain = gain
        
    def data_store(self):
        '''!
        Stores the data in a csv format
        '''
        self._data_list.append((utime.ticks_ms(),self.sensor_share.read()))
        
    def print_data(self):
        for data_point in data_list:
            print(f"{data_point[0]},{data_point[1]}")