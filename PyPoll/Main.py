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

votenums = polls["Candidate"].value_counts()
print(votenums)