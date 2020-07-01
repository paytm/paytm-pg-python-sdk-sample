import logging

from SampleData import SampleData

from paytmpg import PaymentDetailsBuilder, PaymentStatusDetailBuilder
from paytmpg import RefundDetailBuilder, RefundStatusDetailBuilder
from paytmpg import MerchantProperty, LibraryConstants
from paytmpg import Payment, Refund

"""
    This class has example of how to initialize and make api calls to hit paytmpg
    servers. Here Merchant will change in objects as per requirement and make api
    calls
"""


def create_txn_token_with_required_params():
    """Merchant can change create_txn_token_with_required_params according to his need
    This method create a PaymentDetail object having all the required parameters
    and call SDK's create TxnToken method to get InitiateTransactionResponseBody
    object having token which will be used in future transactions such as getting
    payment options
    :return: txn_token
    """

    """Channel through which call initiated [enum (APP, WEB, WAP, SYSTEM)]"""
    channel_id = SampleData.get_channel_id()

    """Unique order for each order request"""
    order_id = SampleData.generate_random_string(6)

    """Transaction amount and the currency value"""
    txn_amount = SampleData.get_money()

    """User information contains user details cid : <Mandatory> user unique
    identification with respect to merchant
    """
    user_info = SampleData.get_user_info()

    """paymentDetails object will have all the information required to make
    createTxnToken call
    """
    payment_details = PaymentDetailsBuilder(channel_id, order_id, txn_amount, user_info).build()
    """Making call to SDK method which will return a InitiateTransactionResponse
    object that will contain a token which can be used for validation purpose for
    future transactions
    """
    response = Payment.createTxnToken(payment_details)
    print("Json response :: ", response.get_json_response())
    # print("token:: ", response.get_response_object().get_body().get_txn_token())
    # print("result-code:: ", response.get_response_object().get_body().get_result_info().get_result_code())
    # print("result_status:: ", response.get_response_object().get_body().get_result_info().get_result_status())
    # print("result_msg:: ", response.get_response_object().get_body().get_result_info().get_result_msg())
    """ End of Function """


def create_txn_token_with_paytm_sso_token_and_payment_mode():
    """Merchant can change create_txn_token_with_paytm_sso_token_and_payment_mode according
    to his need.

    This method create a paymentDetails object with required parameters, payment
    modes and PaytmSSOToken. This method calls SDK's createTxnToken method to get
    the InitiateTransactionResponseBody object having token which will be used in
    future transactions such as getting payment options

    Merchant can only use payment modes for this transaction which he will
    specify in this call if these payment modes are applicable on the merchant
    :return: txn token
    """

    """Merchants who want to use PG with Wallet and configure payment-modes for
    accepting payments with paytmSSOTokenS
    """

    """ Channel through which call initiated [enum (APP, WEB, WAP, SYSTEM)] """
    channel_id = SampleData.get_channel_id()

    """ Unique order for each order request """
    order_id = SampleData.generate_random_string(6)

    """ Transaction amount and the currency value """
    txn_amount = SampleData.get_money()

    """User information contains user details cid : <Mandatory> user unique
    identification with respect to merchant
    """
    user_info = SampleData.get_user_info()

    """ Paytm Token for a user """
    paytm_sso_token = SampleData.get_paytm_sso_token()

    """list of the payment modes which needs to enable. If the value provided then
    only listed payment modes are available for transaction
    """
    enable_payment_mode = SampleData.get_enable_payment_modes()

    """list of the payment modes which need to disable. If the value provided then
    all the listed payment modes are unavailable for transaction
    """
    disable_payment_mode = SampleData.get_disable_payment_modes()

    """paymentDetails object will have all the information required to make
    createTxnToken call
    """
    payment_details = PaymentDetailsBuilder(channel_id, order_id, txn_amount, user_info).set_paytm_sso_token(paytm_sso_token)\
        .set_enable_payment_mode(enable_payment_mode).set_disable_payment_mode(disable_payment_mode).build()

    """Making call to SDK method which will return a InitiateTransactionResponse
    object that will contain a token which can be used for validation purpose for
    future transactions
    """
    response = Payment.createTxnToken(payment_details)
    print(response.get_json_response())
    # print(response.get_response_object().get_body().get_txn_token())
    """ End of Function """


def create_txn_token_with_all_params():

    """Merchant can change createTxnTokenwithAllParams according to his need.

    This method create a PaymentDetails object having all the parameters and
    calls SDK's createTxnToken method to get the InitiateTransactionResponseBody
    object having token which will be used in future transactions such as getting
    payment options
    """
    """Merchants who want to use PG with Wallet, configure paymentmodes, send
    Order details and Extended Information for accepting
    payments
    """

    """ Channel through which call initiated [enum (APP, WEB, WAP, SYSTEM)] """
    channel_id = SampleData.get_channel_id()

    """ Unique order for each order request """
    order_id = SampleData.generate_random_string(6)

    """ Transaction amount and the currency value """
    txn_amount = SampleData.get_money()

    """User information contains user details cid : <Mandatory> user unique
    identification with respect to merchant
    """
    user_info = SampleData.get_user_info()

    """ Paytm Token for a user """
    paytm_sso_token = SampleData.get_paytm_sso_token()

    """list of the payment modes which needs to enable. If the value provided then
        only listed payment modes are available for transaction
    """
    enable_payment_mode = SampleData.get_enable_payment_modes()

    """list of the payment modes which need to disable. If the value provided then
    all the listed payment modes are unavailable for transaction
    """
    disable_payment_mode = SampleData.get_disable_payment_modes()

    """ This contain the Goods info for an order. """
    goods = SampleData.get_goods_info()

    """ This contain the shipping info for an order. """
    shipping_info = SampleData.get_shipping_info()

    """ promo_code that user is using for the payment """
    promo_code = SampleData.get_promo_code()

    """ This contain the set of parameters for some additional information """
    extend_info = SampleData.get_extend_info()

    emi_option = SampleData.get_emi_option()
    card_token_required = SampleData.get_card_token_required()

    """PaymentDetail object will have all the information required to make
    createTxnToken call
    """
    payment_details = PaymentDetailsBuilder(channel_id, order_id, txn_amount, user_info)\
        .set_paytm_sso_token(paytm_sso_token).set_enable_payment_mode(enable_payment_mode)\
        .set_disable_payment_mode(disable_payment_mode).set_goods(goods).set_shipping_info(shipping_info)\
        .set_promo_code(promo_code).set_extend_info(extend_info).set_emi_option(emi_option)\
        .set_card_token_required(card_token_required).build()

    """Making call to SDK method which will return a InitiateTransactionResponse
        object that will contain a token which can be used for validation purpose for
        future transactions
    """
    response = Payment.createTxnToken(payment_details)
    print(response.get_json_response())
    # print(response.get_response_object().get_body().get_txn_token())
    """ End of Function """


def get_payment_status():

    """
    Merchant will use getPaymentStatus after complete Payment. This method
    (Mandatory Parameters)require OrderId ID. This will return the status for the
    specific OrderId ID.

    :return:
    """
    """Merchants who want to get TransactionStatus """
    """ Unique order for each order request """
    order_id = "YOUR_ORDER_ID"

    read_timeout = 30*1000

    """PaymentStatusDetail object will have all the information required to make
    getPaymentStatus calls
    """
    payment_status_detail = PaymentStatusDetailBuilder(order_id)\
        .set_read_timeout(read_timeout).build()
    """Making call to SDK method which will return a
    NativeMerchantStatusResponse object that will contain the Transaction
    Status Response regarding the Order Id
    """
    response = Payment.getPaymentStatus(payment_status_detail)
    print(response.get_json_response())
    # print(response.get_response_object().get_body().get_result_info().get_result_msg())
    """ End of Function """


def do_refund():
    """Merchant will use doRefund after complete Payment. This method (Mandatory
    Parameters)require Transaction ID, Transaction Type and Refund Amount. This
    will initiate the refund for the specific Transaction ID.
    :return: None
    """
    """ Unique order for each order request """
    # Order id for which refund request needs to be raised 
    order_id = "YOUR_ORDER_ID"
    """ Unique refund id """
    ref_id = "UNIQUE_REFUND_ID"
    """ Transaction ID returned in Paytm\pg\process\PaymentStatus Api """
    # some old txn_id corresponding to order_id
    txn_id = "PAYTM_TRANSACTION_ID"
    """ Transaction Type for refund """
    txn_type = "REFUND"

    """Refund Amount to be refunded (should not be greater than the Amount paid in the Transaction)"""
    refund_amount = "1"

    """refund object will have all the information required to make refund call"""
    refund = RefundDetailBuilder(order_id, ref_id, txn_id, txn_type, refund_amount)\
        .set_sub_wallet_amount(SampleData.get_sub_wallet_amount())\
        .set_extra_params_map(SampleData.get_extra_params_map()).build()
    """Making call to SDK method which will return a AsyncRefundResponseBody object
    that will contain the Refund Response regarding the Transaction Id
    """
    response = Refund.doRefund(refund)
    print(response.get_json_response())
    # print(response.get_response_object().get_body().get_result_info().get_result_msg())
    """ End of Function """


def set_initial_parameters():
    """ setting parameter which are related to merchant and logging
    :return:
    """
    """Handler which is of file or stream"""
    is_file_handler = False
    if is_file_handler:
        # Your log file path here 
        file_path = "/path/log/file.log"
        mode = "w"
        handler = logging.FileHandler(file_path, mode)
    else:
        handler = logging.StreamHandler()
    """Adding formatter"""
    formatter = logging.Formatter("%(name)s: %(levelname)s: %(message)s")
    handler.setFormatter(formatter)

    MerchantProperty.set_logging_disable(False)
    MerchantProperty.set_log_handler(handler)
    MerchantProperty.set_logging_level(logging.DEBUG)

    environment = LibraryConstants.STAGING_ENVIRONMENT
    # Find your Merchant ID and Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
    mid = "YOUR_MID_HERE"
    merchant_key = "YOUR_KEY_HERE"
    # Website: For Staging - WEBSTAGING, For Production - DEFAULT */
    website = "YOUR_WEBSITE_NAME"
    # Client Id e.g C11
    client_id = "YOUR_CLIENT_ID_HERE"

    callbackUrl = "MERCANT_CALLBACK_URL"
    MerchantProperty.set_callback_url(callbackUrl)

    MerchantProperty.initialize(environment, mid, merchant_key, client_id, website)
    MerchantProperty.set_connect_timeout(80)


def get_refund_status():

    # Order id for which refund status needs to be checked
    order_id = "YOUR_ORDER_ID"

    # Refund id of the refund request for which refund status needs to be checked
    ref_id = "UNIQUE_REFUND_ID"

    """Refund status detail object"""
    refund_status_details = RefundStatusDetailBuilder().set_order_id(order_id).set_ref_id(ref_id).build()
    response = Refund.getRefundStatus(refund_status_details)
    print(response.get_json_response())
    # print(response.get_response_object().get_body().get_result_info().get_result_msg())
    """ End of Function """


if __name__ == '__main__':
    set_initial_parameters()
    create_txn_token_with_required_params()
    create_txn_token_with_paytm_sso_token_and_payment_mode()
    create_txn_token_with_all_params()
    get_payment_status()
    do_refund()
    get_refund_status()
