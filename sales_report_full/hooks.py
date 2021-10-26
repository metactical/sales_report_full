# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sales_report_full"
app_title = "Sales Report Full"
app_publisher = "Techlift"
app_description = "Sales Report Full"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "palash@techlift.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/css/sales_report_full.css"
# app_include_js = "/assets/sales_report_full/js/sales_report_full.js"

# include js, css files in header of web template
# web_include_css = "/assets/sales_report_full/css/sales_report_full.css"
# web_include_js = "/assets/sales_report_full/js/sales_report_full.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
#doctype_js = {
#    "Packing Slip" : "public/js/packing_slip.js"
#    }
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

# Website user home page (by function)
# get_website_user_home_page = "sales_report_full.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sales_report_full.install.before_install"
# after_install = "sales_report_full.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sales_report_full.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sales_report_full.tasks.all"
# 	],
# 	"daily": [
# 		"sales_report_full.tasks.daily"
# 	],
# 	"hourly": [
# 		"sales_report_full.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sales_report_full.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sales_report_full.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sales_report_full.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sales_report_full.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sales_report_full.task.get_dashboard_data"
# }

fixtures = [{
    "dt": "Custom Field",
    "filters": [["name", "in", [
        'Packing Slip-item_barcode',
        'Packing Slip Item-scanned_qty'
    ]]]
}]
