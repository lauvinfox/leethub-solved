# Write your MySQL query statement below
# SELECT 
#     p.customer_id,
#     COUNT(p.customer_id) AS count_no_trans
# FROM 
#     Visits p
# LEFT JOIN
#     Transactions q
# ON 
#     p.visit_id = q.visit_id
# WHERE 
#     q.amount IS NULL
# GROUP BY 
#     p.customer_id;

SELECT customer_id, COUNT(v.visit_id) as count_no_trans 
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id