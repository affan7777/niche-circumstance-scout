import streamlit as st

# User inputs
st.title("📈 Niche Opportunity Scout")
st.subheader("Find side hustles based on trending micro-investments!")

location = st.text_input("🌍 Your Location", "Los Angeles, CA")
budget = st.number_input("💸 Your Budget ($)", min_value=10, max_value=10000, value=500, step=10)
interests = st.multiselect(
    "🎯 Your Interests",
    ["Tech Gadgets", "Home Decor", "Fitness", "Pet Accessories", "DIY"],
    default=["Tech Gadgets", "Home Decor"]
)

# Sample trending items (mock data)
trending_items = [
    {"name": "Mini Projectors", "category": "Tech Gadgets", "cost": 120, "resale_price": 180, "trend_score": 90},
    {"name": "Custom LED Lamps", "category": "Home Decor", "cost": 35, "resale_price": 60, "trend_score": 75},
    {"name": "Resistance Bands Set", "category": "Fitness", "cost": 20, "resale_price": 35, "trend_score": 60},
    {"name": "AI Pet Feeders", "category": "Pet Accessories", "cost": 200, "resale_price": 280, "trend_score": 85},
    {"name": "Wall Collage Kits", "category": "Home Decor", "cost": 10, "resale_price": 25, "trend_score": 45}
]

# Filtering and scoring
def evaluate_opportunities(budget, interests):
    results = []
    for item in trending_items:
        if item["category"] in interests and item["cost"] <= budget:
            profit = item["resale_price"] - item["cost"]
            roi = (profit / item["cost"]) * 100
            score = (roi * 0.4) + (item["trend_score"] * 0.6)
            results.append({
                "name": item["name"],
                "category": item["category"],
                "cost": item["cost"],
                "profit": profit,
                "roi": round(roi, 2),
                "score": round(score, 2)
            })
    return sorted(results, key=lambda x: x["score"], reverse=True)

# Show recommendations
if st.button("🔍 Find Opportunities"):
    results = evaluate_opportunities(budget, interests)
    if results:
        for item in results:
            st.markdown(f"### 💡 {item['name']}")
            st.write(f"- Category: {item['category']}")
            st.write(f"- Cost: ${item['cost']}")
            st.write(f"- Estimated Profit: ${item['profit']}")
            st.write(f"- ROI: {item['roi']}%")
            st.write(f"- Score: {item['score']}")
            st.markdown("---")
    else:
        st.warning("No matching opportunities found within your budget and interests.")
