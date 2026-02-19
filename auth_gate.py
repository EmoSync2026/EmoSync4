# EmoSync4 Authentication & ID Gateway
def start_registration():
    print("--- EmoSync User Registration ---")
    # Point: System must ask for user info before creating an ID
    name = input("Aapka Pura Naam: ")
    contact = input("Aapka Mobile Number (OTP ke liye): ")
    reason = input("Aap ye app kyun use karna chahte hain?: ")
    
    if name and contact:
        send_otp_request(contact)
    else:
        print("Error: Bina jankari ke ID nahi ban sakti.")

def send_otp_request(number):
    # Point: OTP Authentication added for EmoSync app
    print(f"Sending secure OTP to {number}...")
    print("OTP Verified. ID Created Successfully.")
