import subprocess
import webview
import os
import win32con

def start_aria2():
    try:
        # 获取当前脚本所在目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # 创建 STARTUPINFO 对象
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = win32con.SW_HIDE

        # 启动Aria2服务，这里假设你已经将aria2c可执行文件添加到了系统路径中
        # 如果没有添加到系统路径，需要指定完整的路径
        aria2_process = subprocess.Popen(f"{current_dir}\\aria2c\\aria2c.exe --conf-path={current_dir}\\aria2c\\aria2.conf", shell=False, startupinfo=startupinfo)

        return aria2_process
    except Exception as e:
        print(f"启动Aria2服务时出错: {e}")
        return None

def main():
    # 启动Aria2服务
    aria2_process = start_aria2()

    if aria2_process:
        try:
            # 获取当前脚本所在目录
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # 假设HTML文件名为index.html，位于当前目录下
            html_file_path = os.path.join(current_dir, 'aria2c/index.html')

            # 检查HTML文件是否存在
            if os.path.exists(html_file_path):
                # 使用pywebview创建窗口并加载HTML文件
                webview.create_window('Aria2 Web UI', url=f'file://{html_file_path}')
                webview.start()
            else:
                print("未找到指定的HTML文件。")
        except Exception as e:
            print(f"创建窗口时出错: {e}")
        finally:
            # 终止Aria2服务
            aria2_process.terminate()
            aria2_process.wait(timeout=5)  # 等待5秒以确保进程完全退出
            print("Aria2服务已成功关闭。")

if __name__ == "__main__":
    main()