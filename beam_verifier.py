from moment_capacity import moment_capacity_calculator
import GLOBAL_VAR

def calc_alpha():
    eq = 0.85 - 0.004 * (GLOBAL_VAR.f_c - 55) 
    if GLOBAL_VAR.f_c <= 55:
        return 0.85
    elif ( eq < 0.75 ):
        return 0.75
    else:
        return eq

def calc_beta():
    eq = 0.85 - 0.008 * (GLOBAL_VAR.f_c - 30)

    if GLOBAL_VAR.f_c <= 30:
        return 0.85
    elif eq < 0.85:
        return eq
    else:
        return 0.65

#============= For a_fromTOP and a_fromBott Calculations =============

def calc_c_actual(A, beta1, alpha1):
    numerator = (GLOBAL_VAR.fy * A)
    denominator = (GLOBAL_VAR.bw * beta1 * alpha1 * GLOBAL_VAR.f_c)
    return numerator / denominator

def calc_a(A, beta1, alpha1):
    c_actual = calc_c_actual(A, beta1, alpha1)
    return round(c_actual * beta1, 4)

#======================= For a_max_fromTop and a_max_fromBott ============

#dFromTop and dFromBott
def calc_d(cov):
    return GLOBAL_VAR.h - cov

def calc_cb(d):
    numerator = GLOBAL_VAR.Ep_cmax * d
    denomitor = GLOBAL_VAR.Ep_cmax + (GLOBAL_VAR.fy / GLOBAL_VAR.Es)

    return numerator / denomitor

def calc_a_max(beta1, d):
    cb = calc_cb(d)
    return round(0.75 * beta1 * cb, 4)

#================================= e-3

def convert_to_exp(num):
    for i in range(1,4):
        num *=10
    return round(num,4)

#============================= MAIN ==================================

def beam_verification():
    
    global a_max_fromTop, a_max_fromBott,a_fromTop, a_fromBott,dFromTop, dFromBott,alpha1

    #needed for c_actual_fromTop/fromBott

    alpha1 = calc_alpha()   
    beta1 = calc_beta()    

    #print(alpha1,"alph:a\nbeta:",beta1)


    #============= a_fromTop a_fromBott ===========

    a_fromTop = calc_a(GLOBAL_VAR.As_bott_prov, beta1, alpha1)

    a_fromBott = calc_a(GLOBAL_VAR.As_top_prov, beta1, alpha1)

    #print(a_fromTop, ": a TOP\n a BOTT: ",a_fromBott)


    #============== a_max_fromTop a_max_fromBott ==========

    dFromTop = calc_d(GLOBAL_VAR.covTop)

    dFromBott = calc_d(GLOBAL_VAR.covBott)

    #print(dFromTop, ": d TOP\n d BOTT: ",dFromBott)

    a_max_fromTop = calc_a_max(beta1, dFromTop)

    a_max_fromBott = calc_a_max(beta1, dFromBott)

    #print(a_max_fromTop, ": a_max TOP\n a_max BOTT: ",a_max_fromBott)


    #=============== MOMENT CAPACITY CALCULATOR ==============

    M_design = abs(GLOBAL_VAR.M)
    M_cap = moment_capacity_calculator()

    #print("M_design: ",M_design,"\nM_cap: ",M_cap)

    #SAFETY / UTILIZATION FACTOR
    utilityRatioForFlexure = convert_to_exp( M_design / M_cap )

    return utilityRatioForFlexure


