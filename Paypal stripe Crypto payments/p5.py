import paypalrestsdk
from paypalrestsdk import BillingAgreement
import logging

logging.basicConfig(level=logging.INFO)
paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AUCzUxdYUtNUfRnJwQ5UD6J_CcV8zu_oPGXfraz6eYWz3FtLjsKizUmV7OR_oFyvm6OU-0SvPJdmvuWZ",
  "client_secret": "EC6vJsJYFz2KM08uPN4E-1J11uLqYbo43YzDV111qlL1JZnmY2uCKT2PufaR9V8Ovfp2WmBpciwSMtxA" })

payment_token="EC-59636001YC8176622"
billing_agreement_response = BillingAgreement.execute(payment_token)
print(billing_agreement_response.id)