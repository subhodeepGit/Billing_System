# Copyright (c) 2022, SOUL Limited and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import flt
class SalesBill(Document):
	def validate(self):
		self.calculate_total()
	def calculate_total(self):
		total_price=0
		for item in self.get("items_list"):
			total_price+=flt(item.total_price)
		self.grand_total=total_price