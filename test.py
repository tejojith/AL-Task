# digit
#123 - 6
#45 - 9
# 100 - 1
import pandas as pd
import math


df = pd.read_csv('data.csv')

log_file = open('log_file.csv', 'w')
log_file.write("Index,Original Value,Updated Value,Status\n")

def calculate_sum(value):
  sum = 0
  value = int(value)
  while value > 0:
    num = value%10
    sum += num
    value = value//10

  return sum
    
## have to caluculate sum for decimal as well as expenonetial values
for index,value in df['Value'].items():
    
       
    try:
      
      initial = value
    
      if pd.isna(value):
         raise ValueError("Missing Value")


      if value[:3] == 'exp':
        value = math.exp(int(value[4:-1]))
        
        
    
      if '.' in str(value):
        sum = 0
        
        list = str(value).split('.')
        
        first = int(list[0])
        second = int(list[1])
        sum = calculate_sum(first)
        sum += calculate_sum(second)


      else:
        sum = calculate_sum(value)
      
      df.at[index,'Result'] = int(sum)
      log_file.write(f'{index},{initial},{int(sum)},value changed\n')
    except Exception as e:
       log_file.write(f'{index},{initial},N/A,Value not applicable due to error: {str(e)}\n')
       

log_file.close()
df.to_csv('data.csv', index = False)



