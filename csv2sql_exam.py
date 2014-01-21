#!/usr/bin/python
# -*- coding: utf-8 -*-
# CSV to SQL
# created date : 2014-01-16

# TODO : 모듈화가 좀 ... 

# Input [ csv file ] -> output [sql]

def date_type_to_sql(date_string_with_bar):
    output = date_string_with_bar.replace('|', '-')

    if output.startswith('0000-00-00'):
        return 'null'
    return output


def sql_header(file):
    file.write('BEGIN TRY \n')
    file.write('BEGIN TRAN \n\n')
    
def sql_footer(file):
    file.write('COMMIT TRAN \n')
    file.write('END TRY \n')
    file.write("BEGIN CATCH \n")
    file.write("    IF @@TRANCOUNT > 0 \n")
    file.write("         ROLLBACK TRAN \n")
    file.write("    SELECT 'Error', error_number(), error_state(), error_message() \n")
    file.write("END CATCH \n\n")
    

class CsvModel :
    taffy_gamble_idx = 0
    begin_date = ''
    end_date = ''
    
    def toSQL(self):
        print ('test')
        
    

import sys
import os

table_name = 'ResTblTaffyGamble'
 
csv_file_name = 'TaffyPremiumGiftTable.csv'
file_name = csv_file_name.rsplit('.', 1)[0]
sql_file_name = file_name + '.sql'


raw = []
# read csv
import csv
with open(csv_file_name, newline='', encoding='utf-8') as csvfile:
   reader = csv.reader(csvfile, delimiter=',')   # , quotechar=','
   for row in reader:
       raw.append([reader.line_num-1, row]);

# remove header
del raw[0]


# save
sql_file = open(sql_file_name, 'w')

sql_header(sql_file)
sql_file.write('DELETE FROM ' + table_name + ' \n')

for row in raw:
    seq = row[0]
    cols = row[1]

    # output
    taffy_gamble_idx = cols[0]
    begin_date = date_type_to_sql(cols[1])
    end_date = date_type_to_sql(cols[2])
    
    print ("%s = %s ~ %s" % (taffy_gamble_idx , begin_date , end_date))

    sql = "INSERT INTO " + table_name + " VALUES ("
    # values
    sql += taffy_gamble_idx + ","

    if 'null' == begin_date:
        sql += "null,"
    else:
#        sql += "CONVERT(NVARCHAR(32), '" + begin_date + "', 23), "
        sql += "CONVERT(NVARCHAR(24), \'" + begin_date + " \'+ CAST(dbo.FN_GACHA_RESET_HOUR() as NVARCHAR(2)) + \':00:00\', 120),"

    if 'null' == end_date:
        sql += "null"
    else:
#        sql += "CONVERT(NVARCHAR(32), '" + end_date + "', 23) "
        sql += "CONVERT(NVARCHAR(24), \'" + end_date + " \'+ CAST(dbo.FN_GACHA_RESET_HOUR() as NVARCHAR(2)) + \':00:00\', 120)"        
        

    for col_num in range(3,9):
        if col_num in [4,5]:
            sql +=  ",\'" + cols[col_num] + '\''            
        else:
            sql +=  ", " + cols[col_num]

    #sql += cols[4] + ", "
    #sql += cols[5] + ", "
    #sql += cols[6] + ", "
    #sql += cols[7] + ", "    
    sql += ") \n"

        
    sql_file.write(sql)    

sql_footer(sql_file)
sql_file.close()



input("Press any key.")
