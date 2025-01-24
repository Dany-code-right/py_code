for 대답 in range(2):
    기분 = input("""
오늘 기분 어때?
    1. 좋아요.
    2. 다행이.?
    3. 그래?
               """1
            )
    if 기분 == 1:
        print("다행이야!")
    elif 기분 == 2:
        print("그렇군")
    elif 기분 == "나빠요":
        print("뭘 도와줄까?")
    else:
        print("흠...")
