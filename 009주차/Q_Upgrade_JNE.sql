select item_id,
       item_name,
       rarity
from item_info
-- null이 아닌 모든 고유한 parent_item_id를 찾아, 이들 중에서 item_info 테이블에 존재하지 않는 아이템 ID를 가진 아이템들을 선택
where item_id not in (select parent_item_id from item_tree where parent_item_id is not null)
order by item_id desc
