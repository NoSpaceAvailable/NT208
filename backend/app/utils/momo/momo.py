import uuid
import requests
import hmac
import hashlib
from base64 import b64encode
from app.global_config import history_config, momo_config
from app.utils.timing import *

def generate_transaction_hash(
    sender_hash: str,
    receiver_hash: str,
    amount: int,
    timestamp: str,
    salt: bytes = history_config['TRANSACTION_SALT'],
) -> str:
    if len(sender_hash) != 64 or len(receiver_hash) != 64:
        raise ValueError("Sender and receiver hashes must be 64 characters long")
    if not isinstance(sender_hash, str) or not isinstance(receiver_hash, str):
        raise ValueError("Sender and receiver hashes must be strings")
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    if not isinstance(salt, bytes) or len(salt) != 4:
        raise ValueError("Salt must be 4 bytes")
    
    transaction_string = f"{sender_hash}{receiver_hash}{amount}{timestamp}".encode("utf-8")
    
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

    def create_payment_url(self, amount: int, 
                           wallet_address: str, 
                           message: str, 
                           timestamp: str = get_current_time()) -> str:
        self.orderId = generate_transaction_hash(wallet_address, wallet_address, amount, timestamp)
        self.requestId = str(uuid.uuid4())
        self.orderInfo = message
        self.extraData = b64encode(timestamp.encode("utf-8")).decode("utf-8")
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
