"""
Cấu hình Danh mục và Mặt hàng Giao dịch tại Sở Giao dịch Hàng hóa Việt Nam (MXV).
Bao gồm 4 nhóm hàng hóa chính thức: Nông sản, Nguyên liệu công nghiệp, Kim loại, Năng lượng.
"""

EXCHANGE_RATE = 25400

MXV_INFO = {
    # 1. Nhóm Nông sản (Grain & Oilseed - Sàn CBOT)
    "Đậu tương": {
        "ticker": "ZS=F",
        "unit_full": "Dạ (Bushel)",
        "unit": "Dạ",
        "multiplier": EXCHANGE_RATE / 100,
        "category": "Nông sản",
        "margin": 45_000_000,
        "lot_size": 1000
    },
    "Khô đậu tương": {
        "ticker": "ZM=F",
        "unit_full": "Tấn ngắn (Short Ton)",
        "unit": "Tấn",
        "multiplier": EXCHANGE_RATE,
        "category": "Nông sản",
        "margin": 45_000_000,
        "lot_size": 100
    },
    "Dầu đậu tương": {
        "ticker": "ZL=F",
        "unit_full": "Pound (lb)",
        "unit": "Pound",
        "multiplier": EXCHANGE_RATE / 100,
        "category": "Nông sản",
        "margin": 40_000_000,
        "lot_size": 60000
    },
    "Ngô": {
        "ticker": "ZC=F",
        "unit_full": "Dạ (Bushel)",
        "unit": "Dạ",
        "multiplier": EXCHANGE_RATE / 100,
        "category": "Nông sản",
        "margin": 35_000_000,
        "lot_size": 1000
    },
    "Lúa mì Chicago": {
        "ticker": "ZW=F",
        "unit_full": "Dạ (Bushel)",
        "unit": "Dạ",
        "multiplier": EXCHANGE_RATE / 100,
        "category": "Nông sản",
        "margin": 50_000_000,
        "lot_size": 1000
    },
    "Lúa mì Kansas (HRW)": {
        "ticker": "KE=F",
        "unit_full": "Dạ (Bushel)",
        "unit": "Dạ",
        "multiplier": EXCHANGE_RATE / 100,
        "category": "Nông sản",
        "margin": 45_000_000,
        "lot_size": 1000
    },
    "Gạo thô": {
        "ticker": "ZR=F",
        "unit_full": "Tạ (Cwt)",
        "unit": "Tạ",
        "multiplier": EXCHANGE_RATE / 100,
        "category": "Nông sản",
        "margin": 35_000_000,
        "lot_size": 2000
    },
    "Yến mạch": {
        "ticker": "ZO=F",
        "unit_full": "Dạ (Bushel)",
        "unit": "Dạ",
        "multiplier": EXCHANGE_RATE / 100,
        "category": "Nông sản",
        "margin": 30_000_000,
        "lot_size": 1000
    },

    # 2. Nhóm Nguyên liệu công nghiệp (Softs & Industrial - Sàn ICE)
    "Cà phê": {
        "ticker": "KC=F",
        "unit_full": "Pound (lb)",
        "unit": "Pound",
        "multiplier": EXCHANGE_RATE / 100,
        "category": "Nguyên liệu công nghiệp",
        "margin": 85_000_000,
        "lot_size": 37500
    },
    "Đường 11": {
        "ticker": "SB=F",
        "unit_full": "Pound (lb)",
        "unit": "Pound",
        "multiplier": EXCHANGE_RATE / 100,
        "category": "Nguyên liệu công nghiệp",
        "margin": 30_000_000,
        "lot_size": 112000
    },
    "Ca cao": {
        "ticker": "CC=F",
        "unit_full": "Tấn (Tonne)",
        "unit": "Tấn",
        "multiplier": EXCHANGE_RATE,
        "category": "Nguyên liệu công nghiệp",
        "margin": 150_000_000,
        "lot_size": 10
    },
    "Bông sợi": {
        "ticker": "CT=F",
        "unit_full": "Pound (lb)",
        "unit": "Pound",
        "multiplier": EXCHANGE_RATE / 100,
        "category": "Nguyên liệu công nghiệp",
        "margin": 60_000_000,
        "lot_size": 50000
    },
    "Nước cam đông lạnh": {
        "ticker": "OJ=F",
        "unit_full": "Pound (lb)",
        "unit": "Pound",
        "multiplier": EXCHANGE_RATE / 100,
        "category": "Nguyên liệu công nghiệp",
        "margin": 60_000_000,
        "lot_size": 15000
    },
    
    # 3. Nhóm Kim loại (Metals - Sàn COMEX & NYMEX)
    "Vàng": {
        "ticker": "GC=F",
        "unit_full": "Ounce (Troy oz)",
        "unit": "Ounce",
        "multiplier": EXCHANGE_RATE,
        "category": "Kim loại",
        "margin": 230_000_000,
        "lot_size": 100
    },
    "Bạc": {
        "ticker": "SI=F",
        "unit_full": "Ounce (Troy oz)",
        "unit": "Ounce",
        "multiplier": EXCHANGE_RATE,
        "category": "Kim loại",
        "margin": 200_000_000,
        "lot_size": 5000
    },
    "Đồng": {
        "ticker": "HG=F",
        "unit_full": "Pound (lb)",
        "unit": "Pound",
        "multiplier": EXCHANGE_RATE,
        "category": "Kim loại",
        "margin": 120_000_000,
        "lot_size": 25000
    },
    "Bạch kim": {
        "ticker": "PL=F",
        "unit_full": "Ounce (Troy oz)",
        "unit": "Ounce",
        "multiplier": EXCHANGE_RATE,
        "category": "Kim loại",
        "margin": 90_000_000,
        "lot_size": 50
    },
    "Palađi": {
        "ticker": "PA=F",
        "unit_full": "Ounce (Troy oz)",
        "unit": "Ounce",
        "multiplier": EXCHANGE_RATE,
        "category": "Kim loại",
        "margin": 150_000_000,
        "lot_size": 100
    },

    # 4. Nhóm Năng lượng (Energy - Sàn NYMEX & ICE)
    "Dầu thô (WTI)": {
        "ticker": "CL=F",
        "unit_full": "Thùng (Barrel)",
        "unit": "Thùng",
        "multiplier": EXCHANGE_RATE,
        "category": "Năng lượng",
        "margin": 150_000_000,
        "lot_size": 1000
    },
    "Dầu Brent": {
        "ticker": "BZ=F",
        "unit_full": "Thùng (Barrel)",
        "unit": "Thùng",
        "multiplier": EXCHANGE_RATE,
        "category": "Năng lượng",
        "margin": 160_000_000,
        "lot_size": 1000
    },
    "Khí tự nhiên": {
        "ticker": "NG=F",
        "unit_full": "MMBtu",
        "unit": "MMBtu",
        "multiplier": EXCHANGE_RATE,
        "category": "Năng lượng",
        "margin": 90_000_000,
        "lot_size": 10000
    },
    "Xăng pha chế": {
        "ticker": "RB=F",
        "unit_full": "Gallon",
        "unit": "Gallon",
        "multiplier": EXCHANGE_RATE / 100,
        "category": "Năng lượng",
        "margin": 110_000_000,
        "lot_size": 42000
    },
    "Dầu sưởi (DO)": {
        "ticker": "HO=F",
        "unit_full": "Gallon",
        "unit": "Gallon",
        "multiplier": EXCHANGE_RATE / 100,
        "category": "Năng lượng",
        "margin": 120_000_000,
        "lot_size": 42000
    }
}

CATEGORIES = ["Nông sản", "Nguyên liệu công nghiệp", "Kim loại", "Năng lượng"]

QUICK_ITEMS = [
    "Đậu tương", "Ngô", "Lúa mì Chicago", "Khô đậu tương", "Dầu đậu tương", "Gạo thô",
    "Cà phê", "Đường 11", "Ca cao", "Bông sợi",
    "Vàng", "Bạc", "Đồng", "Bạch kim",
    "Dầu thô (WTI)", "Dầu Brent", "Khí tự nhiên", "Xăng pha chế"
]
