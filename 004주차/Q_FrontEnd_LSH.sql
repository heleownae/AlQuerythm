select distinct ID,	EMAIL,	FIRST_NAME,	LAST_NAME
from SKILLCODES , DEVELOPERS 
where (SKILLCODES.code & DEVELOPERS.skill_code)
and SKILLCODES.CATEGORY = 'Front End'
order by DEVELOPERS.ID;