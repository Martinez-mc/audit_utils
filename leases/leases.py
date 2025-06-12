# Helpers
# -----------------------------------------------------------------------
def pv_factor_lumpsum(rate, periods):
    """Returns pv factor of lumpsum"""
    pv_factor = 1 / (1 + rate)**periods
    return pv_factor

def pv_factor_annuity(cat, rate, periods):
    pv_factor = 0.00
    if cat == 'Ordinary':
        # Computes the pv factor of Ordinary Annuity
        pv_factor = (1 - 1 / (1 + rate)**periods) / rate
        return pv_factor
    
    elif cat == 'Due':
        # Computes the pv factor of an Annuity Due
        pv_factor = ((1 - (1 + rate)**-periods) / rate) * (1 + rate)
        return pv_factor
    else:
        raise ValueError("Wrong option used.")
# ------------------------------------------------------------------------

# -------------------------------------------------------------------------
# If any of the folowing tests returns True, the lease will be categorized
# as a Finance Lease, else it will be an Operating Lease
# ------------------------------------------------------------------------
def ownership_test(transfer):
    if transfer == True:
        return True
    else: 
        return False
    
def purchase_option_test(option):
    if option == True:
        return True
    else:
        return False

def lease_term_test(lease_terms, useful_life):
    """If lease term is equal or greater than 75% of useful life return True (75% Test)"""
    if lease_terms >= useful_life * .75:
        return True
    else:
        return False
    
def present_value_test(cat, rate, residual, fair_value, terms, pmts):
    """If pv of payments and residual greater than fair value of assets return True (90% Test) """
    if cat == 'Ordinary':
        pv_factor = pv_factor_annuity('Ordinary', rate, terms)
        pv_of_pmts = pmts * pv_factor
        pv_of_residual = residual * pv_factor_lumpsum(rate, terms)
        if pv_of_pmts + pv_of_residual > (fair_value * .90):
            return True
        else: 
            return False
    elif cat == 'Due':
        pv_factor = pv_factor_annuity('Due', rate, terms)
        pv_of_pmts = pmts * pv_factor
        pv_of_residual = residual * pv_factor_lumpsum(rate, terms)

        if pv_of_pmts + pv_of_residual > (fair_value * .90):
            return True
        else: 
            return False
    else:
        raise ValueError("Wrong option used.")

def alternative_use_test(alt_use):
    # Specialized Equipment
    if alt_use == True:
        return True
    else:
        return False

