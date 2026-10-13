# Smoke test: re-derive the discretised columns of dataD.csv from data.csv with the thresholds used in preprocess.ipynb.
# Usage: python scripts/check_discretization.py .
import sys
import pandas as pd, numpy as np
d = pd.read_csv(sys.argv[1]+'/data.csv'); D = pd.read_csv(sys.argv[1]+'/dataD.csv')
print(d.shape, D.shape, 'NaN:', int(d.isna().sum().sum()), int(D.isna().sum().sum()))
print(d.describe().T[['min','max']])
for c in d.columns[6:]: print(c, d[c].value_counts().to_dict())

x = d.copy()
x['DBP']=np.select([d.DBP<80,d.DBP<90,d.DBP<=120],[0,1,2],3)
x['SBP']=np.select([d.SBP<120,d.SBP<130,d.SBP<140,d.SBP<=180],[0,1,2,3],4)
x['FastingBloodSugar']=np.select([d.FastingBloodSugar<100,d.FastingBloodSugar<126],[0,1],2)
x['Triglycerides']=np.select([d.Triglycerides<150,d.Triglycerides<200,d.Triglycerides<500],[0,1,2],3)
x['HDLcholestrol']=np.select([d.HDLcholestrol<40,d.HDLcholestrol<=60],[0,1],2)
x['LDLcholestrol']=np.select([d.LDLcholestrol<100,d.LDLcholestrol<130,d.LDLcholestrol<160,d.LDLcholestrol<190],[0,1,2,3],4)
for c in d.columns[:6]: print(c,'matches dataD:', (x[c].values==D[c].values).mean())
