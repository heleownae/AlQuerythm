-- 정답
SELECT item_id, item_name, rarity
FROM item_info
WHERE item_id NOT IN (
    SELECT parent_item_id
    FROM item_tree
    WHERE parent_item_id IS NOT NULL
)
ORDER BY item_id DESC;


-- 오답
WITH T1 AS (
    SELECT item_id, parent_item_id
    FROM item_tree
    WHERE parent_item_id IS NOT NULL
)
SELECT item_id, item_name, rarity
FROM item_info
WHERE item_id NOT IN T1.parent_item_id
ORDER BY item_id DESC;
