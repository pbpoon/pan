from django.db import models
from django.db.models import Sum


class WaterNum(models.Model):
    account = models.ForeignKey('account.Account', related_name='water_num', verbose_name='所属户号')
    desc = models.CharField('描述', max_length=28, null=True, blank=True)
    create_d = models.DateTimeField('录入日期', auto_now_add=True)
    update_d = models.DateTimeField('修改日期', auto_now=True)
    is_del =models.BooleanField('是否注销', default=False)

    class Meta:
        verbose_name = '水表号'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1}):({2})'.format(self.account, self.desc, self.rate.latest('mark_date'))


class WaterRate(models.Model):
    WaterNum = models.ForeignKey('WaterNum', related_name='rate', verbose_name='水表号码')
    mark_d = models.ForeignKey('CenterWater', related_name='account_rate', verbose_name='抄表日期')
    m3 = models.DecimalField('用水数量', max_digits=9, decimal_places=2)
    ps = models.CharField('备注信息', max_length=200, null=True, blank=True)
    is_pay = models.BooleanField('已缴费', default=False)
    create_d = models.DateTimeField('录入日期', auto_now_add=True)
    update_d = models.DateTimeField('修改日期', auto_now=True)

    class Meta:
        verbose_name = '水费'
        verbose_name_plural = verbose_name

    def get_total_price(self):
        return self.m3 * self.mark_d.real_price()


class CenterWater(models.Model):
    mark_d = models.DateField('抄表日期', auto_now_add=True)
    m3 = models.DecimalField('用水数量', max_digits=9, decimal_places=2)
    ps = models.CharField('备注信息', max_length=200, null=True, blank=True)
    price = models.DecimalField('单价', max_digits=5, decimal_places=2, default=3.6, help_text='水费单价，默认是3.6元/m3')
    is_pay = models.BooleanField('已缴费', default=False)

    class Meta:
        verbose_name = '总表信息'
        verbose_name_plural = verbose_name
        get_latest_by = 'mark_d'
        ordering = ['-mark_d']

    def get_total_rate(self):
        return self.m3 * self.price

    def get_total_account_m3(self):
        return self.account_rate.aggregate(total_account_m3 =Sum('m3'))

    def get_balance_m3(self):
        return self.m3 - self.get_total_account_m3()

    def real_price(self):
        return self.get_total_rate() / self.get_total_account_m3()

    def __str__(self):
        return '{0}:{0}'.format(self.mark_d, self.m3)