from xlrd import open_workbook

DS = []

wb = open_workbook('DataSet.xlsx')
values = []
for s in wb.sheets():
    #print 'Sheet:',s.name
    num_of_col = s.ncols
    for row in range(s.nrows):
        BlessObj = {}
        BlessObj['Name'] = s.cell(row,0).value
        BlessObj['FirstBless'] = s.cell(row,1).value
        BlessObj['LastBless'] = s.cell(row, 2).value
        BlessObj['Category'] = s.cell(row,3).value
        BlessObj['Picture'] = 0
        DS.append(BlessObj)

#print (DS[0])
