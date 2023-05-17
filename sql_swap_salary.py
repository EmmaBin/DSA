#https://leetcode.com/problems/swap-salary/description/

UPDATE Salary
set sex=
case
    when sex = 'm' then 'f'
    when sex='f' then 'm'
end;