// Copyright (c) 2022, SOUL Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sales Bill',
{
// 	// validate:function(frm) {
// 	// 	let num = frm.doc.customer_number;
// 	// 	let num1 = num.toString();
// 	// 	if (num1.length != 10)
// 	// 	{
// 	// 		frappe.throw('Enter valid Phone Number');
// 	// 		frappe.validated = false;
// 	// 	}
// 	}items_list
});
frappe.ui.form.on('Item List',"quantity", function(frm,cdt,cdn){
    var item=locals[cdt][cdn]
    if(item.item_price>0){
        item.item_price==" " && item.quantity ==" "
        item.total_price=item.item_price*item.quantity
    }
    else{
        frappe.throw("Please Enter the Valid Data");
    }
    cur_frm.refresh_field("items_list");
})