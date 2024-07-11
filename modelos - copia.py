import numpy

def modelo_utpSuper(d_fuga, d_tube, p_tube, p_atmos, subte, direccion, forma):
    """
        Diametro tuberia: milimetros
        Presion tuberia: bar
        Presion atmosferica: bar
    """
    flujo = 0

    if subte == "subterranea":
        flujo = 0.55 *0.168* (1 + numpy.power((d_fuga/d_tube),4)) * numpy.power(d_fuga,2) * (p_tube + p_atmos)
    else:
        flujo = 0.55 * (1 + 0.34*numpy.power((d_fuga/d_tube),4)) * numpy.power(d_fuga,2) * (p_tube + p_atmos)
    if forma=="Total" and direccion == "bi":
        flujo = flujo*2

    return flujo

def modelo():
    #TODO
    return 0

def modelo2():
    #TODO
    return 0

def diametro_hidraulico(a,p,d_tube):
    formula= ((a*4)/numpy.pi)
    d_apa = numpy.sqrt(formula)
    
    if d_apa<=d_tube:
        diametro=d_apa
    else:
        diametro=d_tube
    #4*a/p
    return diametro

def rho_interior(p, R_gas, temp):
    R_gas = 518.2   #valor temporal
    rho_int = p/R_gas*temp
    return rho_int

def calc_area(forma, diametro, alto, largo, longitud):
    area = 0
    if forma == "circ":
        area = numpy.pi * numpy.square(diametro/2)
    elif forma == "rect":
        area = alto * largo
    elif forma == "tria":
        area = alto * largo / 2
    elif forma == "recta":
        #Valor preestablecido de alto en mm
        a = 1.5
        area = longitud * a
    else:
        area = numpy.pi * alto * largo

    return area

def calc_peri(forma, diametro, alto, largo, longitud):
    peri = 0
    if forma == "circ":
        peri = numpy.pi * diametro
    elif forma == "rect":
        peri = 2 * (alto + largo)
    elif forma == "tria":
        peri = 3 * largo
    elif forma == "recta":
        #Valor preestablecido de alto en mm
        a = 1.5
        peri = 2 * (longitud + a)
    else:
        peri = 2 * numpy.pi * numpy.sqrt((numpy.square(alto) + numpy.square(largo)) / 2)

    return peri

def vol_muerto(diametro, longitud):
    vol = numpy.pi * numpy.square(diametro/2000) * longitud
    return vol

#Valores estandarizados de tuberias RDE 21 PVC
def diametro_interno(diametro):
    d_int = 0
    #Valores retornados son en mm
    if diametro == 0.5:
        d_int = 16.72
    elif diametro == 0.75:
        d_int = 21.88
    elif diametro == 1:
        d_int = 27.36
    elif diametro == 1.25:
        d_int = 34.42
    elif diametro == 1.5:
        d_int = 39.36
    elif diametro == 2:
        d_int = 49.32
    elif diametro == 2.25:
        d_int = 59.14
    elif diametro == 3:
        d_int = 73.74
    elif diametro == 4:
        d_int = 93.52
    elif diametro == 6:
        d_int = 137.72
    elif diametro == 8:
        d_int = 179.22
    elif diametro == 21:
        d_int = 18.18
    elif diametro == 26:
        d_int = 23.63
    elif diametro == 33:
        d_int = 30.2
    elif diametro == 42:
        d_int = 38.14
    elif diametro == 48:
        d_int = 43.68
    elif diametro == 60:
        d_int = 54.58
    elif diametro == 73:
        d_int = 66.07
    elif diametro == 88:
        d_int = 80.42
    elif diametro == 114:
        d_int = 103.42
    elif diametro == 168:
        d_int = 152.22
    elif diametro == 200:
        d_int = 181.22
# acero in
    elif diametro == 0.501:
        d_int = 15.79
    elif diametro == 0.751:
        d_int = 19.91
    elif diametro == 1.001:
        d_int = 26.64
    elif diametro == 1.251:
        d_int = 35.05
    elif diametro == 1.501:
        d_int = 40.89
    elif diametro == 2.001:
        d_int = 52.5
    elif diametro == 2.501:
        d_int = 62.07
    elif diametro == 3.001:
        d_int = 77.92
    elif diametro ==  4.001:
        d_int = 102.26
    elif diametro == 6.001:
        d_int = 154.05
    elif diametro == 8.001:
        d_int = 202.71
    elif diametro == 10.001:
        d_int = 254.5
    elif diametro == 12.001:
        d_int = 303.22
    elif diametro == 14.001:
        d_int = 330.2
    elif diametro == 16.001:
        d_int = 381.0
    elif diametro == 18.001:
        d_int = 431.8
    elif diametro == 20.001:
        d_int = 482.6

#acero milimetros
    elif diametro == 20:
        d_int = 13.6
    elif diametro == 25:
        d_int = 18.6
    elif diametro == 30:
        d_int = 22
    elif diametro == 38:
        d_int = 28
    elif diametro == 44.5:
        d_int = 34.5
    elif diametro == 51:
        d_int = 41
    elif diametro == 54:
        d_int = 44
    elif diametro == 57:
        d_int = 46.2
    elif diametro == 63.5:
        d_int = 52.7
    elif diametro == 70:
        d_int = 57.4
    elif diametro == 82.5:
        d_int = 71.3
    elif diametro == 108:
        d_int = 95.4
    elif diametro == 127:
        d_int = 112.8
    elif diametro == 133:
        d_int = 118.8
    elif diametro == 152:
        d_int = 136.4
    elif diametro == 159:
        d_int = 143
    elif diametro == 177.8:
        d_int = 161.8
    elif diametro == 244.5:
        d_int = 226.9
    elif diametro == 298.5:
      d_int = 278.5
    return d_int

def diametro_interno1(diametro):
    Material="Polietileno"
    #Valores retornados son en mm
    if diametro == 0.5:
        Material="Polietileno"
    elif diametro == 0.75:
        Material="Polietileno"
    elif diametro == 1:
        Material="Polietileno"
    elif diametro == 1.25:
        Material="Polietileno"
    elif diametro == 1.5:
        Material="Polietileno"
    elif diametro == 2:
        Material="Polietileno"
    elif diametro == 2.25:
        Material="Polietileno"
    elif diametro == 3:
        Material="Polietileno"
    elif diametro == 4:
        Material="Polietileno"
    elif diametro == 6:
        Material="Polietileno"
    elif diametro == 8:
        Material="Polietileno"
    elif diametro == 21:
        Material="Polietileno"
    elif diametro == 26:
        Material="Polietileno"
    elif diametro == 33:
        Material="Polietileno"
    elif diametro == 42:
        Material="Polietileno"
    elif diametro == 48:
        Material="Polietileno"
    elif diametro == 60:
        Material="Polietileno"
    elif diametro == 73:
        Material="Polietileno"
    elif diametro == 88:
        Material="Polietileno"
    elif diametro == 114:
        Material="Polietileno"
    elif diametro == 168:
        Material="Polietileno"
    elif diametro == 200:
        Material="Polietileno"
# acero in
    elif diametro == 0.501:
        Material="Acero"
    elif diametro == 0.751:
        Material="Acero"
    elif diametro == 1.001:
        Material="Acero"
    elif diametro == 1.251:
        Material="Acero"
    elif diametro == 1.501:
        Material="Acero"
    elif diametro == 2.001:
        Material="Acero"
    elif diametro == 2.501:
        Material="Acero"
    elif diametro == 3.001:
        Material="Acero"
    elif diametro ==  4.001:
        Material="Acero"
    elif diametro == 6.001:
        Material="Acero"
    elif diametro == 8.001:
        Material="Acero"
    elif diametro == 10.001:
        Material="Acero"
    elif diametro == 12.001:
        Material="Acero"
    elif diametro == 14.001:
        Material="Acero"
    elif diametro == 16.001:
        Material="Acero"
    elif diametro == 18.001:
        Material="Acero"
    elif diametro == 20.001:
        Material="Acero"

#acero milimetros
    elif diametro == 20:
        d_int = 13.6
        Material="Acero"
        Unidades="mm"
    elif diametro == 25:
        d_int = 18.6
        Material="Acero"
        Unidades="mm"
    elif diametro == 30:
        d_int = 22
        Material="Acero"
        Unidades="mm"
    elif diametro == 38:
        d_int = 28
        Material="Acero"
        Unidades="mm"
    elif diametro == 44.5:
        d_int = 34.5
        Material="Acero"
        Unidades="mm"
    elif diametro == 51:
        d_int = 41
        Material="Acero"
        Unidades="mm"
    elif diametro == 54:
        d_int = 44
        Material="Acero"
        Unidades="mm"
    elif diametro == 57:
        d_int = 46.2
        Material="Acero"
        Unidades="mm"
    elif diametro == 63.5:
        d_int = 52.7
        Material="Acero"
        Unidades="mm"
    elif diametro == 70:
        d_int = 57.4
        Material="Acero"
        Unidades="mm"
    elif diametro == 82.5:
        d_int = 71.3
        Material="Acero"
        Unidades="mm"
    elif diametro == 108:
        d_int = 95.4
        Material="Acero"
        Unidades="mm"
    elif diametro == 127:
        d_int = 112.8
        Material="Acero"
        Unidades="mm"
    elif diametro == 133:
        d_int = 118.8
        Material="Acero"
        Unidades="mm"
    elif diametro == 152:
        d_int = 136.4
        Material="Acero"
        Unidades="mm"
    elif diametro == 159:
        d_int = 143
        Material="Acero"
        Unidades="mm"
    elif diametro == 177.8:
        d_int = 161.8
        Material="Acero"
        Unidades="mm"
    elif diametro == 244.5:
        d_int = 226.9
        Material="Acero"
        Unidades="mm"
    elif diametro == 298.5:
      d_int = 278.5
      Material="Acero"
      Unidades="mm"
    return Material

def diametro_interno2(diametro):
    d_int = 0
    Material="Polietileno"
    Unidades="in"
    #Valores retornados son en mm
    if diametro == 0.5:
        Material="Polietileno"
        Unidades="in"
    elif diametro == 0.75:
        Material="Polietileno"
        Unidades="in"
    elif diametro == 1:
        d_int = 27.36
        Material="Polietileno"
        Unidades="in"
    elif diametro == 1.25:
        d_int = 34.42
        Material="Polietileno"
        Unidades="in"
    elif diametro == 1.5:
        d_int = 39.36
        Material="Polietileno"
        Unidades="in"
    elif diametro == 2:
        d_int = 49.32
        Material="Polietileno"
        Unidades="in"
    elif diametro == 2.25:
        d_int = 59.14
        Material="Polietileno"
        Unidades="in"
    elif diametro == 3:
        d_int = 73.74
        Material="Polietileno"
        Unidades="in"
    elif diametro == 4:
        d_int = 93.52
        Material="Polietileno"
        Unidades="in"
    elif diametro == 6:
        d_int = 137.72
        Material="Polietileno"
        Unidades="in"
    elif diametro == 8:
        d_int = 179.22
        Material="Polietileno"
        Unidades="in"
    elif diametro == 21:
        d_int = 18.18
        Material="Polietileno"
        Unidades="mm"
    elif diametro == 26:
        d_int = 23.63
        Material="Polietileno"
        Unidades="mm"
    elif diametro == 33:
        d_int = 30.2
        Material="Polietileno"
        Unidades="mm"
    elif diametro == 42:
        d_int = 38.14
        Material="Polietileno"
        Unidades="mm"
    elif diametro == 48:
        d_int = 43.68
        Material="Polietileno"
        Unidades="mm"
    elif diametro == 60:
        d_int = 54.58
        Material="Polietileno"
        Unidades="mm"
    elif diametro == 73:
        d_int = 66.07
        Material="Polietileno"
        Unidades="mm"
    elif diametro == 88:
        d_int = 80.42
        Material="Polietileno"
        Unidades="mm"
    elif diametro == 114:
        d_int = 103.42
        Material="Polietileno"
        Unidades="mm"
    elif diametro == 168:
        d_int = 152.22
        Material="Polietileno"
        Unidades="mm"
    elif diametro == 200:
        d_int = 181.22
        Material="Polietileno"
        Unidades="mm"
# acero in
    elif diametro == 0.501:
        d_int = 15.79
        Material="Acero"
        Unidades="in"
    elif diametro == 0.751:
        d_int = 19.91
        Material="Acero"
        Unidades="in"
    elif diametro == 1.001:
        d_int = 26.64
        Material="Acero"
        Unidades="in"
    elif diametro == 1.251:
        d_int = 35.05
        Material="Acero"
        Unidades="in"
    elif diametro == 1.501:
        d_int = 40.89
        Material="Acero"
        Unidades="in"
    elif diametro == 2.001:
        d_int = 52.5
        Material="Acero"
        Unidades="in"
    elif diametro == 2.501:
        d_int = 62.07
        Material="Acero"
        Unidades="in"
    elif diametro == 3.001:
        d_int = 77.92
        Material="Acero"
        Unidades="in"
    elif diametro ==  4.001:
        d_int = 102.26
        Material="Acero"
        Unidades="in"
    elif diametro == 6.001:
        d_int = 154.05
        Material="Acero"
        Unidades="in"
    elif diametro == 8.001:
        d_int = 202.71
        Material="Acero"
        Unidades="in"
    elif diametro == 10.001:
        d_int = 254.5
        Material="Acero"
        Unidades="in"
    elif diametro == 12.001:
        d_int = 303.22
        Material="Acero"
        Unidades="in"
    elif diametro == 14.001:
        Unidades="in"
    elif diametro == 16.001:
        Unidades="in"
    elif diametro == 18.001:
        Unidades="in"
    elif diametro == 20.001:
        Unidades="in"

#acero milimetros
    elif diametro == 20:
        Unidades="mm"
    elif diametro == 25:
        Unidades="mm"
    elif diametro == 30:
        Unidades="mm"
    elif diametro == 38:
        Unidades="mm"
    elif diametro == 44.5:
        Unidades="mm"
    elif diametro == 51:
        Unidades="mm"
    elif diametro == 54:
        Unidades="mm"
    elif diametro == 57:
        Unidades="mm"
    elif diametro == 63.5:
        Unidades="mm"
    elif diametro == 70:
        Unidades="mm"
    elif diametro == 82.5:
        Unidades="mm"
    elif diametro == 108:
        Unidades="mm"
    elif diametro == 127:
        Unidades="mm"
    elif diametro == 133:
        Unidades="mm"
    elif diametro == 152:
        Unidades="mm"
    elif diametro == 159:
        Unidades="mm"
    elif diametro == 177.8:
        Unidades="mm"
    elif diametro == 244.5:
        Unidades="mm"
    elif diametro == 298.5:
      Unidades="mm"
    return Unidades

def diametro_equi(diametro, escape):
    equi = 0
    if escape == "min":
        if diametro == 0.75:
            equi = 0.225
        elif diametro == 1 or diametro == 26:
            equi = 0.3
        elif diametro == 1.25 or diametro == 33:
            equi = 0.375
        elif diametro == 1.5 or diametro == 42:
            equi = 0.45
        elif diametro == 2 or diametro == 48:
            equi = 0.6
        elif diametro == 2.25 or diametro == 60:
            equi = 0.675
        elif diametro == 3 or diametro == 73:
            equi = 0.9
        elif diametro == 88: #3.5
            equi = 1.05
        elif diametro == 4:
            equi = 1.2
        elif diametro == 114: #4.5
            equi = 1.35
        elif diametro == 6:
            equi = 1.8
        elif diametro == 168: #6.5
            equi = 1.95
    elif escape == "parcial":
        if diametro == 0.75:
            equi = 0.525
        elif diametro == 1 or diametro == 26:
            equi = 0.7
        elif diametro == 1.25 or diametro == 33:
            equi = 0.875
        elif diametro == 1.5 or diametro == 42:
            equi = 1.05
        elif diametro == 2 or diametro == 48:
            equi = 1.4
        elif diametro == 2.25 or diametro == 60:
            equi = 1.575
        elif diametro == 3 or diametro == 73:
            equi = 2.1
        elif diametro == 88: #3.5
            equi = 2.45
        elif diametro == 4:
            equi = 2.8
        elif diametro == 114: #4.5
            equi = 3.15
        elif diametro == 6:
            equi = 4.2
        elif diametro == 168: #6.5
            equi = 4.55
    else:
        if diametro < 26:
            equi = diametro
        else:
            if diametro == 26:
                equi = 1
            elif diametro == 33:
                equi = 1.25
            elif diametro == 42:
                equi = 1.5
            elif diametro == 48:
                equi = 2
            elif  diametro == 60:
                equi = 2.25
            elif diametro == 73:
                equi = 3
            elif diametro == 88: #3.5
                equi = 3.5
            elif diametro == 114: #4.5
                equi = 4.5
            elif diametro == 168: #6.5
                equi = 6.5

    return equi

def presion_atmos(altura):
    valor = 0
    #Presion nivel del mar 14.7 psi
    P_0 = 14.7
    #Temperatura nivel del mar 15 K
    T_0 = 288.15
    #Taza de lapso de temperatura (idk) K/m
    L = 0.00976
    #Cosntante presion calor J/(kg*K)
    C = 1004.68506
    #Gravedad m/s^2
    G = 9.80665
    #Masa molar aire kg/mol
    M = 0.02896968
    #Constante de gas universal J/(mol*K)
    R_0 = 8.314462618

    #valor = P_0 * numpy.float_power(1 - ((G * altura) / (C * T_0)), C * M / R_0)*0.0689476

    valor= P_0 * numpy.float_power(numpy.e,-G*altura/(R_0/M*T_0))*0.0689476

    return valor
