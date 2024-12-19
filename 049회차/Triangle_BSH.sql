SELECT
    x,
    y,
    z,
    IF((x+y>z AND x+z>y AND y+z>x), 'Yes', 'No') AS triangle  # 삼각형 조건은 찾아봄.
FROM
    Triangle;
