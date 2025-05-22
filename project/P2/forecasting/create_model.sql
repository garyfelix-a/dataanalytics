CREATE OR REPLACE MODEL `the-retina-457110-i6.p2_dataset.sales_qty_forecast_model`
OPTIONS(model_type='LINEAR_REG', input_label_cols=['Qty'] ) AS
SELECT
  Category,           -- Categorical variable: product category
  Product,            -- Categorical variable: product
  INR_Amount,         -- Numeric feature: INR amount
  Qty                 -- Target variable: quantity of products sold
FROM
  `the-retina-457110-i6.p2_dataset.final_sales`;
  
