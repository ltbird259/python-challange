#declare libraries
import pandas as pd

#import data
basedata = pd.DataFrame(pd.read_csv("../Instructions/PyBank/resources/budget_data.csv"))

#total months
months = basedata["Date"].count()
print(months)

#total profit
totalprofit = basedata["Profit/Losses"].sum()
print(totalprofit)

#average profit
averageprofit = basedata["Profit/Losses"].mean()
print(averageprofit)

#declare vars for 'for' loop
profitdiffgain = 0
profitdiffloss = 0
previous = 0
#iterate through records checking to see largest difference
for record in basedata["Profit/Losses"]:
#finding largest profit
    if record - previous > profitdiffgain:
        profitdiffgain = record - previous
#finding largest loss
    elif record - previous < profitdiffloss:
        profitdiffloss = record - previous
    previous = record


print(f"""

Financial analysis
------------------------------------
Total months: {months}
Total profit: ${totalprofit}
Average profit: ${averageprofit}

Greatest increase in profit: ${profitdiffgain}
Greatest decrease in profit: ${profitdiffloss}

End of report.
""")