# NHÓM 10 — CÂY TRÒ CHƠI: MINIMAX VÀ ALPHA–BETA
**4 sinh viên · 10 ngày · bảo vệ 15–20 phút**
**Nguyễn Bích Vân|Biểu diễn tri thức và tìm kiếm nâng cao — IAI–UET–VNU**

## 1. Mở tệp nào?
- `De_Nhom10_SinhVien.pdf`: đề chính, 85 điểm sản phẩm chung + 15 điểm bảo vệ cá nhân.
- `HuongDan_Nhom10_Python.pdf`: giải thích cách đọc và chạy mã.
- `MauBaoCao/`: Word hoặc LaTeX để điền, PDF xem bố cục; mẫu trống 6 trang.
- `KeHoach_10Ngay.md`, `DanY_BaoVe.md`: lịch và khung trình bày.


## 2. Chạy ngay
Giải nén toàn bộ ZIP. Trong VS Code mở thư mục `GiuaKy_Nhom10_CayTroChoi_4SV_10Ngay`. Các tệp chạy nằm ngay đây, không gõ `cd python`. Dùng Python/Anaconda 3.10+; không cần `pip install`.

```text
python kiem_tra_moi_truong.py
python chay_mau.py
python minimax_alphabeta_toi_gian.py
python -m unittest -v test_mau test_nhom_mau
```

Mã mẫu đầy đủ, không có `NotImplementedError`. Bản tối giản dùng list lồng nhau; bản đầy đủ dùng `make_tree` từ list điểm lá phẳng. Đọc hướng dẫn trước khi đổi lẫn hai định dạng.

## 3. Thực nghiệm
```text
python run.py --case T0 --algo minimax --tag T0_mm
python run.py --case T0 --algo alphabeta --trace --tag trace_T0
python run.py --case T1 --algo alphabeta --step --tag step_T1
python run.py --batch --tag bat_buoc
python tao_du_lieu.py --seed 1026
python run.py --data du_lieu_nhom.json --tag tu_tao
```
Đổi seed theo nhóm. Tạo lại tệp cũ cần thêm `--overwrite` có chủ ý. `--batch` tạo **24 cấu hình**; dữ liệu riêng N1/N2 tạo **8 cấu hình**. Mọi kết quả vào `output/`. `--step` dừng ngay trong đệ quy: Enter ở Terminal để tiếp tục; Ctrl+C dừng, không giả vờ hoàn thành.

Đo thời gian tùy chọn: thêm `--repeat 3` ở batch để lấy trung vị. Không bật step/trace khi đo. Số nút và chất lượng kết quả là bằng chứng chính trên các cây nhỏ.

## 4. Bài nhóm cần làm
Trình bày thuật toán; tính tay B1–B4; tạo N1 (16 lá MAX), N2 (8 lá MIN); tự viết ít nhất **8 test**, mỗi người 2, gồm 3 kỳ vọng tay độc lập. So sánh kết quả, phát hiện lỗi và điền báo cáo; không phải tự viết lại thuật toán từ đầu.

Đổi `LEAVES`, `ROOT_PLAYER`, `ALGORITHM`, `ORDER` trong `chay_mau.py` để học. Không sửa T0/T1/T2; tạo dữ liệu riêng trong JSON. Thứ tự LR/RL áp dụng ở mọi nút.

## 5. Nộp bài
Điền mẫu báo cáo và xuất `BaoCao.pdf` (6–8 trang chính), có `TinhTay.pdf`, `ThuyetTrinh.pptx` (6–8 slide). Sao `README_NOP_MAU.md` thành `README_NOP.md`, `DongGop_MAU.md` thành `DongGop.md`, rồi điền.

```text
python chay_kiem_thu.py
python dong_goi.py
```
Lệnh test yêu cầu `test_nhom.py` do nhóm viết; lưu log thật kể cả lỗi. Công cụ ZIP chỉ kiểm thành phần và số dòng, không chấm nội dung. Kiểm ZIP có đủ mã phụ thuộc; giải nén và chạy lại trên máy thành viên khác.

## 6. Quy tắc cần nhớ
Utility 0 là lá; `None` khác 0. Chọn action bằng so sánh nghiêm, cắt cho phép dấu bằng. Alpha/beta không reset giữa các con. `visited=expanded+leaves`; `pruned_branches` không phải tổng lá bị bỏ. Bảng `returns` của Alpha–Beta chứa cả cận; `principal_variation` chỉ có trong Minimax đầy đủ. Bốn người đều phải giải thích được hai thuật toán.


