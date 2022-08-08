// Copyright (c) 2022, SOUL Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('District', {
	onload:function(frm)
    {
        frm.set_query("state", function() {
            return {
                filters: {
                    "country":frm.doc.country
                }
            };
        });
    }
});
