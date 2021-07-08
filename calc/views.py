from django.shortcuts import render
from django.http import HttpResponse
from pycoingecko import CoinGeckoAPI
from django import forms
from .graphs import *


cg = CoinGeckoAPI()


def index(request):

    response = cg.get_price(
        ids='cardano', vs_currencies='usd', include_market_cap='true')

    ada_price = response['cardano']['usd']
    ada_market_cap = response['cardano']['usd_market_cap']

    class NameForm(forms.Form):
        my_cardano = forms.IntegerField(label='Amount Of Cardano (ADA):', initial=1000, widget=forms.TextInput(
            attrs={'autofocus': True}))
        my_ada_price = forms.FloatField(
            label='Cardano ADA Price:', initial=ada_price)

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():

            amount_of_cardano = float(form['my_cardano'].value())
            cardano_worth = amount_of_cardano * \
                float(form['my_ada_price'].value())
            ada_yearly_rewards = amount_of_cardano * 0.046083
            ada_monthly_income = ada_yearly_rewards / 12
            usd_yearly_rewards = float(
                form['my_ada_price'].value()) * ada_yearly_rewards
            usd_monthly_income = usd_yearly_rewards / 12

            my_ada_list = ada_total(amount_of_cardano, float(form['my_ada_price'].value()))
            my_monthly_list = monthly_yearly(amount_of_cardano, float(form['my_ada_price'].value()))

            return render(request, 'calc/calc.html', {
                'ada_price': "{:,.2f}".format(ada_price),
                'ada_market_cap': "{:,.2f}".format(ada_market_cap),
                'amount_of_cardano': "{:,.2f}".format(amount_of_cardano),
                'cardano_worth': "{:,.2f}".format(cardano_worth),
                'ada_yearly_rewards': "{:,.4f}".format(ada_yearly_rewards),
                'ada_monthly_income': "{:,.4f}".format(ada_monthly_income),
                'usd_yearly_rewards': "{:,.2f}".format(usd_yearly_rewards),
                'usd_monthly_income': "{:,.2f}".format(usd_monthly_income),
                'form': form,
                'my_ada_list': my_ada_list,
                'my_monthly_list': my_monthly_list,
            })

        else:

            form = NameForm()

            amount_of_cardano = 1000
            cardano_worth = amount_of_cardano * ada_price
            ada_yearly_rewards = amount_of_cardano * 0.046083
            ada_monthly_income = ada_yearly_rewards / 12
            usd_yearly_rewards = ada_price * ada_yearly_rewards
            usd_monthly_income = usd_yearly_rewards / 12

            my_ada_list = ada_total(amount_of_cardano, float(form['my_ada_price'].value()))
            my_monthly_list = monthly_yearly(amount_of_cardano, float(form['my_ada_price'].value()))

            return render(request, 'calc/calc.html', {
                'ada_price': "{:,.2f}".format(ada_price),
                'ada_market_cap': "{:,.2f}".format(ada_market_cap),
                'amount_of_cardano': "{:,.2f}".format(amount_of_cardano),
                'cardano_worth': "{:,.2f}".format(cardano_worth),
                'ada_yearly_rewards': "{:,.4f}".format(ada_yearly_rewards),
                'ada_monthly_income': "{:,.4f}".format(ada_monthly_income),
                'usd_yearly_rewards': "{:,.2f}".format(usd_yearly_rewards),
                'usd_monthly_income': "{:,.2f}".format(usd_monthly_income),
                'form': form,
                'my_ada_list': my_ada_list,
                'my_monthly_list': my_monthly_list,
            })

    else:

        form = NameForm()

        amount_of_cardano = 1000
        cardano_worth = amount_of_cardano * ada_price
        ada_yearly_rewards = amount_of_cardano * 0.046083
        ada_monthly_income = ada_yearly_rewards / 12
        usd_yearly_rewards = ada_price * ada_yearly_rewards
        usd_monthly_income = usd_yearly_rewards / 12

        my_ada_list = ada_total(amount_of_cardano, float(form['my_ada_price'].value()))
        my_monthly_list = monthly_yearly(amount_of_cardano, float(form['my_ada_price'].value()))

        return render(request, 'calc/calc.html', {
            'ada_price': "{:,.2f}".format(ada_price),
            'ada_market_cap': "{:,.2f}".format(ada_market_cap),
            'amount_of_cardano': "{:,.2f}".format(amount_of_cardano),
            'cardano_worth': "{:,.2f}".format(cardano_worth),
            'ada_yearly_rewards': "{:,.4f}".format(ada_yearly_rewards),
            'ada_monthly_income': "{:,.4f}".format(ada_monthly_income),
            'usd_yearly_rewards': "{:,.2f}".format(usd_yearly_rewards),
            'usd_monthly_income': "{:,.2f}".format(usd_monthly_income),
            'form': form,
            'my_ada_list': my_ada_list,
            'my_monthly_list': my_monthly_list,
        })
