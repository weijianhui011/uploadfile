import xlrd
class XLDateinof(object):
    def __init__(self,path=''):
        self.xl = xlrd.open_workbook(path)

    def get_sheetinfo_by_name(self,name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheetinfo()

    def get_sheetinfo(self):
        infolist=[]
        for row in range(0,self.sheet.nrows):
            info = self.sheet.row_values(row)
            infolist.append(info)
        return infolist

if __name__=="__main__":
    datainfo= XLDateinof(r'F:\unitest\fileupload\test_data\get_params_headers_data.xlsx')
    alldata = datainfo.get_sheetinfo_by_name('TestData')
    print(alldata)