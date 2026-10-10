-- 1. Churn rate by customer segment
SELECT
    Cluster,
    COUNT(*) AS total_customers,
    SUM(Churn = 'Yes') AS churned_customers,
    ROUND(AVG(Churn = 'Yes') * 100, 2) AS churn_rate_pct
FROM customer_churn
GROUP BY Cluster
ORDER BY churn_rate_pct DESC;


-- 2. Churn rate by contract type
SELECT
    Contract,
    COUNT(*) AS total_customers,
    SUM(Churn = 'Yes') AS churned_customers,
    ROUND(AVG(Churn = 'Yes') * 100, 2) AS churn_rate_pct
FROM customer_churn
GROUP BY Contract
ORDER BY churn_rate_pct DESC;


-- 3. Churn rate by payment method
SELECT
    PaymentMethod,
    COUNT(*) AS total_customers,
    SUM(Churn = 'Yes') AS churned_customers,
    ROUND(AVG(Churn = 'Yes') * 100, 2) AS churn_rate_pct
FROM customer_churn
GROUP BY PaymentMethod
ORDER BY churn_rate_pct DESC;


-- 4. Monthly billing by retention priority
SELECT
    Priority,
    COUNT(*) AS total_customers,
    ROUND(AVG(ChurnProbability) * 100, 2) AS avg_churn_risk_pct,
    ROUND(SUM(MonthlyCharges), 2) AS monthly_charges_total
FROM customer_churn
GROUP BY Priority
ORDER BY avg_churn_risk_pct DESC;