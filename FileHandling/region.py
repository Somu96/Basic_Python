import openpyxl

geo_x6 = openpyxl.load_workbook(filename = '/Users/sdeshnoo/desktop/X6 Count in all Geos.xlsx')
sheet1 = geo_x6.sheetnames
s1 = geo_x6[sheet1[0]]
print(s1["A3"].value)
col1 = s1['A']
col2 = s1['B']
ref_list = [col1, col2]
value_list=[]

for a in ref_list:
      temp_list =[]
      for b in a:
            temp_list.append(b.value)
      value_list.append(temp_list)
#print(value_list)

len1 = len(value_list)
j = 0
result_dict = {}
am_value = 0
ap_value = 0
emea_value = 0
con_list = ['NAW', 'NAE', 'LA']
print(value_list)

for j, a in enumerate(value_list[0]):
    #print ("j:{}".format(j))
    if a == 'TERRITORY':
        continue

    if a in con_list:
        am_value = am_value + value_list[1][j]
        result_dict.update({'Americas' : am_value})
    else:
         if result_dict.get(a):
            # print ("a:{}, old_value:{}, new_value:{}".format(a, result_dict.get(a), value_list[1][j]))
             val = result_dict.get(a) + value_list[1][j]
         else:
            # print("from else")
             val = value_list[1][j]

         result_dict.update({a:val})

print(result_dict)


      
'''for a in value_list[0]:
      if a == 'TERRITORY':
            j+=1
            continue
      
      if a in con_list:
            am_value = am_value + value_list[1][j]
            result_dict.update({'Americas' : am_value})
      elif a == 'AP' :
            ap_value = ap_value + value_list[1][j]
      else:
            emea_value = ap_value + value_list[1][j]
      j+=1
result_dict.update({'AP' : ap_value})
result_dict.update({'EMEA' : am_value})
print(result_dict)'''
