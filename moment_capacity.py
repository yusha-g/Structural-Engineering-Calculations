import GLOBAL_VAR
import beam_verifier

def get_Beam_Design_Type(a, a_max):
    if a <= a_max:
        return "SRS"
    else:
        return "DRS"

def M_cap_sing(As, d, a):
    #print("M_cap_sing: ", As * GLOBAL_VAR.fy * ( d - (a/2) ))
    return As * GLOBAL_VAR.fy * ( d - (a/2) )

def M_cap_doub(a_max, d, cov, As):
    eq1 = beam_verifier.alpha1 * GLOBAL_VAR.f_c * GLOBAL_VAR.bw * a_max * ( d - ( a_max / 2 ) )

    eq2 = As - ( eq1 / ( GLOBAL_VAR.fy * (d - a_max/2) ) )

    eq3 = GLOBAL_VAR.fy * ( d - cov )

    #print("alpha: ", beam_verifier.alpha1,"\nAs: ",As,"\nfc: ",GLOBAL_VAR.f_c,"\nfy: ",GLOBAL_VAR.fy,"\nbw: ",GLOBAL_VAR.bw,"\na_max: ",a_max,"\nd: ",d, "\ncov:", cov)
    #print("\nEQ1: ",eq1,"\nEQ2: ", eq2,"\nEQ3: ",eq3)
    #print("\nM_cap_doubt: ", eq1 + ( eq2 * eq3 ))

    return eq1 + ( eq2 * eq3 )

#===================== SAGG

def calc_M_cap_Sagg():
    Beam_Design_Type = get_Beam_Design_Type(beam_verifier.a_fromTop, beam_verifier.a_max_fromTop)
    #print("BEAM_Sagg ", Beam_Design_Type)
    if Beam_Design_Type == "SRS":
        return M_cap_sing(GLOBAL_VAR.As_bott_prov, beam_verifier.dFromTop, beam_verifier.a_fromTop)
    else:
        return M_cap_doub(beam_verifier.a_max_fromTop, beam_verifier.dFromTop, GLOBAL_VAR.covTop, GLOBAL_VAR.As_bott_prov)


#===================== HOGG

def calc_M_cap_Hogg():
    Beam_Design_Type = get_Beam_Design_Type(beam_verifier.a_fromBott, beam_verifier.a_max_fromBott)
    #print("BEAM_Hogg ", Beam_Design_Type)
    if Beam_Design_Type == "DRS":
        return M_cap_sing(GLOBAL_VAR.As_top_prov, beam_verifier.dFromBott, beam_verifier.a_fromBott)
    else:
        return M_cap_doub(beam_verifier.a_max_fromBott, beam_verifier.dFromBott, GLOBAL_VAR.covBott, GLOBAL_VAR.As_top_prov)

def moment_capacity_calculator():
    #print("==== MOMENT CAPACITY ======")
    if GLOBAL_VAR.M < 0: 
        return calc_M_cap_Hogg() * GLOBAL_VAR.phi
    else:
        return calc_M_cap_Sagg() * GLOBAL_VAR.phi