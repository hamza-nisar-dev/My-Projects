from paypalrestsdk import Payment
import paypalrestsdk
paypalrestsdk.configure({
  "mode": "live", # sandbox or live
  "client_id": "AXhC301fBtxP4YFx5K_BXXPg9SG0zo_ZzbqyIYrreQO7Zy578XWoPKAKQ4N6LBebxZwsPCg-zEQ53cXt",
  "client_secret": "EIi74r61Qt6wzuK0pxQNFIl3I-Ws1uWzWTaK_6CpTXpv08M9Abc7MEt9VZd0-tFSTA0Fm0jcAzF-otPn" })




payment = Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"},
    "redirect_urls": {
        "return_url": "https://t.me/NationForexSignals_bot",
        "cancel_url": "https://t.me/NationForexSignals_bot"},

    "transactions": [{

        "amount": {
            "total": "149.99",
            "currency": "USD"},
        "description": "This is the payment transaction description."}]})

if payment.create():
    for link in payment.links:
        if link.rel == "approval_url":
            approval_url = str(link.href)
    c="{}***{}".format(payment.id,approval_url)
    print(c)
