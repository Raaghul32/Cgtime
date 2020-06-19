# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 19:48:42 2020

@author: raagh
"""
import streamlit as st
def calculator(s1,c1,s2,c2,s3,c3,s4,c4,s5,c5,s6,c6):
    if s1*2 in range(51,56):
        a= 5
    elif s1*2 in range(56,66):
        a=6
    elif s1*2 in range(66,76):
        a=7
    elif s1*2 in range(76,86):
        a=8
    elif s1*2 in range(86,91):
        a=9
    else:
        a=10
#Now For Subject two       
        
        
    if s2*2 in range(51,56):
        b= 5
    elif s2*2 in range(56,66):
        b=6
    elif s2*2 in range(66,76):
        b=7
    elif s2*2 in range(76,86):
        b=8
    elif s2*2 in range(86,91):
        b=9
    else:
        b=10
        
        
        
        
    if s3*2 in range(51,56):
        c= 5
    elif s3*2 in range(56,66):
        c=6
    elif s3*2 in range(66,76):
        c=7
    elif s3*2 in range(76,86):
        c=8
    elif s3*2 in range(86,91):
        c=9
    else:
        c=10
        
        
        
    if s4*2 in range(51,56):
        d= 5
    elif s4*2 in range(56,66):
        d=6
    elif s4*2 in range(66,76):
        d=7
    elif s4*2 in range(76,86):
        c=8
    elif s4*2 in range(86,91):
        d=9
    else:
        d=10
        
        
        
        
    if s5*2 in range(51,56):
        e= 5
    elif s5*2 in range(56,66):
        e=6
    elif s5*2 in range(66,76):
        e=7
    elif s5*2 in range(76,86):
        e=8
    elif s5*2 in range(86,91):
        e=9
    else:
        e=10
    
    
    
    
    if s6*2 in range(51,56):
        f= 5
    elif s6*2 in range(56,66):
        f=6
    elif s6*2 in range(66,76):
        f=7
    elif s6*2 in range(76,86):
        f=8
    elif s6*2 in range(86,91):
        f=9
    else:
        f=10
    
    
    tot = (a*c1)+(b*c2)+(c*c3)+(d*c4)+(e*c5)+(f*c6)
    bigt= 10*(c1+c2+c3+c4+c5+c6)
    gpa = (tot/bigt)*10
    return round(gpa,4)
        
def cg(a,b):
    final = ((a*(5))+b)/6
    return round(final,4)

    

st.title('Calculate your sixth semester grade points')
st.header('Only for Sastra University Students')
sub1 = st.number_input('Enter your internal marks out of 50 for subject one')
cre1 = st.slider('Credits for the subject one above',min_value=2,max_value=5,step=1)
sub2 = st.number_input('Enter your internal marks out of 50 for subject two')
cre2 = st.slider('Credits for the subject two above',min_value=2,max_value=5,step=1)
sub3 = st.number_input('Enter your internal marks out of 50 for subject three')
cre3 = st.slider('Credits for the subject three above above',min_value=2,max_value=5,step=1)
sub4 = st.number_input('Enter your internal mark out of 50 for subject four')
cre4 = st.slider('Credits for the subject four above',min_value=2,max_value=5,step=1)
sub5 = st.number_input('Enter your internal mark out of 50 for subject five')
cre5 = st.slider('Credits for the subject five above',min_value=2,max_value=5,step=1)
sub6 = st.number_input('Enter your internal mark out of 50 for subject six')
cre6 = st.slider('Credits for the subject six above',min_value=2,max_value=5,step=1)
cgpa = st.number_input('Current Cgpa with four decimal points')

if st.button('Calculate'):
    sgpa = calculator(sub1,cre1,sub2,cre2,sub3,cre3,sub4,cre4,sub5,cre5,sub6,cre6)
    cgpa = cg(cgpa,sgpa)
    st.balloons()
    st.write('Your SGPA',(sgpa))
    st.write('Your CGPA',(cgpa))