"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('Product')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        products = self.models['Product'].get_products()
        return self.load_view('index.html', products=products)

    def new(self):
        return self.load_view('add.html')

    def edit(self,id,methods='POST'):
    	product = self.models['Product'].get_product(id)
    	return self.load_view('edit.html',name=product['name'], description=product['description'], price=product['price'], id=product['id'])

    def show(self, id):
    	product = self.models['Product'].get_product(id)
    	print product
    	return self.load_view('show.html',name=product['name'], description=product['description'], price=product['price'], id=product['id'])

    def create(self,methods='POST'):
    	info = request.form
    	create_status = self.models['Product'].add_product(info)
    	if create_status['status'] == True:
    		flash("Successfully added a product!","success")
    		return redirect('/products')
    	else:
    		for message in create_status['errors']:
    			flash(message, 'error')
    		return redirect('/products/new')

    def destroy(self,id, methods='POST'):
    	product = self.models['Product'].delete_product(id)
    	flash("You successfully removed product #" + id,'success')
    	return redirect('/products')

    def update(self,id,methods='POST'):
    	info = request.form
    	self.models['Product'].update_product(id,info)
    	id=id
    	return redirect('/products/show/'+ id)

