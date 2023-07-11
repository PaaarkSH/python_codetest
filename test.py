from datetime import datetime


def is_leap_year(year):
    # 윤년 여부를 판단하는 함수
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_date_difference(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    # 날짜 차이 계산
    delta = end - start

    # 총 일 수 차이 계산
    total_days = delta.days

    # 연도와 월을 기준으로 달 수 차이 계산
    start_year = start.year
    start_month = start.month

    end_year = end.year
    end_month = end.month

    year_diff = end_year - start_year
    month_diff = end_month - start_month

    # 윤년 고려하여 달 수 차이 조정
    if month_diff < 0:
        year_diff -= 1
        month_diff += 12

    # 윤년 고려하여 일 수 차이 조정
    leap_years = sum(1 for year in range(start_year, end_year + 1) if is_leap_year(year))

    total_months = year_diff * 12 + month_diff
    adjusted_total_days = total_days - leap_years

    return total_months, adjusted_total_days

# 두 날짜를 입력받아 달 수 차이와 일 수 차이 출력
start_date = '2023-01-01'
end_date = '2023-02-08'

month_diff, day_diff = calculate_date_difference(start_date, end_date)
print("달 수 차이:", month_diff)
print("일 수 차이:", day_diff)
