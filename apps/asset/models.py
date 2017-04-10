from django.db import models
from django.db.models import Sum
from account.models import People


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
    desc = models.CharField('分类描述', max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = '区域名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_total_fm(self):
        return self.num.filter(is_del=False).aggregate(total_fm = Sum('fm'))


class LandNum(models.Model):
    owner = models.ManyToManyField('account.People',through='Owner', related_name='land_num', verbose_name='所有人')
    num = models.CharField('田地号码', max_length=10, db_index=True)
    category = models.ForeignKey('Category', null=True, blank=True, related_name='land_num', verbose_name='分类名称')
    fm = models.DecimalField('分亩', max_digits=5, decimal_places=2, null=False, help_text='单位为分岁')
    is_rent = models.BooleanField('是否出租', default=False)
    ps = models.CharField('备注信息', max_length=200,null=True, blank=True)
    desc = models.CharField('分类描述', max_length=60, null=True, blank=True)
    area = models.ForeignKey('Area', related_name='num', verbose_name='所属区域')
    is_del = models.BooleanField('注销', default=False)

    class Meta:
        verbose_name = '田地信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}{1}'.format(self.area, self.num)


class Owner(models.Model):
    owner = models.ForeignKey('account.People', on_delete=models.CASCADE, verbose_name='所属人')
    old_owner = models.ForeignKey('account.People', related_name='old_owner', verbose_name='原有人')
    num = models.ForeignKey('LandNum', on_delete=models.CASCADE, related_name='owner', verbose_name='田地号码')
    ps = models.TextField('备注信息', null=True, blank=True)
    create_d = models.DateField('添加日期', auto_now_add=True)
    update_d = models.DateTimeField('修改日期', auto_now=True)
    file = models.FileField('资料', upload_to='asset/land/Y%m%/', blank=True)

    class Meta:
        verbose_name = '原所属人田地明细'
        verbose_name_plural = verbose_name
        unique_together = ('owner', 'num')

    def __str__(self):
        # return self.owner.get_full_name
        return '{0} {1}'.format(self.old_owner, self.num)


class LandOwner(People):
    pass

    class Meta:
        verbose_name = '田地所属于人信息'
        verbose_name_plural = verbose_name
        proxy = True



