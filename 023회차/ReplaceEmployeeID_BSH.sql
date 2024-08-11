select ei.unique_id, es.name
from employees as es left join employuni as ei on es.id = ei.id
