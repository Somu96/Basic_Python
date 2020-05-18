import openpyxl

ci = openpyxl.load_workbook(filename = '/Users/sdeshnoo/desktop/B-P-2PI6POV_All.xlsx')
ci_sheet = ci.sheetnames
sheet1 = ci[ci_sheet[0]]
invoice_number = sheet1['I7'].value
print(invoice_number)
invoice_date = sheet1['H7'].value
flag = True
prod_details = []
prod_line = 32

print(sheet1[f'C{prod_line}'].value)

i = 0
while flag:
    print(sheet1[f'C{prod_line}'].value)
    if (sheet1[f'C{prod_line}'].value) == None:
        flag = False
    else:
        prod_details.append([(sheet1[f'C{prod_line}'].value), (sheet1[f'H{prod_line}'].value), (sheet1[f'I{prod_line}'].value), (sheet1[f'k{prod_line}'].value)])
        i+=1
        prod_line+= 1
    
print(prod_details)
     
