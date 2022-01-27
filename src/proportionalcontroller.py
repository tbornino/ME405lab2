'''!@file proportionalcontroller.py
    A class that performs a closed loop proportional control.
    
    @author     Tori Bornino
    @author     Jackson McLaughlin
    @author     Zach Stednitz
    @date       February 3, 2022
'''

class ProportionalController:
    '''! 
    
    '''
    def __init__ (self,setpoint,kp,enc_share):
        '''! 
        Creates a proportional controller by initializing setpoints 
        @param setpoint The initial desired location of the step response  
        @param kp       The proportional gain for the controller.
        @param enc_share 
        
        '''
        self.setpoint = setpoint
        self.kp = kp
        self.enc_share = enc_share
        
    def run(self):
        '''! 
        Continuously runs the control algorithm.
        
        '''
        
    def set_set_point(self):
        '''! 
        Sets the desired setpoint for the step response.
    
        '''
    
    def set_gain(self):
        '''! 
        Sets the proportional gain controller value. 
    
        '''
        