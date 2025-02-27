import streamlit as st
from PIL import Image

def convert_units(value, from_unit, to_unit, conversion_factors):
    # Base unit tak convert karo
    base_value = value * conversion_factors[from_unit]
    # Base unit se target unit tak convert karo
    result = base_value / conversion_factors[to_unit]
    return result

def image_to_base64(image):
    import base64
    from io import BytesIO
    
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def main():
    # Page configuration update
    st.set_page_config(
        page_title="Unit Converter Pro",
        layout="centered",
        initial_sidebar_state="expanded",
        page_icon="♔"  # Streamlit style black crown emoji
    )
    
    # Enhanced styling
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
            border-radius: 10px;
            background-color: #f0f2f6;
        }
        .app-logo {
            width: 180px;  # Logo ki width barha di
            height: 100px;  # Logo ki height barha di
            object-fit: contain;
            display: inline-block;
            vertical-align: middle;
            margin-right: 10px;
            background-color: white;  # Logo ke peeche white background
            padding: 10px;  # Logo ke around padding
            border-radius: 8px;  # Logo ke corners round
        }
        .app-header {
            text-align: center;
            padding: 25px 20px;
            background: linear-gradient(135deg, #00416A, #E4E5E6);  # Naya gradient background
            border-radius: 10px;
            margin-bottom: 30px;
            color: white;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);  # Shadow ko enhance kiya
        }
        .header-content {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 15px;
            gap: 25px;  # Gap barha diya logo aur text ke darmiyaan
        }
        .logo-text {
            font-size: 46px;  # Font size barha diya
            font-weight: bold;
            letter-spacing: 2px;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
            color: #ffffff;
        }
        .creator-text {
            font-size: 18px;  # Font size barha diya
            font-style: italic;
            opacity: 0.9;
            padding-top: 10px;
            border-top: 2px solid rgba(255,255,255,0.3);  # Border ko enhance kiya
            width: 80%;
            margin: 10px auto 0;
        }
        .category-section {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin: 20px 0;
        }
        .result-section {
            background-color: #e8f0fe;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin: 20px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Load logo image
    logo_image = Image.open("assets/logo.png")
    
    # App header with logo
    st.markdown(f"""
        <div class="app-header">
            <div class="header-content">
                <img src="data:image/png;base64,{image_to_base64(logo_image)}" class="app-logo" alt="Unit Converter Logo">
                <div class="logo-text">Unit Converter Pro</div>
            </div>
            <div class="creator-text">Build With ❤️ By Syed Ghulam Mustafa</div>
        </div>
    """, unsafe_allow_html=True)

    # Categories with more options
    categories = {
        "Length": {
            "Kilometer": 1000,
            "Meter": 1,
            "Centimeter": 0.01,
            "Millimeter": 0.001,
            "Mile": 1609.34,
            "Yard": 0.9144,
            "Foot": 0.3048,
            "Inch": 0.0254,
            "Nautical Mile": 1852
        },
        "Weight": {
            "Tonne": 1000,
            "Kilogram": 1,
            "Gram": 0.001,
            "Milligram": 0.000001,
            "Pound": 0.453592,
            "Ounce": 0.0283495,
            "Stone": 6.35029
        },
        "Temperature": {
            "Celsius": "C",
            "Fahrenheit": "F",
            "Kelvin": "K"
        },
        "Area": {
            "Square Meter": 1,
            "Square Kilometer": 1000000,
            "Square Mile": 2589988.11,
            "Square Yard": 0.836127,
            "Square Foot": 0.092903,
            "Acre": 4046.86,
            "Hectare": 10000
        },
        "Volume": {
            "Cubic Meter": 1,
            "Liter": 0.001,
            "Milliliter": 0.000001,
            "Gallon": 0.00378541,
            "Quart": 0.000946353,
            "Cup": 0.000236588
        },
        "Time": {
            "Second": 1,
            "Minute": 60,
            "Hour": 3600,
            "Day": 86400,
            "Week": 604800,
            "Month": 2592000,
            "Year": 31536000
        }
    }

    with st.container():
        st.markdown('<div class="category-section">', unsafe_allow_html=True)
        # Category selection
        category = st.selectbox("Select Category", list(categories.keys()))
        
        # Input aur output units k columns
        col1, col2 = st.columns(2)

        with col1:
            from_unit = st.selectbox("From", list(categories[category].keys()))
            value = st.number_input("Enter Value", value=1.0)

        with col2:
            to_unit = st.selectbox("To", list(categories[category].keys()))
        st.markdown('</div>', unsafe_allow_html=True)

    # Conversion logic
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = ((value - 32) * 5/9) + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = ((value - 273.15) * 9/5) + 32
        else:
            result = value
    else:
        result = convert_units(value, from_unit, to_unit, categories[category])

    # Enhanced result display
    st.markdown('<div class="result-section">', unsafe_allow_html=True)
    st.markdown("### Conversion Result")
    st.markdown(f"<h2>{value:,.6g} {from_unit} = {result:,.6g} {to_unit}</h2>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <div style='text-align: center; margin-top: 30px; padding: 20px; background-color: #f8f9fa; border-radius: 10px;'>
            <p style='color: #666; font-size: 14px;'>© 2024 Unit Converter Pro | All Rights Reserved</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 