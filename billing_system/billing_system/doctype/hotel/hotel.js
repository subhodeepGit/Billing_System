// Copyright (c) 2022, SOUL Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('Hotel', {
	onload:function(frm)
    {
        frm.set_query("state", function() {
            return {
                filters: {
                    "country":frm.doc.country
                }
            };
        });
		frm.set_query("district", function() {
            return {
                filters: {
                    "state":frm.doc.state
                }
            };
        });
    }
});
