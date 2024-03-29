from . import __version__ as app_version

app_name = "billing_system"
app_title = "Billing System"
app_publisher = "SOUL Limited"
app_description = "Billing System"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "Soul@soul.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/billing_system/css/billing_system.css"
# app_include_js = "/assets/billing_system/js/billing_system.js"

# include js, css files in header of web template
# web_include_css = "/assets/billing_system/css/billing_system.css"
# web_include_js = "/assets/billing_system/js/billing_system.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "billing_system/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Hotel Room Package" : "public/js/hotel_room_package.js",
	"Hotel Room Pricing" : "public/js/hotel_room_pricing.js",
	"Hotel Room Reservation" : "public/js/hotel_room_reservation.js",
	"Hotel Room Type" : "public/js/hotel_room_type.js",
	"Restaurant Menu" : "public/js/restaurant_menu.js"
	}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "billing_system.install.before_install"
# after_install = "billing_system.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "billing_system.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Loyalty Point Entry": {
		"before_save": "billing_system.billing_system.doctype.loyalty_point_entry.before_save"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	# "all": [
# 	# 	"billing_system.tasks.all"
# 	# ],
# 	# "daily": [
# 	# 	"billing_system.tasks.daily"
# 	# ],
# 	# "hourly": [
# 	# 	"billing_system.tasks.hourly"
# 	# ],
# 	# "weekly": [
# 	# 	"billing_system.tasks.weekly"
# 	# ]
# 	"monthly": [
# 		"billing_system.scheduled_tasks.loyalty_program_expiry"
# 	]
# }

# Testing
# -------

# before_tests = "billing_system.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "billing_system.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "billing_system.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"billing_system.auth.validate"
# ]

# fixtures = [
# 	{"dt": "Warehouse"},
# 	{"dt": "Account"},
#
# ]
