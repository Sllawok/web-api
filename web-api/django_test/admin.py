from rest_framework.authtoken.admin import TokenAdmin

admin.site.register(Token)

TokenAdmin.raw_id_fields = ['user']