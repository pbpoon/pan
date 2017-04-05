from django.shortcuts import render
from django.views.generic import FormView
from account.forms import FileForm
from .models import Area, Category, LandNum, Owner
from account.models import People
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
            list2 = []
            area = [Area(name=str(x)) for x in set(table.col_values(2, 1))]
            categroy = [Category(name=str(x)) for x in set(table.col_values(1, 1))]
            # print(area)
            # Area.objects.bulk_create(area)
            # Category.objects.bulk_create(categroy)
            for rownum in range(1, nrows):
                row = table.row_values(rownum)

                for index, i in enumerate(range(len(colnames))):
                    if row:
                        if index == 0:
                            people = People.objects.all()
                            sname = str(row[i])
                            if people.filter(first_name=sname[:1], last_name=sname[1:6]).exists():
                                row[i] = people.get(first_name=sname[:1], last_name=sname[1:6])
                            else:
                                row[i] = ''
                            row[7] = str(row[i])
                        elif index == 1:
                            row[i] = Category.objects.get(name=str(row[i]))
                        elif index == 2:
                            row[i] = Area.objects.get(name=str(row[i]))
                        elif index == 4:
                            row[i] = decimal.Decimal(row[i])
                        elif index == 6:
                            if row[i]:
                                row[i] = row[5] + '--编辑备注:' + str(row[i])
                            else:
                                row[i] = row[5]
                        else:
                            row[i] = str(row[i])


                # if not LandNum.objects.filter(area=row[2], num=row[3]):
                land = LandNum(area=row[2], num=row[3], category=row[1], fm=row[4], ps=row[6])
                land.save()
                owner = Owner(owner=row[0], old_owner=row[7], num=land, ps=row[6])
                owner.save()



            print('OK')
                # account = row[10],
        # People.objects.bulk_create(list)