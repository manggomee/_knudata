import time, asyncio  # 시간 관련 모듈과 비동기 실행을 위한 asyncio 모듈 불러오기

async def q():
    print("530 * 212는 얼마야?")  # 질문 출력
    await asyncio.sleep(1)  # 5초간 비동기 대기 (blocking 없이)
    print("답이 틀렸잖아")

async def a():
    print("3600입니다.")  # 답변 출력
    await asyncio.sleep(2)
    print("하지만 빨랐쥬?")

async def main():
    await asyncio.gather(q(), a())  # 두 함수를 동시에 비동기 실행

if __name__ == "__main__":
    asyncio.run(main())  # ✅ 비동기 함수 실행은 asyncio.run으로 감싸야 함
