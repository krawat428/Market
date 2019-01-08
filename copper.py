import pandas as pd

sl=3
amnt=100000

def func2(amnt):
    num=amnt/50
    num2=""
    num2=int(num)
    num3=str(num2)
    pnt=num3[:-3]
    num4=int(pnt)*1000
    return(num4)



import xlwt 
from xlwt import Workbook 
  

wb = Workbook() 
  
# create sheet. 
sheet1 = wb.add_sheet('Sheet 1')

def func1(value,column_number):
    
   
    for i in range(days):
        sheet1.write(i,column_number,value[i])
    wb.save('xlwt cp.xls')

file = 'copper_2018.xlsx'

x = pd.ExcelFile(file)

print(x.sheet_names)

df1 = x.parse('Sheet1')

open=[]
high=[]
low=[]
close=[]
p_close=[]
date=[]
gap_ud=[]
pnt=[]
temp=[]
temp1=[]
days=len(df1["Date"])-1
print(days)

for i in range(days):
    open.append(df1.round(2)['Open'][i])
    high.append(df1.round(2)['High'][i])   
    low.append(df1.round(2)['Low'][i])
    close.append(df1.round(2)['Close'][i])
    p_close.append(df1.round(2)['Previous Close'][i])
    date.append(df1.round(2)['Date'][i])
for i in range(days):
    temp.append(open[i].round(2)-p_close[i].round(2))
    temp1.append("%.2f"%temp[i])
    gap_ud.append(float(temp1[i]))
temp=[]
temp1=[]

#points calculation
for i in range(days):

    if gap_ud[i] > 0:
        if open[i] - low[i] > sl:
            temp.append(-sl)
        else:
            temp.append(close[i]-open[i])
        
    elif gap_ud[i] < 0:
        if open[i] - high[i] < -sl:
            temp.append(-sl)
        else:
            temp.append(open[i]-close[i])
        
    else:
        temp.append(0)
    temp1.append("%.2f"%temp[i])
    pnt.append(float(temp1[i]))

data=[]
data2=[]

for i in range(days):
    d_profit=0
    if amnt < 150000:
        d_profit=pnt[i]*2000
        data2.append(d_profit)
        amnt=int(amnt)+int(d_profit)
        print(amnt)
        data.append(amnt)
        continue
    d_profit=(int(func2(amnt))*pnt[i])
    data2.append(d_profit)
    amnt=int(amnt)+int(d_profit)
    data.append(amnt)
    print(int(amnt))

func1(gap_ud,0)
func1(pnt,1)
func1(data2,2)
func1(data,3)
