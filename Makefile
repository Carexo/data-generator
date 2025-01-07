generate-all: generate-users generate-products generate-studies generate-courses generate-meetings generate-orders

generate-users:
	python3 -m users.users

generate-products:
	python3 -m products.products

generate-studies:
	python3 -m products.studies

generate-courses:
	python3 -m products.courses

generate-meetings:
	python3 -m products.meetings

generate-orders:
	python3 -m orders.orders
