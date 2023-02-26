#!/usr/bin/env python
# coding: utf-8

# # Assigment_24-02-2023

# ## 1. List any five functions of the pandas library with execution.
# 
# ### Ans:-
#         There are five functions from the pandas library with an example of their execution:
#         
#         1.read_csv(): This function is used to read CSV files and returns a DataFrame.
#         
#         2.groupby(): This function is used to group rows in a DataFrame based on some criteria. 
#         
#         3.dropna(): This function is used to remove missing values from a DataFrame.
#         
#         4.merge(): This function is used to merge two DataFrames based on a common column. 
#         
#         5.describe():- This function generates descriptive statistics of a DataFrame, including count, mean, standard 
#                        deviation, minimum, maximum, and quartiles.
#                        
#                        
# 

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('D:\\Manas_HP Laptop Backup_13112019\\DATA Science Class Video\\09.Week=08 DS Study Meterial\\Day-14_Logistic Regrassion\\train.csv')


# In[3]:


df.head()


# In[4]:


print(df.head())


# In[5]:


grouped = df.groupby('Survived')['Age'].mean()


# In[6]:


print(grouped)


# In[7]:


df.isnull


# In[8]:


clean_df = df.dropna()


# In[9]:


print(clean_df.head())


# In[10]:


df=df.describe()


# In[11]:


print(df.describe())


# ## 2. Given a Pandas DataFrame df with columns 'A','B', and 'C', Write a Python function to re-index the DataFrame with a new index that starts from 1 and increments by 2 for each row.
# 
# ### Ans:-
# 

# In[12]:


df = pd.DataFrame({'A':[1,2,3,4,5],
                  'B':[6,7,8,9,10],
                  'C':[11,12,13,14,15]})


# In[13]:


len(df)


# In[14]:


print(df)


# In[15]:


def reindex_df(df):
    new_index = range(1,2*len(df),2)
    df.index = new_index
    return(df)
df = reindex_df(df)
print(df)


# ## 3. You have a pandas DataFrame df with a column name 'Values'.Write a python function that iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The function should print the sum to the console.
# 
# ## For example, if the value column of df  contains the values [10,20,30,40,50,],your function should be calculate and print the sum of the first three values,which is 60.
# 
# ### Ans:-

# In[16]:


df = pd.DataFrame({'values':[10,20,30,40,50]})
print(df)


# In[17]:


df['values'][:4]


# In[18]:


def sum_first_three(df):
    num = 0
    for i in df['values'][:3]:
        num += i
    print("Sum of first three numbers: ",num)


# In[19]:


df = pd.DataFrame({'values':[10,20,30,40,50]})
sum_first_three(df)


# ## 4. Given a Pandas Data Frame df with a column 'TEXT', write a python function to create a new column 'Word_Count' that contains the number of words in each row of the 'TEXT' Column.
# 
# ### Ans:-
# 

# In[20]:


df = pd.DataFrame({'TEXT':['My Name is Manas Ranjan Pandey','My wife Name is Sunandini Pandey', 'My Daughter Name is Sejal Pandey']})

def count_word(text):
    return len(text.split())
df['word_count'] = df['TEXT'].apply(count_word)

print(df)


# ## 5. How are Data Frame.size() and Data Frame.shape() different?
# 
# ### Ans:-
# 
#         Both DataFrame.size and DataFrame.shape are attributes of a Pandas DataFrame that provide information about the DataFrame's dimensions. However, they represent different pieces of information:
# 
#         DataFrame.size: Returns the number of elements in the DataFrame, which is equal to the product of the number of rows and the number of columns in the DataFrame. This attribute returns a single integer value.
# 
#         DataFrame.shape: Returns a tuple containing the number of rows and columns in the DataFrame. The first element of 
#     the tuple represents the number of rows, and the second element represents the number of columns.
# 

# In[21]:


df = pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8],'C':[9,10,11,12]})

print("Size of the DataFrame",df.size)
print("Shape of the Datashape",df.shape)


# ## 6. Which function of pandas do we use to read an excel file?
# 
# ### Ans:-
# 
#         Pandas provides a function read_excel() to read data from an Excel file into a Pandas DataFrame. The read_excel()
#         function is a versatile and flexible way to read data from an Excel file because it can handle various types of 
#         Excel files, including .xls, .xlsx, and .xlsm.
# 
#         In the code above, the read_excel() function reads an Excel file named 'filename.xlsx' and returns the data as a 
#         Pandas DataFrame object. By default, the function reads the first sheet of the Excel file. If you want to read a
#         specific sheet, you can specify the sheet name or index using the sheet_name parameter.
# 
#        You can also use other parameters of read_excel() to specify options such as the range of rows and columns to read, 
#        the header row, and the data type of columns. Please refer to the pandas documentation for more details on the 
#        read_excel() function and its parameters.
#         

# ## 7. You have a Pandas Data Frame df that contains a column named 'Email' that contains email addresses in the format 'username@domain.com'.
# ## Write a python function that creates a new column 'Username' in df that contains only the username part of each email address.
# 
# ### The user name is the part of the email address that appears before the  '@' symbol.For example, if the email address is 'john.doe@example.com',the 'Username'column should contain 'john.doe'.your function should be extract the user name from each email address and store it in the new 'username'column.
# 
# ### Ans:-

# In[22]:


df = pd.DataFrame({'Email':['manas.pandey@vodafoneidea.com','patelsunandini@gmail.com','pandey.sejal@gmail.com']})

def get_username(email):
    return email.split('@')[0]
df['Username']= df['Email'].apply(get_username)
print(df)
    


# In[23]:


df = pd.DataFrame({'Email':['manas.pandey@vodafoneidea.com','patelsunandini@gmail.com','pandey.sejal@gmail.com']})

get_username = lambda email: email.split('@')[0]
df['Username']= df['Email'].apply(get_username)
print(df)


# ## 8. You have a pandas DataFrame df with column 'A','B', and 'C'. write a python function that select all rows where the value in column 'A' is grater than 5 and the value in column 'B' is less than 10.The function should return a new DataFrame that contains only the selected rows.
#  ### for Example, if df contains the following values:
#  
#  |A|  |B|  |C|
#  |-|  |-|  |-|
#  |3|  |5|  |1|
#  |8|  |2|  |7|
#  |6|  |9|  |4|
#  |2|  |3|  |5|
#  |9|  |1|  |2|
#  
#  ### Your Function should select the following rows: A B C
#  
#  ### 8 2 7
#  ### 9 1 2
#  
#  ### The Function should return a new DataFrame that contains only the select rows.
#  
#  ### Ans:-

# In[24]:


df = pd.DataFrame({'A':[3,8,6,2,9],'B':[5,2,9,3,1],'C':[1,7,4,5,2]})
new_df = df[(df['A']>5) & (df['B']<10)]
print(new_df)


# ## 9. Give a pandas DataFrame df with a column 'values', Write a python function to calculate the mean, median and standard deviation of the values in the values column.
# 
# ### Ans:-

# In[25]:


df = pd.DataFrame({'Values':[19,80,19,88,20,14]})
mean_values = df['Values'].mean()
median_values = df['Values'].median()
std_values = df['Values'].std()

print('Mean_value: ',mean_values)
print('Median_value: ',median_values)
print("Standard_Deviation:",std_values)


# ## 13.To used the basic function of pandas, what is the first and foremost necessary library that needs to be imported?
# 
# ### Ans:-
#     The first and foremost library that needs to be imported to use the basic functions of pandas is pandas itself. The pandas
#     library provides a powerful and flexible toolset for working with structured data, especially for data manipulation, 
#     analysis, and cleaning.
# 
#     Here's an example of how to import the pandas library in Python:
#     
# ## import pandas as pd
#      
#      In this example, we use the import statement to import the pandas library and then assign it an alias pd using the as
#      keyword. This alias is a common convention used in the pandas community to make the code more readable and concise. 
#      Once the pandas library is imported, you can start using its basic functions and data structures, such as Series and
#      DataFrame, in your Python code.
# 
# 

# ## 12 . Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a python function to select all rows where the date is between '2023-01-01' and '2023-01-31'
# 
# ### Ans:-
# 
# 

# In[26]:


df = pd.DataFrame({'Date':['2023-01-01','2023-01-06','2023-02-25',"2023-05-15",'2023-01-31','2023-02-16']})

new_df = df[df['Date'].between('2023-01-01', '2023-01-31')]
print(new_df)
                   


# ## 10. Give a Pandas DataFrame df with a column 'Sales' and a column 'Date', Write a python function to create a new column 'MovingAverage' that contains the moving average of the sales for past 7 days for each row in the DataFrame. The moving average should be calculated using a window of size 7 and should include the current day.
# 
# ### Ans:-
# 
# 

# In[1]:


import pandas as pd


# In[ ]:


def add_moving_average(df):
    df.set_index('Date',inplace=True)
df['Movingaverage'] = df['sale'].rolling(window=7,min_periods =1).mean()


# ## 11. You have a panads DataFrame df with a column 'Date'.Write a python function that creates a new column 'Weekday' in the DataFrame.The weekday column should contain the weekday name (e.g. Monday,Tuesday) corresponding the each date in the date column.
# 
# ### For Example, if df contains the following values:
#           Date
#           2023-01-01
#           2023-01-02
#           2023-01-03
#           2023-01-04
#           2023-01-05
#           2023-01-06
# ### You function should create the following DateFrame:
# 
#              Date        Weekday
#           2023-01-01     Sunday
#           2023-01-02     Monday
#           2023-01-03     Tuesday
#           2023-01-04     Thrushday
#           2023-01-05     Friday
#           2023-01-06     Satuarday
# ### The function should return the modified Dataframe.
# 
# ### Ans:-

# In[1]:


import pandas as pd


# In[2]:


data= {'Date':pd.date_range(start='2023-02-01',end = '2023-02-16')}
df=pd.DataFrame(data)
def add_weekday_column(df):
    df['weekday'] = df['Date'].dt.day_name()
    return(df)
df=add_weekday_column(df)
print (df)


# ### The function uses the dt accessor of the 'Date' column to access the datetime properties of the column, and then calls the day_name() method to get the name of the weekday for each date. The new 'Weekday' column is added to the DataFrame using the assignment operator.
