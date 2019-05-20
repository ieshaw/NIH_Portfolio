# NIH Portfolio Optimization

## Reviewing Lo et.al (2012)

They showed the efficient fronteir (portfolio optimization) [Figure 4, page 6] of investment accross the 7 buckets (AID, CHD, CNS, DDK, HLB, ONC, NMH)  of the NIH, with the returns signalled by an auto-regressive lag on YLL for the year 2005 based on the ROI from 1980-2003. They showed (with varying gamma [difference from current allocations, decribed in the middle of the left side column on page 5]) and with/without Alzheimer effects [decribed on the bottom of the right column on page 2]), how the efficient fronteir compares to different perspectives on the current NIH-funding. They claim, I believe rightfully so, how this shoes that the current NIH funding is inefficient. 

### Recreating

In order to re-create this experiment, here are our steps

1. Auto-regress funding with YLL to find the lag for each group (choose strongest R^2)
2. Find the correlation of these lagged YLL's
3. Establish the mean ROI for each bucket
4. Calculate Covariance Matrix
5. Vary the mu_not to develop efficient frontier
6. Compare to the historical NIH allocation
7. Show with and without dimentia effect
8. Show with different gammas

## Extending Further Invesitgation

Show same plot with two tweaks.

1. Use all the buckets we have (~78) vs. the 9 Lo et. al used
2. Do the same analysis with DALYs. Then plot the two efficient frontiers (DALY vs. YLL) and see if they are different