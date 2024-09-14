cow_strike/
│
├── models/
│   ├── cow.py           # Model สำหรับจัดการข้อมูลของวัวแต่ละสี
│   
│
├── views/
│   ├── view.py           # View สำหรับแสดงผลและรับข้อมูลจากผู้ใช้
│                            
│
├── controllers/
│   └── controller.py     # Controller สำหรับควบคุมการทำงานระหว่าง Model และ View
│
├── main.py               # จุดเริ่มต้นของโปรแกรม (การแสดงหน้าจอหลัก)
└── README.md             # อธิบายการทำงานของโปรแกรม


# Cow Strike Registration System

## วิธีการทำงาน
โปรแกรมนี้ใช้แนวคิด MVC (Model-View-Controller) ในการลงทะเบียนวัวเข้าสู่ฟาร์ม โดยมีการแยกส่วนหน้าที่ชัดเจนระหว่างการจัดการข้อมูล (Model), การแสดงผล (View), และการควบคุมการทำงาน (Controller)

### การทำงานของระบบ
1. **View**: รับข้อมูลสีของวัว และข้อมูลเฉพาะของวัวแต่ละสี
2. **Controller**: จัดการการลงทะเบียนวัว และส่งข้อมูลไปยัง Model
3. **Model**: จัดเก็บข้อมูลของวัวและฟาร์ม รวมถึงตรวจสอบข้อกำหนดต่างๆ ของฟาร์ม

### วิธีใช้งาน
1. รันไฟล์ `main.py`
2. เลือกสีของวัว และกรอกข้อมูลที่เกี่ยวข้อง
3. ระบบจะตรวจสอบและลงทะเบียนวัวเข้าสู่ฟาร์มตามข้อมูลที่กรอก

### ข้อกำหนด
- วัวแต่ละสีจะมีข้อกำหนดต่างกันตามที่โจทย์ระบุ
- ฟาร์มแต่ละแห่งจะรับวัวเพียงสีเดียวเท่านั้น
