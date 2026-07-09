import streamlit as st
import math

st.set_page_config(page_title="電商網站 Demo", layout="wide")

# 初始化狀態
if "cart" not in st.session_state:
    st.session_state.cart = []

# 模擬商品資料
products = [
    {"id": i, "name": f"商品{i}", "price": 100+i*10, "old_price": 120+i*10,
     "stock": 10+i, "img": "https://via.placeholder.com/200", "category": "電動工具" if i%2==0 else "手工具"}
    for i in range(1, 31)
]

# CSS 樣式
st.markdown("""
<style>
.container {max-width:1440px; margin:0 auto; padding:0 16px;}
.header {display:flex; justify-content:space-between; align-items:center; background:#222; color:#fff; padding:15px;}
.logo {font-size:28px; font-weight:bold;}
.badge {background:red; color:white; border-radius:50%; padding:2px 6px; font-size:12px; margin-left:5px;}
.hero {background:#f0f0f0; padding:40px; text-align:center; margin-bottom:20px;}
.product-card {border:1px solid #ccc; padding:10px; margin:10px; border-radius:8px; background:#fff;}
.product-card img {width:100%; transition:transform 0.3s;}
.product-card img:hover {transform:scale(1.05);}
.price {color:red; font-weight:bold;}
.old-price {text-decoration:line-through; color:#888;}
@media (max-width:768px) {.product-card {width:100%;}}
@media (min-width:768px) and (max-width:1024px) {.product-card {width:45%;}}
@media (min-width:1024px) {.product-card {width:30%;}}
</style>
""", unsafe_allow_html=True)

# Header Banner
st.markdown(f"<div class='header'><div class='logo'>🛠️ 公司名稱</div><div>🛒 購物車 <span class='badge'>{len(st.session_state.cart)}</span></div></div>", unsafe_allow_html=True)

# Hero 區塊
st.markdown("<div class='hero'><h2>🎉 最新優惠專區</h2><p>夏季促銷 | 新品上架 | VIP專屬優惠</p></div>", unsafe_allow_html=True)

# 搜尋與排序
query = st.text_input("🔍 搜尋商品")
sort_option = st.selectbox("排序方式", ["預設", "價格低→高", "價格高→低"])
page = st.number_input("頁碼", min_value=1, max_value=math.ceil(len(products)/12), value=1)

# 篩選商品
filtered = [p for p in products if query in p["name"]] if query else products
if sort_option == "價格低→高":
    filtered.sort(key=lambda x: x["price"])
elif sort_option == "價格高→低":
    filtered.sort(key=lambda x: -x["price"])

# 分頁
per_page = 12
start = (page-1)*per_page
end = start+per_page
page_products = filtered[start:end]

# 商品卡片
cols = st.columns(3)
for idx, p in enumerate(page_products):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class='product-card'>
            <img src='{p['img']}'>
            <h3>{p['name']}</h3>
            <p><span class='old-price'>{p['old_price']} 元</span> <span class='price'>{p['price']} 元</span></p>
            <p>庫存: {p['stock']} 件</p>
        </div>
        """, unsafe_allow_html=True)
        qty = st.number_input(f"數量 ({p['name']})", min_value=1, max_value=p['stock'], key=f"qty_{p['id']}")
        if st.button(f"加入購物車: {p['name']}", key=f"btn_{p['id']}"):
            st.session_state.cart.append({"name": p["name"], "price": p["price"], "quantity": qty})
            st.success(f"✅ 已加入購物車: {p['name']} x {qty}")
