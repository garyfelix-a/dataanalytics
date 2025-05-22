-- Make predictions for the next sales data
SELECT
  Category,
  Product,
  Amount,
  predicted_qty
FROM
  ML.PREDICT(MODEL `the-retina-457110-i6.p2_dataset.sales_qty_forecast_model`,
    (SELECT
     "Shoes" AS Category,
     "Adidas Shoes" AS Product,
     100000 AS Amount,
     FROM
      `the-retina-457110-i6.p2_dataset.new_sales_data`)) AS forecast;