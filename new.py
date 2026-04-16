import random
import streamlit as st

# Page title – makes it feel like a real game!
st.title("🎲 Dice Rolling Game!")
st.write("Enter how many rolls you want, then click 'Ready' for each one. Wrong click? No roll lost!")

# Input for number of rolls
roll = st.number_input("How many times do you wanna roll?", min_value=1, max_value=20, value=5)

# Track current roll number
if 'current_roll' not in st.session_state:
    st.session_state.current_roll = 0
if 'rolls_left' not in st.session_state:
    st.session_state.rolls_left = roll

# Button to "ready" (like your y/n input)
if st.button("Ready? Click to Roll! (or close tab to quit)"):
    st.session_state.current_roll += 1
    
    if st.session_state.current_roll > roll:
        st.error("All rolls done! Refresh to play again.")
    else:
        # Roll the dice (like your random code)
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        result = (x, y)
        
        # Show result (like your print)
        st.success(f"🎲 Roll #{st.session_state.current_roll}: ({result[0]}, {result[1]})")
        st.balloons()  # Fun animation – feels real!
        
        # Update rolls left
        st.session_state.rolls_left -= 1
        st.info(f"Rolls left: {st.session_state.rolls_left}")

# End message
if st.session_state.current_roll >= roll:
    st.balloons()
    st.write(f"🎉 Your {roll} rolls are finished. Thank you for choosing us...")

# Sidebar for "n" quit (optional)
st.sidebar.write("Want to stop early? Just close the tab! 🚪")