# ME405 Lab 2: Control Freaks

## Closed Loop Controller Layout
We are using a simple closed loop feedback system that connects a single proportional controller to a motor driver that turns our motor. 
Using the encoder position readings, we are able to send an error signal back to the motor driver. When a step input is supplied and the output
position does not match the desired setpoint, the error signal value is reported as *actual encoder position - desired encoder position*.
