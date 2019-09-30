'''

'''
def main():
        
    ###########################################    
    # UA ANGL Thermo Ar cocktail script (gettered air)
    
    info('Argus VI Ar Procedure Script')
    
    #reset valving, pump prep/MS
    close('8') # MS inlet
    open('1')  # Prep ion
    open('9')  # MS ion
    close('2') # Aux 1
    close('3') # Aux 2
    close('4') # Pipette Ref Out
    close('5') # Pipette Ref In
    
    
    #load the air shot into the pipette
    close('6')  # for explicit completeness close the other pipette. not strictly necessary
    close('7')
    
    close('4')
    open('5')
    sleep(30)
    close('5')
    
    #load pipette into V1
    open('4')
    sleep (30)
    
    
    # when doing automated analysis the extraction script should stop here
    # since this is a procedure script we need to do the equilibration and post_equilibration
    # steps here
    
    # The following should only be used in procedures scripts NOT in extraction scripts 
    #gas into MS
    close('4')
    close ('9')
    open ('8')
    
    # equilibrate
    sleep(15)
    close('8')
    open ('1')
    
    # reset prep line to default state
    # when doing automated analysis this would go in your post_equilibration script
    open('1')  # Prep ion
    close('2') # Aux 1
    close('3') # Aux 2
    close('4') # Pipette Ref Out
    close('5') # Pipette Ref In
    
    # when doing automated analysis the following would go in your post_measurement script
    # but you don't want to pump away the gas you just loaded so its commented out here
    # open('9') # MS Ion pump
    
    
        