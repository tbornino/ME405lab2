from matplotlib import pyplot
import serial
import time

while True:
    set_point_str = input("enter desired setpoint (degrees): ")
    p_gain_str = input("enter desired proportional gain (%/degree): ")
    i_gain_str = input("enter desired integral gain (%/degree-s): ")
    d_gain_str = input("enter desired derivative gain (%/(degree/s)): ")
    t_step_str = input("enter time to run step response (seconds): ")
    try:
        float(p_gain_str)
        float(i_gain_str)
        float(d_gain_str)
        float(set_point_str)
        float(t_step_str)
    except ValueError:
        print("Invalid value given, try again")
    else:
        break
t_step = float(t_step_str)

port = "COM3"
with serial.Serial(port, 115200, timeout=1) as ser_port:
#     ser_port.write(b'\x03\x04')
#     time.sleep(2)
    ser_port.write(set_point_str.encode() + b'\r\n')
    ser_port.write(p_gain_str.encode() + b'\r\n')
    ser_port.write(i_gain_str.encode() + b'\r\n')
    ser_port.write(d_gain_str.encode() + b'\r\n')
    ser_port.write(t_step_str.encode() + b'\r\n')
    time.sleep(t_step + 1)
    xs = []
    ys = []
    for i in range(int(t_step * 100)):
        line = ser_port.readline()
        print(line)
        cells = line.split(b',')
        try:
            x = float(cells[0].strip())
            y = float(cells[1].strip())
        except (ValueError, IndexError):
            continue
        xs.append(x)
        ys.append(y)
print(xs)
print(ys)
pyplot.plot(xs, ys)
pyplot.xlabel("time [ms]")
pyplot.ylabel("position [ticks]")
pyplot.show()