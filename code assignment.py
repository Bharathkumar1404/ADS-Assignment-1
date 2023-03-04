#importing the libraries
import pandas as pd
import matplotlib.pyplot as plt


# line is used for creating the function 
def avg_temp_of_months():
    '''
    this function is used to Createa line plot by using Temperatures and Years
    
    Returns
    it shows line plot

    '''
    #it is used for maintaining the figure
    plt.figure(figsize = (10, 6))
    #this line is used to plot the line graph
    plt.plot(temp_data['YEAR'], temp_data['JAN-FEB'], label = 'Jan-feb')
    plt.plot(temp_data['YEAR'], temp_data['MAR-MAY'],label = 'mar-may')
    plt.plot(temp_data['YEAR'], temp_data['JUN-SEP'], label = 'jun-sep')
    plt.plot(temp_data['YEAR'], temp_data['OCT-DEC'], label = 'oct-dec',
             marker = '*')
    #it indicates the diiferent types of values in graph
    plt.legend(loc = 'upper left')
    plt.title('Temperatures in different months')
    plt.xlabel('Years')
    plt.ylabel('Degrees')
    # it shows the axis lines
    plt.grid()
# it shows the graph
    plt.show()


#the line is used to create a function 
def sales_units_FF(df, col_name):
    '''
    

    Parameters
    
    df : used pandas data type
        reading the csv file
    col_name : string type
        function is used to groupby the million units coloumn and 
        returnig the values by iterrows arugumnet and plots the pie chart.

    Returns
    it shows pie chart
    '''
    df2 = df.groupby(col_name, as_index = False)['Million Units'].sum()
    plt.figure(figsize = (10, 10))
    exp = [0, 1, 0.05, 0, 1.5, 0, 0]
    plt.title('Sales Percentage by Form Factor')
    plt.pie(df2['Million Units'], labels = df2[col_name], autopct = '%.2f%%', 
            explode = exp)
    plt.show()


def companies_sales_units(df, col_name):
    '''
    

    Parameters
    
    df : used pandas data type
        to read the csv file.
    col_name : string type
        it is used to plot the bar chart horizontally from million units and 
        manufacturer.

    Returns
    it shows the bar chart

    '''
    plt.figure(figsize = (10, 5))
    plt.barh(df[col_name], df['Million Units'])
    plt.title('Sales of different companies')
    plt.legend()
    plt.grid()
    plt.xlabel("Million Units")
    plt.ylabel("Manufacturer")
    plt.show()
    
    
# The above line is used for reading the csv.dataset using pandas 
temp_data = pd.read_csv('temperatures.csv')

#the above line is used for returning the first five values
print(temp_data.head())

#ploting years over degrees
print(avg_temp_of_months())

# The above line is used for reading the csv.dataset using pandas 
df = pd.read_csv('List of best-selling mobile phones.csv')

# used to split the string 
l = []
df['Million Units'] = df['Million Units'].str.split('[')
print(df['Million Units'])
for i, j in df[['Million Units']].iterrows():
    l.append(float(j[0][0]))
print(l)
df['Million Units'] = l

#plopting units over form factor
print(sales_units_FF(df, 'Form factor'))

#ploting units over manufacturer
print(companies_sales_units(df, 'Manufacturer'))
    
 
