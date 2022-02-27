---
outgoing_links:
  - Zet/Thinking/❕ 210714195600 - Zettelkasten Workflow
  - Zet/Permanent Note
  - Zet/Obsidian
backlinks:
  - Zet/Writing/Zettelkasten Workflow
title: Zettelkasten Workflow
UID: 220227164300
created: 27-Feb-2022
tags:
  - 'created/2022/Feb/27'
  - 'seeding'
  - 'permanent/think'
aliases: 220227164300
publish: True
---
## Notes:
Bản nâng cấp workflow thứ 2, workflow này giúp thuận tiện hơn rất nhiều trong việc tạo ghi chú. Bản cũ ở đây [[❕ 210714195600 - Zettelkasten Workflow]]

Dưới đây là một ví dụ khi mình đọc tài liệu trên wiki và tạo [[Permanent Note]]

Template này cho ghi chú Source/Reference. Có điền thông tin nguồn mà mình đọc, nó có thể là sách, báo. Nếu là website thì dẫn link...
[[@ wiki, Cronus]]
![[Pasted image 20220227164721.png]]

### Ghi chú loại 1: 
Các sự kiện, định nghĩa, so sánh, ... mình sẽ có một ID ở đầu và phía sau một câu ngắn gọn mô tả nội dung ghi chú.

![[Pasted image 20220227165012.png]]

Cấu trúc ghi chú loại 1 này thường bao gồm 3 phần:
![[Pasted image 20220227165407.png]]

- Phần **Notes**: ghi lại nội dung của ghi chú, phần này nên giữ nguyên nội dung, chỉ nên sửa chính tả, cú pháp. Nếu có sửa bóc tách nội dung ra 2, 3 ghi chú khác nhau từ ghi chú này thì nên xem có bao nhiêu ghi chú đã link đến ghi chú này. Lúc đó, ta sẽ có những chỉnh sửa thích hợp ở những ghi chú đó tương ứng với thay đổi ở ghi chú hiện tại mình đang cần sửa. Tuy nhiê, nên hạn chế hành động sửa, tách nội dung của một [[Permanent Note]]!!!
- Phần **Source**: Ghi lại ghi chú nguồn `[[@ wiki, Cronus]]`, về sau sẽ tìm được nguồn một cách dễ dàng. Phần này có thể sẽ update thêm source nếu nó được nói ở một nguồn khác. Ví dụ dưới đây là một thông tin mình cùng đọc được ở cả wiki/Gaia:![[Pasted image 20220227170111.png]]. Nếu là source từ một quyển sách, mình sẽ ghi thêm thông tin trang bao nhiêu (`p.trang`) ngay sau đường link dẫn đến sách ![[Pasted image 20220227171619.png]]
- Phần **Relate**: Phần này giúp cho ghi chú hiện tại của bạn có một ngữ cảnh rõ ràng, và bạn cũng dễ dàng tìm lại các ghi chú liên quan để hỗ trợ việc viết và hiểu ghi chú hơn.
![[Pasted image 20220227170448.png]]


### Ghi chú loại 2: 
Các ghi chú về tên sự vật, hiện tượng mình sẽ xếp thuộc loại Garden và không có ID ở đầu, những ghi chú này thường được các ghi chú loại 1 nhắc đến, mình sẽ tổng hợp các ghi chú đó và nó tự hóa thành ghi chú garden sau đó. Các ghi chú này thường sẽ tích hợp nhiều `aliases` ở phần header YAML của file mardown.

Các ghi chú Garden
![[Pasted image 20220227165248.png]]

aliases trong YAML header
![[Pasted image 20220227171940.png]]

Nội dung ghi chú sẽ là một bảng tổng hợp, tập hợp nhiều **cây ghi chú**
![[Pasted image 20220227170744.png]]


Ở chế độ view ở [[Obsidian]] sẽ như này
![[Pasted image 20220227170927.png]]
![[Pasted image 20220227171007.png]]

