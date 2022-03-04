---
outgoing_links:
  - Zet/Hệ số ELO
title: Cách tính toán hệ số ELO
UID: 210826213627
tags:
  - 'created/2021/Aug/26'
  - 'permanent/concept'
aliases:
  - Cách tính toán hệ số ELO
publish: true
---
# Cách tính toán hệ số ELO

## Notes:
Ví dụ hai người chơi [[Cờ Vua]]
- người 1 có điểm số [[Hệ số ELO]] là Ra
- người 2 có điểm số Elo là Rb

```
Ea=Qa/(Qa+Qb)
Eb=Qb/(Qa+Qb)
```
với
```
Qa=10^(Ra/400)
Qb= 10^(Rb/400)
```

Khi kết thúc trận đấu, với các kết quả:
- Thắng: được 1 điểm
- Hòa được 0.5 điểm
- Thua được 0 điểm

Hệ số ELO mới sau khi kết thúc ván cờ
```
Ra' = Ra + K(Aa-Ea)
Rb' = Rb + K(Ab-Eb)
```
Với K là hệ số kiểm soát lạm phát.
**- Hệ số K**
+ K = 25 dành cho kỳ thủ mới có cường số dưới 1600
+ K = 20 dành cho kỳ thủ mới có cường số dưới 2000
+ K = 15 dành cho kỳ thủ có cường số dưới 2400.
+ K = 10 dành cho kỳ thủ có cường số trên 2400

Ví dụ kỳ thủ A là 1613, của kỳ thủ B là 1609, K = 20
- Ea = 0.506
- Eb = 0.494.
Kỳ thủ A bị thua kỳ thủ B. điểm số mới
- Ra’ = 1613 + 20(0 – 0.506) = 1603
- Rb’ = 1609 + 20(1 – 0.494) = 1619

## Ideas & thoughts:

## Created:
- [[2021-08-26]]
