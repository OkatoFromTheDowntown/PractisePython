import os
import openpyxl


class Cooker:
    def src(self, path):
        self.wb = openpyxl.load_workbook(path)
        self.ws = self.wb.sheetnames
        self.file = os.path.basename(path)
        return self

    def getWorkBook(self):
        return self.wb if self.wb else ''

    def getSheets(self):
        return self.ws if self.ws else ''

    def pipe(self, task):
        if self.getWorkBook():
            task(self)
        return self

    def save(self, dest=r'./tmp/'):
        if self.getWorkBook():
            self.wb.save(dest + self.file)
        return self


def test():
    cooker = Cooker()

    def print_workbookname(obj: Cooker):
        print('WorkBook: ' + obj.getWorkBook())

    def print_worksheets(obj: Cooker):
        for sheet in obj.getSheets():
            print('Sheet: ' + sheet)

    cooker.src(r'./test.xlsx').pipe(
        print_workbookname).pipe(print_worksheets).save(r'/dev/null')


if __name__ == '__main__':
    test()
