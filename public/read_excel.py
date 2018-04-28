import xlrd


class XLDateInfo(object):
    def __init__(self, path=''):
        self.xl = xlrd.open_workbook(path)
        self.sheet = None

    def get_sheet_info_by_name(self, name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheet_info()

    def get_sheet_info(self):
        infolist = []
        for row in range(0, self.sheet.nrows):
            info = self.sheet.row_values(row)
            infolist.append(info)
        return infolist


if __name__ == "__main__":
    data_info = XLDateInfo(r'..\test_data\get_params_headers_data.xlsx')
    all_data = data_info.get_sheet_info_by_name('TestData')
    print(all_data)
