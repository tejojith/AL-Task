# digit
#123 - 6
#45 - 9
# 100 - 1
import pandas as pd



df = pd.read_csv('Data.csv')

log_file = open('log_file.csv', 'w')
log_file.write("Index,Original Value,Updated Value,Status\n")

for index,value in df['Value'].items():
    sum = 0
    
    try:
      
      initial = value
    
      if pd.isna(value):
         raise ValueError("Missing Value")

      value = int(value)
      while value > 0:
          num = value%10
          sum += num
          value = value//10
      df.at[index,'Result'] = int(sum)
      log_file.write(f'{index},{initial},{value},value changed\n')
    except Exception as e:
       log_file.write(f'{index},{initial},N/A,Value not applicable due to error: {str(e)}\n')
       

log_file.close()
df.to_csv('data.csv', index = False)



