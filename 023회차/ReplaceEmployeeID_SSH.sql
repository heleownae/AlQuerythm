select u.unique_id, e.name
from employees e left join employuni U on e.id = u.id;
