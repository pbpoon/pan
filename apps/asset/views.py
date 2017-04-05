from django.shortcuts import render
from django.views.generic import FormView
from account.forms import FileForm
from .models import Area, Category, LandNum
from  account.models import People
import xlrd
import decimal


class FileUploadView(FormView):
    template_name = 'account/file.html'
    form_class = FileForm

    def form_valid(self, form):
        f = form.files.get('file')
        if f:
            data = xlrd.open_workbook(file_contents=f.read())
            # table = data.sheet_by_name(by_name)
            table = data.sheets()[0]
            nrows = table.nrows  # 总行数
            colnames = table.row_values(0)  # 表头列名称数据
            print(colnames)
            list = []
            area = [Area(name=str(x)) for x in set(table.col_values(2, 1))]
            categroy = [Category(name=str(x)) for x in set(table.col_values(1, 1))]
            print(area)
            Area.objects.bulk_create(area)
            Category.objects.bulk_create(categroy)
            for rownum in range(1, nrows):
                row = table.row_values(rownum)

                for index, i in enumerate(range(len(colnames))):
                    if row:
                        if index == 0:
                            people =People.objects.all()
                            sname = str(row[i])
                            sname = sname[:1] + ' ' + sname[1:6]
                            if sname in people:
                                row[i] = people.get(first_name=sname[:1], last_name=sname[2:6])
                                row[99] = str(row[i])
                        elif index == 1:
                            row[i] = Category.objects.get(name=str(row[i]))
                        elif index == 2:
                            row[i] = Area.objects.get(name=str(row[i]))
                        elif index == 4:
                            row[i] = decimal.Decimal(row[i])
                        elif index == 6:
                            row[i] = row[5] + '--编辑备注:' + str(row[i])
                        else:
                            row[i] = str(row[i])

                if not LandNum.objects.filter(area=row[2], num=row[3]):
                    list.append(LandNum(area=row[2], num=row[3], fm=row[4], owner=row[0],
                                        old_owner=row[99], ps=row[6]))




                print(list)
                # account = row[10],
        # People.objects.bulk_create(list)