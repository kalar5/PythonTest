import xlrd


# python对excel数据获取
def getTestdata(cel, raw):
    testData = xlrd.open_workbook('./data/test.xls')
    sheet = testData.sheet_by_name('Sheet1')
    value = sheet.cell(cel, raw).value
    print(value)
    return(value)
