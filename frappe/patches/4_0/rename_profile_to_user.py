import frappe

from frappe.model import rename_field

def execute():
	tables = frappe.db.sql_list("show tables")
	if "tabUser" not in tables:
		frappe.rename_doc("DocType", "Profile", "User", force=True)

	if frappe.db.exists("DocType", "Website Route Permission"):
		frappe.reload_doc("website", "doctype", "website_route_permission")
		rename_field("Website Route Permission", "profile", "user")
	frappe.reload_doc("website", "doctype", "blogger")
	rename_field("Blogger", "profile", "user")
