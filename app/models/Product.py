from system.core.model import Model
import re

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()
   
    def get_products(self):
        query = "SELECT * from products"
        return self.db.query_db(query)

    def get_product(self,id):
        query = "SELECT * from products where id = :id"
        data = {'id': id}
        return self.db.get_one(query, data)

    def add_product(self,info,methods='POST'):
    	PRICE_REGEX = re.compile(r'^\d{0,8}(\.\d{1,4})?$')
    	errors = []
    	if not info['price']:
    		errors.append('Price cannot be blank')
    	elif not PRICE_REGEX.match(info['price']):
    		errors.append('Price can only be numbers')
    	if errors:
    		return {'status': False, 'errors':errors}
    	else:
	        sql = "INSERT into products (name, description, price, created_at, updated_at) values(:name, :description, :price, NOW(), NOW())"
	        data = {'name': info['name'], 'description': info['description'], 'price': info['price']}
	        products = self.db.query_db(sql, data)
	        return {'status': True}

    def update_product(self,id,info,methods="POST"):
    	query = "UPDATE products SET name=:name, description=:description, price=:price, updated_at=NOW() WHERE id=:id"
    	values = {
    			"name": info['name'],
    			"description": info['description'],
    			"price": info['price'],
    			"id":id
    	}
    	return self.db.query_db(query,values)

    def delete_product(self,id):
    	query = "DELETE from products WHERE id=:id"
    	data = {'id':id}
    	return self.db.query_db(query,data)
