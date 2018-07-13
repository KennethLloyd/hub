import frappe

def get_context(context):
    name = frappe.local.request.args['name']
    items = frappe.get_all('Hub Item', fields=['*'], filters={'name': name})
    if len(items) == 0:
        raise frappe.DoesNotExistError()
    context.item = items[0]
    context.title = context.item.name
    context.no_breadcrumbs = False
    categories = frappe.get_all('Hub Category', filters={'name': context.item.hub_category}, fields=['*'])
    category = categories[0]
    context.parents = [{"name": "All categories", "route": "/item-listing/"}, {"name": category.parent_hub_category}, {"name": category.name, "route": "/category-products/?category_name=%s" % (category.name)}]
