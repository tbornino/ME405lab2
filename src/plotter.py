from matplotlib import pyplot
import serial
import time

PPR = 256*4*16

# Collect input
while True:
    set_point_str = input("enter desired setpoint (degrees): ")
    p_gain_str = input("enter desired proportional gain (%/degree): ")
    i_gain_str = input("enter desired integral gain (%/degree-s): ")
    d_gain_str = input("enter desired derivative gain (%/(degree/s)): ")
    t_step_str = input("enter time to run step response (seconds): ")
    # Make sure all inputs are valid numbers
    try:
        float(p_gain_str)
        float(i_gain_str)
        float(d_gain_str)
        t_step = float(t_step_str)
        set_point = float(set_point_str)
    except ValueError:
        print("Invalid value given, try again")
    else:
        break

# Open serial port with the Nucleo
   port = "COM3"
with serial.Serial(port, 115200, timeout=1) as ser_port:
    # Send gains to Nucleo, with line ending
    ser_port.write(set_point_str.encode() + b'\r\n')
    ser_port.write(p_gain_str.encode() + b'\r\n')
    ser_port.write(i_gain_str.encode() + b'\r\n')
    ser_port.write(d_gain_str.encode() + b'\r\n')
    ser_port.write(t_step_str.encode() + b'\r\n')
    time.sleep(t_step + 1)
    # Receive data from the Nucleo and process it into 2 lists
    xs = []
    ys = []
    for i in range(int(t_step * 100)):
        line = ser_port.readline()
        if line == b'Done!\r\n':
            break
        cells = line.split(b',')
        try:
            x = float(cells[0].strip())
            y = float(cells[1].strip())
        except (ValueError, IndexError):
            continue
        xs.append(x)
        ys.append(y)
# Plot step response
pyplot.plot(xs, ys)
# Plot line for setpoint
t_max = xs[-1]
set_point_ticks = set_point * PPR / 360
pyplot.plot([0, t_max], [set_point_ticks, set_point_ticks], 'r--')
pyplot.xlabel("time [ms]")
pyplot.ylabel("position [ticks]")
pyplot.show()