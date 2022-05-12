from re import L
import frappe
from frappe.utils.data import format_date
from frappe.utils import get_url_to_form
from frappe.utils import cint, cstr, parse_addr

def loyalty_program_expiry(doc):
    msg="""<p>Thank You for SHopping with us. Your Loyalty points details are:</p><br>"""
    msg+="""<b>Loyalty Points:</b> {0}<br>""".format(doc.get('loyalty_points'))
    msg+="""<b>Purchase Amount:</b> {0}<br>""".format(doc.get('purchase_amount'))
    msg+="""<b>Expiry date:</b> {0}<br>""".format(doc.get('expiry_date'))
    # send_mail(frappe.db.get_value("Student",doc.get('student'),"student_email_id"),'Application status',msg)
    send_mail(frappe.db.get_value("Customer",doc.get('customer'),"email_id"),'Loyalty Point Entry',msg)

def send_mail(recipients,subject,message):
    if has_default_email_acc():
        frappe.sendmail(recipients=recipients,subject=subject,message = message)
    
def has_default_email_acc():
    for d in frappe.get_all("Email Account", {"default_outgoing":1}):
       return "true"
    return ""