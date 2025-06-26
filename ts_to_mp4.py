import tkinter as tk
from tkinter import filedialog, messagebox
import ffmpeg
import os

# 建立主視窗
window = tk.Tk()
window.title("TS ➜ MP4 轉檔工具")
window.geometry("400x200")

selected_file = None  # 用來記錄選到的檔案路徑

# 選取檔案的函式


def select_file():
    global selected_file
    file_path = filedialog.askopenfilename(
        filetypes=[("TS 檔案", "*.ts")],
        title="選擇 TS 檔"
    )
    if file_path:
        selected_file = file_path
        file_label.config(text=f"已選檔案：{os.path.basename(selected_file)}")

# 執行轉檔的函式


def convert_file():
    if not selected_file:
        messagebox.showwarning("警告", "請先選擇 .ts 檔案！")
        return

    output_file = os.path.splitext(selected_file)[
        0] + ".mp4"    # 取得輸出檔案的路徑，將副檔名改為 .mp4

    try:
        ffmpeg.input(selected_file).output(
            # 使用 ffmpeg 進行轉檔，並允許覆寫輸出檔案
            output_file).run(overwrite_output=True)

        messagebox.showinfo("成功", f"轉檔完成：{output_file}")
    except ffmpeg.Error as e:
        messagebox.showerror("錯誤", f"轉檔失敗：\n{e}")


# --- UI 元件設計 ---
file_label = tk.Label(window, text="尚未選擇檔案")
file_label.pack(pady=10)

select_btn = tk.Button(window, text="選擇 TS 檔", command=select_file)
select_btn.pack(pady=5)

convert_btn = tk.Button(window, text="轉換成 MP4", command=convert_file)
convert_btn.pack(pady=5)

# 執行主視窗迴圈
window.mainloop()
