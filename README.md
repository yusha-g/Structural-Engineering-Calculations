# Scientific Python Developer Test
[git repo link](https://github.com/yusha-g/Structural-Engineering-Calculations)
<hr>

# TOC
## [1. Files](#files)

## [2.Errors](#dicrepancies-in-smath-files)
&ensp;&ensp; **[2.1.Test Outputs](#test-outputs)** <br/>
&ensp;&ensp; **[2.2.Omision of Exponent](#omission-of-exponent-in-utilityratioforflexture)** <br/>
&ensp;&ensp; **[2.3.Input Categorization in Moment Capacity Calculator](#input-categorization-in-moment-capacity-calculator)** <br/>

## [3. Testing](#testing)

## Files
The assignment utilizes 3 files. 

### _GLOBAL_VAR.py_

- Some variables are required across modules. 
- These common variables are stored in GLOBAL_VAR.py
- All values must be initialised `(GLOBAL_VAR.set_variables())` before proceeding with beam verification.
- _**`NOTE`: value of M is given in kN m, the input must be given in N m (x 1000)**_

### _beam_verifier.py_
`INPUT: None` <br/>
`OUTPUT: utilityRationForFlexture`
- Since all required values are initialised in GLOBAL_VAR, no parameters need to be passed.
- It calculates the following values for moment capacity calculator:
    - a_fromTop, a_fromBott
    - a_max_fromTop, a_max_fromBott,
    - dFromTop, dFromBott
    - alpha1

### _moment_capacity.py_
`INPUT:`
- The following values are imported from beam_verifier:
    - a_fromTop, a_fromBott
    - a_max_fromTop, a_max_fromBott,
    - dFromTop, dFromBott
    - alpha1
- The following values are inputted globally:
    - fy, f'c
    - As_bott_prov, As_top_prov
    - bw
    - covTop, covBott

`OUTPUT: M_cap`
- After calculations, it return the **M_cap** value to beam_verifier.py


## Dicrepancies in SMath Files
### Test Outputs
- In developer_test.sm we are given the following values:
    - fy = 500
    - f_c = 40
    - As_top_prov = 1000

- However, in moment_capacity.sm, we are given a different set of test values:
    - fy = 675
    - f_c = 45
    - As_top_prov = 525

- Upon calculation, the following values are attained:
<table>
<tr>

<th></th>
<th>developer_test</th>
<th>moment_capacity</th>

</tr>

<tr>
<td>
a_max_fromBott / a_max_fromTop
</td>

<td>
138.6
</td>

<td>
113.3647
</td>

</tr>

<tr>
<td>
a_fromTop
</td>

<td>
134.0196
</td>

<td>
160.8235
</td>

</tr>

<tr>
<td>
a_fromBott
</td>

<td>
49.0196
</td>

<td>
30.8824
</td>

</tr>

<tr>
<td>
beta1
</td>

<td>
0.77
</td>

<td>
0.73
</td>

</tr>

<tr style="font-weight: bold;">
<td>
M_design
</td>

<td>
1 x 10^5
</td>

<td>
1 x 10^5
</td>

</tr>

<tr style="font-weight: bold;">
<td>
M_cap
</td>

<td>
1.5032 x 10^8
</td>

<td>
1.1813 x 10^8
</td>

</tr>

<tr style="font-weight: bold;">
<td>
utilityRatioForFlexture
</td>

<td>
0.6652 x 10^-3
</td>

<td>
0.8465 x 10^-3
</td>

</tr>

</table>

So, the given test output for utilityRatioForFlexture is valid for the set of inputs in moment_capacity.sm

### Omission of Exponent in utilityRatioForFlexture
- As mentioned above, the value of test output value is coming to 0.8465 x 10^-3
- However, only 0.8465 is mentioned in the document. 

### Input Categorization in Moment Capacity Calculator
- in moment_capacity.sm variables are categorized into 2:
    - Local inputs
    - Imported Inputs (from developer test)
- Among this, dFromTop and dFromBott are categorized as local inputs even though they are calculated in developer_test.
- It would be more fitting if dFromTop and dFromBott were classified as Imported Inputs.
- The code is written assuming the same. moment_capacity imports the variables from developer_test

## Testing
- `pytest test_developer.py`
- Two tests are provided with the above mentioned set of values <br/>
![Testing-Image](/SMath%20Files/test.png)