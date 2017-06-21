## Errors in test Q1 USING EXACT FORMS USED IN COMMISSIONING

### Crossrail

The idea is to pick up some sample issues. Once they are corrected, the fix may
be propogated to other errors.

---
**M-KEY**   RDEL Total Budget/BL
**DM**      FB C72
**ISSUE**   Master shows 37.8/red. compare shows 37.80. current shows 37.8

---

**M-KEY**   Non-Gov Total Budget/BL 
**DM**      FB C135
**ISSUE**   Master shows 0/green. compare shows 7,192.10. current shows <dash>.
It obtains this by linking directly to FB H72. In comare, formula is SUM(H44)
which is the sum of Non-Gov both Revenue and Capital - Baseline. This figures have not
propogated properly in the Q1.

---

**M-KEY**   Total Budget/BL
**DM**      FB C136
**ISSUE**   Master shows 7576.77/green. compares shows 14,768.87. current shows
7,576.8. current obtained by =SUM(C133:C135).

---

**M-KEY**   Non-Gov Total Forecast/BL 
**DM**      FB D135
**ISSUE**   Master shows 84/green. compare shows 7,037.02. current shows 84.0.
It obtains this by linking directly to FB H73. In comare, formula is SUM(H45)
which is the sum of Non-Gov both Revenue and Capital - Forecast. This figures have not
propogated properly in the Q1.

---

**M-KEY**   Total Forecast
**DM**      FB D136
**ISSUE**   Master shows 7581.504952/green. compares shows 14,534.52. current shows
7,581.5. current obtained by =SUM(C133:C135).

