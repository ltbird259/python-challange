#pypoll analysis
#libraries
import pandas as pd
#import data
polls = pd.DataFrame(pd.read_csv("../Instructions/PyPoll/resources/election_data.csv"))

#count of votes
pollcount = polls["Candidate"].count()
print(pollcount)

#Candidates who got votes
candidates = polls["Candidate"].unique()
print(candidates)

khan =0
correy=0
li=0
otooley=0
for vote in polls["Candidate"]:
    if vote =="Khan":
        khan += 1
    elif vote =="Correy":
        correy += 1
    elif vote =="Li":
        li +=1
    elif vote =="O'Tooley":
        otooley += 1
    else:
        print("problem")

arrayvotes = [khan,correy,li,otooley]
winner = max(arrayvotes)
sumvotes = sum(arrayvotes)

khanpercent = (khan/sumvotes) *100
correypercent = (correy/sumvotes) *100
lipercent = (li/sumvotes) *100
otooleypercent = (otooley/sumvotes) *100


print(f"""
Results of poll
Number of votes cast: {pollcount}
All candidates who received votes:
{candidates}
Vote count and percentages
Khan: %{khanpercent} - {khan}
Correy: %{correypercent} - {correy}
Li: %{lipercent} - {li}
O'Tooley: %{otooleypercent} - {otooley}

Winner: Khan

""")