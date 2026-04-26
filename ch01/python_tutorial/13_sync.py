# 동기 프로그래밍
import time

def fetch_data_sync(delay):
  print(f"시작(딜레이: {delay})")
  time.sleep(delay)
  print(f"완료(딜레이: {delay})")
  return f"딜레이: {delay}"

def main_sync():
  result1 = fetch_data_sync(2)
  result2 = fetch_data_sync(1)
  print(f"결과: {result1}, {result2}")
  
main_sync()