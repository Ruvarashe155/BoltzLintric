from django.contrib import admin

# Register your models here.

from .models import (
    Service,
    Project,
    Testimonial,
    TeamMember,
    ContactMessage,
    SiteStatistic
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_active',
        'created_at',
    )
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'is_featured',
        'created_at',
    )
    list_filter = (
        'category',
        'is_featured',
    )
    search_fields = (
        'title',
        'client',
        'description',
    )
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'company',
        'is_active',
        'created_at',
    )
    list_filter = ('is_active',)
    search_fields = (
        'name',
        'company',
        'message',
    )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'position',
        'is_active',
    )
    list_filter = ('is_active',)
    search_fields = (
        'name',
        'position',
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'subject',
        'is_read',
        'created_at',
    )

    list_filter = (
        'is_read',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'subject',
        'message',
    )

    readonly_fields = (
        'created_at',
    )

    list_editable = (
        'is_read',
    )

@admin.register(SiteStatistic)
class SiteStatisticAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'label',
        'order',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'value',
        'label',
    )

    list_editable = (
        'order',
        'is_active',
    )
