select ei.unique_id, es.name
from employees es left join employuni ei on es.id = ei.id
