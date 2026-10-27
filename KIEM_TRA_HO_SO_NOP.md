**Kết quả kiểm tra hồ sơ nộp Nhóm 10 — ngày 27/10/2026**

**Kết luận:** Có đủ thành phần để nộp và tái chạy thành công. Chưa phát hiện sai kết quả thuật toán trong phạm vi kiểm tra. Hồ sơ hiện vẫn cần chỉnh số trang báo cáo, số slide, một ký hiệu trong bài tính tay và một số phần trình bày/minh chứng trước khi chốt ZIP.

Đã đối chiếu trực tiếp với `De_Nhom10_SinhVien.pdf` (8 trang), `README_BAT_DAU.md`, `DanY_BaoVe.md`, `MauBaoCao/HUONG_DAN_DIEN.md`; đọc báo cáo, xem đủ 14 trang tính tay và 9 slide thực tế trong PPTX; kiểm tra mã, JSON/CSV, log và nội dung ZIP. Các lệnh sinh kết quả được chạy trên bản giải nén ở `/tmp/nhom10_review/extracted/Nhom10_CayTroChoi_GiuaKy`, giữ nguyên hồ sơ gốc.

**Những điểm cần xử lý, theo mức ưu tiên**

| Mức | Vị trí | Phát hiện và ảnh hưởng | Đề xuất cụ thể |
|---|---|---|---|
| Cần sửa trước khi nộp | `BaoCao.pdf`, trang 1–10 | Có **10 trang nội dung chính**. Trang 1 đã chứa phần mô hình; trang 3, 6, 9 vẫn là nội dung chính, không phải phụ lục. Đề trang 8 yêu cầu **6–8 trang nội dung chính**. | Dàn lại về tối đa 8 trang. Có thể tận dụng khoảng trắng lớn ở trang 3, 6, 9; giữ phần phân tích, tránh chỉ thu nhỏ chữ. |
| Cần sửa trước khi nộp | `ThuyetTrinh.pptx` | Có **9 slide**, tất cả đều hiển thị. Đề yêu cầu **6–8 slide**, không nêu ngoại lệ bỏ qua slide bìa. Báo cáo trang 10 lại đánh dấu mục “6–8 slide” là đạt. | Gộp/bỏ một slide, ví dụ gộp thông tin bìa vào slide mô hình hoặc đưa hình N1/N2 vào phần kết quả. Cập nhật số trang chân slide và checklist. |
| Cần sửa ký hiệu | `TinhTay.pdf`, trang 11, cột xử lý sau khi B cắt trên T1 | Ô đóng khung ghi `V(B)=10`, trong khi phần đầu trang đã tính giá trị thật của B là 2 và phần giải thích bên dưới nói đây chỉ là cận trên. Ký hiệu này dễ bị đọc thành khẳng định sai về giá trị Minimax. | Ghi rõ **“B trả r=10, UPPER: V(B) ≤ 10; giá trị thật V(B)=2”**. Giữ lại dấu/chú thích đính chính theo yêu cầu của đề, không thay dự đoán cũ mà không ghi nhận. |
| Cần sửa lệnh hiển thị | `ThuyetTrinh.pptx`, slide 9; `ThuyetTrinh.pdf`, trang 9 | Lệnh hiển thị `python3 run.py –batch –tag bat_buoc`: dấu trước `batch`, `tag` là dấu dài `–`, không phải hai dấu gạch nối ASCII `--`. Gõ nguyên như vậy sẽ không chạy đúng. | Hiển thị `python3 run.py --batch --tag bat_buoc`. Nếu xuất bằng LaTeX, dùng cách giữ nguyên hai dấu gạch như `-{}-` hoặc môi trường mã phù hợp. README hiện đã ghi đúng. |
| Nên xử lý trước khi nộp | `TinhTay.pdf`, trang 2 | Cả công cụ trích văn bản và dựng ảnh đều báo ba lỗi **`Bad block header in flate stream`**. Xác định được ở ba Form XObject trên trang 2. | Xuất/ghép lại trang này từ nguồn tốt rồi kiểm tra PDF. Cả 14 trang hiện vẫn dựng được và phần phép tính chính đọc được; đây là lỗi cấu trúc PDF, chưa có căn cứ kết luận toàn bộ bài tính tay hỏng. |
| Thiếu phần trình bày theo đề | `BaoCao.pdf`, trang 7; `MauBaoCao/BaoCao.tex`, dòng 182–202 | Mục D2(b), đề trang 7 yêu cầu tỷ lệ tiết kiệm lá cho **từng cặp tương ứng**. Báo cáo mới ghi tỷ lệ cho 6 cặp T0/T1/T2, chưa ghi đủ 5 cặp tham số, 1 cặp affine và 4 cặp dữ liệu riêng. CSV gốc cũng không có cột tỷ lệ này. | Bổ sung bảng/đoạn tổng hợp 10 tỷ lệ còn thiếu. Số liệu đúng đã liệt kê ở bảng kiểm chứng bên dưới. Không cần sửa thuật toán hay CSV gốc. |
| Thiếu minh chứng cần chuẩn bị | Phần C1 của đề, trang 6; báo cáo/README/slide hiện tại | Chưa thấy ghi **3 sự kiện được dự đoán trước khi tiếp tục `--step`**. Có trace và kế hoạch demo, nhưng chưa có ba dự đoán cụ thể. Chế độ step trong mã chạy được. | Chuẩn bị ba dự đoán ngắn trên T1 và lệnh demo bên dưới; chỉ ghi nhóm đã thực hiện sau khi thực sự diễn tập. Đây là thiếu minh chứng trong hồ sơ, không phải bằng chứng nhóm chưa từng chạy step. |
| Nên làm sạch bản cuối | `BaoCao.pdf`, trang 1; `MauBaoCao/BaoCao.tex`, dòng 51 | Còn nguyên đoạn hướng dẫn của mẫu: “Hướng dẫn: thay [Điền]… Mẫu trống 6 trang… Chọn Word hoặc LaTeX…”. | Bỏ đoạn hướng dẫn khi hoàn thiện báo cáo. Không phải một ô nội dung chuyên môn chưa điền, nhưng làm bản cuối trông chưa được nghiệm thu. |

**Kết quả kiểm tra theo từng thành phần nộp**

| Thành phần | Kết quả |
|---|---|
| `BaoCao.pdf` | Đủ các mảng chính: mô hình, truy hồi, mã giả Minimax, giải thích Alpha–Beta, đối chiếu tay/code, tham số, affine, dữ liệu riêng, test, hai lỗi thử nghiệm, giới hạn, phân công và tái chạy. Các con số được kiểm tra đều khớp. Cần xử lý các điểm về số trang và phần thiếu ở trên. |
| `TinhTay.pdf` | Đủ B1 trang 1–3, B2 trang 4–6, B3 trang 7–10, B4 trang 11, N2 trang 12–14. Các phép tính chính, đường chơi, nhánh cắt và số đếm đúng; cần chỉnh ký hiệu B4 và lỗi PDF trang 2. |
| `ThuyetTrinh.pptx` | Đủ nội dung thuật toán, ví dụ T0/T1, kết quả N1/N2, test và giới hạn. Số liệu khớp JSON/CSV. PPTX không thiếu ảnh/tài nguyên liên kết, giải nén kiểm tra không lỗi. Cần giảm 9 xuống tối đa 8 slide và sửa lệnh trên slide cuối. |
| `test_nhom.py` | **9/9 test PASS**, đáp ứng đề yêu cầu **ít nhất 8**, phân bổ 2–2–3–2 theo bảng đóng góp. Bốn test đầu có bước suy luận độc lập. Có assert, không có test rỗng, không cần thư viện ngoài chuẩn. Không cần bỏ test thứ 9 để ép về đúng 8. |
| `du_lieu_nhom.json` | Đúng N1: 16 lá/MAX; N2: 8 lá/MIN. Utility nguyên trong [-20,30], mỗi cây có ít nhất bốn giá trị phân biệt, khác T0/T1/T2. Tái tạo bằng seed **2579** được đúng dữ liệu hiện có. |
| `output/bat_buoc.json` và `.csv` | Đúng **24 cấu hình**, đủ 12 cơ bản + 10 tham số + 2 affine. Không trùng/thiếu cấu hình so với ma trận yêu cầu; từng trường CSV khớp JSON. |
| `output/tu_tao.json` và `.csv` | Đúng **8 cấu hình**, đủ hai cây × hai thuật toán × hai thứ tự. CSV khớp JSON. |
| `output/trace_T0.json` và `.csv` | Đúng T0/Alpha–Beta/LR: (10,A), visited=22, expanded=12, leaves=10, cutoffs=3. Trace có đủ sự kiện; số vô cực dùng chuỗi `-inf`/`+inf` hợp lệ trong JSON. |
| `output/t11.json` và `.csv` | Đúng t=11/Alpha–Beta/LR: (11,A), visited=21, leaves=9, cutoffs=4; có cắt thêm L04. Đây là minh chứng bổ sung hợp lệ. |
| `output/ket_qua_test.txt` | Log hiện có ghi 9 test, OK, EXIT_CODE=0; kết quả phù hợp lần kiểm tra mới. |
| `README_NOP.md` | Các lệnh tái chạy hoạt động; seed, số cấu hình, số test, dữ liệu và chỉ số chính đúng. Câu “mọi kết quả… khớp 100%” ở dòng 76 nên đi cùng ghi chú đính chính ký hiệu/cách ghi cửa sổ, tránh che mất khác biệt trình bày. |
| `DongGop.md` | Đủ bốn thành viên, MSSV nhất quán với báo cáo/README; phân công test 2–2–3–2 và các commit dẫn chiếu phù hợp lịch sử cục bộ đã kiểm tra. Chưa có cơ sở kiểm chứng độc lập các khẳng định về ký xác nhận, tập bảo vệ và lần chạy trên máy Hiếu ngày 25/10 chỉ từ hồ sơ này. |
| `tree_model.py`, `search.py`, `data_cases.py`, `run.py` | Không phát hiện sai trong các cấu hình và test đã kiểm tra; còn nguyên nội dung so với commit khởi tạo của repo. Nhận biết lá 0, chọn action nghiêm, cắt khi bằng ngưỡng, truyền cửa sổ và RL ở mọi nút đúng quy ước. |
| `test_mau.py`, `test_nhom_mau.py` | 24 test mẫu + 2 ví dụ đều PASS; cùng 9 test nhóm thành **35/35**. Không thấy nhóm sao chép nguyên hai test ví dụ để thay cho các test riêng. |
| `chay_mau.py`, `minimax_alphabeta_toi_gian.py`, `kiem_tra_moi_truong.py` | Chạy thành công trên bản giải nén. |
| `tao_du_lieu.py`, `chay_kiem_thu.py`, `dong_goi.py` | Tạo dữ liệu, lưu log và đóng gói thành công trên bản giải nén. Công cụ đóng gói chỉ kiểm thành phần/số dòng, nên việc chạy được không xác nhận yêu cầu 6–8 trang/slide. |
| `thu_loi.py` | Là bản cố ý dùng `score >= best` tại MAX, đúng vai trò thử lỗi. Không được `run.py` hay bộ test bình thường import. Không coi đây là lỗi thuật toán của bản chính. Hạn chế tái tạo: file chỉ định nghĩa hàm; chạy trực tiếp không tự chạy test và hiện chỉ lưu biến thể lỗi thứ hai. |
| `Nhom10_CayTroChoi_GiuaKy.zip` | Kiểm CRC không lỗi, có **30 file**; toàn bộ file trong ZIP khớp byte với bản tương ứng tại thư mục gốc lúc kiểm tra. Có đủ mã phụ thuộc; giải nén rồi chạy chuỗi lệnh thành công. Những lỗi hồ sơ nêu trên cũng đang nằm trong ZIP, cần đóng gói lại sau khi sửa. |

**Đối chiếu số liệu của toàn bộ 16 cặp Minimax/Alpha–Beta**

Mỗi dòng dưới đây ứng với hai cấu hình dùng cùng cây/thứ tự. Hai thuật toán khớp cả value và action. Tỷ lệ = 100 × (1 − số lá Alpha–Beta / số lá Minimax).

| Cây | Thứ tự | Value/action | Lá Minimax | Lá Alpha–Beta | Tiết kiệm |
|---|---|---|---:|---:|---:|
| T0 | LR | 10 / A | 16 | 10 | 37,5% |
| T0 | RL | 10 / A | 16 | 16 | 0% |
| T1 | LR | 10 / A | 4 | 3 | 25% |
| T1 | RL | 10 / A | 4 | 4 | 0% |
| T2 | LR | -4 / A | 8 | 8 | 0% |
| T2 | RL | -4 / A | 8 | 7 | 12,5% |
| T0(t=8) | LR | 10 / A | 16 | 10 | 37,5% |
| T0(t=10) | LR | 10 / A | 16 | 10 | 37,5% |
| T0(t=11) | LR | 11 / A | 16 | 9 | 43,75% |
| T0(t=12) | LR | 12 / A | 16 | 9 | 43,75% |
| T0(t=14) | LR | 12 / A | 16 | 9 | 43,75% |
| T0, u → 2u−7 | LR | 13 / A | 16 | 10 | 37,5% |
| N1 | LR | 13 / A | 16 | 9 | 43,75% |
| N1 | RL | 13 / A | 16 | 16 | 0% |
| N2 | LR | -13 / B | 8 | 8 | 0% |
| N2 | RL | -13 / B | 8 | 6 | 25% |

Đã kiểm tra thêm trên cả 32 bản ghi: đủ trường, value là int, `visited = expanded + leaves`, tập nút đã thăm/chưa thăm phân hoạch đúng cây, `returns` chỉ chứa các nút đã thăm, gốc nhánh cắt nằm trong các nút chưa thăm. Minimax duyệt đủ và có PV chính xác; Alpha–Beta có PV=null. Giá trị gốc và ý nghĩa EXACT/UPPER/LOWER ở mọi nút trả về được đối chiếu bằng phép tính Minimax độc lập từ cây, không chỉ so hai output với nhau.

Khi chạy lại, toàn bộ trường kết quả trong `bat_buoc`, `tu_tao`, `trace_T0`, `t11` khớp bản đã lưu, ngoại trừ `elapsed_ms` vốn thay đổi giữa các lần chạy. Không dùng thời gian của một lần chạy để kết luận tăng tốc.

**Những nội dung tính tay đã xác nhận**

- B1: đủ 15 nút trong; T0 có R=10, chọn A; PV LR là R → A → A1 → A12 → L04; 31 nút, 16 lá.
- B2: T0/LR đọc L01,L02,L03,L04,L05,L06,L07,L08,L09,L11; bỏ các gốc L10,L12,B2; không thăm 9 nút; 22=12+10; tiết kiệm 37,5% lá. Phải giữ alpha=10 khi chuyển A sang B.
- B3: V(R)=10 khi 0≤t<10; V(R)=t khi 10≤t≤12; V(R)=12 khi 12<t≤20. Action luôn A. PV đổi sang A11/L01 tại t=10 và sang L02 khi t>12; L04 bị cắt khi t≥11. Kết quả t=10,11,14 và dãy lá trong bài tay đúng.
- B4: giá trị thật A=10, B=2, R=10. B trả 10/UPPER khi chạy Alpha–Beta LR. Bản cập nhật action bằng `>=` có thể trả (10,B). Báo cáo trang 6 giải thích đúng; ký hiệu đóng khung ở bài tay cần thống nhất như đã nêu.
- N2: tầng sát lá có -15,11,-19,-13; A=11, B=-13; gốc MIN chọn B, value=-13. Minimax có PV R→B→B2→L08. Alpha–Beta LR đọc 8 lá, RL đọc 6 lá, cắt cây con A1.

Lưu ý cách ghi cửa sổ: B3 trang 9–10 ghi `(alpha, beta')` sau cập nhật, ví dụ `(10,4)` tại B11. `search.py` dòng 49–60 kiểm tra dừng trước khi cập nhật beta, nên sự kiện PRUNE cùng chỗ ghi `(10,+inf)`. Hai cách vẫn dẫn đến cùng phép cắt; **không coi khác biệt này là lỗi thuật toán**. Nên chú thích rõ quy ước khi tuyên bố đối chiếu trace. Ở B2 trang 4, dòng A21 sau khi đọc L06 cũng đang ghi beta hiện tại 8 dưới cột “cửa sổ khi vào”, trong khi cửa sổ lúc vào A21 là `(-inf,10)`; nên phân biệt hai khái niệm.

Đoạn cuối B4 có thảo luận đổi điều kiện cắt sang nghiêm và cũng nhắc đến việc không giữ quy tắc hòa. Để tránh bị hiểu là đề xuất sửa bằng cách đổi quy ước đề, nên chốt rõ như báo cáo: **giữ cắt có dấu bằng, dùng so sánh nghiêm để cập nhật action**.

**Minh chứng thực thi và demo**

Các lệnh chính đã chạy thành công trong bản ZIP giải nén: kiểm tra môi trường; hai chương trình mẫu; 35 unit test; script ghi log; batch 24 cấu hình; dữ liệu riêng 8 cấu hình; trace T0; trace t=11; tạo dữ liệu seed 2579 ra tên mới; đóng gói; T1 với `--step`.

Hai thử nghiệm lỗi được kiểm chứng bằng bản hàm tạm trong bộ nhớ, không sửa file chương trình:

| Biến thể | Test phát hiện | Kết quả thực tế |
|---|---|---|
| Khởi tạo MAX bằng 0 | Test 1 | ERROR `StopIteration` khi Minimax dựng PV do action không hợp lệ. Khớp báo cáo trang 9. |
| Chọn action MAX bằng `>=` | Test 3 | FAIL tại Alpha–Beta: `(10,'B') != (10,'A')`. Khớp báo cáo trang 9. |

Lệnh phù hợp cho phần C1/demo:

```text
python run.py --case T1 --algo alphabeta --order LR --step --tag demo_T1
```

Ba dự đoán có thể chuẩn bị trước khi tiếp tục từng bước:

1. Khi vào B, cửa sổ là `(10,+inf)` vì A đã trả 10 cho gốc.
2. Đọc L03=10 thì B cắt L04, trả 10 với cờ UPPER; chưa biết giá trị thật của B từ lần chạy này.
3. Gốc nhận số trả 10 của B nhưng giữ action=A do so sánh nghiêm; kết quả cuối `(10,A)`.

Đây là nội dung gợi ý cho buổi tập, không phải ghi nhận các thành viên đã thực hiện dự đoán trước trong quá khứ.

**Những điểm nhỏ và giới hạn kiểm tra**

- `test_nhom.py` chưa ghi tên/MSSV người phụ trách ngay trong comment/docstring. `DongGop.md` và báo cáo đã ánh xạ đủ, nên không thiếu phân công theo đề; nếu muốn đáp ứng trọn checklist AGENTS.md của nhóm thì bổ sung chú thích sau khi nhóm đồng ý sửa file.
- Mỗi slide trong PPTX hiện là một ảnh PNG phủ toàn trang. Cấu trúc hợp lệ, không phải lỗi yêu cầu đề, nhưng muốn sửa chữ cần sửa nguồn rồi xuất ảnh/PPTX lại hoặc dựng phần chữ có thể chỉnh. Chưa kiểm tra trình chiếu bằng Microsoft PowerPoint; đã kiểm tra XML, các ảnh thực tế và quan hệ tài nguyên.
- Slide cuối ghi phần Minh là “B2–B4”; nên viết “B2, B4” để không hiểu nhầm Minh chủ trì cả B3, vốn thuộc Ngân.
- `NoiDung_ThuyetTrinh.md` dòng 5 mô tả 7 slide, không còn khớp PPTX 9 slide hiện tại. Đây là tài liệu làm việc, không nằm trong ZIP; cập nhật nếu dùng nó để tập thuyết trình.
- Hai bản `BaoCao.pdf` ở gốc và trong `MauBaoCao/` khác byte nhưng văn bản trích xuất giống nhau. Không phát hiện khác biệt nội dung giữa hai bản này.
- Bài tay có một số chỗ gạch sửa; lịch sử Git cũng có cập nhật bài tay. Nên ghi rõ đính chính cụ thể theo yêu cầu đề trang 4, thay vì chỉ dùng câu “khớp 100%”. Không thể suy ra thời điểm tính tay trước/sau chạy mã chỉ từ bản PDF cuối.
- Các mốc chạy 23/10 trong báo cáo và tái chạy 25/10 trong README không tự thân mâu thuẫn, vì có thể là những lần chạy khác nhau. Lần kiểm tra này chỉ xác nhận trạng thái hiện tại; không thay thế xác nhận thực tế của thành viên về ngày chạy, chữ ký hay buổi tập.
- Không cần đưa các PDF đề/mẫu, file LaTeX build, `~$ThuyetTrinh.pptx` hay toàn bộ Git vào ZIP. ZIP hiện không chứa file khóa PowerPoint này và đã có đủ phụ thuộc để chạy.

Sau khi chỉnh hồ sơ, cần xuất lại PDF/PPTX, cập nhật các tham chiếu số trang trên slide nếu bố cục báo cáo đổi, chạy `python dong_goi.py` và kiểm tra lại bản ZIP cuối. Không cần thay thuật toán để xử lý các phát hiện hiện tại.

Tệp bằng chứng kiểm tra tạm: `/tmp/nhom10_review/rerun.log`, `/tmp/nhom10_review/data_validation.json`, `/tmp/nhom10_review/mutation_checks.log`. Không sửa mã, báo cáo, slide, dữ liệu, output hay ZIP gốc trong lần rà soát này; chỉ thêm tài liệu kiểm tra này.
