#

from poc_app.models import *

# Create Users
user_1 = CribUser.objects.create_user('archit', 'archit@crib.in', 'pass')
user_2 = CribUser.objects.create_user('anmol', 'anmol@crib.in', 'pass')
user_4 = CribUser.objects.create_user('sarthak', 'sarthak@crib.in', 'pass')

user_1.is_operator = True
user_2.is_operator = True
user_4.is_tenant = True
user_1.save()
user_2.save()
user_4.save()

# Create Operators
op1 = Operator()
op1.name = 'Archit'
op1.state = 'Noida'
op1.user = user_1
op1.save()

op2 = Operator()
op2.name = 'Anmol'
op2.state = 'Ghaziabad'
op2.user = user_2
op2.save()

t1 = Tenant()
t1.name = 'Sarthak'
t1.age = 26
t1.user = user_4
t1.operator = op1
t1.save()

# 86933b29171df09ebf66e4080a97e54f83af1f0d archit key
# 68f45eb78dc56efc9a89495e5c5d41941a334c8d sarthak key
# 240fcabdae8c8b5fd5ae62d87214f37e771e68db anmol key


############ ADDING GROUPS #############
from django.contrib.auth.models import Group
my_group = Group.objects.create(name='SpecialOperators')


from poc_app.models import Operator
op_user = Operator.objects.get(user__username='archit').user
op_user.groups.add(my_group)