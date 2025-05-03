import uuid
import requests
import hmac
import hashlib
from ...global_config import momo_config

def generate_transaction_hash(
    wallet_address: str,
    amount: int,
    salt: bytes = momo_config['transaction_salt'],
) -> str:
    if not isinstance(wallet_address, str):
        raise ValueError("Sender and receiver hashes must be strings")
    if len(wallet_address) != 64:
        raise ValueError("Address must be 64 characters long")
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    if not isinstance(salt, bytes) or len(salt) != 4:
        raise ValueError("Salt must be 4 bytes")
    
    transaction_string = f"{wallet_address}{amount}".encode("utf-8")
    return hashlib.sha256(transaction_string + salt).hexdigest()

class Momo:
    def __init__(self):
        self.endpoint = momo_config["endpoint"]
        self.accessKey = "F8BBA842ECF85"
        self.secretKey = "K951B6PE1waDMi640xX08PD3vg6EkVlz"
        self.partnerCode = "MOMO"
        self.partnerName = "MoMo Payment"
        self.storeId = "Almacenar"
        self.requestType = "payWithMethod"
        self.redirectUrl = momo_config["redirect_url"]
        self.ipnUrl = momo_config["ipn_url"]
        self.lang = "vi"
        self.autoCapture = True

    def create_payment_url(self, amount: int, wallet_address: str, message: str) -> str:
        self.orderId = generate_transaction_hash(wallet_address, amount)
        self.requestId = str(uuid.uuid4())
        self.orderInfo = message
        self.extraData = ""
        self.orderGroupId = ""

        raw_signature = (
            f"accessKey={self.accessKey}&amount={amount}&extraData={self.extraData}"
            f"&ipnUrl={self.ipnUrl}&orderId={self.orderId}&orderInfo={self.orderInfo}"
            f"&partnerCode={self.partnerCode}&redirectUrl={self.redirectUrl}"
            f"&requestId={self.requestId}&requestType={self.requestType}"
        )

        # Generate HMAC SHA256 signature
        self.signature = hmac.new(
            self.secretKey.encode('ascii'),
            raw_signature.encode('ascii'),
            hashlib.sha256
        ).hexdigest()

        data = {
            'partnerCode': self.partnerCode,
            'orderId': self.orderId,
            'partnerName': self.partnerName,
            'storeId': self.storeId,
            'ipnUrl': self.ipnUrl,
            'amount': str(amount),
            'lang': self.lang,
            'requestType': self.requestType,
            'redirectUrl': self.redirectUrl,
            'autoCapture': self.autoCapture,
            'orderInfo': self.orderInfo,
            'requestId': self.requestId,
            'extraData': self.extraData,
            'signature': self.signature,
            'orderGroupId': self.orderGroupId
        }

        response = requests.post(
            self.endpoint,
            json = data,
        )

        if response.status_code != 200:
            raise Exception(f"Failed to create MoMo payment URL: {response.text}")
            
        return response.json().get('payUrl')
