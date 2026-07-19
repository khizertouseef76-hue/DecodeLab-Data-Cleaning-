
-- STEP 1: Broad Operational Overview
SELECT 
    COUNT(*) AS total_orders,
    SUM(TotalPrice) AS total_revenue,
    AVG(TotalPrice) AS average_order_value
FROM orders;

-- STEP 2: High-Value Order Segmentation
SELECT 
    OrderID, 
    CustomerID, 
    Product, 
    TotalPrice
FROM orders
WHERE TotalPrice > 2000
ORDER BY TotalPrice DESC;

-- STEP 3: Product Class Performance Strategy
SELECT 
    Product,
    SUM(Quantity) AS total_units_sold,
    SUM(TotalPrice) AS total_gross_revenue
FROM orders
GROUP BY Product
ORDER BY total_gross_revenue DESC;

-- STEP 4: Marketing Attribution Diagnostics
SELECT 
    ReferralSource,
    COUNT(*) AS customer_acquisition_count,
    SUM(TotalPrice) AS channel_gross_revenue
FROM orders
GROUP BY ReferralSource
ORDER BY channel_gross_revenue DESC;