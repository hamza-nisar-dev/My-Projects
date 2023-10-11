import paypalrestsdk
from paypalrestsdk import BillingPlan
import logging
paypalrestsdk.configure({
  "mode": "live", # sandbox or live
  "client_id": "AQZOPuRug5f8YVWnodKfKW66HagDEw-8I_F5r-8HI7zmkGB90RWi9IsEewH7zRzDPVcx7M02gD_uggIU",
  "client_secret": "EPnax0sjn4INvphP-kLGaRYVP3VxkMsDaF4itJBkJXe9dQ9jtyGPiC2WOPR-bz0FfyGANWNS1dgPsbx3" })
billing_plan = BillingPlan({
    "description": "🔑 3 MONTH ACCESS VIP 🔑  £30",
    "merchant_preferences": {
        "auto_bill_amount": "yes",
        "cancel_url": "http://www.cancel.com",
        "initial_fail_amount_action": "continue",
        "max_fail_attempts": "0",
        "return_url": "https://3e5a-167-71-65-85.eu.ngrok.io/subscribe",
         "setup_fee": {
            "currency": "GBP",
            "value": "30"
        }
    },
    "name": "Better WinningsVIP",
    "payment_definitions": [
        {
            "amount": {
                "currency": "GBP",
                "value": "30"
            },
            "cycles": "0",
            "frequency": "MONTH",
            "frequency_interval": "3",
            "name": "🔑 3 MONTH ACCESS VIP 🔑  £30",
            "type": "REGULAR"
        }],
    "type": "INFINITE"
})
if billing_plan.create():
    billing_plan.activate()
    print("Billing Plan [%s] created successfully" % (billing_plan.id))
else:
    print(billing_plan.error)