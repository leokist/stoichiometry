from flask import render_template, request, redirect, url_for, session
from app import app
from stoichiometry import *
from decimal import *

@app.route('/')
def index():
    return render_template('index.html')

@app.post('/calc')
def calc():

    comb_c = int(request.form.get('comb_c', 0 , type=Decimal))
    comb_o = int(request.form.get('comb_o', 0 , type=Decimal))
    comb_h = int(request.form.get('comb_h', 0 , type=Decimal))
    comb_n = int(request.form.get('comb_n', 0 , type=Decimal))

    oxid_c = int(request.form.get('oxid_c', 0 , type=Decimal))
    oxid_o = int(request.form.get('oxid_o', 0 , type=Decimal))
    oxid_h = int(request.form.get('oxid_h', 0 , type=Decimal))
    oxid_n = float(request.form.get('oxid_n', 0 , type=Decimal))


    comb = Reactants(comb_c, comb_o, comb_h, comb_n)
    oxid = Reactants(oxid_c, oxid_o, oxid_h, oxid_n)

    reacao = Reaction(comb, oxid)

    if comb_c==0 and comb_o==0 and comb_h==0 and comb_n==0:
        fuel_error = "Invalid Fuel"
        c = fuel_error
    elif comb_c==0 and comb_h==0 and (comb_o!=0 or comb_n!=0):
        fuel_error = "Invalid Fuel"
        c = fuel_error
    else:
        fuel_error = "OK"

    if oxid_o==0:
        oxidizer_error = "Invalid Oxidizer"
        c = oxidizer_error
    else:
        oxidizer_error = "OK"


    if fuel_error=="OK" and oxidizer_error=="OK":   
        reacao.Stoichiometry()
        c = reacao.fullReaction
    elif fuel_error=="Invalid Fuel" and oxidizer_error=="Invalid Oxidizer":
        c = fuel_error + " and " + oxidizer_error
    
    return render_template('results.html', **locals())