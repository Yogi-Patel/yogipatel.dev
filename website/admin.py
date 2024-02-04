from django.contrib import admin
from .models import Project, Skill, Image, Contact, Certifications

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    # The order of the objects in the admin is how it will show up on the website
    list_display = ('project_title', 'software_type', 'show_project', 'featured', 'start_date', 'end_date', 'priority')
    ordering = ['-featured', 'priority', '-end_date']
    list_editable = ['show_project', 'featured', 'priority']
    # ordering by -end_date means that the latest project will show up first

    search_fields = ['project_title', 'software_type']
    actions = ['priority_minus_one', 'priority_plus_one']

    def priority_minus_one(self, request, queryset):
        for skill in queryset:
            # Decrease the priority by 1
            skill.priority -= 1
            skill.save()

    def priority_plus_one(self, request, queryset):
        for skill in queryset:
            # Increase the priority by 1
            skill.priority += 1
            skill.save()



@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = ('skill_title', 'display_skill_type', 'priority')
    ordering = ['skill_type', 'priority'] # 1 will be the highest priority
    search_fields = ['skill_title', 'skill_type']
    actions = ['priority_minus_one', 'priority_plus_one']

    list_editable = ['priority']

    def priority_minus_one(self, request, queryset):
        for skill in queryset:
            # Decrease the priority by 1
            skill.priority -= 1
            skill.save()

    def priority_plus_one(self, request, queryset):
        for skill in queryset:
            # Increase the priority by 1
            skill.priority += 1
            skill.save()

    def display_skill_type(self, obj):
        # Get the skill type in a human readable form
        return obj.get_skill_type_display()
    display_skill_type.short_description = 'Skill Type'  # Set the custom column name here



@admin.register(Certifications)
class CertificationsAdmin(admin.ModelAdmin):

    list_display = ('certification_title', 'issued_on', 'expires_on', 'priority')
    ordering = ['priority'] # 1 will be the highest priority
    search_fields = ['certification_title']
    actions = ['priority_minus_one', 'priority_plus_one']

    list_editable = ['priority']

    def priority_minus_one(self, request, queryset):
        for certification in queryset:
            # Decrease the priority by 1
            certification.priority -= 1
            certification.save()

    def priority_plus_one(self, request, queryset):
        for certification in queryset:
            # Increase the priority by 1
            certification.priority += 1
            certification.save()



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = ('image_title', 'project', 'priority')
    ordering = ['project', 'priority']
    search_fields = ['project__project_title', 'image_title']
    actions = ['priority_minus_one', 'priority_plus_one']

    list_editable = ['priority']

    def priority_minus_one(self, request, queryset):
        for image in queryset:
            # Decrease the priority by 1 
            image.priority -= 1
            image.save()

    def priority_plus_one(self, request, queryset):
        for image in queryset:
            # Increase the priority by 1 
            image.priority += 1
            image.save()



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    search_fields = ['first_name', 'last_name', 'email']
    list_display = ('first_name', 'last_name', 'email')
    