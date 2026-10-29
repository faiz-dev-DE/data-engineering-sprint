-- 1. Create Dimension Tables
CREATE TEMPORARY TABLE dim_customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    country VARCHAR(50)
);

CREATE TEMPORARY TABLE dim_products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50)
);

-- 2. Create Central Fact Table
CREATE TEMPORARY TABLE fact_sales (
    sale_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    revenue_usd DECIMAL(10,2)
);

-- 3. Populate Dimension Data
INSERT INTO dim_customers VALUES 
(1, 'Aarav Sharma', 'India'),
(2, 'Emily Smith', 'USA'),
(3, 'Priya Patel', 'India'),
(4, 'John Doe', 'USA');

INSERT INTO dim_products VALUES 
(10, 'Flagship Smartphone', 'Electronics'),
(20, 'Ergonomic Desk Chair', 'Furniture'),
(30, 'Wireless Earbuds', 'Electronics');

-- 4. Populate Transaction Fact Data
INSERT INTO fact_sales VALUES 
(501, 1, 10, '2026-10-01', 1200.00),
(502, 2, 20, '2026-10-02', 450.00),
(503, 1, 30, '2026-10-05', 150.00),
(504, 3, 10, '2026-10-10', 1200.00),
(505, 4, 20, '2026-10-12', 450.00),
(506, 2, 10, '2026-10-15', 1200.00);

-- 5.Solution
SELECT
    c.country,
    p.category,
    SUM(f.revenue_usd) AS total_revenue,
    DENSE_RANK() OVER (
        PARTITION BY c.country
        ORDER BY SUM(f.revenue_usd) DESC
    ) AS category_rank
FROM dim_customers c
JOIN fact_sales f
    ON c.customer_id = f.customer_id
JOIN dim_products p
    ON f.product_id = p.product_id
GROUP BY
    c.country,
    p.category;
