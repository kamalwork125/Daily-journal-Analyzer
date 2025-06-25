import pandas as pd 
import numpy as np
from colorama import Fore,Style
print(Fore.RED+"----Daily journal Analyzer----"+Style.BRIGHT)
task=[]
while True:
 date= int(input("input date here"))
 mood=int(input(" Enter your current mood:"))
 sleep=int(input("ENter number of hours slept:"))
 journal =input("Enter your journal note here:")
 task.append([date,mood,sleep,journal])
 df=pd.DataFrame(task,columns=["date","mood","sleep","journal"])
 average=df['mood'].mean()
 print("Average of mood is:",average)
 avg=df['sleep'].mean()
 print("Average of sleep is:",avg)
 correlation = df['sleep'].corr(df['mood'])
 print(f"\n📊 Correlation between sleep and mood: {correlation:.2f}")
 df.to_csv("Daily_journal",sep='|',index=False)
 print("\n✅ Data saved successfully to file")