--3. Average GFS Dollar amount for successful orders(Deleted_at is null on Customer Orders table)
select avg(Dollars)
from 
(
select sum(case when (line_item_type = 'food_sale') then amount_cents
			  when (line_item_type = 'tax') then amount_cents
			  when (line_item_type = 'tax_refund') then -1*(abs(amount_cents))
			  when (line_item_type = 'food_sale_refund') then -1*(abs(amount_cents)) else 0 end) / 100 as Dollars
		   from event_finance_line_items efli
		   inner join event_finance_customer_order_line_items efcoli on efcoli.line_item_id = efli.id
		   inner join event_finance_customer_orders efco on efcoli.customer_order_id = efco.id
		   where efco.deleted_at is null
		   group by efco.id
) as inner_query


--4. Percentage of Online and Offline Successful orders
select (cast(sum(case when transacted_offline = false then 1 end) AS Float) / cast((select count(*) from event_finance_customer_orders where deleted_at is null) AS Float)) * 100 AS Percentage_of_online_orders,
(cast(sum(case when transacted_offline = true then 1 end) AS Float) / cast((select count(*) from event_finance_customer_orders where deleted_at is null) AS Float)) * 100 AS Percentage_of_offline_orders
from event_finance_customer_orders
where deleted_at is null