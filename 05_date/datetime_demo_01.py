from datetime import datetime, timedelta

days = 30
#昨天
end_date = datetime.now() - timedelta(1)
#昨天的前 days前
start_date = end_date - timedelta(days=days)

# 格式化日期
formatted_start_date = start_date.strftime("%Y-%m-%d")
formatted_end_date = end_date.strftime("%Y-%m-%d")

print(formatted_start_date, formatted_end_date)
