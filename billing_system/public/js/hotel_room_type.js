frappe.ui.form.on('Hotel Room Type', {
    onload:function(frm)
    {
        frm.set_query('item', 'amenities', function() {
            return {
                filters: {
                    "item_group":frm.doc.item_group
                }
            };
        });
    }
});