from django.db import models
from django.db.models import Sum, Avg


class Category(models.Model):

    name = models.CharField('分类名称', max_length=20, db_index=True)
    desc = models.CharField('分类描述', max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = '分类名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField('区域名称', max_length=20, db_index=True)
    category = models.ForeignKey('Category', related_name='area', verbose_name='分类名称')
    desc = models.CharField('分类描述', max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = '区域名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_total_fm(self):
        return self.num.filter(is_del=False).aggregate(total_fm = Sum('fm'))


class LandNum(models.Model):
    num = models.CharField('田地号码', max_length=10, db_index=True)
    fm = models.DecimalField('分亩', max_digits=5, decimal_places=2, null=False, help_text='单位为分岁')
    is_rent = models.BooleanField('是否出租', default=False)
    ps = models.TextField('备注信息', null=True, blank=True)
    desc = models.CharField('分类描述', max_length=60, null=True, blank=True)
    area = models.ForeignKey('Area', related_name='num', verbose_name='所属区域')
    is_del = models.BooleanField('注销', default=False)
    file = models.FileField('资料', upload_to='asset/land/Y%m%/')

    class Meta:
        verbose_name = '田地信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}{}'.format(self.area, self.num)


class Owner(models.Model):
    land_num = models.ForeignKey('LandNum', related_name='owner', verbose_name='田地号码')
    owner = models.ForeignKey('account.People', related_name='land', verbose_name='所属人')
    old_owner = models.CharField('原所属人', max_length=50, null=True, blank=True)
    ps = models.CharField('备注信息', max_length=200, null=True, blank=True)
    create_d = models.DateField('添加日期', auto_now_add=True)
    update_d = models.DateTimeField('修改日期', auto_now=True)

    class Meta:
        verbose_name = '田地原所属人信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}{}'.format(self.owner, self.land_num)



