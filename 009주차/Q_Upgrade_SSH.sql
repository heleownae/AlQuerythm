#test케이스 실패

with temp as (
select item_id
from item_tree
where item_id in (select parent_item_id
                  from item_tree) or parent_item_id is null
    )

select item_id, item_name, rarity
from item_info
where item_id not in (select item_id
                      from temp)
order by item_id desc;


#성공

select item_id, item_name, rarity
from item_info
where item_id not in (select parent_item_id
                      from item_tree
                      where parent_item_id is not null)
order by item_id desc;
