# Write your MySQL query statement below
SELECT 
    l.machine_id,
    ROUND(avg(r.timestamp - l.timestamp), 3) as processing_time
FROM 
    Activity l
JOIN 
    Activity r
ON 
    l.machine_id=r.machine_id AND
    l.process_id=r.process_id AND
    l.activity_type='start' AND
    r.activity_type='end'
GROUP BY
    l.machine_id
    