### spider-college
> 目前已爬取2651条高校基本信息，31个城市的199条历年高考分数线,
#### 使用事项
> 在爬去全国高校基本信息时，会出现重复的数据,请执行下面的删除重复记录sql语句进行排除。
#### 删除重复记录值
    
    DELETE
    FROM
        college
    WHERE
        name IN (
        SELECT name FROM (
            SELECT
                name
            FROM
                college
            GROUP BY
                name
            HAVING
                COUNT(id) > 1
        ) AS tab1
        )
    AND id NOT IN (
        SELECT id FROM (
            SELECT
            MIN(id) AS id 
            FROM
            college
            GROUP BY
            name
            HAVING
            COUNT(id) > 1
        ) AS tab2
    )


#### 数据库MySQL操作

    SELECT * FROM score where city = '河南'    
    SELECT * FROM college where name = '四川文理学院'
    SELECT s.category,s.score_line,s.score_list FROM city c,score s  WHERE s.city=c.name and s.city = '河南'