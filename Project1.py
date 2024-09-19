#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[3]:


dataset=pd.read_excel(r"C:\Users\DELL\Downloads\College.x.xlsx")


# In[5]:


dataset.shape


# In[9]:


dataset.head()


# In[11]:


dataset.info()


# In[13]:


pd.isnull(dataset)


# In[15]:


pd.isnull(dataset).sum()


# In[17]:


dataset['Rating'] = dataset['Rating'].str.replace('*', '', regex=False)


# In[19]:


dataset.head()


# In[21]:


dataset['Rating'] = pd.to_numeric(dataset['Rating'], errors='coerce').astype(float)


# In[23]:


dataset.info()


# In[93]:


dataset.columns


# In[77]:


median_rating = dataset['Rating'].median()
dataset['Rating'] = dataset['Rating'].fillna(median_rating)


# In[31]:


dataset.head(20)


# In[35]:


mode_location = dataset['Location'].mode()[0]
dataset['Location'] = dataset['Location'].fillna(mode_location)


# In[37]:


dataset.head(16)


# In[39]:


mode_study_program = dataset['Study Program'].mode()[0]
dataset['Study Program'] = dataset['Study Program'].fillna(mode_study_program)


# In[43]:


dataset.head(20)


# In[47]:


mode_affiliate = dataset['Affiliation'].mode()[0]
dataset['Affiliation'] = dataset['Affiliation'].fillna(mode_affiliate)


# In[49]:


dataset.head(20)


# In[51]:


mode_sector = dataset['Sector'].mode()[0]
dataset['Sector'] = dataset['Sector'].fillna(mode_sector)


# In[55]:


dataset.head(20)


# In[57]:


dataset.describe()


# # Visualization of Academic Results

# In[326]:


import seaborn as sns
import matplotlib.pyplot as plt
average_ratings_by_sector = dataset.groupby('Sector')['Rating'].mean().reset_index()
plt.figure(figsize=(12, 8))
sns.barplot(x='Sector', y='Rating', data=average_ratings_by_sector, hue='Sector')
plt.title('Average Academic Results (Ratings) by Sector')
plt.xlabel('Sector')
plt.ylabel('Average Rating')
plt.xticks(rotation=45) 
plt.show()



# # Rating & Sector : Public Sector has better Academic Results then Private according to Rating

# In[ ]:


import pandas as pd
study_program_counts = dataset['Study Program'].value_counts()
threshold = 15 
frequent_programs = study_program_counts[study_program_counts > threshold].index
filtered_dataset = dataset[dataset['Study Program'].isin(frequent_programs)]
print(filtered_dataset)
filtered_dataset.to_excel('filtered_data_frequent_programs.xlsx', index=False)


# In[328]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
threshold = 10
program_counts = dataset['Study Program'].value_counts()
frequent_programs = program_counts[program_counts > threshold].index
filtered_dataset = dataset[dataset['Study Program'].isin(frequent_programs)]
average_ratings_program = filtered_dataset.groupby('Study Program')['Rating'].mean().reset_index()
average_ratings_program = average_ratings_program.sort_values(by='Rating', ascending=False)
plt.figure(figsize=(12, 8))
sns.barplot(x='Rating', y='Study Program', data=average_ratings_program,hue='Study Program')
plt.title(f'Average Rating by Study Program (Threshold: {threshold} occurrences)')
plt.xlabel('Average Rating')
plt.ylabel('Study Program')
plt.show()


# # FA, ICS Computer Science, FSC Pre Engineering, FSc Pre Medical,ICOM have more Ratings which represent good Academic Results 

# In[330]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
threshold = 1
counts = dataset['Institute_Name'].value_counts()
frequent_institutes = counts[counts > threshold].index
filtered_dataset = dataset[dataset['Institute_Name'].isin(frequent_institutes)]
average_ratings = filtered_dataset.groupby('Institute_Name')['Rating'].mean().reset_index()
plt.figure(figsize=(12, 8))
sns.barplot(x='Rating', y='Institute_Name', data=average_ratings, hue='Institute_Name')
plt.title(f'Average Rating by Institute (Threshold: {threshold} occurrences)')
plt.xlabel('Average Rating')
plt.ylabel('Institute_Name')
plt.show()


# # Rating & Institute : Federal Board has good Academic result According to it's Rating

# # Visualization of Faculty Quality

# In[334]:


average_ratings_sector = dataset.groupby('Sector')['Rating'].mean().reset_index()
plt.figure(figsize=(12, 8))
sns.barplot(x='Rating', y='Sector', data=average_ratings_sector, hue='Sector')
plt.title('Average Rating by Sector')
plt.xlabel('Average Rating')
plt.ylabel('Sector')
plt.show()


# # Higher Ratings of any Sector might Correlate with better quality of Faculty  

# In[338]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
threshold = 10  
program_counts = dataset['Study Program'].value_counts()
frequent_programs = program_counts[program_counts > threshold].index
filtered_dataset = dataset[dataset['Study Program'].isin(frequent_programs)]
average_ratings_program = filtered_dataset.groupby('Study Program')['Rating'].mean().reset_index()
average_ratings_program = average_ratings_program.sort_values(by='Rating', ascending=False)
plt.figure(figsize=(12, 8))
sns.barplot(x='Rating', y='Study Program', data=average_ratings_program, hue='Study Program')
plt.title(f'Average Rating by Study Program (Threshold: {threshold} occurrences)')
plt.xlabel('Average Rating')
plt.ylabel('Study Program')
plt.show()


# # FA, ICS Computer Science, FSc Pre Medical, Fsc Pre Engineering, ICOM study programs might have higher Ratings due to Better faculty  

# # (C) Visualization of Resources 

# In[340]:


# Calculate average rating by Sector
average_ratings_sector = dataset.groupby('Sector')['Rating'].mean().reset_index()

# Plot
plt.figure(figsize=(12, 8))
sns.barplot(x='Rating', y='Sector', data=average_ratings_sector, hue='Sector')
plt.title('Average Rating by Sector')
plt.xlabel('Average Rating')
plt.ylabel('Sector')
plt.show()


# # Different Sectors have Different Resource Levels , Sectors with high ratings might have good resources

# In[354]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
affiliation_threshold = 3
affiliation_counts = dataset['Affiliation'].value_counts()
valid_affiliations = affiliation_counts[affiliation_counts >= affiliation_threshold].index
filtered_dataset = dataset[dataset['Affiliation'].isin(valid_affiliations)]
plt.figure(figsize=(12, 8))
bars = plt.barh(filtered_dataset['Affiliation'], filtered_dataset['Rating'], color='teal', edgecolor='none')
plt.title('Average Rating by Affiliation')
plt.xlabel('Average Rating')
plt.ylabel('Affiliation')
for bar in bars:
    bar.set_edgecolor('none')

plt.show()





# # Affiliation that has more ratings may have good resources 

# In[356]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
location_threshold =2
location_counts = dataset['Location'].value_counts()
valid_locations = location_counts[location_counts >= location_threshold].index
filtered_dataset = dataset[dataset['Location'].isin(valid_locations)
print("Valid Locations After Filtering:")
print(filtered_dataset['Location'].value_counts())
location_resources = filtered_dataset.groupby('Location')['Rating'].mean().reset_index()
all_valid_locations = pd.DataFrame({'Location': valid_locations})
location_resources_full = pd.merge(all_valid_locations, location_resources, on='Location', how='left')
location_resources_full['Rating'] = location_resources_full['Rating'].fillna(0)
location_resources_full = location_resources_full.sort_values(by='Rating', ascending=False)
plt.figure(figsize=(12, 8))
sns.barplot(x='Rating', y='Location', data=location_resources_full, hue='Location')
plt.title('Average Rating by Location (Approximation of Resources)')
plt.xlabel('Average Rating')
plt.ylabel('Location')
plt.show()





# # Location may vary the Resources

# # Conclusion:

# In[ ]:


According to the analysis,
On the basis of Rating , the public sector, FA,ICS Computer Science, Pre Medical , Pre Engineering,ICOM in Study Program and Federal Board
in Institute Name have good Academic results.
By Rating, Public Sector and  FA,ICS Computer Science, Pre Medical , Pre Engineering,ICOM in Study Program have good quality of Faculty.
In Rating, Public sector, University of Sargodha,Peshawar,Federal Institute and UMT in Study program and 30-A Johar Town Lahore by Location has
good Reources.    


