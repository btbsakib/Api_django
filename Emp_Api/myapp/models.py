from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=30)
    position = models.CharField(max_length=100)
    hiring_date = models.DateField(default='2021-01-01')
    description=models.CharField(max_length=500,default='',blank=True)

    def __str__(self):
        return self.first_name
    
class LeaveRequest(models.Model):

    employee = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='leaverequests') 
    start_date = models.DateField(max_length=50, blank=True, default='')
    end_date = models.DateField(max_length=50, blank=True, default='')
    #attachment_url = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=25,choices=(('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')))


    def __str__(self):

        return f"Leave request for {self.employee} - {self.start_date} to {self.end_date}"
    
 
