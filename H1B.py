import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


d23=pd.read_csv("h1b_datahubexport-2023.csv")
d22=pd.read_csv("h1b_datahubexport-2022.csv")
d21=pd.read_csv("h1b_datahubexport-2021.csv")
d20=pd.read_csv("h1b_datahubexport-2020.csv")
d19=pd.read_csv("h1b_datahubexport-2019.csv")
d18=pd.read_csv("h1b_datahubexport-2018.csv")
d17=pd.read_csv("h1b_datahubexport-2017.csv")
d16=pd.read_csv("h1b_datahubexport-2016.csv")
d15=pd.read_csv("h1b_datahubexport-2015.csv")
d14=pd.read_csv("h1b_datahubexport-2014.csv")
d13=pd.read_csv("h1b_datahubexport-2013.csv")
d12=pd.read_csv("h1b_datahubexport-2012.csv")
d11=pd.read_csv("h1b_datahubexport-2011.csv")
d10=pd.read_csv("h1b_datahubexport-2010.csv")
d09=pd.read_csv("h1b_datahubexport-2009.csv")

d09['Initial Approvals'] = d09['Initial Approvals'].str.replace(',', '').astype(int)
d10['Initial Approvals'] = d10['Initial Approvals'].str.replace(',', '').astype(int)
d11['Initial Approvals'] = d11['Initial Approvals'].str.replace(',', '').astype(int)
d12['Initial Approvals'] = d12['Initial Approvals'].str.replace(',', '').astype(int)
d13['Initial Approvals'] = d13['Initial Approvals'].str.replace(',', '').astype(int)
d14['Initial Approvals'] = d14['Initial Approvals'].str.replace(',', '').astype(int)
d15['Initial Approvals'] = d15['Initial Approvals'].str.replace(',', '').astype(int)
d16['Initial Approvals'] = d16['Initial Approvals'].str.replace(',', '').astype(int)
d17['Initial Approvals'] = d17['Initial Approvals'].str.replace(',', '').astype(int)
d18['Initial Approvals'] = d18['Initial Approvals'].str.replace(',', '').astype(int)
d19['Initial Approvals'] = d19['Initial Approvals'].str.replace(',', '').astype(int)
# d20['Initial Approvals'] = d20['Initial Approval'].str.replace(',', '').astype(int)




t23 = d23['Initial Approval'].sum()
t22 = d22['Initial Approval'].sum()
t21 = d21['Initial Approval'].sum()
t20 = d20['Initial Approval'].sum()
t19 = d19['Initial Approvals'].sum()
t18 = d18['Initial Approvals'].sum()
t17 = d17['Initial Approvals'].sum()
t16 = d16['Initial Approvals'].sum()
t15 = d15['Initial Approvals'].sum()
t14 = d14['Initial Approvals'].sum()
t13 = d13['Initial Approvals'].sum()
t12 = d12['Initial Approvals'].sum()
t11 = d11['Initial Approvals'].sum()
t10 = d10['Initial Approvals'].sum()
t09 = d09['Initial Approvals'].sum()

cat=['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']
values=[t09,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23]


e09 = d09['Employer'].value_counts()
e10 = d10['Employer'].value_counts()
e11 = d11['Employer'].value_counts()
e12 = d12['Employer'].value_counts()
e13 = d13['Employer'].value_counts()
e14 = d14['Employer'].value_counts()
e15 = d15['Employer'].value_counts()
e16 = d16['Employer'].value_counts()
e17 = d17['Employer'].value_counts()
e18 = d18['Employer'].value_counts()
e19 = d19['Employer'].value_counts()
e20 = d20['Employer'].value_counts()
e21 = d21['Employer'].value_counts()
e22 = d22['Employer'].value_counts()
e23 = d23['Employer'].value_counts()

total_sum = e09.add(e10, fill_value=0).add(e11, fill_value=0).add(e12, fill_value=0).add(e13, fill_value=0).add(e14, fill_value=0).add(e15, fill_value=0).add(e16, fill_value=0).add(e17, fill_value=0).add(e18, fill_value=0).add(e19, fill_value=0).add(e20, fill_value=0).add(e21, fill_value=0).add(e22, fill_value=0).add(e23, fill_value=0)


############# PLOTTING HIGHEST EMPLOYER GRAPH #######################


# Assuming total_sum is your Pandas Series containing the summed counts
top_10_values = total_sum.nlargest(10)

# Convert the index and values of the top 10 values to a DataFrame for plotting
top_10_df = top_10_values.reset_index(name='Counts')

# Create the bar plot using Seaborn
plt.figure(figsize=(10, 6))  # Set the size of the plot
sns.barplot(x=top_10_values.index, y='Counts', data=top_10_df)

# Set labels and title
plt.xlabel('Companies')
plt.ylabel('Counts')
plt.title('Highest H1B Visa Recruiters from 2009-23')

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

#############################################################

#PLOTTING LINE GRAPH OF H1B APPROVALS

# dat={'Year': cat,'Approvals':values}

# sns.lineplot(x='Year', y='Approvals', data=dat)

# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()


# # Adding labels and title
# plt.xlabel('Year')
# plt.ylabel('Approvals')
# plt.title('H1B Data Analysis')

# # Show the plot
# plt.show()
