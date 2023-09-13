'''
======= GLOBAL INPUT - MATERIALPROPERTIES =========
fy -> Design Compressive strength of concrete
f_c ->  Design Yeild strength of steel
Ep_cmax -> Maximum concrete strain
Es -> Modulus of elasticity of steel

========= GLOBAL INPUT - STRENGTH REDUCTION FACTORS =========
phi -> Strength reduction factor for Flexure

======= LOCAL INPUT - SECTION GEOMETRY =========
bw -> Width of the beam
h -> Overall Depth of the section

======= LOCAL INPUT - REBAR AND COVERS =========
covBott -> Effective cover (to centre of bottom longitudinal reinforcement)
covTop -> Effective cover(to centre of top longitudinal reinforcement)
As_bott_prov -> Bottom main reinforcement
As_top_prov -> Top main reinforcement

======= LOCAL INPUT - ANALYSIS RESULTS =========
M -> Moment imported from analysis results (N m)

'''

def set_variables(
    g_fy, g_f_c, g_Ep_cmax, g_Es,
    g_phi,
    g_bw, g_h,
    g_covBott, g_covTop, g_as_top_prov, g_as_bott_prov, 
    g_M
):
    
    global fy, f_c, Ep_cmax, Es
    global As_bott_prov, As_top_prov
    global phi, bw, h, M
    global covTop, covBott

    fy = g_fy
    f_c = g_f_c
    Ep_cmax = g_Ep_cmax
    Es = g_Es
    As_bott_prov = g_as_bott_prov
    As_top_prov = g_as_top_prov
    phi = g_phi
    bw = g_bw
    h = g_h
    M = g_M
    covTop = g_covTop
    covBott = g_covBott