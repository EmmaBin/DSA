#https://leetcode.com/problems/fix-names-in-a-table/description/

SELECT user_id, 
CONCAT(UPPER(SUBSTR(name, 1,1)), LOWER(SUBSTR(name, 2))) as name 
FROM Users
order by user_id