frappe.ui.form.on('Hotel Room Pricing', {
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
