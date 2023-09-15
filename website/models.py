from django.db import models
from django.template.defaultfilters import slugify 

# Create your models here.

class Project(models.Model):
    # Model for storing Projects for /index and /portfolio
    
    project_title = models.CharField(max_length=75, help_text="MAX_LENGTH = 75", verbose_name="Project Title")

    start_date = models.DateField(verbose_name="Start Date")

    end_date = models.DateField(verbose_name="End Date")

    software_type = models.CharField(max_length = 50, help_text = "MAX_LENGTH = 50", verbose_name="Software Type")

    technologies_used = models.CharField(max_length = 150, help_text = "MAX_LENGTH = 150", verbose_name="Technologies Used")

    short_description = models.CharField(max_length = 150, help_text = "Try to reach 125 characters for uniform card sizes. MAX_LENGTH = 150", verbose_name="Short Description")

    long_description = models.TextField(verbose_name="Long Description")

    code_url = models.URLField(max_length = 300, blank = True, null = True, help_text = "Optional. MAX_LENGTH = 300", verbose_name="Code URL")

    deployment_url = models.URLField(max_length = 300, blank = True, null = True, help_text = "Optional. MAX_LENGTH = 300", verbose_name="Deployment URL")

    slug = models.SlugField(max_length = 150, blank = True, null = True, help_text = "Optional. MAX_LENGTH = 150", verbose_name="Slug")
    

    def __str__(self):
        return f"{self.project_title}"

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.project_title)
        return super().save(*args, **kwargs)
    
    
    


class Skill(models.Model):
    # Model for storing skills on the /about page 
    
    SKILL_TYPES = [
        #(<value_to_be_set_in_db>, <human_readable_representation),
        (1, "Programming Language"),
        (2, "Programming Framework"),
        (3, "Tool"),
        (4, "Other"),
    ]

    
    icon = models.ImageField(upload_to="skill_icons", verbose_name="Icon")
    
    skill_title = models.CharField(max_length=50, help_text="MAX_LENGTH = 50" , verbose_name="Skill Title")
    
    skill_description = models.CharField(max_length=75, help_text="MAX_LENGTH = 75", verbose_name="Skill Description")
    
    skill_type = models.IntegerField(choices=SKILL_TYPES, help_text="Skill type decides which one to show first", verbose_name="Skill Type")

    priority = models.IntegerField(help_text="Enter an Integer", verbose_name="Priority")


    def __str__(self):
        return f"Skill: {self.skill_title} | Priority: {self.priority}"
    




class Image(models.Model):
    # Model for storing Images for the Project Model in a Many-to-One relation 

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images", verbose_name="Project")
    
    image = models.ImageField(upload_to="project_images", verbose_name="Image")
    
    image_title = models.CharField(max_length=150, help_text="MAX_LENGTH = 150", verbose_name="Image Title") 
    
    slug = models.SlugField(max_length=150, blank=True, null=True, help_text="Optional. MAX_LENGTH = 150", verbose_name="Slug")
    
    priority = models.IntegerField(help_text="Enter an Integer", verbose_name="Priority")


    def __str__(self):
        return f"Image: {self.image_title} | Project: {self.project.project_title} | Priority: {self.priority}"

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.image_title)
        return super().save(*args, **kwargs)
    




class Contact(models.Model):
    # Model for storing all the submissions made using the /contact form 

    first_name = models.CharField(max_length = 150, verbose_name="First Name")

    last_name = models.CharField(max_length = 150, blank=True, null=True, help_text="Optional.", verbose_name="Last Name")

    email = models.EmailField(verbose_name="E-mail")

    subject = models.CharField(max_length = 150, blank=True, null=True, help_text="Optional.", verbose_name="Subject")

    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name} | e-mail: {self.email}"
    
