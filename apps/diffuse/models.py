# from __future__ import unicode_literals
# from django.utils.datastructures import MultiValueDictKeyError
# from django.db import models
# import re
# import bcrypt
# from django import forms
# from django.utils.encoding import python_2_unicode_compatible
# from django.utils.translation import ugettext_lazy as _
#
# # Create your models here.
# class Game(models.Manager):
#     def registerVendor(self, postData):
#         results = {'status': True, 'errors': [], 'user': None}
#         if len(postData['vendor_name']) < 2:
#             results['status'] = False
#             results['errors'].append('Vendor Name Must be at Least 2 Character.')
#         if len(postData['vendor_address']) < 10:
#             results['status'] = False
#             results['errors'].append('Vendor Address Must be at Least 10 Characters.')
#         if len(postData['vendor_city']) < 1:
#             results['status'] = False
#             results['errors'].append('Vendor City Must be at Least 1 Characters.')
#         if len(postData['vendor_state']) < 1:
#             results['status'] = False
#             results['errors'].append('Vendor State Must be at Least 1 Characters.')
#         if len(postData['vendor_zip']) < 1:
#             results['status'] = False
#             results['errors'].append('Vendor Zip Code Must be at Least 1 Characters.')
#         if len(postData['vendor_phone']) < 8:
#             results['status'] = False
#             results['errors'].append('Vendor Phont Must be at Least 8 Characters.')
#
#         return results
#
#     def createVendor(self, postData, club_id):
#         user = Vendor.objects.create(
#             vendor_name=postData['vendor_name'],vendor_address=postData['vendor_address'],vendor_city=postData['vendor_city'],vendor_state=postData['vendor_state'],
#             vendor_zip=postData['vendor_zip'],vendor_phone=postData['vendor_phone'],vendor_fax=postData['vendor_fax'],vendorclub = Club.objects.get(id = club_id),
#             vendorclubid = club_id)
#         return user
#
# @python_2_unicode_compatible
# class Game(models.Model):
#     vendor_name = models.CharField(max_length=30)
#     vendor_address = models.CharField(max_length=100)
#     vendor_city = models.CharField(max_length=30)
#     vendor_state = models.CharField(max_length=30)
#     vendor_zip = models.IntegerField()
#     vendor_phone = models.CharField(max_length=30)
#     vendor_fax = models.CharField(max_length=30)
#     vendorclub = models.ForeignKey(Club, on_delete=models.CASCADE)
#     vendorclubid = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now = True)
#     objects = VendorManager()
#
#     def __str__(self):
#         return self.vendor_name
