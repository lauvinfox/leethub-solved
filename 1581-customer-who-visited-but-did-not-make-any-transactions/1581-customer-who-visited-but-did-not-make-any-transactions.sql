# Write your MySQL query statement below
SELECT 
    p.customer_id,
    COUNT(p.visit_id) AS count_no_trans
FROM 
    Visits p
LEFT JOIN
    Transactions q
ON 
    p.visit_id = q.visit_id
WHERE 
    q.transaction_id IS NULL
GROUP BY 
    p.customer_id;

