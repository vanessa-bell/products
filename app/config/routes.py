from system.core.router import routes
routes['/products'] = 'Products#index'
routes['/products/new'] = 'Products#new'
routes['POST']['/products/create'] = 'Products#create'
routes['/products/edit/<id>'] = 'Products#edit'
routes['/products/show/<id>'] = 'Products#show'
routes['POST']['/products/destroy/<id>'] = 'Products#destroy'
routes['POST']['/products/update/<id>'] = 'Products#update'

