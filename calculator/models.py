from django.db import models

# Create your models 
class Enroller(models.Model):
   name= models.CharField(max_length=50)
   address=models.TextField()
   pincode=models.CharField(max_length=50)
   mobile=models.CharField(max_length=50)
   email=models.CharField(max_length=50)
   
   adhar_card = models.FileField(upload_to='calculator/upload_file/adhar/')
   pan_card = models.FileField(upload_to='calculator/upload_file/pan')

   # adhar_card=models.FileField()
   # pan_card=models.FileField()
   loan_amount=models.IntegerField()
   tenure=models.IntegerField() 
   intrest_rate=models.DecimalField(max_digits=7,decimal_places=2) 




   
# Monthly Home Loan EMI
# ₹19,668
# View Details
# Principal Amount
# ₹25,00,000
# Interest Amount
# ₹45,80,304
# Total Amount Payable
# ₹70,80,304
# Need more information?