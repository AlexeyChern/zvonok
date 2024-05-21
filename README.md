1. select article.* from article left join comment on article.id=comment.article_id where comment.id is NULL;
2. В файле zvonok.py