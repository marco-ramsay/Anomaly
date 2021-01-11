from django.db import models

# Create your models here.

class Project(models.Model):
    client = models.CharField(max_length=200, null=True)
    logo = models.FileField(blank=True)
    location = models.CharField(max_length=200, null=True)
    vessel = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.client

class Anomaly(models.Model):
    TYPE = (('AW', 'AW'),('DB', 'DB'),)
    STATUS = (('Client_signed', 'Client_signed'),('Not_Signed', 'Not_Signed'),)
    HIST = (('Yes', 'Yes'), ('No', 'No'),)
    CRIT = (('Select', 'Select'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'),)
    REF = (('N/A', 'N/A'), ('Hist-001', 'Hist-001'), ('Hist-001', 'Hist-001'),)
    client = models.ForeignKey(Project, null=True, on_delete= models.CASCADE)
    asset = models.CharField(max_length=200, null=True)
    component = models.CharField(max_length=200, null=True)
    sub_component = models.CharField(max_length=200, null=True)
    anomaly_id = models.CharField(max_length=200, null=True)
    criticality = models.CharField(max_length=200, default='Select', choices=CRIT)
    code = models.CharField(max_length=200, null=True, choices=TYPE)
    DateTime = models.DateTimeField(null=True)
    is_hist = models.CharField(max_length=200, default='No', choices=HIST)
    hist_ref = models.CharField(max_length=200, default='N/A', choices=REF)
    comments = models.TextField(null=True)
    review_status = models.CharField(max_length=200, default='Not_Signed', choices=STATUS)
    pdf_upload = models.FileField(null=True)
    inspector = models.CharField(max_length=200, null=True)
    coord = models.CharField(max_length=200, null=True)
    obcr = models.CharField(max_length=200, null=True)
    image_1 = models.FileField( null=True)
    image_1_description = models.CharField(max_length=200, default='Image_1', blank=True)
    image_2 = models.FileField( null=True)
    image_2_description = models.CharField(max_length=200, default='Image_2', blank=True)
    video = models.FileField( null=True)
    video_description = models.CharField(max_length=200, default='Anomaly Video', blank=True)


    def __str__(self):
        return self.anomaly_id




# class Customer(models.Model):
# 	name = models.CharField(max_length=200, null=True)
# 	phone = models.CharField(max_length=200, null=True)
# 	email = models.CharField(max_length=200, null=True)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)
#
# 	def __str__(self):
# 		return self.name
#
#
# class Tag(models.Model):
# 	name = models.CharField(max_length=200, null=True)
#
# 	def __str__(self):
# 		return self.name
#
# class Product(models.Model):
# 	CATEGORY = (
# 			('Indoor', 'Indoor'),
# 			('Out Door', 'Out Door'),
# 			)
#
# 	name = models.CharField(max_length=200, null=True)
# 	price = models.FloatField(null=True)
# 	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
# 	description = models.CharField(max_length=200, null=True, blank=True)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)
# 	tags = models.ManyToManyField(Tag)
#
# 	def __str__(self):
# 		return self.name
#
# class Order(models.Model):
# 	STATUS = (
# 			('Pending', 'Pending'),
# 			('Out for delivery', 'Out for delivery'),
# 			('Delivered', 'Delivered'),
# 			)
#
# 	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
# 	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)
# 	status = models.CharField(max_length=200, null=True, choices=STATUS)
