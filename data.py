import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('athlete_events.csv')
print('eventFirst few lines of Olympic dataset:')
print(df.head())

print("\nBasic statistics of the dataset:")
print(df.describe())

india_data = df[df['Team'] == 'India']
print("\nDetails of India in the Olympic Games:")
print(india_data)

top_countries = df['Team'].value_counts().head(10)
print("\nTop 10 Participating Countries:")
print(top_countries)



gender_participation = df['Sex'].value_counts()
print("\nGender-wise Participation:")
print(gender_participation)


plt.figure(figsize=(8, 5))
sns.countplot(x='Sex', data=df, palette='Set2')
plt.title('Gender-wise Participation in Olympics (1896-2016)')
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(df['Age'].dropna(), bins=20, kde=True, color='skyblue')
plt.title('Age-wise Participation in Olympics (1896-2016)')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()


medals_count = df['Medal'].value_counts()
print("\nCount of Medals:")
print(medals_count)

plt.figure(figsize=(8, 5))
sns.countplot(x='Medal', data=df, palette='viridis')
plt.title('Count of Medals in Olympics (1896-2016)')
plt.show()

print("\nConcluding Remarks:")
print("The analysis provides insights into the Olympic data between 1896-2016, including details of India's participation, top participating countries, gender distribution, age demographics, and the count of medals.")
