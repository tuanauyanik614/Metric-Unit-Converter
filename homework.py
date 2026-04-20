def m_m():
    m_m = ("Metric conversion", "Unit Prefix conversion (centi, mili, kilo)", "EXIT")
    print(f"==========MAIN MENU==========")
    for m, u in enumerate(m_m):
        print(f"{m + 1}. {u}")


def m_c():
    m_c = ("inches->centimeters", "centimeters->inches", "miles->kilometers", "kilometers->miles", "ounces->grams",
           "grams->ounces", "Back to Main Menu")
    print(f"==========METRIC CONVERSIONS==========")
    for e, a in enumerate(m_c):
        print(f"{e + 1}. {a}")


def inc_cm(a):
    a = a * 2.54
    return a


def cm_inc(b):
    b = b / 2.54
    return b


def mil_km(a):
    a = a * 1.61
    return a


def km_mil(b):
    b = b / 1.61
    return b


def ounc_gr(a):
    a = a * 28.35
    return a


def gr_ounc(b):
    b = b / 28.35
    return b


def u_m():
    u_m = ["Convert to centi (x10⁻²)", "Convert to mili (x10⁻³)", "Convert to kilo (x10³)", "Back to Main Menu"]
    print(f"==========UNIT PREFIX CONVERSION==========")
    for k, a in enumerate(u_m):
        print(f"{k + 1}. {a}")


def to_centi(g):
    g = g * 10 ** -2
    return g


def to_mili(g):
    g = g * 10 ** -3
    return g


def to_kilo(g):
    g = g * 10 ** 35
    return g


while True:
    m_m()
    t = input(f"Choose an option:")
    if not t.isdigit():
        print("please enter a number")
        continue
    t = int(t)
    if t <= 3:
        m_c()
        if t == 1:
            while True:
                m_c()
                n = input(f"Select conversion(1-7):")
                if not  n.isdigit ():
                    print("please enter a number")
                    continue
                n = int(n)
                m = float(input("value?"))
                if n == 1:
                    rslt = inc_cm(m)
                    print(rslt)
                elif n == 2:
                    rslt_1 = cm_inc(m)
                    print(rslt_1)
                elif n == 3:
                    rslt_2 = mil_km(m)
                    print(rslt_2)
                elif n == 4:
                    rslt_3 = km_mil(m)
                    print(rslt_3)
                elif n == 5:
                    rslt_4 = ounc_gr(m)
                    print(rslt_4)
                elif n == 6:
                    rslt_5 = gr_ounc(m)
                    print(rslt_5)
                elif n == 7:
                    break
                else:
                    print("we only have 7 option")
                    continue
        if t == 2:
            while True:
                u_m()
                s = input(f"Select convertion (1-4):")
                if not  s.isdigit():
                    print("please enter a number")
                    continue
                s = int(s)
                r = float(input(f"Value?"))
                if s == 1:
                    o = to_centi(r)
                    print(o)
                elif s == 2:
                    o = to_mili(r)
                    print(o)
                elif s == 3:
                    o = to_kilo(r)
                    print(o)
                elif s == 4:
                    break
                else:
                    print("We only have 4 option")
                    continue
        if t == 3:
            print("Good bye")
            break
    else:
        print("we have only 3 option")
        continue
