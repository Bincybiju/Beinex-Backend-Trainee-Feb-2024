create database customer;
use customer;
select * from customer.customer_master;
select * from customer.sales_order;

-- 2) Write a command to display first 10 rows.
SELECT * FROM customer.customer_master LIMIT 10;
SELECT * FROM customer.sales_order LIMIT 10;

-- 3) Identify unique items?
SELECT DISTINCT Item FROM customer.sales_order;

-- 4) Identify any unit cost is negative?
SELECT * FROM customer.sales_order where Unit_Cost<0;

-- 5) Identify minimum and maximum unit price happened for same item.
SELECT Item, MIN(Unit_Cost) AS min_unit_price, MAX(Unit_Cost) AS max_unit_price
FROM customer.sales_order
GROUP BY Item;

-- 6) Identify the Total sales happened in the year of 2021?
SELECT SUM(Total) AS total_sales_2021
FROM customer.sales_order
WHERE YEAR(STR_TO_DATE(OrderDate, '%d-%m-%Y')) = 2021;

-- 7) Which item is sold maximum in the year 2021?
SELECT Item, SUM(Units) AS total_units_sold
FROM customer.sales_order
WHERE YEAR(STR_TO_DATE(OrderDate, '%d-%m-%Y')) = 2021
GROUP BY Item
ORDER BY total_units_sold DESC
LIMIT 1;

-- 8) Identify the region with highest and lowest sales.
SELECT cm.Region, SUM(so.Total) AS total_sales
FROM customer.customer_master AS cm
JOIN customer.sales_order AS so ON cm.Customer_ID = so.Customer_ID
GROUP BY cm.Region
ORDER BY total_sales DESC
LIMIT 1;

SELECT cm.Region, SUM(so.Total) AS total_sales
FROM customer.customer_master AS cm
JOIN customer.sales_order AS so ON cm.Customer_ID = so.Customer_ID
GROUP BY cm.Region
ORDER BY total_sales ASC
LIMIT 1;

-- 9) Identify the customer name having highest sales for the year 2022.
SELECT cm.Customer, SUM(so.Total) AS total_sales_2022
FROM customer.customer_master AS cm
JOIN customer.sales_order AS so ON cm.Customer_ID = so.Customer_ID
WHERE YEAR(STR_TO_DATE(so.OrderDate, '%d-%m-%Y')) = 2022
GROUP BY cm.Customer
ORDER BY total_sales_2022 DESC
LIMIT 1;

-- 10) Which item has highest and lowest unit cost?
SELECT Item, `Unit_Cost` AS max_unit_cost
FROM customer.sales_order
WHERE `Unit_Cost` = (SELECT MAX(`Unit_Cost`) FROM customer.sales_order);

SELECT Item, `Unit_Cost` AS min_unit_cost
FROM customer.sales_order
WHERE `Unit_Cost` = (SELECT MIN(`Unit_Cost`) FROM customer.sales_order);

-- 11) Identify items starts with letter 'P'.
SELECT * FROM customer.sales_order
WHERE Item LIKE 'P%';

-- 12) Filter the table having items Pen and Pencil.
SELECT * FROM customer.sales_order
WHERE Item IN ('Pen', 'Pencil');

-- 13) Filter the table with unit cost between 1 and 100.
SELECT * FROM customer.sales_order
WHERE `Unit_Cost` BETWEEN 1 AND 100;

-- 14) Identify the customer with more no of transaction(no of entries).
SELECT Customer_ID, COUNT(*) AS transaction_count
FROM customer.sales_order
GROUP BY Customer_ID
ORDER BY transaction_count DESC
LIMIT 1;

-- 15) Identify which item has maximum sales in each region.
SELECT cm.Region, so.Item, SUM(so.Units) AS total_units_sold
FROM customer.customer_master AS cm
JOIN customer.sales_order AS so ON cm.Customer_ID = so.Customer_ID
GROUP BY cm.Region, so.Item
HAVING SUM(so.Units) = (SELECT MAX(total_units_sold)
                        FROM (SELECT cm.Region, so.Item, SUM(so.Units) AS total_units_sold
                              FROM customer.customer_master AS cm
                              JOIN customer.sales_order AS so ON cm.Customer_ID = so.Customer_ID
                              GROUP BY cm.Region, so.Item) AS max_sales_per_region
                        WHERE max_sales_per_region.Region = cm.Region)
ORDER BY cm.Region;

-- 16) Create 5 more scenarios using important inbuilt functions of MySQL.

-- Calculate Total Revenue for Each Customer:
SELECT Customer_ID, SUM(Total) AS total_revenue
FROM sales_order
GROUP BY Customer_ID;

-- Find Average Unit Cost of Items:
SELECT AVG(`Unit_Cost`) AS average_unit_cost
FROM sales_order;

-- Calculate the Total Revenue Absolute Value for Each Customer:
SELECT Customer_ID,ABS(SUM(Total)) AS total_revenue_absolute
FROM sales_order
GROUP BY Customer_ID;

-- Identify Orders with Even Unit Counts:
SELECT * FROM sales_order
WHERE MOD(Units, 2) = 0;

-- Create a Concatenated String of Customer ID and Item for Each Order:
SELECT CONCAT(Customer_ID, '-', Item) AS customer_item_concat
FROM sales_order;














