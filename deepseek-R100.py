import time
import random

def main():
    print("欢迎使用deepseek-R100（输入 exit 退出）")
    while True:
        user_input = input("用户：")
        if user_input.strip().lower() == "exit":
            print("程序已退出。")
            break
        delay = random.randint(5, 20)
        time.sleep(delay)
        print("服务器繁忙，请稍后再试。")

if __name__ == "__main__":
    main()
