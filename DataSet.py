from xlrd import open_workbook
fi = open("ds.py", "w", encoding='utf8')
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
        BlessObj['Special'] = s.cell(row,3).value
        BlessObj['Picture'] = s.cell(row,4).value
        DS.append(BlessObj)

fi.write("DS = [")
s = ""
for i in range(len(DS)):
    s += str(DS[i])
    if i < len(DS)-1:
        s += ","
    else:
        s += "]"
fi.write(s)
fi.close()
