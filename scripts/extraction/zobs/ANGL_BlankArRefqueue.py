'''
sensitivity_multiplier: 0.5
modifier: 1
'''
def main():
        
    ###########################################    
    # UA ANGL Thermo Ar cocktail queue (gettered air)
    
    info (Argus VI Ar cocktail Script)
    
    #reset valving, pump prep/MS
    close ('8') # MS inlet
    open ('1')  # Prep ion
    open ('9')  # MS ion
    close ('2') # Aux 1
    close ('3') # Aux 2
    close ('4') # Pipette Ref Out
    close ('5') # Pipette Ref In
    
    #gas into manifold
    if analysis_type=='blank'
    close ('1')
    open ('4') #Pipette Ref In
    sleep (30)
    
    else:
    open ('5') #Pipette Ref Out
    sleep (30)
    close ('5')
    close ('1')
    open ('4') #Pipette Ref In
    sleep (30)
    
    #gas into MS
    close('4')
    close ('9')
    open ('8')
    
    
        