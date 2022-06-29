frappe.ui.form.on('Restaurant Menu', {
    onload:function(frm)
    {
        frm.set_query('item', 'items', function() {
            return {
                filters: {
                    "item_group":frm.doc.item_group
                }
            };
        });
    }
});