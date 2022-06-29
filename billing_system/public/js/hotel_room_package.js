frappe.ui.form.on('Hotel Room Package', {
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