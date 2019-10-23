frappe.ui.form.on("Customer", {
    "onload": function(frm, cdt, cdn) {
        console.log(frm.doc.name)
    }
})
