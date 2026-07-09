import streamlit as st
import math

st.title("最新優惠")
st.write("這裡顯示所有個人防護商品")
# 模擬商品資料
products = [
    {"id": i, "name": f"商品{i}", "price": 100+i*10, "old_price": 120+i*10,
     "stock": 10+i, "img": "https://via.placeholder.com/200", "category": "電動工具" if i%2==0 else "手工具"}
    for i in range(1, 31)
]

# Header
st.markdown(f"<div style='display:flex;justify-content:space-between;align-items:center;background:#f5f5f5;padding:10px;'>"
            f"<div style='font-size:24px;font-weight:bold;'>🛠️ 公司Logo</div>"
            f"<div>🛒 購物車 <span style='background:red;color:white;border-radius:50%;padding:2px 6px'>{len(st.session_state.get('cart',[]))}</span></div></div>",
            unsafe_allow_html=True)

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
        st.image(p["img"], caption=p["name"])
        st.write(f"💲 {p['price']} 元 (原價 {p['old_price']} 元)")
        st.write(f"庫存: {p['stock']} 件")
        if st.button(f"加入購物車: {p['name']}", key=f"btn_{p['id']}"):
            st.session_state.setdefault("cart", []).append(p)
            st.success(f"✅ 已加入購物車: {p['name']}")
