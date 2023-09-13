from beam_verifier import beam_verification
import GLOBAL_VAR

'''
    fy, f_c, Ep_cmax, Es,
    phi,
    bw, h,
    covBott, covTop, As_top_prov, As_bott_prov,
    M
'''

def test_1():
    #setting all the global variables
    GLOBAL_VAR.set_variables(
        675, 45, 0.003, 200000,
        0.85,
        300, 500,
        60, 60, 525, 2734,
        -100000
        )
    

    result = beam_verification()

    print ("utilityRatioForFlexure = ",result,"x 10^-3")

    assert result == 0.8465

def test_2():
    #setting all the global variables
    GLOBAL_VAR.set_variables(
        500, 40, 0.003, 200000,
        0.85,
        300, 500,
        60, 60, 1000, 2734,
        -100000
        )
    

    result = beam_verification()

    print ("utilityRatioForFlexure = ",result,"x 10^-3")

    assert result == 0.6652

test_2()