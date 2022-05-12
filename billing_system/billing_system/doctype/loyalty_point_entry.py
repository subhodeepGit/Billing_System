import frappe
from billing_system.billing_system.notification.custom_notification import loyalty_program_expiry

def before_save(doc, method):
    loyalty_program_expiry(doc)