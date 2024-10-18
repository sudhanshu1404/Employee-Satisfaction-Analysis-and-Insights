
#import required library
import pandas as pd
import numpy as np


#Load the dataset
data = pd.read_csv(r"C:\Users\Sudhanshu\OneDrive\Desktop\employee_experience_survey_data.csv")

#show data 
data

data.head() #for show only 5 rows of data set

#Summary of data
data.info()

#Wheater checking data columns
data.columns

data.isna()

#Identify Duplicate rows in a DataFrame or Series
data.duplicated()

#.sum() with duplicated() to Count the number of duplicate rows
data.duplicated().sum()

#Now we Counting Missing Values:
data.isnull().sum()


# # Descriptive Statstics Analysis
# Claculate the 'overall engagement Engagement and job satisfication'
desc_status = data[['Overall Engagement','Job Satisfaction']].describe()
#Display the result
print(desc_status)

# mapping" generally refers to creating a relationship between two sets of data, typically achieved using 
dictionaries or functions like map().
# In[102]:


#Here We Mapping the categorical responses to numeric values
mapping = {
    'Strongly Disagree': 1,
    'Disagree': 2,
    'Neutral': 3,
    'Agree': 4,
    'Strongly Agree': 5
}

# Applying the mapping to the columns
data['Overall Engagement'] = data['Overall Engagement'].map(mapping)
data['Job Satisfaction'] = data['Job Satisfaction'].map(mapping)


#Now we Calculating the mean, median, and mode for the selected columns
mean_values = data[['Overall Engagement', 'Job Satisfaction']].mean()
median_values = data[['Overall Engagement', 'Job Satisfaction']].median()
mode_values = data[['Overall Engagement', 'Job Satisfaction']].mode()

# Displaying the results
print("Mean:\n", mean_values)
print("\n")
print("Median:\n", median_values)
print("\n")
print("Mode:\n", mode_values)

# # ○ Identify any key trends in the survey results

#import libraby for data visualization
import matplotlib.pyplot as plt


# Step 2: Convert survey responses to numeric values
#using mapping which is previous same as

# Apply the mapping to satisfaction-related columns
columns_convert = ['Job Satisfaction', 'Work-Life Balance', 'Compensation Satisfaction']
data[columns_convert] = data[columns_convert].replace(mapping)

# Step 3: Calculate average satisfaction scores for each age group
age_satisfaction = data.groupby('Age Bracket')[columns_convert].mean()

# Step 4: Calculate average satisfaction scores for each department
department_satisfaction = data.groupby('Department')[columns_convert].mean()

# Step 5: Calculate average satisfaction scores for each gender
gender_satisfaction = data.groupby('Gender')[columns_convert].mean()

# Step 6: Plot satisfaction trends by Age Bracket
plt.figure(figsize=(10, 5))
age_satisfaction.plot(kind='bar', title='Average_Satisfaction by Age Bracket', ax=plt.gca())
plt.ylabel('Average Score')
plt.xticks(rotation=45)
plt.show()

# Step 7: Plot satisfaction trends by Department
plt.figure(figsize=(10, 5))
department_satisfaction.plot(kind='bar', title='Average Satisfaction by Department', ax=plt.gca())
plt.ylabel('Average Score')
plt.xticks(rotation=40)
plt.tight_layout()
plt.show()


# Step 8: Plot satisfaction trends by Gender
plt.figure(figsize=(10, 5))
gender_satisfaction.plot(kind='bar', title='Average Satisfaction by Gender', ax=plt.gca())
plt.ylabel('Average Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()





# # 2. Inferential Statistics:
import scipy.stats as stats
# Sample DataFrame (replace with your actual DataFrame)
data = pd.DataFrame({
    'Department': ['IT', 'IT', 'HR', 'HR', 'IT', 'HR', 'IT', 'HR'],
    'Job Satisfaction': [4, 5, 3, 2, 4, 3, 5, 2]
})

# Extract Job Satisfaction for IT and HR
it_satisfaction = data[data['Department'] == 'IT']['Job Satisfaction']
hr_satisfaction = data[data['Department'] == 'HR']['Job Satisfaction']

# Conduct the t-test
t_statistic, p_value = stats.ttest_ind(it_satisfaction, hr_satisfaction)

# Print results
print(f"T-statistic: {t_statistic}, P-value: {p_value}")

# Conclusion
alpha = 0.05  # significance level
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in Job Satisfaction between IT and HR.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in Job Satisfaction between IT and HR.")

# Sample DataFrame (replace with your actual DataFrame)
data = pd.DataFrame({
    'Work-Life Balance': [4, 5, 3, 2, 4, 3, 5, 2],
    'Overall Engagement': [5, 4, 3, 2, 4, 3, 5, 2]
})

# Calculate correlation coefficient
correlation = data['Work-Life Balance'].corr(data['Overall Engagement'])

# Print the Correlation-Coefficient
print(f"Correlation Coefficient: {correlation}")
#Conditional statement 
# Interpret the correlation coefficient
if correlation > 0:
    print("There is a positive correlation between Work-Life Balance and Overall Engagement.")
elif correlation < 0:
    print("There is a negative correlation between Work-Life Balance and Overall Engagement.")
else:
    print("There is no correlation between Work-Life Balance and Overall Engagement.")

#Perform correlation analysis
#.corr() function calculates the Pearson correlation coefficient between the two specified columns.
#+1 indicates a perfect positive correlation.
##0 indicates no linear correlation.
#-1 indicates a perfect negative correlation.
#correlation_coefficient: This variable stores the computed correlation coefficient value.
correlation_coefficient = data['Work-Life Balance'].corr(data['Overall Engagement'])

#Display the correlation coefficient
print(f"Correlation between Work-Life Balance and Overall Engagement: {correlation_coefficient:.2f}")
