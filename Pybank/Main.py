#declare libraries
import pandas as pd

#import data
basedata = pd.DataFrame(pd.read_csv("../Instructions/PyBank/resources/budget_data.csv"))

#total months
months = basedata["Date"].count()
# print(months)

#total profit
totalprofit = basedata["Profit/Losses"].sum()
# print(totalprofit)


#declare vars for 'for' loop
profitdiffgain = 0
profitdiffloss = 0
previous = 0
alldiff = []
#iterate through records checking to see largest difference
for record in basedata["Profit/Losses"]:
#define profit difference
    profitdiff = record - previous
    #store profit diff
    alldiff.append(profitdiff)
    #finding largest profit
    if profitdiff > profitdiffgain:
        profitdiffgain = profitdiff
#finding largest loss
    elif profitdiff < profitdiffloss:
        profitdiffloss = profitdiff
    previous = record
#finding the mean    
alldiffmean = sum(alldiff)/len(alldiff)

#print results
print(f"""

Financial analysis
------------------------------------
Total months: {months}
Total profit: ${totalprofit}

Average profit change: ${alldiffmean}
Greatest increase in profit: ${profitdiffgain}
Greatest decrease in profit: ${profitdiffloss}

End of report.
""")