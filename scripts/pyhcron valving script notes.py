'''
sensitivity_multiplier: 0.5
modifier: 1
'''
def main():
    
    # use info to relay info to the user. e.g these info messages 
    # will appear in pychron's Console
    info('Jan Air Script')
    
    # this is a comment
    
    # this is an open valve command 
    open(description='Outer Pipette 2')
    
    # to delay/wait/sleep
    
    sleep(1) # wait 1 second
    
    #this is a close command
    close(description='Outer Pipette 2')
    
    # this is an open command using valve names
    
    open('1') # notice 1 is in quotes
    # open(1) this is invalid
    
    # you can use this approach or write a script called BlankArRef.py
    # i prefer this. why becomes clearer when writing experiments
    if analysis_type=='blank':
        # don't actually fill the pipette
    else:
        # fill pipette
        
    ###########################################    
    # UA ANGL Thermo Ar cocktail queue (gettered air)
    
    info (Argus VI Ar cocktail Script)
    
    #reset valving, pump prep/MS
    close ('8') # MS inlet
    open ('1')  # Prep ion
    open ('9')  # MS ion
    close ('2') # Aux 1
    close ('3') # Aux 2
    
    #gas into manifold
    open ('5') #Pipette Ref Out
    sleep (30)
    close ('5')
    close ('1')
    open ('4') #Pipette Ref In
    sleep (30)
    
    #gas into MS
    open ('8')
    
    
        