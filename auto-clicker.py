import pyautogui
import time
import keyboard

def get_click_positions():
    positions = []
    print("\t*-----------------------------*")
    print("\t|1. 将鼠标移动到需要点击的位置|")
    print("\t|2. 按F9键锁定一个位置(可多选)|")
    print("\t|3. 按F10键开始自动点击       |")
    print("\t|4. 按F12键停止自动点击       |")
    print("\t*-----------------------------*")
    
    try:
        while True:
            # 检测F9键按下，记录当前鼠标位置
            if keyboard.is_pressed('f9'):
                while keyboard.is_pressed('f9'):
                    time.sleep(0.1)
                pos = pyautogui.position()
                positions.append(pos)
                print(f"已记录位置 {len(positions)}: {pos}")
            # 检测F10键按下，结束位置设置
            if keyboard.is_pressed('f10'):
                while keyboard.is_pressed('f10'):
                    time.sleep(0.1)
                if len(positions) == 0:
                    print("请至少记录一个位置！")
                    continue
                break
            # 小延迟，降低CPU占用
            time.sleep(0.05)
    
    except Exception as e:
        print(f"设置过程出错: {e}")
    return positions

def auto_click_loop(positions, interval=0.3):
    print(f"\n将在2秒后开始循环点击 {len(positions)} 个位置...")
    print("按F12键停止程序")
    time.sleep(2)
    print("开始循环点击...")
    click_count = 0
    try:
        while True:
            # 检查是否按下了F12停止键
            if keyboard.is_pressed('f12'):
                break
            time.sleep(0.3)
            for i, (x, y) in enumerate(positions, 1):
                # 每次点击前检查停止键
                if keyboard.is_pressed('f12'):
                    break
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.click()
                click_count += 1
                print(f"总点击次数: {click_count} | 当前位置: {i}/{len(positions)} {x},{y}", end='\r')
                if i < len(positions):
                    time.sleep(interval)
            # 再次检查停止键
            if keyboard.is_pressed('f12'):
                break
                
    except KeyboardInterrupt:
        pass  # 捕获Ctrl+C
    print(f"\n已停止点击，共点击了 {click_count} 次")

if __name__ == "__main__":
    import os
    # 禁用PyAutoGUI的安全功能（防止鼠标移到角落停止）
    pyautogui.FAILSAFE = False
    click_positions = get_click_positions()
    print(f"已设置 {len(click_positions)} 个点击位置，准备开始循环")
    # 开始循环点击，间隔0.3秒
    auto_click_loop(click_positions, 0.3)
