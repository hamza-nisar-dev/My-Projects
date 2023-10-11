import paypalrestsdk
from paypalrestsdk import BillingPlan, ResourceNotFound


from paypalrestsdk import BillingAgreement, ResourceNotFound
paypalrestsdk.configure({
  "mode": "live", # sandbox or live
  "client_id": "ASmykyYYX7erjW9a50hEvfXoWRJUQUaw1FANt5jgvqBozeT5ktVSCvnb-wuntz-kP4bB_5GbBFol2wf3",
  "client_secret": "ENuCh8j63Sqw_MFaaty8VX43vuXBSNXAaj4Ol_VJA2rfTg3rRe70UgR4C8FMZVIPXra7IBCz8U9mvWbk" })



try:
    billing_plan = BillingPlan.find("P-8TR43224GH324102KMCYBFRA")
    print(billing_plan)

except ResourceNotFound as error:
    print("Billing Plan Not Found")