import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Users\bosox\Desktop\Data Visualization\Data Prep with Python\hmeq.csv",
    na_values=["", " ", "NA", "NaN"] 
)

cleaned_df = df.dropna()

cleaned_df = cleaned_df.rename(columns={
    'LOAN': 'Loan_amount',
    'VALUE': 'Appraised_Value',
    'JOB': 'Borrowers_Job',
    'YOJ': 'Years_Employed',
    'CLAGE': 'Credit_Line_Age',
    'NINQ': 'Recent_Credit_Lines',
    'CLNO': 'Total_Credit_Lines'
})


reason_map = {
    'DebtCon': 'Debt Consolidation',
    'HomeImp': 'Home Improvement'
}

job_map = {
    'Mgr': 'Manager',
    'Office': 'Office Worker',
    'Other': 'Other/Unknown',
    'ProfExe': 'Professional/Executive',
    'Sales': 'Sales',
    'Self': 'Self-Employed'
}


cleaned_df['REASON'] = cleaned_df['REASON'].replace(reason_map)
cleaned_df['Borrowers_Job'] = cleaned_df['Borrowers_Job'].replace(job_map)

cleaned_df['REASON'] = cleaned_df['REASON'].str.strip()
cleaned_df['Borrowers_Job'] = cleaned_df['Borrowers_Job'].str.strip()

avg_lines = cleaned_df.groupby('BAD')['Total_Credit_Lines'].mean()
std_lines = cleaned_df.groupby('BAD')['Total_Credit_Lines'].std()

print(cleaned_df.head(15))

plt.bar(avg_lines.index, avg_lines, yerr=std_lines, capsize=5)
plt.xlabel('BAD')
plt.ylabel('Average Total Credit Lines')
plt.title('Average Total Credit Lines by BAD')
plt.show()

avg_debtinc = cleaned_df.groupby('BAD')['DEBTINC'].mean()
std_debtinc = cleaned_df.groupby('BAD')['DEBTINC'].std()

plt.bar(avg_debtinc.index, avg_debtinc, yerr=std_debtinc, capsize=5, color='orange')
plt.xlabel('BAD')
plt.ylabel('Average DEBTINC')
plt.title('Average DEBTINC by BAD')
plt.show()


