# Python-and-SQL-Fooda-pipeline

Analysis Overview 
Popup customers visit a location inside their company or building to buy lunch, place their order directly with restaurant staff, pay for their order with cash or credit and their food is made to order on the spot. If you’re not familiar with how a Fooda Popup works, watch this video.

Your goal is to integrate customer orders data with line items generated by our Point of Sale to enable analysis
Accessing Data 

Our Popup customers buy from restaurants in person.

Orders are uniquely identified with an id from the 
event_finance_customer_orders table 

Successful orders have a null in the customer order deleted_at field; canceled orders (e.g. declined credit card) have a timestamp in the deleted_at field 

Each order has many associated line items representing food purchased, tax, discounts and payment method. See line_item_type on the line items table

Each order has one or many associated ‘food_sale’ line items representing sales

Each order has one or many associated ‘tax’ line items representing sales tax for each food item 

A customer order can optionally have a ‘food sale refund’ and ‘tax refund’ line items that represents the amount refunded amount

Gross Food Sales (GFS) is defined as the sum of all food sales plus tax, minus refunds

Orders can optionally have discount line items (of type: coupon, voucher, subsidy) associated but none are required 

Each order has one and only one payment line item type of ‘cash payment’ or ‘credit card payment’ 
Database Tables:
event_finance_customer_orders(Orders collected by Point of Sale),
event_finance_line_items(Customer orders are made up of a collection of line items),
event_finance_customer_order_line_items(Join table between line items & customer orders)

