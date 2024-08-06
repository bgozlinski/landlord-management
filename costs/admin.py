from django.contrib import admin
from costs.models import Cost


class CostAdmin(admin.ModelAdmin):
    list_display = ('flat', 'cost_type', 'amount', 'invoice_number', 'invoice_date', 'cost_date_to_pay', 'cost_is_paid')
    list_filter = ('cost_is_paid', 'cost_type', 'invoice_date', 'cost_date_to_pay')
    search_fields = ('flat__city_name', 'flat__street_name', 'invoice_number')
    ordering = ('flat', 'cost_date_to_pay')
    readonly_fields = ('invoice_number', 'invoice_date')

    def cost_is_paid(self, obj):
        return obj.cost_is_paid
    cost_is_paid.boolean = True  # Display as a green checkmark


admin.site.register(Cost, CostAdmin)
