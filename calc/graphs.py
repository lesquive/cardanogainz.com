# importing the required module



def ada_total(amount_of_cardano, ada_price):
    
    amount_year = []
    
    for i in range(10):
        
        total_ada = (amount_of_cardano * 0.046083) + amount_of_cardano
        
        if amount_year:
            amount_year.append(round(amount_year[-1] + (amount_year[-1] * 0.046083), 2))
            
        else:
            amount_year.append(round(total_ada,2))
            
    return amount_year

def monthly_yearly(amount_of_cardano, ada_price):
    
    yearly_ada = ada_total(amount_of_cardano, ada_price)
    
    monthly_yearly = []
    
    for i in yearly_ada:

        ada_yearly_rewards = i * 0.046083
        usd_yearly_rewards = ada_price * ada_yearly_rewards
        usd_monthly_income = usd_yearly_rewards / 12
        
        monthly_yearly.append(round(usd_monthly_income,2))

    
    return monthly_yearly