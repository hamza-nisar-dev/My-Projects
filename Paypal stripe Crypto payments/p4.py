import paypalrestsdk
from paypalrestsdk import BillingAgreement
import logging
from datetime import datetime, timedelta
logging.basicConfig(level=logging.INFO)
paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AUCzUxdYUtNUfRnJwQ5UD6J_CcV8zu_oPGXfraz6eYWz3FtLjsKizUmV7OR_oFyvm6OU-0SvPJdmvuWZ",
  "client_secret": "EC6vJsJYFz2KM08uPN4E-1J11uLqYbo43YzDV111qlL1JZnmY2uCKT2PufaR9V8Ovfp2WmBpciwSMtxA" })
a=(datetime.now()+ timedelta(hours=1)).replace(microsecond=0).isoformat()
a=a+"Z"
print(a)
billing_agreement = BillingAgreement({
    "name": "Fast Speed Agreement",
    "description": "Agreement for Fast Speed Plan",
    "start_date": a,
    "plan": {
        "id": "P-9AN08042TF186922CX2EXKQQ"
    },
    "payer": {
        "payment_method": "paypal"
    }
})
if billing_agreement.create():
    print("Billing Agreement created successfully")
    print(billing_agreement)
    for link in billing_agreement.links:
        if link.rel == "approval_url":
            approval_url = link.href
            print(
                "For approving billing agreement, redirect user to\n [%s]" % (approval_url))
            ass=approval_url.split("&token=")
            ass=ass[1].split("]")
            ass=ass[0].strip()
            print(ass)
else:
    print(billing_agreement.error)

# After user approves the agreement, call execute with the payment token appended to
# the redirect url to execute the billing agreement.
# https://github.paypal.com/pages/lkutch/paypal-developer-docs/api/#execute-an-agreement
