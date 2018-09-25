from time import sleep

def linearize_temp(voltage):
    if voltage <= 0.0:
        c0 = 0.0e0
        c1 = 2.5173462e1
        c2 = -1.1662878e0
        c3 = -1.0833638e0
        c4 = -8.9773540e-1
        c5 = -3.7342377e-1
        c6 = -8.6632643e-2
        c7 = -1.0450598e-2
        c8 = -5.1920577e-4
        c9 = 0.0e0
    elif voltage > 0.0 and voltage <= 20.644:
        c0 = 0.0e0
        c1 = 2.508355e1
        c2 = 7.860106e-2
        c3 = -2.503131e-1
        c4 = 8.315270e-2
        c5 = -1.228034e-2
        c6 = 9.804036e-4
        c7 = -4.413030e-5
        c8 = 1.057734e-6
        c9 = -1.052755e-8
    elif voltage > 20.644 and voltage <= 54.886:
        c0 = -1.318058e2
        c1 = 4.830222e1
        c2 = -1.646031e0
        c3 = 5.464731e-2
        c4 = -9.650715e-4
        c5 = 8.802193e-6
        c6 = -3.110810e-8
        c7 = 0.0e0
        c8 = 0.0e0
        c9 = 0.0e0

    temp_c = c0 + c1*voltage**1 + c2*voltage**2 + c3*voltage**3 + c4*voltage**4 + c5*voltage**5 + c6*voltage**6 + c7*voltage**7 + c8*voltage**8 + c9*voltage**9
    voltage = round(voltage, 2)
    temp_c = round(temp_c)
    print('temp: ' + str(temp_c) + '    voltage:' + str(voltage))

v = -5.89
for i in range(3038):
    linearize_temp(float(v))
    v = v + 0.02
