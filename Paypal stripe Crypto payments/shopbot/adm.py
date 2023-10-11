from paypalrestsdk import BillingPlan
import paypalrestsdk
paypalrestsdk.configure({
  "mode": "live", # sandbox or live
  "client_id": "ASmykyYYX7erjW9a50hEvfXoWRJUQUaw1FANt5jgvqBozeT5ktVSCvnb-wuntz-kP4bB_5GbBFol2wf3",
  "client_secret": "ENuCh8j63Sqw_MFaaty8VX43vuXBSNXAaj4Ol_VJA2rfTg3rRe70UgR4C8FMZVIPXra7IBCz8U9mvWbk" })


history = BillingPlan.all(
    {"status": "CREATED", "page_size": 5, "page": 1, "total_required": "yes"})
print(history)

print("List BillingPlan:")
for plan in history.plans:
    print("  -> BillingPlan[%s]" % (plan.id))