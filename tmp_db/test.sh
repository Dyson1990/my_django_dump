#!/bin/bash

# 替换 'YOUR_SQL_QUERY' 为你要执行的实际SQL查询字符串
SQL_DATA='{"sql": "SELECT * FROM t"}'

# 使用给定的CSRF Token发送POST请求
curl -X POST \
     -H "Content-Type: application/json" \
     -H "X-CSRFToken: nKKA4zaSTZNsspX1KAWcequGnMfqnigE4oDM0EtDu6k3qtqRYCgZjciqCeTxyqY9" \
     -d "$SQL_DATA" \
     http://127.0.0.1:8000/tmp_db/sql/

# 输出响应
echo $response
